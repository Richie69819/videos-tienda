"""Ajusta los cortes a fronteras naturales de habla (nunca a media palabra).

Toma los segmentos aprobados por el usuario y los mueve unos milisegundos hasta
el arranque de palabra / fin de frase mas cercano, ademas de buscar silencios
reales en el audio con FFmpeg silencedetect.

Uso:
    python snap.py --segmentos aprobados.json --transcripcion transcript.json \
        --video entrada.mp4 --output ajustados.json [--sin-silencio]
"""
from __future__ import annotations

import argparse
import re

from common import load_json, media_info, run, save_json

MIN_DUR, MAX_DUR = 4.0, 90.0
VENTANA_INICIO = 1.2   # s hacia atras que aceptamos mover el inicio
VENTANA_FIN = 3.0      # s hacia adelante que aceptamos alargar el final
COLA = 0.30            # s de aire despues de la ultima palabra


def todas_las_palabras(transcripcion: dict) -> list:
    palabras = []
    for s in transcripcion.get("segments", []):
        for w in s.get("words", []) or []:
            palabras.append({"ini": float(w["start"]), "fin": float(w["end"]),
                             "t": (w.get("word") or "").strip()})
    return sorted(palabras, key=lambda w: w["ini"])


def silencios(video: str, duracion: float) -> list:
    """Intervalos de silencio detectados por FFmpeg: [(inicio, fin), ...]."""
    proc = run(["ffmpeg", "-hide_banner", "-i", video, "-af",
                "silencedetect=noise=-32dB:d=0.25", "-f", "null", "-"], check=False)
    salida, res, abierto = proc.stderr or "", [], None
    for linea in salida.splitlines():
        m = re.search(r"silence_start:\s*(-?[\d.]+)", linea)
        if m:
            abierto = float(m.group(1))
        m = re.search(r"silence_end:\s*([\d.]+)", linea)
        if m and abierto is not None:
            res.append((abierto, float(m.group(1))))
            abierto = None
    if abierto is not None:
        res.append((abierto, duracion))
    return res


def silencio_cercano(puntos: list, t: float, radio: float = 0.6):
    """Centro del silencio mas cercano a t, si cae dentro del radio."""
    mejor, dist = None, radio
    for ini, fin in puntos:
        centro = (ini + fin) / 2
        if abs(centro - t) < dist:
            mejor, dist = centro, abs(centro - t)
    return mejor


def ajustar(seg: dict, palabras: list, sil: list, duracion: float) -> dict:
    ini_orig, fin_orig = float(seg["start"]), float(seg["end"])

    # --- inicio: retroceder al arranque de la palabra que estemos partiendo ---
    ini = ini_orig
    candidatas = [w for w in palabras if abs(w["ini"] - ini_orig) <= VENTANA_INICIO]
    if candidatas:
        # Preferimos una palabra que inicie frase (la anterior termina en . ! ?)
        inicio_frase = []
        for w in candidatas:
            previas = [p for p in palabras if p["fin"] <= w["ini"]]
            if not previas or re.search(r"[.!?]$", previas[-1]["t"]):
                inicio_frase.append(w)
        elegida = min(inicio_frase or candidatas, key=lambda w: abs(w["ini"] - ini_orig))
        ini = max(0.0, elegida["ini"] - 0.12)
    # Si hay un silencio justo ahi, cortamos en medio del silencio: suena limpio.
    s = silencio_cercano(sil, ini)
    if s is not None:
        ini = max(0.0, s)

    # --- fin: alargar hasta terminar la frase ---
    fin = fin_orig
    posteriores = [w for w in palabras if w["fin"] > fin_orig - 0.05]
    for w in posteriores:
        if w["fin"] > fin_orig + VENTANA_FIN:
            break
        if re.search(r"[.!?]$", w["t"]):
            fin = w["fin"]
            break
    else:
        dentro = [w for w in palabras if w["ini"] < fin_orig < w["fin"]]
        if dentro:
            fin = dentro[-1]["fin"]
    fin += COLA
    s = silencio_cercano(sil, fin)
    if s is not None and s > ini + MIN_DUR:
        fin = s

    fin = min(fin, duracion)
    if fin - ini < MIN_DUR:
        fin = min(duracion, ini + MIN_DUR)
    if fin - ini > MAX_DUR:
        fin = ini + MAX_DUR

    r = dict(seg)
    r.update(start=round(ini, 3), end=round(fin, 3),
             duracion=round(fin - ini, 2),
             delta_inicio_ms=int((ini - ini_orig) * 1000),
             delta_fin_ms=int((fin - fin_orig) * 1000))
    return r


def main():
    ap = argparse.ArgumentParser(description="Ajusta cortes a fronteras de habla")
    ap.add_argument("--segmentos", required=True)
    ap.add_argument("--transcripcion", required=True)
    ap.add_argument("--video", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--sin-silencio", action="store_true", help="mas rapido: solo palabras")
    args = ap.parse_args()

    datos = load_json(args.segmentos)
    palabras = todas_las_palabras(load_json(args.transcripcion))
    duracion = media_info(args.video)["duration"]
    sil = [] if args.sin_silencio else silencios(args.video, duracion)
    if not args.sin_silencio:
        print(f"{len(sil)} silencios detectados")

    ajustados = [ajustar(s, palabras, sil, duracion) for s in datos["segments"]]
    salida = dict(datos)
    salida["segments"] = ajustados
    save_json(args.output, salida)

    for s in ajustados:
        print(f"  #{s.get('id','?')}: {s['start']:.2f} -> {s['end']:.2f} "
              f"({s['duracion']}s) | inicio {s['delta_inicio_ms']:+d}ms, fin {s['delta_fin_ms']:+d}ms")
    print(f"\najustados -> {args.output}")


if __name__ == "__main__":
    main()
