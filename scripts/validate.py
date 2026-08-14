"""Revision final antes de subir: que ningun video salga roto o mudo.

Comprueba resolucion 1080x1920, codec H.264, pista de audio con sonido real,
duracion dentro de limites y peso razonable.

Uso:
    python validate.py ./videos
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from common import media_info, run

LIMITES = {"min_seg": 3, "max_seg": 180, "max_mb": 250}


def revisar(path: Path) -> dict:
    r = {"archivo": path.name, "errores": [], "avisos": []}
    info = media_info(path)
    r["info"] = info

    if not info["has_video"]:
        r["errores"].append("sin pista de video")
        return r
    if (info["width"], info["height"]) != (1080, 1920):
        r["avisos"].append(f"no es 1080x1920 (es {info['width']}x{info['height']})")
    if info["vcodec"] != "h264":
        r["avisos"].append(f"codec {info['vcodec']} (las redes prefieren h264)")
    if info["duration"] < LIMITES["min_seg"]:
        r["errores"].append(f"dura {info['duration']:.1f}s, demasiado corto")
    if info["duration"] > LIMITES["max_seg"]:
        r["avisos"].append(f"dura {info['duration']:.0f}s: revisa el limite de la red")
    if info["size"] / 1024**2 > LIMITES["max_mb"]:
        r["avisos"].append(f"pesa {info['size']/1024**2:.0f} MB")

    if not info["has_audio"]:
        r["avisos"].append("sin audio (en TikTok/Reels el video mudo rinde peor)")
    else:
        det = run(["ffmpeg", "-hide_banner", "-v", "info", "-i", str(path),
                   "-af", "volumedetect", "-f", "null", "-"], check=False)
        for linea in (det.stderr or "").splitlines():
            if "mean_volume" in linea:
                try:
                    vol = float(linea.split("mean_volume:")[1].split("dB")[0])
                    r["info"]["volumen_db"] = vol
                    if vol < -50:
                        r["errores"].append("el audio esta en silencio")
                except (IndexError, ValueError):
                    pass

    # Decodificado completo: detecta archivos truncados o con frames corruptos
    dec = run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "null", "-"], check=False)
    if dec.returncode != 0 or (dec.stderr or "").strip():
        primera = (dec.stderr or "").strip().splitlines()[:1]
        r["errores"].append(f"error al decodificar: {primera[0] if primera else 'desconocido'}")
    return r


def main():
    ap = argparse.ArgumentParser(description="Valida los videos exportados")
    ap.add_argument("ruta", help="archivo o carpeta")
    args = ap.parse_args()

    p = Path(args.ruta)
    archivos = sorted(p.glob("*.mp4")) if p.is_dir() else [p]
    if not archivos:
        print("no hay videos que revisar")
        return

    fallos = 0
    for a in archivos:
        r = revisar(a)
        estado = "ERROR" if r["errores"] else ("aviso" if r["avisos"] else "ok")
        i = r["info"]
        print(f"[{estado:5s}] {r['archivo']:40s} {i['width']}x{i['height']} "
              f"{i['duration']:5.1f}s {i['size']/1024**2:6.1f}MB")
        for e in r["errores"]:
            print(f"         ERROR: {e}")
            fallos += 1
        for w in r["avisos"]:
            print(f"         aviso: {w}")

    print(f"\n{len(archivos)} revisados, {fallos} con error")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
