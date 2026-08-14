"""Paso 1 - Chequeo previo: herramientas, GPU, y salud del archivo de entrada.

Uso:
    python preflight.py [ARCHIVO ...] [--json salida.json]

Sin archivos solo reporta el entorno. Devuelve codigo 1 si falta algo critico.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from common import has_nvenc, hhmmss, media_info, run, save_json, workdir

IMAGENES = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}


def check_entorno() -> dict:
    est = {"ffmpeg": bool(shutil.which("ffmpeg")), "ffprobe": bool(shutil.which("ffprobe"))}
    est["nvenc"] = has_nvenc() if est["ffmpeg"] else False
    try:
        import faster_whisper  # noqa: F401
        est["faster_whisper"] = True
    except ImportError:
        est["faster_whisper"] = False
    try:
        import cv2  # noqa: F401
        est["opencv"] = True
    except ImportError:
        est["opencv"] = False
    tmp = workdir()
    est["tmp"] = str(tmp)
    total, _, libre = shutil.disk_usage(tmp)
    est["disco_libre_gb"] = round(libre / 1024**3, 1)
    return est


def check_archivo(path: Path) -> dict:
    r = {"archivo": str(path), "avisos": [], "errores": []}
    if not path.exists():
        r["errores"].append("no existe")
        return r
    if path.suffix.lower() in IMAGENES:
        info = media_info(path)
        r.update(tipo="imagen", ancho=info["width"], alto=info["height"])
        if info["width"] < 720:
            r["avisos"].append(f"resolucion baja ({info['width']}px de ancho); se vera pixeleada en 1080x1920")
        return r

    info = media_info(path)
    r.update(
        tipo="video",
        duracion=round(info["duration"], 2),
        duracion_txt=hhmmss(info["duration"]),
        ancho=info["width"], alto=info["height"], fps=info["fps"],
        vcodec=info["vcodec"], acodec=info["acodec"],
        tamano_mb=round(info["size"] / 1024**2, 1),
    )
    if not info["has_video"]:
        r["errores"].append("el archivo no trae pista de video")
    if info["duration"] < 1:
        r["errores"].append("dura menos de 1 segundo")
    if not info["has_audio"]:
        r["avisos"].append("sin pista de audio: no se puede transcribir ni poner subtitulos automaticos")
    if info["width"] and info["height"] and info["width"] < info["height"]:
        r["avisos"].append("el video ya es vertical; el reencuadre sera minimo")
    if info["duration"] > 3600:
        r["avisos"].append("dura mas de 1 hora: transcribir tardara bastante")

    # Audio realmente silencioso (grabaciones con microfono apagado)
    if info["has_audio"]:
        det = run(["ffmpeg", "-hide_banner", "-v", "info", "-t", "60", "-i", str(path),
                   "-af", "volumedetect", "-f", "null", "-"], check=False)
        for linea in (det.stderr or "").splitlines():
            if "mean_volume" in linea:
                try:
                    val = float(linea.split("mean_volume:")[1].split("dB")[0])
                    r["volumen_medio_db"] = val
                    if val < -50:
                        r["avisos"].append("el audio esta practicamente en silencio")
                except (IndexError, ValueError):
                    pass
    return r


def main():
    ap = argparse.ArgumentParser(description="Chequeo previo de videos-tienda")
    ap.add_argument("archivos", nargs="*", help="videos o imagenes de entrada")
    ap.add_argument("--json", help="guardar el reporte en este archivo")
    args = ap.parse_args()

    rep = {"entorno": check_entorno(), "archivos": []}
    for a in args.archivos:
        rep["archivos"].append(check_archivo(Path(a)))

    e = rep["entorno"]
    print("== Entorno ==")
    print(f"  FFmpeg .......... {'ok' if e['ffmpeg'] else 'FALTA (critico)'}")
    print(f"  GPU NVENC ....... {'si (render rapido)' if e['nvenc'] else 'no (se usa CPU)'}")
    print(f"  faster-whisper .. {'ok' if e['faster_whisper'] else 'no (sin subtitulos automaticos)'}")
    print(f"  OpenCV .......... {'ok (reencuadre por rostro)' if e['opencv'] else 'no (reencuadre al centro)'}")
    print(f"  Disco libre ..... {e['disco_libre_gb']} GB en {e['tmp']}")

    fatal = not e["ffmpeg"]
    for a in rep["archivos"]:
        print(f"\n== {Path(a['archivo']).name} ==")
        if a.get("tipo") == "video":
            print(f"  {a['ancho']}x{a['alto']} @ {a['fps']}fps | {a['duracion_txt']} | {a['tamano_mb']} MB | audio: {a['acodec'] or 'ninguno'}")
        elif a.get("tipo") == "imagen":
            print(f"  imagen {a['ancho']}x{a['alto']}")
        for w in a["avisos"]:
            print(f"  aviso: {w}")
        for x in a["errores"]:
            print(f"  ERROR: {x}")
            fatal = True

    if args.json:
        save_json(args.json, rep)
        print(f"\nreporte -> {args.json}")

    sys.exit(1 if fatal else 0)


if __name__ == "__main__":
    main()
