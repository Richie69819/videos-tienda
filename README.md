# videos-tienda

Skill de Claude Code para convertir material crudo en **Reels / TikToks / Shorts de
1080x1920** listos para publicar: subtitulos animados palabra por palabra, gancho en
los primeros segundos, CTA de marca y exportacion con las specs de cada red.

Nace de combinar dos skills existentes y quitarles lo que estorbaba:

| | [claude-shorts](https://github.com/AgriciDaniel/claude-shorts) | [claude-code-skill-creatomate](https://github.com/Sara-Saraireh/claude-code-skill-creatomate) | **videos-tienda** |
|---|---|---|---|
| Motor de render | Remotion (necesita Node + Chrome headless) | API de pago en la nube | **FFmpeg + libass local**, nube opcional |
| Entrada | solo video largo | assets sueltos por URL | video largo, clip corto **o fotos** |
| Scripts | `.sh` (no corren en Windows) | SDK de Node | Python puro, multiplataforma |
| Costo por video | gratis | por minuto renderizado | gratis en local |
| Enfoque | cortes virales genericos | composicion generica | **vender producto** |

Lo que se conservo de cada una: el pipeline interactivo, la rubrica de puntuacion y las
specs de plataforma de `claude-shorts`; la idea de composicion declarativa desde assets
(slideshows con Ken Burns, textos por escena) y el motor en nube de `creatomate`.

## Que necesita

| | |
|---|---|
| **FFmpeg** (obligatorio) | con `libass`. `winget install Gyan.FFmpeg` |
| **Python 3.9+** (obligatorio) | solo libreria estandar para lo basico |
| GPU NVIDIA | opcional; con NVENC el render es 5-10x mas rapido |
| `faster-whisper` | opcional; solo para subtitulos automaticos desde el audio |
| `opencv-python` | opcional; mejora el reencuadre siguiendo rostros |
| Llave de Creatomate | opcional; solo para el motor en la nube |

```bash
pip install -r requirements.txt   # opcionales: whisper + opencv + numpy/pillow
```

## Instalacion

```powershell
# Windows
.\install.ps1
```

```bash
# Mac / Linux
bash install.sh
```

Copia la skill a `~/.claude/skills/videos-tienda` y verifica dependencias. Tambien
sirve clonar el repo directo en esa ruta.

## Uso

Dentro de Claude Code basta con pedirlo en lenguaje normal ("hazme un reel con estas
fotos", "sacame 3 cortes de este video"). Los scripts tambien corren sueltos:

```bash
# Fotos de producto -> reel vertical
python scripts/slideshow.py --imagenes fotos/ --out reel.mp4 \
    --textos "Anillo dona||PETG resistente||Envio gratis" \
    --gancho "Tu gato ya tiene|donde rascarse" --cta "michilab.store"

# Clip corto -> reel con subtitulos automaticos
python scripts/transcribe.py clip.mp4 --output transcript.json --idioma es
python scripts/render_clip.py --input clip.mp4 --out reel.mp4 \
    --captions transcript.json --estilo bold --gancho "Nadie te dice esto|del PETG"

# Video largo -> cortes (Claude elige los momentos leyendo la transcripcion)
python scripts/snap.py --segmentos aprobados.json --transcripcion transcript.json \
    --video largo.mp4 --output ajustados.json

# Cierre
python scripts/export.py --entrada renders/ --plataforma todas --salida videos/
python scripts/validate.py videos/
```

## Como funciona el render sin Node

Los subtitulos se generan como archivo **ASS** y los quema FFmpeg con libass. La
palabra activa se resalta emitiendo un evento por palabra con la pagina completa; la
entrada animada se hace con `\t()`. Las tipografias van en `assets/fonts/` y se pasan
con `fontsdir`, asi que no hace falta instalarlas en el sistema.

Resultado: un clip de 30 s se renderiza en segundos con NVENC, sin `npm install`, sin
Chrome headless y sin subir nada a ningun servidor.

## Estructura

```
SKILL.md                  el flujo que sigue Claude
references/
  rubrica.md              como puntuar segmentos de un video largo
  ganchos.md              moldes de gancho, guion y copy
  plataformas.md          specs y zonas seguras por red
  estilos.md              los 4 estilos de subtitulo
  reencuadre.md           las 3 estrategias de 9:16
  nube-creatomate.md      motor opcional en la nube
scripts/
  common.py               utilidades de FFmpeg y rutas
  preflight.py            chequeo de entorno y del archivo
  transcribe.py           faster-whisper con tiempos por palabra
  snap.py                 corta en frontera de frase, no a media palabra
  momentos.py             elige momentos por movimiento y nitidez (material sin voz)
  lote.py                 renderiza decenas de clips desde un plan JSON
  pantalla_final.py       cierre de marca (imagen suelta, tarjeta o velo)
  make_ass.py             motor de subtitulos animados
  reframe.py              decide el reencuadre 9:16
  render_clip.py          render de un clip vertical
  slideshow.py            fotos -> video con Ken Burns
  export.py               codificacion por plataforma
  validate.py             revision final antes de subir
  creatomate_render.py    motor en la nube (REST, sin SDK)
assets/fonts/             Montserrat, Bangers, Inter (OFL)
curso-photoshop/          curso gratuito de Photoshop en YouTube (guiones y plan)
```

## Curso de Photoshop en YouTube

`curso-photoshop/` lleva el plan completo de un curso gratuito de 30 clases, de abrir
el programa a generar 200 imagenes de producto sin tocar el raton: la malla, el plan de
lanzamiento, los guiones clase por clase y las referencias de automatizacion. Los
Shorts de cada clase se renderizan con los mismos scripts de este repo (`lote.py` y
`export.py`). Empieza en [curso-photoshop/README.md](curso-photoshop/README.md).

## Creditos

- [claude-shorts](https://github.com/AgriciDaniel/claude-shorts) de Daniel Agrici (MIT)
- [claude-code-skill-creatomate](https://github.com/Sara-Saraireh/claude-code-skill-creatomate) de Sara Saraireh (MIT)
- Tipografias Montserrat, Bangers e Inter bajo licencia OFL (ver `assets/fonts/OFL.txt`)

MIT. Ver [LICENSE](LICENSE).

