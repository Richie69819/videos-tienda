"""Codificacion final por plataforma (TikTok / Reels / Shorts).

Cada red recomprime lo que subes: entregarle el bitrate y el loudness que espera
evita una segunda recompresion agresiva. Especificaciones en references/plataformas.md.

Uso:
    python export.py --entrada render/ --plataforma todas --salida ./videos/
    python export.py --entrada corto.mp4 --plataforma tiktok --salida ./videos/
"""
from __future__ import annotations

import argparse
from pathlib import Path

from common import has_nvenc, media_info, run

PLATAFORMAS = {
    "youtube": {
        "sufijo": "yt", "nombre": "YouTube Shorts", "max_seg": 60, "max_mb": 256,
        "cpu": ["-c:v", "libx264", "-preset", "slow", "-b:v", "12M", "-maxrate", "14M",
                "-bufsize", "24M", "-profile:v", "high", "-level", "4.2"],
        "gpu": ["-c:v", "h264_nvenc", "-preset", "p5", "-tune", "hq", "-b:v", "12M",
                "-maxrate", "14M", "-bufsize", "24M", "-profile:v", "high", "-level", "4.2"],
        "audio": ["-c:a", "aac", "-b:a", "192k", "-ar", "48000"],
    },
    "tiktok": {
        "sufijo": "tt", "nombre": "TikTok", "max_seg": 180, "max_mb": 287,
        "cpu": ["-c:v", "libx264", "-preset", "slow", "-crf", "18",
                "-maxrate", "10M", "-bufsize", "20M"],
        "gpu": ["-c:v", "h264_nvenc", "-preset", "p5", "-tune", "hq", "-rc", "vbr",
                "-cq", "18", "-b:v", "0", "-maxrate", "10M", "-bufsize", "20M"],
        "audio": ["-c:a", "aac", "-b:a", "128k", "-ar", "44100"],
    },
    "instagram": {
        "sufijo": "ig", "nombre": "Instagram Reels", "max_seg": 90, "max_mb": 250,
        "cpu": ["-c:v", "libx264", "-preset", "slow", "-b:v", "4500k",
                "-maxrate", "5000k", "-bufsize", "10M", "-profile:v", "high", "-level", "4.2"],
        "gpu": ["-c:v", "h264_nvenc", "-preset", "p5", "-tune", "hq", "-b:v", "4500k",
                "-maxrate", "5000k", "-bufsize", "10M", "-profile:v", "high", "-level", "4.2"],
        "audio": ["-c:a", "aac", "-b:a", "128k", "-ar", "44100"],
    },
}


def exportar(entrada: Path, plataforma: str, salida: Path, gpu: bool) -> dict:
    spec = PLATAFORMAS[plataforma]
    info = media_info(entrada)
    destino = salida / f"{entrada.stem}_{spec['sufijo']}.mp4"

    cmd = ["ffmpeg", "-y", "-hide_banner", "-v", "error", "-i", str(entrada)]
    cmd += spec["gpu"] if gpu else spec["cpu"]
    if info["has_audio"]:
        cmd += ["-af", "loudnorm=I=-14:TP=-1:LRA=11"] + spec["audio"]
    else:
        cmd += ["-an"]
    cmd += ["-pix_fmt", "yuv420p", "-movflags", "+faststart", str(destino)]
    run(cmd)

    res = media_info(destino)
    avisos = []
    if res["duration"] > spec["max_seg"]:
        avisos.append(f"dura {res['duration']:.0f}s y {spec['nombre']} admite {spec['max_seg']}s")
    if res["size"] / 1024**2 > spec["max_mb"]:
        avisos.append(f"pesa {res['size']/1024**2:.0f} MB (limite {spec['max_mb']} MB)")
    return {"archivo": destino, "plataforma": spec["nombre"], "info": res, "avisos": avisos}


def main():
    ap = argparse.ArgumentParser(description="Exporta a formato de cada red")
    ap.add_argument("--entrada", required=True, help="archivo o carpeta con los renders")
    ap.add_argument("--plataforma", default="todas",
                    choices=list(PLATAFORMAS) + ["todas"])
    ap.add_argument("--salida", default="./videos")
    ap.add_argument("--cpu", action="store_true")
    args = ap.parse_args()

    ent = Path(args.entrada)
    fuentes = sorted(ent.glob("*.mp4")) if ent.is_dir() else [ent]
    if not fuentes:
        print("no hay .mp4 que exportar")
        return

    salida = Path(args.salida)
    salida.mkdir(parents=True, exist_ok=True)
    gpu = (not args.cpu) and has_nvenc()
    objetivo = list(PLATAFORMAS) if args.plataforma == "todas" else [args.plataforma]

    print(f"{len(fuentes)} video(s) x {len(objetivo)} plataforma(s) | {'GPU NVENC' if gpu else 'CPU'}\n")
    filas = []
    for f in fuentes:
        for p in objetivo:
            r = exportar(f, p, salida, gpu)
            filas.append(r)
            print(f"  {r['archivo'].name:38s} {r['plataforma']:18s} "
                  f"{r['info']['duration']:5.1f}s  {r['info']['size']/1024**2:6.1f} MB")
            for a in r["avisos"]:
                print(f"    aviso: {a}")

    print(f"\n{len(filas)} archivos en {salida.resolve()}")


if __name__ == "__main__":
    main()
