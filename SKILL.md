---
name: videos-tienda
description: >-
  Estudio de video vertical para tiendas en linea: convierte videos largos, clips
  sueltos o fotos de producto en Reels / TikToks / Shorts 1080x1920 con subtitulos
  animados, gancho en los primeros segundos y CTA de marca. Motor local con FFmpeg
  (gratis, con GPU) y motor opcional en la nube con Creatomate. USAR cuando el usuario
  hable de "hacer un video/reel/tiktok/short", "video del producto", "subtitulos",
  "cortar un video largo", "sacar clips", "video con mis fotos", "timelapse de la
  impresion", "contenido para redes" o pase archivos de video/fotos para publicar.
  Complementa a la skill tiendas-en-linea (esa cotiza y sube productos; esta hace el video).
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - AskUserQuestion
---

# videos-tienda — estudio de video vertical para la tienda

Combina dos enfoques: el pipeline interactivo de extraccion de cortes de video largo
(claude-shorts) y la generacion de video por composicion desde assets (Creatomate),
en un solo flujo pensado para vender producto.

**Tu papel:** eres el editor. Analizas el material, propones los cortes y los textos,
el usuario aprueba, tu renderizas. Nunca renderices sin mostrar antes que vas a hacer.

## Antes de nada

Los scripts viven en `scripts/` dentro de esta misma carpeta de skill. En Windows se
invocan con `python`; en Mac/Linux con `python3`. Todas las rutas con espacios van
entre comillas.

Chequeo inicial (siempre, es rapido):

```
python "<SKILL>/scripts/preflight.py" "<archivo de entrada>"
```

Reporta FFmpeg, GPU NVENC, faster-whisper, espacio en disco y la salud del archivo
(resolucion, duracion, si trae audio, si el audio esta mudo). Si falta FFmpeg, para
y dilo: sin eso no hay nada que hacer.

## Elige el flujo

| Material que trae el usuario | Flujo | Script principal |
|---|---|---|
| Video largo **con voz** (podcast, live, explicacion) | **A. Cortes por transcripcion** | `transcribe.py` → `render_clip.py` |
| Grabaciones **sin voz** (el gato jugando, la pieza en la mano, timelapse) | **B. Cortes por imagen** | `momentos.py` → `render_clip.py` |
| Clip corto ya listo | **C. Clip directo** | `render_clip.py` |
| Solo fotos de producto | **D. Fotos** | `slideshow.py` |

Si no queda claro, pregunta con AskUserQuestion antes de procesar nada.

---

## Flujo A — video largo a cortes

### 1. Transcribir
```
python "<SKILL>/scripts/transcribe.py" "<video>" --output "%TEMP%/videos-tienda/transcript.json" --idioma es
```
Usa `--modelo small` si la GPU tiene poca VRAM o si urge. Reporta idioma, palabras y
tiempo que tardo.

### 2. Analizar (esto lo haces tu, no un script)
Lee `transcript.json` y `references/rubrica.md`. Puntua **8-12 candidatos** de 15-55 s
con las 6 dimensiones de la rubrica (las 5 clasicas mas **intencion de compra**, que es
la que importa en una tienda). Para cada candidato define:

- inicio y fin en segundos
- gancho de 2 lineas (`"linea 1|linea 2"`) que **no repita** lo que se oye
- una frase de por que funciona

Al leer la transcripcion, limpia tambien el texto para los subtitulos: quita muletillas
(este, o sea, eh, como que), corrige errores obvios de transcripcion y **no toques los
tiempos**. Guarda el resultado como `transcript_limpio.json` con la misma estructura.

### 3. Presentar y aprobar
Muestra una tabla y pregunta con AskUserQuestion: que cortes, que estilo de subtitulo,
que plataforma.

```
| # | Tiempo        | Dur | Pts | Gancho                        | Por que                          |
|---|---------------|-----|-----|-------------------------------|----------------------------------|
| 1 | 04:22 → 05:01 | 39s | 87  | "Nadie te dice esto del PETG" | Dato concreto + objecion resuelta|
```

Nunca renderices cortes que el usuario no aprobo.

### 4. Ajustar los cortes
```
python "<SKILL>/scripts/snap.py" --segmentos aprobados.json --transcripcion transcript.json --video "<video>" --output ajustados.json
```
Mueve los cortes a inicio de palabra / fin de frase / silencio real. Reporta los deltas.

### 5. Renderizar cada corte
```
python "<SKILL>/scripts/render_clip.py" --input "<video>" --desde 262 --hasta 301 --out "corto_01.mp4" --captions transcript_limpio.json --estilo bold --gancho "Nadie te dice esto|del PETG" --cta "michilab.store"
```

### 6. Exportar y validar (ver "Cierre")

---

## Flujo B — muchos clips de material sin voz

Es el caso normal de una tienda: grabaciones de la mascota usando el producto o de la
pieza girando en la mano, sin locucion. Aqui no hay transcripcion que analizar, asi que
los momentos se eligen por **imagen**.

### 1. Detectar momentos
```
python "<SKILL>/scripts/momentos.py" "<video>" --n 5 --duracion 8 --modo gato --hojas --output momentos.json
```

- `--modo gato` pesa el movimiento: zarpazo, salto, persecucion.
- `--modo producto` pesa la nitidez: la pieza quieta y enfocada en la mano.
- `--modo quieto` para plano fijo de producto.
- `--hojas` genera una tira de 4 fotogramas por candidato.

### 2. Revisar las tiras con tus propios ojos
**Lee las tiras que genero `--hojas` antes de renderizar.** El detector mide movimiento
y nitidez, no entiende la escena: puede proponer un tramo donde el producto ya salio de
cuadro o donde solo se ve el fondo. Descarta esos y quedate con los buenos.

### 3. Renderizar el lote
Escribe un plan en JSON (un clip por entrada, con su gancho) y renderiza todo junto:

```
python "<SKILL>/scripts/lote.py" --plan plan.json --salida "./Para publicar" --validar
```

El plan se guarda en UTF-8, asi que los acentos y los signos de interrogacion llegan
intactos a los subtitulos — pasarlos como argumento por la consola de Windows los rompe.
Referencia del formato en el encabezado de `lote.py`.

Varia el gancho entre clips del mismo producto: es la forma barata de descubrir que
angulo retiene. Ritmo de referencia: 10 clips de 7-8 s se renderizan en ~50 s con NVENC.

### 4. Exportar y validar (ver "Cierre")

## Flujo C — clip corto ya grabado

Un solo comando. Si el clip no tiene voz, usa `--sin-subtitulos` y apoyate en el gancho,
los textos y la musica.

```
python "<SKILL>/scripts/render_clip.py" --input "clip.mp4" --out "reel.mp4" --contenido producto --gancho "Se imprime en 4 horas|y aguanta garras" --cta "michilab.store" --musica "pista.mp3"
```

Opciones que importan:
- `--contenido persona|producto|pantalla` decide el reencuadre (rostro, fondo desenfocado, banda de marca). `auto` lo detecta solo.
- `--centro 0.0-1.0` corrige a mano si el reencuadre automatico corta mal el producto.
- `--velocidad 1.08` acelera un poco: retiene mas en TikTok sin que se note.
- `--audio limpio --nivel-audio -18` para grabaciones de celular a distancia: el audio crudo viene muy bajo (-40 dB) y normalizarlo a -14 sube el zumbido del cuarto. `limpio` recorta graves y aplica denoise antes de normalizar. `--audio mudo` si vas a poner musica encima.

## Flujo D — fotos de producto a video

```
python "<SKILL>/scripts/slideshow.py" --imagenes "carpeta-fotos" --out "reel.mp4" --segundos 2.6 --estilo michilab --textos "Anillo dona||PETG resistente||Envio gratis" --gancho "Tu gato ya tiene|donde rascarse" --cta "michilab.store" --musica "pista.mp3"
```

- `--textos` lleva un texto por foto separados por `|` (vacio = esa foto sin texto).
- `--fondo blur` (default) se ve mejor con fotos cuadradas de producto; `olivo` y `crema` son de marca.
- `--zoom alterna` da el efecto Ken Burns variando el movimiento en cada foto.

Un reel de 5-6 fotos a 2.6 s queda en ~14 s, que es la duracion que mejor retiene.

---

## Cierre (los tres flujos terminan igual)

```
python "<SKILL>/scripts/export.py" --entrada "<carpeta o archivo>" --plataforma todas --salida "./videos"
python "<SKILL>/scripts/validate.py" "./videos"
```

`export.py` genera una variante por red (`_yt`, `_tt`, `_ig`) con el bitrate y el
loudness que cada una espera. `validate.py` revisa resolucion, codec, audio real y
peso; **si marca error, no entregues el archivo**: vuelve a renderizar.

Cierra con una tabla de archivos y una propuesta de copy + hashtags para publicar.

---

## Reglas

1. **Preflight siempre**, antes de procesar.
2. **Aprobacion antes de renderizar** en los flujos A y B (los que eligen que cortar). En C y D basta con describir que vas a hacer.
3. **Gancho en los primeros 3 segundos, siempre.** Sin gancho el video no retiene.
4. **El gancho no repite lo que se escucha**, lo complementa.
5. **Nada de social proof inventado** (ventas, clientes felices, testimonios). Regla de marca.
6. **Sin emojis de corazon** en textos ni copy; el emoji de la marca es 🐾.
7. **Costos:** el motor local es gratis (solo luz). Creatomate cobra por minuto renderizado; usalo solo si el usuario lo pide.
8. **Nunca subas ni publiques nada** a redes ni a la tienda sin permiso explicito de esa tanda.
9. Si un render falla, lee el error de FFmpeg y arreglalo; no entregues un archivo a medias.
10. Los temporales viven en `%TEMP%/videos-tienda` (configurable con `VIDEOS_TIENDA_TMP`). Ofrece limpiarlos al terminar.

## Estilos de subtitulo

| Estilo | Tipografia | Look | Para |
|---|---|---|---|
| `michilab` | Montserrat ExtraBold | crema con palabra activa naranja | **default** de la tienda |
| `bold` | Montserrat ExtraBold | MAYUSCULAS, palabra activa amarilla | educativo, explicaciones |
| `bounce` | Bangers | colores rotando y rebote | entretenimiento, el gato haciendo desastre |
| `clean` | Inter Bold | minimalista blanco | testimonios, tono serio |

Detalle visual en `references/estilos.md`.

## Referencias

| Necesitas | Lee |
|---|---|
| Puntuar segmentos de un video largo | `references/rubrica.md` |
| Escribir el gancho / guion del video | `references/ganchos.md` |
| Specs y zonas seguras de cada red | `references/plataformas.md` |
| Ajustar el look de los subtitulos | `references/estilos.md` |
| Decidir el reencuadre 9:16 | `references/reencuadre.md` |
| Render en la nube / plantillas | `references/nube-creatomate.md` |

## Cuando algo falla

- **Whisper no usa la GPU** (`cublas64_12.dll no encontrado`): el script reintenta en CPU solo y avisa; con `--modelo small` el tiempo es aceptable. Para habilitar la GPU: `pip install nvidia-cublas-cu12 nvidia-cudnn-cu12`.
- **Subtitulos sin tipografia correcta:** libass toma las fuentes de `assets/fonts/`; si el texto sale con otra fuente, revisa que ese .ttf siga ahi.
- **FFmpeg se queja del filtergraph en Windows:** casi siempre es una ruta con `:` o espacios; los scripts ya trabajan con rutas relativas desde el temporal.
- **NVENC falla:** agrega `--cpu` a cualquier script.
