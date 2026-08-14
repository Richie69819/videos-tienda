"""Utilidades compartidas del motor local (FFmpeg + Python).

Todo el pipeline de videos-tienda pasa por aqui: sondeo de archivos, deteccion de
GPU, rutas seguras para filtergraphs de FFmpeg y presets de codificacion.

No requiere dependencias externas: solo FFmpeg en el PATH.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Lienzo vertical estandar para Reels / TikTok / Shorts
W, H, FPS = 1080, 1920, 30

# Paleta Michilab
OLIVO = "#5a6640"
CREMA = "#f5f2e9"
NARANJA = "#e08a5b"


# --------------------------------------------------------------------------- #
# Ejecucion
# --------------------------------------------------------------------------- #
def die(msg: str, code: int = 1):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(code)


def run(args, cwd=None, check=True, quiet=True):
    """Ejecuta un comando y devuelve CompletedProcess (stdout/stderr como texto)."""
    proc = subprocess.run(
        args,
        cwd=str(cwd) if cwd else None,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and proc.returncode != 0:
        tail = "\n".join((proc.stderr or "").strip().splitlines()[-25:])
        die(f"fallo el comando:\n  {' '.join(str(a) for a in args)}\n{tail}")
    if not quiet:
        print(proc.stdout)
    return proc


def need(binary: str):
    path = shutil.which(binary)
    if not path:
        die(f"no encuentro '{binary}' en el PATH. Instalalo antes de continuar.")
    return path


# --------------------------------------------------------------------------- #
# Sondeo de medios
# --------------------------------------------------------------------------- #
def ffprobe_raw(path) -> dict:
    need("ffprobe")
    proc = run([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", str(path),
    ])
    return json.loads(proc.stdout or "{}")


def media_info(path) -> dict:
    """Resumen practico de un archivo de video/audio/imagen."""
    p = Path(path)
    if not p.exists():
        die(f"no existe el archivo: {p}")
    raw = ffprobe_raw(p)
    v = next((s for s in raw.get("streams", []) if s.get("codec_type") == "video"), None)
    a = next((s for s in raw.get("streams", []) if s.get("codec_type") == "audio"), None)
    fmt = raw.get("format", {})

    fps = 0.0
    if v and v.get("avg_frame_rate", "0/0") not in ("0/0", None):
        num, _, den = v["avg_frame_rate"].partition("/")
        try:
            fps = float(num) / float(den or 1)
        except (ValueError, ZeroDivisionError):
            fps = 0.0

    return {
        "path": str(p.resolve()),
        "duration": float(fmt.get("duration") or (v or {}).get("duration") or 0.0),
        "size": int(fmt.get("size") or p.stat().st_size),
        "width": int((v or {}).get("width") or 0),
        "height": int((v or {}).get("height") or 0),
        "fps": round(fps, 3),
        "vcodec": (v or {}).get("codec_name"),
        "acodec": (a or {}).get("codec_name"),
        "has_video": v is not None,
        "has_audio": a is not None,
    }


# --------------------------------------------------------------------------- #
# GPU / codificacion
# --------------------------------------------------------------------------- #
def has_nvenc() -> bool:
    """True si este FFmpeg trae h264_nvenc Y la GPU responde de verdad."""
    need("ffmpeg")
    listed = run(["ffmpeg", "-hide_banner", "-encoders"], check=False)
    if "h264_nvenc" not in (listed.stdout or ""):
        return False
    # Prueba real: 1 frame de color a nul. Si no hay driver, falla aqui y no en produccion.
    probe = run([
        "ffmpeg", "-hide_banner", "-v", "error", "-f", "lavfi",
        "-i", "color=c=black:s=256x256:d=0.1", "-c:v", "h264_nvenc",
        "-frames:v", "1", "-f", "null", "-",
    ], check=False)
    return probe.returncode == 0


def video_args(gpu: bool, quality: str = "alta") -> list:
    """Argumentos del codificador de video para renders intermedios y finales."""
    if gpu:
        cq = {"alta": "19", "media": "23", "borrador": "28"}[quality]
        return ["-c:v", "h264_nvenc", "-preset", "p5", "-tune", "hq",
                "-rc", "vbr", "-cq", cq, "-b:v", "0", "-pix_fmt", "yuv420p"]
    crf = {"alta": "18", "media": "22", "borrador": "27"}[quality]
    preset = "medium" if quality != "borrador" else "veryfast"
    return ["-c:v", "libx264", "-preset", preset, "-crf", crf, "-pix_fmt", "yuv420p"]


# --------------------------------------------------------------------------- #
# Rutas dentro de filtergraphs (el dolor de cabeza de Windows)
# --------------------------------------------------------------------------- #
def filter_path(path, cwd=None) -> str:
    """Devuelve una ruta usable dentro de un filtro de FFmpeg.

    FFmpeg parte los filtros por ':' y ',', asi que 'C:\\Users\\...' rompe el
    filtergraph. Preferimos una ruta relativa al cwd del proceso (sin ':' ni
    '\\'); si no se puede (otra unidad), escapamos la absoluta.
    """
    p = Path(path).resolve()
    if cwd:
        try:
            rel = os.path.relpath(p, Path(cwd).resolve())
            if ":" not in rel:
                return rel.replace("\\", "/")
        except ValueError:
            pass  # unidades distintas en Windows
    return str(p).replace("\\", "/").replace(":", r"\:")


def subtitles_filter(ass_path, cwd) -> str:
    """Filtro `subtitles` con la carpeta de fuentes de la skill.

    Se pasa fontsdir para que libass encuentre Montserrat/Bangers/Inter aunque
    no esten instaladas en el sistema.
    """
    ass = filter_path(ass_path, cwd)
    fdir = filter_path(fonts_dir(), cwd)
    return f"subtitles=filename='{ass}':fontsdir='{fdir}'"


def ensure_dir(path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def workdir(name: str = "videos-tienda") -> Path:
    """Carpeta temporal de trabajo (configurable con VIDEOS_TIENDA_TMP)."""
    base = os.environ.get("VIDEOS_TIENDA_TMP")
    if not base:
        base = os.path.join(os.environ.get("TEMP") or "/tmp", name)
    return ensure_dir(base)


def skill_root() -> Path:
    return Path(__file__).resolve().parent.parent


def fonts_dir() -> Path:
    return skill_root() / "assets" / "fonts"


def hhmmss(seconds: float) -> str:
    seconds = max(0.0, float(seconds))
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def load_json(path) -> dict:
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(path, data):
    ensure_dir(Path(path).parent)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    return path
