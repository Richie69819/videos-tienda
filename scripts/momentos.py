"""Encuentra los mejores momentos de un video SIN voz (b-roll de producto o mascota).

El flujo de video largo se apoya en la transcripcion para elegir los cortes, pero el
material de tienda casi nunca tiene locucion: es el gato jugando o la pieza girando en
la mano. Aqui la seleccion es visual.

Dos metricas por fotograma, calculadas a baja resolucion (rapido):
  movimiento - diferencia media contra el fotograma anterior
  nitidez    - energia de bordes; se desploma cuando hay barrido de camara

    --modo gato      pesa el movimiento (queremos accion: zarpazo, salto, persecucion)
    --modo producto  pesa la nitidez (queremos la pieza quieta y enfocada)

Uso:
    python momentos.py video.MOV --n 6 --duracion 8 --modo gato --output momentos.json --hojas
"""
from __future__ import annotations

import argparse
import subprocess

import numpy as np

from common import ensure_dir, hhmmss, media_info, run, save_json, workdir

ANCHO, ALTO = 160, 284   # resolucion de analisis (vertical); suficiente y muy rapido
MUESTREO = 5             # fotogramas por segundo analizados


def perfil(video: str) -> tuple[np.ndarray, np.ndarray]:
    """Devuelve (movimiento, nitidez) por fotograma muestreado."""
    cmd = ["ffmpeg", "-v", "error", "-i", str(video),
           "-vf", f"fps={MUESTREO},scale={ANCHO}:{ALTO},format=gray",
           "-f", "rawvideo", "-pix_fmt", "gray", "-"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    tam = ANCHO * ALTO
    movimiento, nitidez, previo = [], [], None
    while True:
        crudo = proc.stdout.read(tam)
        if len(crudo) < tam:
            break
        f = np.frombuffer(crudo, dtype=np.uint8).reshape(ALTO, ANCHO).astype(np.float32)
        # Nitidez: cuanta energia hay en los bordes. El barrido de camara la aplasta.
        nitidez.append(float(np.abs(np.diff(f, axis=0)).mean() + np.abs(np.diff(f, axis=1)).mean()))
        movimiento.append(0.0 if previo is None else float(np.abs(f - previo).mean()))
        previo = f
    proc.stdout.close()
    proc.wait()
    return np.array(movimiento), np.array(nitidez)


def normalizar(v: np.ndarray) -> np.ndarray:
    if v.size == 0:
        return v
    lo, hi = np.percentile(v, 5), np.percentile(v, 95)
    if hi - lo < 1e-6:
        return np.zeros_like(v)
    return np.clip((v - lo) / (hi - lo), 0, 1)


def elegir(mov: np.ndarray, nit: np.ndarray, modo: str, dur: float,
           n: int, separacion: float, duracion_video: float) -> list:
    """Ventana deslizante + supresion de solapados: los N mejores momentos."""
    m, s = normalizar(mov), normalizar(nit)
    if modo == "producto":
        puntaje = 0.35 * m + 0.65 * s
    elif modo == "quieto":
        puntaje = 0.15 * m + 0.85 * s
    else:  # gato
        puntaje = 0.72 * m + 0.28 * s

    ventana = max(1, int(dur * MUESTREO))
    if len(puntaje) <= ventana:
        return [{"id": 1, "start": 0.0, "end": round(duracion_video, 2), "score": 100}]

    # Media movil = puntaje de cada ventana posible
    acum = np.concatenate([[0], np.cumsum(puntaje)])
    medias = (acum[ventana:] - acum[:-ventana]) / ventana

    elegidos = []
    orden = np.argsort(-medias)
    minimo = int(separacion * MUESTREO)
    for i in orden:
        if len(elegidos) >= n:
            break
        if all(abs(int(i) - j) >= minimo for j in elegidos):
            elegidos.append(int(i))

    elegidos.sort()
    bruto = medias[elegidos]
    tope = bruto.max() if bruto.size else 1
    salida = []
    for k, i in enumerate(elegidos, 1):
        ini = i / MUESTREO
        fin = min(ini + dur, duracion_video)
        salida.append({
            "id": k,
            "start": round(ini, 2),
            "end": round(fin, 2),
            "duracion": round(fin - ini, 2),
            "score": int(round(100 * medias[i] / tope)) if tope else 0,
            "movimiento": round(float(m[i:i + ventana].mean()), 3),
            "nitidez": round(float(s[i:i + ventana].mean()), 3),
        })
    return salida


def hoja_contacto(video: str, seg: dict, destino) -> str:
    """Tira de 4 fotogramas del candidato, para revisarlo de un vistazo."""
    out = str(destino / f"m{seg['id']:02d}_{int(seg['start'])}s.jpg")
    fps = 4.0 / max(seg["duracion"], 0.1)
    run(["ffmpeg", "-y", "-hide_banner", "-v", "error",
         "-ss", str(seg["start"]), "-t", str(seg["duracion"]), "-i", str(video),
         "-vf", f"fps={fps:.4f},scale=200:-1,tile=4x1", "-frames:v", "1", "-q:v", "4", out],
        check=False)
    return out


def main():
    ap = argparse.ArgumentParser(description="Detecta los mejores momentos de un video sin voz")
    ap.add_argument("video")
    ap.add_argument("--n", type=int, default=6, help="cuantos momentos proponer")
    ap.add_argument("--duracion", type=float, default=8.0, help="segundos por momento")
    ap.add_argument("--modo", default="gato", choices=["gato", "producto", "quieto"])
    ap.add_argument("--separacion", type=float,
                    help="segundos minimos entre momentos (default: la duracion, para que no se traslapen)")
    ap.add_argument("--output")
    ap.add_argument("--hojas", action="store_true", help="genera tiras de revision")
    args = ap.parse_args()

    info = media_info(args.video)
    mov, nit = perfil(args.video)
    if mov.size == 0:
        print("no pude leer fotogramas del video")
        return

    separacion = args.separacion if args.separacion is not None else args.duracion
    momentos = elegir(mov, nit, args.modo, args.duracion, args.n,
                      separacion, info["duration"])

    print(f"{info['width']}x{info['height']} | {hhmmss(info['duration'])} | modo {args.modo}")
    for m in momentos:
        print(f"  #{m['id']}: {hhmmss(m['start'])} -> {hhmmss(m['end'])} "
              f"({m['duracion']}s) puntaje {m['score']:3d} "
              f"[mov {m['movimiento']:.2f} nit {m['nitidez']:.2f}]")

    if args.hojas:
        destino = ensure_dir(workdir() / "momentos" / info["path"].split("\\")[-1].split("/")[-1].rsplit(".", 1)[0])
        for m in momentos:
            m["hoja"] = hoja_contacto(args.video, m, destino)
        print(f"  tiras de revision -> {destino}")

    if args.output:
        save_json(args.output, {"video": info["path"], "modo": args.modo, "segments": momentos})
        print(f"  -> {args.output}")


if __name__ == "__main__":
    main()
