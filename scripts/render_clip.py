"""Render de un clip vertical: recorte + reencuadre + subtitulos + gancho + CTA.

Es el equivalente local al render de Remotion de claude-shorts, pero con FFmpeg
y libass: sin Node, sin Chrome headless y con NVENC si hay GPU.

Uso:
    python render_clip.py --input largo.mp4 --desde 262 --hasta 301 --out corto.mp4 \
        --captions transcript.json --estilo bold --modo auto \
        --gancho "Nadie te dice esto|del PETG" --cta "michilab.store"
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from common import (FPS, H, W, OLIVO, die, ensure_dir, has_nvenc, media_info,
                    run, subtitles_filter, video_args, workdir)


def cadena_reencuadre(modo: str, centro: float) -> str:
    if modo == "blur":
        return (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
                f"boxblur=luma_radius=32:luma_power=2,eq=brightness=-0.05[bg];"
                f"[0:v]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
                f"[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1[v]")
    if modo == "pantalla":
        color = "0x" + OLIVO.lstrip("#")
        return (f"[0:v]scale={W}:-2:force_original_aspect_ratio=decrease,"
                f"pad={W}:{H}:(ow-iw)/2:(oh-ih)*0.42:color={color},setsar=1[v]")
    # crop: rellena la pantalla y recorta alrededor del centro de interes
    return (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
            f"crop={W}:{H}:x='(iw-ow)*{centro:.3f}':y='(ih-oh)/2',setsar=1[v]")


def main():
    ap = argparse.ArgumentParser(description="Renderiza un clip vertical con subtitulos")
    ap.add_argument("--input", required=True)
    ap.add_argument("--desde", type=float, default=0.0)
    ap.add_argument("--hasta", type=float, default=0.0, help="0 = hasta el final")
    ap.add_argument("--out", required=True)
    ap.add_argument("--captions", help="transcript.json para subtitulos automaticos")
    ap.add_argument("--estilo", default="michilab",
                    choices=["bold", "bounce", "clean", "michilab"])
    ap.add_argument("--modo", default="auto", choices=["auto", "crop", "blur", "pantalla"])
    ap.add_argument("--contenido", default="auto", choices=["auto", "persona", "producto", "pantalla"])
    ap.add_argument("--centro", type=float, help="0=izquierda, 0.5=centro, 1=derecha")
    ap.add_argument("--gancho", default="", help='"linea 1|linea 2"')
    ap.add_argument("--cta", default="")
    ap.add_argument("--plataforma", default="todas", choices=["tiktok", "instagram", "youtube", "todas"])
    ap.add_argument("--logo", help="PNG con transparencia, esquina superior")
    ap.add_argument("--musica", help="pista de fondo bajo la voz")
    ap.add_argument("--volumen-musica", type=float, default=0.12)
    ap.add_argument("--velocidad", type=float, default=1.0, help="1.05-1.15 acelera un poco (retiene mas)")
    ap.add_argument("--sin-subtitulos", action="store_true")
    ap.add_argument("--cpu", action="store_true")
    args = ap.parse_args()

    info = media_info(args.input)
    hasta = args.hasta if args.hasta > 0 else info["duration"]
    if hasta <= args.desde:
        die("--hasta debe ser mayor que --desde")
    dur = round((hasta - args.desde) / max(args.velocidad, 0.1), 3)

    modo, centro = args.modo, args.centro
    if modo == "auto" or centro is None:
        from reframe import analizar
        r = analizar(args.input, args.desde, hasta, args.contenido)
        modo = r["modo"] if args.modo == "auto" else args.modo
        centro = r["centro"] if centro is None else centro
        print(f"reencuadre: {modo} (centro {centro}) - {r['razon']}")

    tmp = ensure_dir(workdir() / "clip")
    ass = None
    if (args.captions and not args.sin_subtitulos) or args.gancho or args.cta:
        ass = tmp / (Path(args.out).stem + ".ass")
        cmd = [sys.executable, str(Path(__file__).parent / "make_ass.py"),
               "--estilo", args.estilo, "--out", str(ass),
               "--plataforma", args.plataforma, "--duracion", str(dur)]
        if args.captions and not args.sin_subtitulos:
            cmd += ["--captions", args.captions, "--desde", str(args.desde), "--hasta", str(hasta)]
        if args.gancho:
            cmd += ["--gancho", args.gancho]
        if args.cta:
            cmd += ["--cta", args.cta]
        subprocess.run(cmd, check=True)

    gpu = (not args.cpu) and has_nvenc()

    # --- video ---
    partes = [cadena_reencuadre(modo, centro or 0.5)]
    etiqueta = "v"
    if args.velocidad != 1.0:
        partes.append(f"[{etiqueta}]setpts=PTS/{args.velocidad}[vs]")
        etiqueta = "vs"
    if ass:
        partes.append(f"[{etiqueta}]{subtitles_filter(ass, tmp)}[vsub]")
        etiqueta = "vsub"
    if args.logo:
        partes.append(f"[2:v]scale=180:-1[lg];[{etiqueta}][lg]overlay=W-w-60:110[vlogo]")
        etiqueta = "vlogo"

    # --- audio ---
    entradas = ["-ss", f"{args.desde}", "-t", f"{hasta - args.desde}", "-i", args.input]
    idx_musica = None
    if args.musica:
        idx_musica = 1
        entradas += ["-stream_loop", "-1", "-t", f"{dur}", "-i", args.musica]
    if args.logo:
        # el logo siempre entra como indice 2 para que el filtro sea estable
        if idx_musica is None:
            entradas += ["-f", "lavfi", "-t", "0.1", "-i", "anullsrc=r=44100:cl=stereo"]
        entradas += ["-loop", "1", "-i", args.logo]

    mapa_audio, filtro_audio = None, None
    if info["has_audio"]:
        base = "[0:a]"
        if args.velocidad != 1.0:
            base_f = f"{base}atempo={args.velocidad}[a0];"
            base = "[a0]"
        else:
            base_f = ""
        if idx_musica is not None:
            filtro_audio = (f"{base_f}[{idx_musica}:a]volume={args.volumen_musica}[mus];"
                            f"{base}[mus]amix=inputs=2:duration=first:dropout_transition=0,"
                            f"loudnorm=I=-14:TP=-1:LRA=11[aout]")
        else:
            filtro_audio = f"{base_f}{base}loudnorm=I=-14:TP=-1:LRA=11[aout]"
        mapa_audio = "[aout]"
    elif idx_musica is not None:
        filtro_audio = (f"[{idx_musica}:a]volume={args.volumen_musica * 3},"
                        f"loudnorm=I=-14:TP=-1:LRA=11[aout]")
        mapa_audio = "[aout]"

    cadena = ";".join(partes + ([filtro_audio] if filtro_audio else []))
    cmd = ["ffmpeg", "-y", "-hide_banner", "-v", "error"] + entradas
    cmd += ["-filter_complex", cadena, "-map", f"[{etiqueta}]"]
    if mapa_audio:
        cmd += ["-map", mapa_audio, "-c:a", "aac", "-b:a", "160k", "-ar", "44100"]
    cmd += ["-t", f"{dur}", "-r", str(FPS)]
    cmd += video_args(gpu, "alta") + ["-movflags", "+faststart", str(Path(args.out).resolve())]
    run(cmd, cwd=tmp)

    res = media_info(args.out)
    print(f"clip -> {args.out}")
    print(f"  {res['width']}x{res['height']} | {res['duration']:.1f}s | "
          f"{res['size']/1024**2:.1f} MB | {'GPU' if gpu else 'CPU'}")


if __name__ == "__main__":
    main()
