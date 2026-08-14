"""Pantalla final de marca: el cierre que manda a la tienda.

Un clip que termina en seco desperdicia el unico momento en que el espectador ya
decidio quedarse. Este script agrega el cierre, en dos modos:

  tarjeta  - agrega 1.8 s de tarjeta solida despues del clip (el clip no se toca)
  encima   - dibuja el cierre sobre los ultimos 2 s del clip (no cambia la duracion)

La tarjeta se dibuja con Pillow, no con subtitulos, para tener control fino de
tipografia, colores de marca y posicion dentro de la zona segura.

Persuasion: una promesa, una facilidad y una direccion. Nada de cifras de ventas
ni testimonios inventados; solo hechos verificables del negocio.

Uso:
    python pantalla_final.py clip.mp4 --out final.mp4
    python pantalla_final.py "carpeta" --out "carpeta salida" --modo encima
    python pantalla_final.py clip.mp4 --out final.mp4 --promesa "Envío gratis a todo México" \
        --facilidad "Entrega en el Metro CDMX" --url michilab.store --nota "Se imprime por pedido"
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from common import (CREMA, FPS, H, NARANJA, OLIVO, W, ensure_dir, has_nvenc,
                    media_info, run, video_args, workdir, fonts_dir)

# Zona segura: la interfaz de TikTok/Reels tapa los ultimos ~450 px y los
# primeros ~210. Todo el cierre vive entre esos limites.
Y_MIN, Y_MAX = 260, 1440


def _rgb(h: str) -> tuple:
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _fuente(tam: int):
    ruta = fonts_dir() / "Montserrat-Bold.ttf"
    if ruta.exists():
        return ImageFont.truetype(str(ruta), tam)
    return ImageFont.load_default()


def _centrar(d, texto, fuente, y, color, lienzo_ancho=W):
    caja = d.textbbox((0, 0), texto, font=fuente)
    d.text(((lienzo_ancho - (caja[2] - caja[0])) / 2 - caja[0], y), texto,
           font=fuente, fill=color)
    return caja[3] - caja[1]


def _ancho(d, texto, fuente) -> int:
    caja = d.textbbox((0, 0), texto, font=fuente)
    return caja[2] - caja[0]


def _pegar_centrado(fondo: Image.Image, logo: Image.Image, ancho: int, y: int) -> int:
    """Pega un PNG con transparencia centrado horizontalmente. Devuelve su alto."""
    escala = ancho / logo.width
    logo = logo.resize((ancho, max(1, int(logo.height * escala))), Image.LANCZOS)
    fondo.alpha_composite(logo, (int((W - ancho) / 2), int(y)))
    return logo.height


def dibujar(marca: str, promesa: str, facilidad: str, url: str, nota: str,
            modo: str, logo: str | None = None, monograma: str | None = None) -> Image.Image:
    """Devuelve la pantalla final como imagen RGBA de 1080x1920.

    Si se pasan los PNG del kit de marca se usan tal cual (sobre fondo olivo van
    las variantes 'claro'). Si no, se compone el wordmark con la tipografia."""
    olivo, crema, naranja = _rgb(OLIVO), _rgb(CREMA), _rgb(NARANJA)
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    tarjeta = modo == "tarjeta"

    if tarjeta:
        ImageDraw.Draw(img).rectangle([0, 0, W, H], fill=olivo + (255,))
        # Textura: la silueta del producto, apenas visible
        capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        dc = ImageDraw.Draw(capa)
        import math
        cx, cy, r = W // 2, 950, 470
        dc.ellipse([cx - r, cy - r, cx + r, cy + r], outline=crema + (20,), width=56)
        dc.ellipse([cx - 165, cy - 165, cx + 165, cy + 165], outline=crema + (20,), width=42)
        for ang in (30, 120, 210, 300):
            hx = cx + int(315 * math.cos(math.radians(ang)))
            hy = cy + int(315 * math.sin(math.radians(ang)))
            dc.ellipse([hx - 56, hy - 56, hx + 56, hy + 56], fill=crema + (16,))
        img = Image.alpha_composite(img, capa)
    else:
        # Velo degradado: deja ver el video arriba, marca abajo, sin pisar la interfaz
        velo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        dv = ImageDraw.Draw(velo)
        y0, y1 = 600, 1480
        for y in range(y0, y1):
            dv.line([(0, y), (W, y)], fill=olivo + (int(240 * min(1.0, (y - y0) / 340)),))
        dv.rectangle([0, y1, W, H], fill=olivo + (240,))
        img = Image.alpha_composite(img, velo)

    d = ImageDraw.Draw(img)
    y = 430 if tarjeta else 700

    # --- monograma ML (solo en la tarjeta; en el velo estorbaria al video) ---
    if tarjeta and monograma and Path(monograma).exists():
        y += _pegar_centrado(img, Image.open(monograma).convert("RGBA"), 190, y) + 54

    # --- wordmark ---
    if logo and Path(logo).exists():
        y += _pegar_centrado(img, Image.open(logo).convert("RGBA"), 620 if tarjeta else 520, y)
    else:
        f_marca = _fuente(118 if tarjeta else 100)
        parte1, parte2 = marca[:5], marca[5:]
        ancho_total = _ancho(d, parte1, f_marca) + _ancho(d, parte2, f_marca)
        x = (W - ancho_total) / 2
        d.text((x, y), parte1, font=f_marca, fill=crema)
        d.text((x + _ancho(d, parte1, f_marca), y), parte2, font=f_marca, fill=naranja)
        y += f_marca.size * 1.25

    d = ImageDraw.Draw(img)
    if nota and tarjeta:
        y += 26
        _centrar(d, nota.upper(), _fuente(38), y, naranja)
        y += 74

    # --- promesa y facilidad, con vineta naranja ---
    f_linea = _fuente(52 if tarjeta else 48)
    y += 70
    for texto in [t for t in (promesa, facilidad) if t]:
        ancho = _ancho(d, texto, f_linea)
        x = (W - ancho - 46) / 2
        d.rounded_rectangle([x, y + 14, x + 22, y + 36], radius=6, fill=naranja)
        d.text((x + 46, y), texto, font=f_linea, fill=crema)
        y += 92

    # --- la direccion: caja crema con texto olivo, el mayor contraste de la pieza ---
    f_url = _fuente(66)
    ancho = _ancho(d, url, f_url)
    caja_w, caja_h = ancho + 110, 122
    x0 = (W - caja_w) / 2
    y0 = min(y + 40, Y_MAX - caja_h)
    d.rounded_rectangle([x0, y0, x0 + caja_w, y0 + caja_h], radius=26, fill=crema)
    caja = d.textbbox((0, 0), url, font=f_url)
    d.text(((W - ancho) / 2 - caja[0], y0 + (caja_h - (caja[3] - caja[1])) / 2 - caja[1]),
           url, font=f_url, fill=olivo)

    return img


def aplicar(entrada: Path, salida: Path, png: Path, modo: str,
            segundos: float, gpu: bool):
    info = media_info(entrada)
    dur = info["duration"]

    if modo == "tarjeta":
        entradas = ["-i", str(entrada), "-loop", "1", "-t", f"{segundos}", "-i", str(png),
                    "-f", "lavfi", "-t", f"{segundos}", "-i", "anullsrc=r=44100:cl=stereo"]
        filtro = (f"[1:v]scale={W}:{H},fps={FPS},format=yuv420p,setsar=1,"
                  f"fade=t=in:st=0:d=0.25[card];"
                  f"[0:v]scale={W}:{H},fps={FPS},format=yuv420p,setsar=1[cl];"
                  f"[0:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[a0];"
                  f"[2:a]aformat=sample_fmts=fltp:sample_rates=44100:channel_layouts=stereo[a1];"
                  f"[cl][a0][card][a1]concat=n=2:v=1:a=1[v][a]")
        mapas = ["-map", "[v]", "-map", "[a]"]
    else:
        inicio = max(0.0, dur - segundos)
        entradas = ["-i", str(entrada), "-loop", "1", "-t", f"{dur}", "-i", str(png)]
        filtro = (f"[1:v]format=rgba,fade=t=in:st={inicio:.2f}:d=0.35:alpha=1[ov];"
                  f"[0:v][ov]overlay=0:0:enable='gte(t,{inicio:.2f})',format=yuv420p[v]")
        mapas = ["-map", "[v]"] + (["-map", "0:a"] if info["has_audio"] else [])

    cmd = ["ffmpeg", "-y", "-hide_banner", "-v", "error"] + entradas
    cmd += ["-filter_complex", filtro] + mapas
    if modo == "tarjeta" or info["has_audio"]:
        cmd += ["-c:a", "aac", "-b:a", "160k", "-ar", "44100"]
    cmd += video_args(gpu, "alta") + ["-movflags", "+faststart", str(salida)]
    run(cmd)
    return media_info(salida)


def main():
    ap = argparse.ArgumentParser(description="Agrega la pantalla final de marca")
    ap.add_argument("entrada", help="archivo .mp4 o carpeta")
    ap.add_argument("--out", required=True, help="archivo o carpeta de salida")
    ap.add_argument("--modo", default="tarjeta", choices=["tarjeta", "encima"])
    ap.add_argument("--segundos", type=float, default=1.8)
    ap.add_argument("--marca", default="Michilab")
    ap.add_argument("--nota", default="Se imprime por pedido")
    ap.add_argument("--promesa", default="Envío gratis a todo México")
    ap.add_argument("--facilidad", default="Entrega en el Metro CDMX")
    ap.add_argument("--url", default="michilab.store")
    ap.add_argument("--logo", help="PNG del wordmark (variante clara si el fondo es oscuro)")
    ap.add_argument("--monograma", help="PNG del monograma/icono")
    ap.add_argument("--solo-png", help="guarda la pantalla como PNG y termina")
    ap.add_argument("--cpu", action="store_true")
    args = ap.parse_args()

    img = dibujar(args.marca, args.promesa, args.facilidad, args.url, args.nota,
                  args.modo, args.logo, args.monograma)
    if args.solo_png:
        img.convert("RGB" if args.modo == "tarjeta" else "RGBA").save(args.solo_png)
        print(f"pantalla -> {args.solo_png}")
        return

    png = ensure_dir(workdir() / "cierre") / f"cierre_{args.modo}.png"
    img.save(png)

    gpu = (not args.cpu) and has_nvenc()
    ent = Path(args.entrada)
    if ent.is_dir():
        destino = ensure_dir(args.out)
        archivos = sorted(ent.glob("*.mp4"))
        print(f"{len(archivos)} clips | modo {args.modo} | {args.segundos}s\n")
        for i, f in enumerate(archivos, 1):
            info = aplicar(f, destino / f.name, png, args.modo, args.segundos, gpu)
            print(f"  [{i}/{len(archivos)}] {f.name:32s} {info['duration']:.1f}s")
        print(f"\nlisto -> {destino.resolve()}")
    else:
        salida = Path(args.out)
        ensure_dir(salida.parent)
        info = aplicar(ent, salida, png, args.modo, args.segundos, gpu)
        print(f"listo -> {salida}  ({info['duration']:.1f}s)")


if __name__ == "__main__":
    main()
