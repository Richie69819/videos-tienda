"""Transcripcion con faster-whisper y timestamps por palabra.

Salida en doble formato (igual que claude-shorts) para que Claude lea el texto
y el motor de subtitulos tenga los tiempos exactos:
  segments[] : {start, end, text, words[]}
  captions[] : {text, startMs, endMs}

Uso:
    python transcribe.py video.mp4 --output transcript.json [--modelo large-v3] [--idioma es]
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from common import die, media_info, save_json, workdir, run


def extraer_audio(video: Path) -> Path:
    """16 kHz mono wav: lo que Whisper quiere y pesa poco."""
    wav = workdir() / (video.stem + ".wav")
    run(["ffmpeg", "-y", "-hide_banner", "-v", "error", "-i", str(video),
         "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(wav)])
    return wav


def cargar_modelo(nombre: str, gpu: bool):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        die("falta faster-whisper. Instala:  pip install faster-whisper")

    if gpu:
        modelo = WhisperModel(nombre, device="cuda", compute_type="float16")
        print(f"modelo {nombre} en GPU (float16)")
    else:
        modelo = WhisperModel(nombre, device="cpu", compute_type="int8")
        print(f"modelo {nombre} en CPU (int8)")
    return modelo


def transcribir(modelo, wav, idioma):
    """Consume el generador completo aqui dentro.

    Importante: faster-whisper devuelve un generador perezoso, asi que los fallos
    de CUDA (por ejemplo cublas64_12.dll ausente) no aparecen al cargar el modelo
    sino al recorrer los segmentos. Por eso el consumo va dentro del try de main().
    """
    segmentos, meta = modelo.transcribe(
        str(wav), language=idioma, word_timestamps=True,
        vad_filter=True, vad_parameters={"min_silence_duration_ms": 400},
        beam_size=5,
    )
    out_segs, captions = [], []
    for s in segmentos:
        palabras = [{"start": round(w.start, 3), "end": round(w.end, 3), "word": w.word.strip()}
                    for w in (s.words or []) if w.word.strip()]
        out_segs.append({"start": round(s.start, 3), "end": round(s.end, 3),
                         "text": s.text.strip(), "words": palabras})
        captions.append({"text": s.text.strip(),
                         "startMs": int(s.start * 1000), "endMs": int(s.end * 1000)})
        print(f"  [{s.start:7.2f}] {s.text.strip()[:80]}")
    return out_segs, captions, meta


def main():
    ap = argparse.ArgumentParser(description="Transcribe con timestamps por palabra")
    ap.add_argument("entrada")
    ap.add_argument("--output", required=True)
    ap.add_argument("--modelo", default="large-v3",
                    help="tiny|base|small|medium|large-v3 (usa small si hay poca VRAM)")
    ap.add_argument("--idioma", default=None, help="es, en... (por defecto autodetecta)")
    ap.add_argument("--cpu", action="store_true")
    args = ap.parse_args()

    entrada = Path(args.entrada)
    info = media_info(entrada)
    if not info["has_audio"]:
        die("el archivo no tiene audio: no hay nada que transcribir")

    wav = extraer_audio(entrada)
    t0 = time.time()

    try:
        modelo = cargar_modelo(args.modelo, gpu=not args.cpu)
        out_segs, captions, meta = transcribir(modelo, wav, args.idioma)
    except Exception as e:
        if args.cpu:
            raise
        # Tipico en Windows sin las librerias CUDA de NVIDIA (cublas/cudnn):
        # el modelo carga pero truena al codificar. Se repite en CPU y listo.
        print(f"aviso: la GPU no pudo transcribir ({type(e).__name__}: "
              f"{str(e).splitlines()[0][:90]}); reintento en CPU")
        print("      para usar la GPU:  pip install nvidia-cublas-cu12 nvidia-cudnn-cu12")
        modelo = cargar_modelo(args.modelo, gpu=False)
        out_segs, captions, meta = transcribir(modelo, wav, args.idioma)

    n_palabras = sum(len(s["words"]) for s in out_segs)
    datos = {
        "language": meta.language,
        "language_probability": round(getattr(meta, "language_probability", 0) or 0, 3),
        "duration": round(info["duration"], 2),
        "model": args.modelo,
        "segments": out_segs,
        "captions": captions,
    }
    save_json(args.output, datos)
    print(f"\ntranscripcion -> {args.output}")
    print(f"  idioma {meta.language} | {len(out_segs)} segmentos | {n_palabras} palabras | "
          f"{time.time()-t0:.0f}s de proceso")


if __name__ == "__main__":
    main()
