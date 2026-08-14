#!/usr/bin/env bash
# Instala videos-tienda en ~/.claude/skills y revisa dependencias.
set -euo pipefail

ORIGEN="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DESTINO="$HOME/.claude/skills/videos-tienda"

if [ "$ORIGEN" != "$DESTINO" ]; then
    mkdir -p "$DESTINO"
    for item in SKILL.md README.md LICENSE requirements.txt; do
        [ -f "$ORIGEN/$item" ] && cp "$ORIGEN/$item" "$DESTINO/"
    done
    for carpeta in scripts references assets; do
        [ -d "$ORIGEN/$carpeta" ] && cp -r "$ORIGEN/$carpeta" "$DESTINO/"
    done
    echo "instalada en $DESTINO"
else
    echo "ya estas en la carpeta de skills: $DESTINO"
fi

echo
echo "== Dependencias =="

revisa() { # nombre comando obligatorio como_instalar
    if command -v "$2" >/dev/null 2>&1; then
        printf "  %-16s ok\n" "$1"
    elif [ "$3" = "si" ]; then
        printf "  %-16s FALTA (obligatorio) -> %s\n" "$1" "$4"
    else
        printf "  %-16s no instalado -> %s\n" "$1" "$4"
    fi
}

revisa "FFmpeg" ffmpeg  si "brew install ffmpeg  |  apt install ffmpeg"
revisa "Python" python3 si "https://python.org"

if command -v python3 >/dev/null 2>&1; then
    if python3 -c "import faster_whisper" 2>/dev/null; then
        printf "  %-16s ok\n" "faster-whisper"
    else
        printf "  %-16s no instalado -> pip install faster-whisper (solo para subtitulos automaticos)\n" "faster-whisper"
    fi
    if python3 -c "import cv2" 2>/dev/null; then
        printf "  %-16s ok\n" "opencv"
    else
        printf "  %-16s no instalado -> pip install opencv-python (mejora el reencuadre)\n" "opencv"
    fi
fi

if command -v ffmpeg >/dev/null 2>&1; then
    if ffmpeg -hide_banner -encoders 2>&1 | grep -q h264_nvenc; then
        printf "  %-16s disponible (render rapido)\n" "GPU NVENC"
    else
        printf "  %-16s no disponible (se usa CPU)\n" "GPU NVENC"
    fi
fi

echo
echo "Listo. Abre Claude Code y pide por ejemplo: 'hazme un reel con estas fotos'."
