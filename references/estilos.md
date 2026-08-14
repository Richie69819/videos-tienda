# Estilos de subtitulo

Los subtitulos se generan como archivo `.ass` y los quema FFmpeg con libass. No hace
falta Node, ni Remotion, ni Chrome headless: el render de un clip de 30 s tarda
segundos con NVENC.

## Los cuatro presets

| | `michilab` (default) | `bold` | `bounce` | `clean` |
|---|---|---|---|---|
| Tipografia | Montserrat ExtraBold | Montserrat ExtraBold | Bangers | Inter Bold |
| Tamano | 66 px | 72 px | 88 px | 56 px |
| Mayusculas | si | si | si | no |
| Color base | crema `#f5f2e9` | blanco | blanco | blanco |
| Palabra activa | naranja `#e08a5b` | amarillo `#FFD700` | color rotando | gris `#E0E0E0` |
| Contorno | olivo, 6 px | negro, 6 px | negro, 8 px | negro, 2 px + sombra |
| Palabras por pagina | 3 | 3 | 2 | 5 |
| Entrada | pop | pop | rebote grande | fundido |
| Para | producto de la tienda | educativo, explicaciones | entretenimiento, el gato | testimonios, tono serio |

Los colores que rota `bounce`: cian, magenta, verde, amarillo, naranja, rosa.

## Como se resuelve la animacion

ASS no tiene "springs" como Remotion, pero `\t()` interpola transformaciones y da el
mismo efecto percibido:

- **pop**: `\fscx86\fscy86\t(0,90,\fscx104\fscy104)\t(90,170,\fscx100\fscy100)` — entra al 86%, se pasa al 104%, se asienta en 100%.
- **rebote**: arranca en 70%, sube a 120%, cae a 100% en 230 ms.
- **fundido**: `\fad(160,0)`.

La animacion corre **solo en la primera palabra de cada pagina**. Si corriera en cada
palabra, la linea entera brincaria a cada rato y se ve barato.

## Palabra activa

Se emite un evento por palabra con la pagina completa y la palabra en curso teñida.
Es lo que da el efecto "karaoke" de TikTok. El karaoke nativo de ASS (`\k`) no sirve
aqui: deja pintadas todas las palabras ya dichas en vez de resaltar solo la actual.

Cada pagina desaparece antes de que empiece la siguiente; sin ese tope, dos paginas se
dibujan encimadas cuando no hay pausa entre ellas.

## Paginado

Una pagina se cierra cuando pasa cualquiera de estas tres cosas:
1. junto el maximo de palabras del estilo,
2. hay una pausa mayor a la ventana del estilo (600-1500 ms),
3. la ultima palabra termina en `.`, `!` o `?`.

Dentro de la pagina, las lineas se reparten por ancho de caracteres (14-26 segun estilo)
para que no salga una linea larguisima y otra de una palabra.

## Tipografias

Viven en `assets/fonts/` y se pasan a libass con `fontsdir`, asi que **no hace falta
instalarlas en el sistema**. Las tres son licencia OFL (ver `assets/fonts/OFL.txt`).

Ojo con el nombre de familia real, que no siempre coincide con el archivo:

| Archivo | Familia que ve libass |
|---|---|
| `Montserrat-Bold.ttf` | `Montserrat ExtraBold` |
| `Bangers-Regular.ttf` | `Bangers` |
| `Inter-Bold.ttf` | `Inter` |

Si agregas una fuente nueva y el texto sale con otra tipografia, casi siempre es que el
`Fontname` del estilo no coincide con la familia interna del `.ttf`.

## Capas

| Capa | Contenido | Posicion |
|---|---|---|
| 0 | subtitulos | abajo, margen segun plataforma |
| 1 | tarjetas de slideshow | abajo (o arriba con `--pos-texto arriba`) |
| 2 | gancho, primeros ~3.5 s | arriba, 220 px de margen |
| 3 | CTA, ultimos 2.6 s | arriba, caja solida olivo |
