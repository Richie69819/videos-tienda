# Especificaciones por plataforma

Todo sale en **1080x1920 (9:16), H.264, yuv420p, MP4 con faststart** y audio
normalizado a **-14 LUFS** (`loudnorm=I=-14:TP=-1:LRA=11`). Cada red recomprime lo que
subes; entregarle el bitrate que espera evita una segunda compresion agresiva.

## Codificacion (lo aplica `export.py`)

| | YouTube Shorts | TikTok | Instagram Reels |
|---|---|---|---|
| Sufijo del archivo | `_yt` | `_tt` | `_ig` |
| Control de tasa | 12 Mbps CBR-ish | CRF/CQ 18 | 4.5 Mbps |
| Maxrate / bufsize | 14M / 24M | 10M / 20M | 5M / 10M |
| Perfil / nivel | high / 4.2 | — | high / 4.2 |
| Audio | AAC 192k @ 48 kHz | AAC 128k @ 44.1 kHz | AAC 128k @ 44.1 kHz |
| Duracion maxima | 60 s | 180 s (segun cuenta) | 90 s |
| Peso maximo | 256 MB | 287 MB | 250 MB |

Con NVENC (`h264_nvenc -preset p5 -tune hq`) el render es 5-10x mas rapido que
`libx264 -preset slow` con calidad equivalente al mismo bitrate. Cualquier script
acepta `--cpu` para forzar CPU si el driver falla.

## Zonas seguras

La interfaz de cada red tapa parte de la pantalla. Estos valores son la mediana de
mediciones de la comunidad sobre 1080x1920 (ninguna plataforma publica los pixeles
oficiales); el margen inferior varia segun lo largo que sea la descripcion.

| Zona | TikTok | YouTube Shorts | Instagram Reels | Universal |
|---|---|---|---|---|
| Arriba | 150 px | 150 px | 210 px | 210 px |
| Abajo | 320 px | 350 px | 340 px | 450 px |
| Izquierda | 60 px | 60 px | 40 px | 60 px |
| Derecha | 120 px | 150 px | 100 px | 150 px |

`make_ass.py` coloca los subtitulos segun `--plataforma`:

| `--plataforma` | Margen inferior |
|---|---|
| `tiktok` | 380 px |
| `instagram` | 400 px |
| `youtube` | 420 px |
| `todas` (default) | 450 px |

Si vas a subir el **mismo archivo a las tres redes**, deja `todas`: 450 px libra
cualquier interfaz. Solo baja el margen si el video es exclusivo de una red.

El gancho ocupa la franja de arriba (220 px de margen superior) y solo aparece los
primeros ~3.5 s, asi que nunca choca con los subtitulos.

## Audio

- Normalizacion a -14 LUFS integrados, pico real -1 dBFS.
- Un video mudo rinde peor en TikTok y Reels: si el material no tiene audio, pon musica con `--musica`.
- Con voz + musica, la musica va a `0.12` de volumen (default de `render_clip.py`): se oye, no estorba.

## Lo que hay que revisar antes de subir

`validate.py` lo comprueba solo: resolucion 1080x1920, codec h264, pista de audio con
sonido real (no silencio), duracion dentro del limite, peso bajo el maximo y que el
archivo decodifique completo sin frames corruptos.
