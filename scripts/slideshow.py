"""Motor de fotos -> video vertical (Ken Burns + transiciones + textos + musica).

Es la idea de los slideshows de Creatomate, pero resuelta en local con FFmpeg:
sin API key, sin subir las fotos a ningun servidor y sin costo por render.

Uso:
    python slideshow.py --imagenes fotos-shopify --out reel.mp4 \
        --segundos 2.6 --estilo michilab \
        --textos "Anillo dona||Hecho en PETG|||Envio gratis" \
        --gancho "Tu gato ya tiene|donde rascarse" --cta "michilab.store" \
        --musica pista.mp3

Los textos se separan con '|' (uno por foto, vacio = sin texto).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from common import (H, W, FPS, die, ensure_dir, has_nvenc, media_info, run,
                    save_json, subtitles_filter, video_args, workdir)

EXT = {".jpg", ".jpeg", ".png", ".webp", ".bmp"}
TRANSICIONES = ["fade", "dissolve", "slideleft", "wipeup", "circleopen", "smoothleft"]
FONDOS = {"blur": None, "olivo": "0x5a6640", "crema": "0xf5f2e9", "negro": "0x000000"}


def juntar_imagenes(entradas) -> list:
    fotos = []
    for e in entradas:
        p = Path(e)
        if p.is_dir():
            fotos += sorted(q for q in p.iterdir() if q.suffix.lower() in EXT)
        elif p.suffix.lower() in EXT:
            fotos.append(p)
        else:
            die(f"no es imagen ni carpeta de imagenes: {p}")
    if not fotos:
        die("no encontre imagenes")
    return fotos


def filtro_diapositiva(indice: int, frames: int, fondo: str, zoom: str) -> str:
    """Compone 9:16 (fondo desenfocado o solido) y aplica Ken Burns."""
    # Se compone al doble de resolucion: el zoompan sobre una imagen grande
    # no "tiembla" al desplazarse subpixel.
    bw, bh = W * 2, H * 2
    if fondo == "blur":
        base = (f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
                f"crop={W}:{H},boxblur=luma_radius=32:luma_power=2,"
                f"eq=brightness=-0.05:saturation=1.1,scale={bw}:{bh}[bg];"
                f"[0:v]scale={bw}:{bh}:force_original_aspect_ratio=decrease[fg];"
                f"[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1[comp];")
    else:
        color = FONDOS[fondo]
        base = (f"color=c={color}:s={bw}x{bh}:d=1[bg];"
                f"[0:v]scale={bw}:{bh}:force_original_aspect_ratio=decrease[fg];"
                f"[bg][fg]overlay=(W-w)/2:(H-h)/2,setsar=1[comp];")

    if zoom == "alterna":
        zoom = ["in", "out", "izq"][indice % 3]

    if zoom == "in":
        z, x, y = "min(zoom+0.0011,1.22)", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    elif zoom == "out":
        z, x, y = "if(lte(zoom,1.0),1.22,max(1.001,zoom-0.0011))", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    elif zoom == "izq":
        z, x, y = "1.15", f"(iw-iw/zoom)*(on/{max(frames-1,1)})", "ih/2-(ih/zoom/2)"
    elif zoom == "der":
        z, x, y = "1.15", f"(iw-iw/zoom)*(1-on/{max(frames-1,1)})", "ih/2-(ih/zoom/2)"
    else:  # sin movimiento
        z, x, y = "1.0", "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"

    return (base + f"[comp]zoompan=z='{z}':x='{x}':y='{y}':"
                   f"d={frames}:s={W}x{H}:fps={FPS},format=yuv420p[v]")


def render_diapositivas(fotos, tmp: Path, seg: float, fondo: str, zoom: str, gpu: bool) -> list:
    frames = max(2, int(round(seg * FPS)))
    salidas = []
    for i, foto in enumerate(fotos):
        out = tmp / f"slide_{i:02d}.mp4"
        cmd = ["ffmpeg", "-y", "-hide_banner", "-v", "error", "-i", str(foto),
               "-filter_complex", filtro_diapositiva(i, frames, fondo, zoom),
               "-map", "[v]", "-frames:v", str(frames), "-r", str(FPS)]
        cmd += video_args(gpu, "alta") + [str(out)]
        run(cmd)
        salidas.append(out)
        print(f"  foto {i+1}/{len(fotos)}: {foto.name}")
    return salidas


def cadena_xfade(n: int, seg: float, trans: float, transicion: str) -> tuple[str, str, float]:
    """Encadena xfade entre diapositivas. Devuelve (filtro, etiqueta, duracion)."""
    if n == 1:
        return "", "0:v", seg
    partes, prev = [], "[0:v]"
    for i in range(1, n):
        et = f"[x{i}]"
        offset = round(i * (seg - trans), 3)
        t = transicion if transicion != "alterna" else TRANSICIONES[(i - 1) % len(TRANSICIONES)]
        partes.append(f"{prev}[{i}:v]xfade=transition={t}:duration={trans}:offset={offset}{et}")
        prev = et
    total = n * seg - (n - 1) * trans
    return ";".join(partes), prev.strip("[]"), total


def tarjetas_desde_textos(textos: list, n: int, seg: float, trans: float, pos: str) -> list:
    tarjetas = []
    for i in range(min(n, len(textos))):
        txt = (textos[i] or "").strip()
        if not txt:
            continue
        ini = i * (seg - trans)
        tarjetas.append({"text": txt,
                         "start": round(ini + 0.25, 2),
                         "end": round(ini + seg - 0.2, 2),
                         "pos": pos})
    return tarjetas


def main():
    ap = argparse.ArgumentParser(description="Fotos -> video vertical 1080x1920")
    ap.add_argument("--imagenes", nargs="+", required=True, help="carpeta y/o archivos de imagen")
    ap.add_argument("--out", required=True)
    ap.add_argument("--segundos", type=float, default=2.6, help="duracion por foto")
    ap.add_argument("--transicion", type=float, default=0.45, help="duracion del cruce")
    ap.add_argument("--efecto", default="alterna",
                    help="transicion: " + ", ".join(TRANSICIONES) + ", alterna")
    ap.add_argument("--fondo", default="blur", choices=list(FONDOS))
    ap.add_argument("--zoom", default="alterna", choices=["in", "out", "izq", "der", "alterna", "no"])
    ap.add_argument("--textos", default="", help="textos por foto separados por '|'")
    ap.add_argument("--pos-texto", default="abajo", choices=["abajo", "arriba"])
    ap.add_argument("--estilo", default="michilab")
    ap.add_argument("--gancho", default="")
    ap.add_argument("--cta", default="")
    ap.add_argument("--musica", help="pista de audio de fondo")
    ap.add_argument("--volumen-musica", type=float, default=0.55)
    ap.add_argument("--cpu", action="store_true", help="forzar codificacion por CPU")
    args = ap.parse_args()

    fotos = juntar_imagenes(args.imagenes)
    gpu = (not args.cpu) and has_nvenc()
    tmp = ensure_dir(workdir() / "slideshow")
    for viejo in tmp.glob("slide_*.mp4"):
        viejo.unlink()

    print(f"{len(fotos)} fotos | {args.segundos}s c/u | fondo {args.fondo} | "
          f"{'GPU NVENC' if gpu else 'CPU'}")
    diapos = render_diapositivas(fotos, tmp, args.segundos, args.fondo, args.zoom, gpu)

    filtro, etiqueta, total = cadena_xfade(len(diapos), args.segundos, args.transicion, args.efecto)

    # Textos: se generan como subtitulos .ass para reusar la tipografia de la skill
    ass = None
    textos = [t for t in args.textos.split("|")] if args.textos else []
    if textos or args.gancho or args.cta:
        tarjetas = tarjetas_desde_textos(textos, len(diapos), args.segundos, args.transicion, args.pos_texto)
        tj = tmp / "tarjetas.json"
        save_json(tj, tarjetas)
        ass = tmp / "textos.ass"
        cmd = [sys.executable, str(Path(__file__).parent / "make_ass.py"),
               "--tarjetas", str(tj), "--estilo", args.estilo, "--out", str(ass),
               "--duracion", str(round(total, 2))]
        if args.gancho:
            cmd += ["--gancho", args.gancho]
        if args.cta:
            cmd += ["--cta", args.cta]
        subprocess.run(cmd, check=True)

    # Pase final: xfade + textos + musica
    cwd = tmp
    entradas = []
    for d in diapos:
        entradas += ["-i", str(d)]
    if args.musica:
        entradas += ["-stream_loop", "-1", "-i", str(args.musica)]

    cadena = filtro
    if ass:
        quemado = subtitles_filter(ass, cwd)
        cadena = (f"{filtro};[{etiqueta}]{quemado}[vout]" if filtro
                  else f"[{etiqueta}]{quemado}[vout]")
        etiqueta = "vout"
    elif not filtro:
        cadena = f"[{etiqueta}]null[vout]"
        etiqueta = "vout"

    cmd = ["ffmpeg", "-y", "-hide_banner", "-v", "error"] + entradas
    cmd += ["-filter_complex", cadena, "-map", f"[{etiqueta}]"]
    if args.musica:
        idx = len(diapos)
        cmd += ["-map", f"{idx}:a", "-af",
                f"volume={args.volumen_musica},afade=t=out:st={max(0,total-1.5):.2f}:d=1.5,"
                f"loudnorm=I=-14:TP=-1:LRA=11",
                "-c:a", "aac", "-b:a", "160k", "-ar", "44100"]
    cmd += ["-t", f"{total:.3f}", "-r", str(FPS)]
    cmd += video_args(gpu, "alta") + ["-movflags", "+faststart", str(Path(args.out).resolve())]
    run(cmd, cwd=cwd)

    info = media_info(args.out)
    print(f"\nlisto -> {args.out}")
    print(f"  {info['width']}x{info['height']} | {info['duration']:.1f}s | "
          f"{info['size']/1024**2:.1f} MB | audio: {info['acodec'] or 'ninguno'}")


if __name__ == "__main__":
    main()
