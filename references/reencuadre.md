# Reencuadre 9:16

Un video horizontal metido a la fuerza en vertical pierde dos tercios de la imagen.
`reframe.py` decide como pasarlo y `render_clip.py` aplica la decision.

## Los tres modos

### `crop` — recorte al centro de interes
Escala hasta llenar 1080x1920 y recorta alrededor de un centro horizontal (`--centro`,
de 0 = izquierda a 1 = derecha). Es lo correcto cuando hay **un sujeto**: una persona
hablando, el gato, las manos armando algo. Llena la pantalla, que es lo que retiene.

### `blur` — encaja completo sobre fondo desenfocado
La imagen entra completa, centrada, y el fondo se rellena con la misma imagen ampliada
y desenfocada. Es el modo para **producto**: no se corta ni un pedazo de la pieza. Es
el default para fotos cuadradas de catalogo.

### `pantalla` — encaja a lo ancho sobre banda de marca
Para grabaciones de pantalla o material muy panoramico. El contenido va al 42% de la
altura (no al centro) para dejar aire abajo donde caen los subtitulos.

## Como se elige solo (`--contenido auto`)

1. Si el video **ya es vertical**, `crop` (el recorte es minimo).
2. Si se detectan **rostros**, `crop` centrado en la mediana de las caras.
3. Si es **muy panoramico** (mas de 2:1), `pantalla`.
4. Si no, `blur`: producto u objeto, se ve completo.

Puedes forzarlo con `--contenido persona|producto|pantalla`.

## Como se estima el centro

Se muestrean 12 fotogramas del clip a 320 px de ancho y:

- **Con OpenCV instalado** (opcional): deteccion de rostros Haar, y se toma la
  **mediana** de los centros — asi un falso positivo suelto no jala el encuadre.
- **Sin OpenCV** (default): centro de masa de la densidad de detalle. Se calcula la
  diferencia horizontal entre pixeles vecinos (donde hay bordes hay contenido), se
  suaviza y se toma el centroide. Para producto sobre fondo liso acierta bien.

El centro se limita para que la ventana de recorte no se salga de la imagen.

## Cuando corregir a mano

El automatico falla si hay dos sujetos separados o si el producto esta muy a un lado.
Se corrige sin volver a analizar:

```
python render_clip.py ... --modo crop --centro 0.32
```

Revisa un fotograma antes de renderizar todo el lote:

```
ffmpeg -y -ss 3 -i entrada.mp4 -frames:v 1 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920:x='(iw-ow)*0.32'" prueba.png
```
