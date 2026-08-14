"""Decide como reencuadrar un video horizontal a 9:16.

Tres estrategias (ver references/reencuadre.md):
  crop     - recorte al centro de interes (personas, gatos, mano trabajando)
  blur     - encaja completo sobre fondo desenfocado (producto, timelapse)
  pantalla - encaja a lo ancho sobre banda de marca (grabaciones de pantalla)

Si OpenCV esta instalado se usa deteccion de rostros; si no, se estima el centro
de interes por densidad de detalle (numpy + Pillow), que para fotos y videos de
producto funciona bien.

Uso:
    python reframe.py video.mp4 [--desde 0 --hasta 30] [--contenido auto] [--output reframe.json]
"""
from __future__ import annotations

import argparse
import shutil

from common import ensure_dir, media_info, run, save_json, workdir

MUESTRAS = 12


def _muestrear(video: str, desde: float, dur: float, tmp) -> list:
    """Extrae fotogramas pequenos repartidos por el clip."""
    ensure_dir(tmp)
    for viejo in tmp.glob("*.png"):
        viejo.unlink()
    paso = max(dur / MUESTRAS, 0.2)
    run(["ffmpeg", "-y", "-hide_banner", "-v", "error", "-ss", f"{desde}",
         "-t", f"{dur}", "-i", video, "-vf", f"fps=1/{paso:.3f},scale=320:-2",
         "-frames:v", str(MUESTRAS), str(tmp / "m_%03d.png")], check=False)
    return sorted(tmp.glob("*.png"))


def _centro_por_rostros(frames) -> float | None:
    try:
        import cv2
    except ImportError:
        return None
    casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    centros = []
    for f in frames:
        img = cv2.imread(str(f))
        if img is None:
            continue
        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        caras = casc.detectMultiScale(gris, 1.15, 5, minSize=(24, 24))
        if len(caras):
            x, _, w, _ = max(caras, key=lambda c: c[2] * c[3])
            centros.append((x + w / 2) / img.shape[1])
    if not centros:
        return None
    centros.sort()
    return float(centros[len(centros) // 2])  # mediana: ignora falsos positivos sueltos


def _centro_por_detalle(frames) -> float:
    """Centro de masa de la 'textura' de la imagen: donde hay bordes hay contenido."""
    import numpy as np
    from PIL import Image

    acumulado = None
    for f in frames:
        g = np.asarray(Image.open(f).convert("L"), dtype=np.float32)
        energia = np.abs(np.diff(g, axis=1)).sum(axis=0)
        energia = energia / (energia.sum() + 1e-6)
        acumulado = energia if acumulado is None else acumulado + energia
    if acumulado is None:
        return 0.5
    # Suavizado para que un borde duro aislado no jale el encuadre
    k = np.ones(21) / 21
    suave = np.convolve(acumulado, k, mode="same")
    x = np.arange(len(suave))
    return float((suave * x).sum() / (suave.sum() + 1e-6) / len(suave))


def analizar(video: str, desde: float, hasta: float, contenido: str) -> dict:
    info = media_info(video)
    dur = max(0.5, min(hasta, info["duration"]) - desde)
    vertical = info["height"] >= info["width"]

    tmp = workdir() / "muestras"
    frames = _muestrear(video, desde, dur, tmp)
    rostro = _centro_por_rostros(frames) if contenido in ("auto", "persona") else None
    centro = rostro if rostro is not None else _centro_por_detalle(frames)
    shutil.rmtree(tmp, ignore_errors=True)

    if contenido == "auto":
        if vertical:
            modo, razon = "crop", "el video ya es vertical: recorte minimo"
        elif rostro is not None:
            modo, razon = "crop", "se detectaron rostros: recorte siguiendo la cara"
        elif info["width"] / max(info["height"], 1) > 2.0:
            modo, razon = "pantalla", "muy panoramico: se encaja sobre banda de marca"
        else:
            modo, razon = "blur", "producto/objeto: se ve completo sobre fondo desenfocado"
    else:
        modo = {"persona": "crop", "producto": "blur", "pantalla": "pantalla"}.get(contenido, "crop")
        razon = f"forzado por --contenido {contenido}"

    # El centro no puede salirse: la ventana de recorte debe caber en la imagen.
    ancho_rel = (info["height"] * 9 / 16) / max(info["width"], 1) if not vertical else 1.0
    limite = min(0.5, max(0.0, ancho_rel / 2))
    centro = max(limite, min(1 - limite, centro))

    return {"video": info["path"], "modo": modo, "centro": round(centro, 3),
            "rostros": rostro is not None, "razon": razon,
            "origen": f"{info['width']}x{info['height']}"}


def main():
    ap = argparse.ArgumentParser(description="Calcula el reencuadre 9:16")
    ap.add_argument("video")
    ap.add_argument("--desde", type=float, default=0.0)
    ap.add_argument("--hasta", type=float, default=1e9)
    ap.add_argument("--contenido", default="auto", choices=["auto", "persona", "producto", "pantalla"])
    ap.add_argument("--output")
    args = ap.parse_args()

    r = analizar(args.video, args.desde, args.hasta, args.contenido)
    print(f"origen {r['origen']} -> modo '{r['modo']}', centro {r['centro']}")
    print(f"  {r['razon']}")
    if args.output:
        save_json(args.output, r)
        print(f"  -> {args.output}")


if __name__ == "__main__":
    main()
