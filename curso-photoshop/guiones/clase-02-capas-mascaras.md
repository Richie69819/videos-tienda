# Clase 2 — Capas y máscaras

La clase bisagra. Si el espectador entiende la máscara, las 28 clases que siguen son
cuesta abajo; si no la entiende, va a sufrir en todas. Por eso va en el día 1 y por eso
dura 14 minutos y no 8.

La idea que hay que dejar clavada: **en Photoshop no se borra. Se tapa.**

## Ficha

| | |
|---|---|
| Clase | 2 de 30 |
| Título | `Curso de Photoshop desde cero — Clase 2: capas y máscaras explicadas de una vez` |
| Duración objetivo | 14:00 |
| Entrega | `02-ficha.jpg`: producto + texto + logo en capas separadas, con el fondo tapado con máscara (no borrado) |
| Requisitos | clase 1 |
| Dónde se puede hacer | Photopea, completo |
| Archivos | `clase-02/` con las fotos, el logo en PNG y el PSD en dos estados: a medias y terminado |
| Atajos nuevos | Ctrl+J, Ctrl+G, Ctrl+Shift+N, Alt+clic, Ctrl+D, F7, X, D, Ctrl+Shift+S |

## Miniatura

- Texto: **NO BORRES**
- Color del módulo 1: naranja de marca
- Qué se ve: la misma foto dos veces, una con el fondo borrado a mordidas y otra limpia
  con la máscara. El borrador tachado.

---

## Guion

### 0:00-0:15 · Gancho y promesa

> **PANTALLA:** una foto con el fondo borrado con el borrador, fea, con mordidas. Al
> lado, la misma con máscara, perfecta, y el fondo **volviendo a aparecer** de un clic.

> "Al final de este video vas a entender lo único que de verdad hay que entender de
> Photoshop, y vas a tener esta ficha de producto hecha por ti. Catorce minutos. Si
> siempre has borrado con el borrador, esto te va a cambiar la forma de trabajar."

### 0:15-2:30 · Teoría: capas

> **PANTALLA:** tres acetatos de verdad, en la mano, encimados frente a la cámara. Si
> no hay cámara, tres rectángulos en pantalla que se separan en perspectiva.

> "Una capa es una hoja transparente. Tu archivo es un montón de hojas encimadas, y lo
> que ves es lo que se ve desde arriba. Eso es todo. No hay más."

> "Tres consecuencias, y de ahí sale el ochenta por ciento de los problemas de un
> principiante:"

> "**Una:** el orden importa. Lo de arriba tapa lo de abajo. En el panel, arriba es
> arriba."

> "**Dos:** solo le haces cosas a la capa **seleccionada**. Cuando algo no funciona, el
> noventa por ciento de las veces es esto: estás trabajando en la capa equivocada.
> Mírame."

> **ERROR A PROPÓSITO:** pintar con el pincel teniendo seleccionada la capa de abajo y
> no ver nada en pantalla.
> "Estoy pintando y no pasa nada... porque estoy pintando debajo de la foto. Pasa a
> todos, todos los días. Mira el panel de capas antes de culpar al programa."

> "**Tres:** cada cosa en su capa. El producto en una, el texto en otra, el logo en
> otra. Cuesta diez segundos más y te permite cambiar una cosa sin rehacer el resto."

**Los controles del panel (F7):**

| Control | Qué hace | Para qué sirve de verdad |
|---|---|---|
| El ojo | Enciende y apaga la capa | Comparar antes y después en un clic |
| Opacidad | Transparencia de la capa | Bajar el logo al 60% para que no grite |
| Bloqueo | Candado | Que no muevas el fondo sin querer |
| Modo de fusión | Cómo se mezcla con la de abajo | De los ~27, se usan 3: **Multiplicar**, **Trama**, **Luz suave** |

> "Los modos de fusión los vas a ver en todos los tutoriales de internet y en todos
> suenan a brujería. Son esto: Multiplicar oscurece y deja pasar lo blanco. Trama
> aclara y deja pasar lo negro. Luz suave sube el contraste. Esos tres, el resto cuando
> tengas tiempo libre."

**Atajos de capas:**

| Atajo | Qué hace |
|---|---|
| **Ctrl+J** | Duplicar la capa. Antes de arriesgar algo, duplica |
| **Ctrl+Shift+N** | Capa nueva vacía |
| **Ctrl+G** | Agrupar las seleccionadas (carpetas, para no perderte en 20 capas) |
| **F7** | Mostrar u ocultar el panel |
| **Alt+clic en el ojo** | Ver **solo** esa capa. El mejor atajo del panel y casi nadie lo sabe |

### 2:30-6:30 · Teoría y práctica: la máscara

> **PANTALLA:** la foto del producto con fondo, el botón de máscara marcado.

> "Ahora lo importante. Quiero quitarle el fondo a esta foto. La forma en que lo hace un
> principiante es con el borrador: **E**, y a tallar. Lo voy a hacer para que veas por
> qué no."

> **ERROR A PROPÓSITO:** borrar un pedazo del fondo con el borrador, incluyendo una
> mordida al producto.
> "Mordí el producto. Y lo peor: eso ya no está. Si guardo y cierro, perdí esos
> píxeles para siempre. **Ctrl+Z**."

> "La forma correcta: una máscara. Con la capa seleccionada, este botón de abajo del
> panel —el rectángulo con el círculo— agrega una máscara de capa. Fíjate que aparece
> un cuadrito blanco al lado de la miniatura de la capa."

> **TEXTO EN PANTALLA, grande, 5 segundos:** `NEGRO TAPA · BLANCO MUESTRA`

> "Esa es la regla completa, y es lo único que tienes que memorizar hoy: en una
> máscara, **lo que pintas de negro se tapa, y lo que pintas de blanco se vuelve a
> ver**. La máscara no es la imagen: es una instrucción de qué se muestra."

> "Entonces: clic en el cuadrito blanco de la máscara, **B** de pincel, **D** para poner
> los colores en negro y blanco por defecto, y **X** para intercambiar entre uno y otro.
> Pinto de negro sobre el fondo... y se va. Pero mira: me pasé y me comí la oreja del
> producto. **X**, ahora tengo blanco, pinto encima... y **regresa**. No lo recuperé de
> la basura: nunca se fue."

> "Eso es la diferencia. El borrador destruye; la máscara tapa. Y tapar es reversible
> para siempre, hasta dentro de dos años cuando abras el archivo."

> **PANTALLA:** apagar la máscara con Shift+clic en su miniatura para mostrar que la
> foto sigue completa debajo.

> "Shift más clic en la máscara la apaga: la foto está entera, intacta. Siempre estuvo."

**La trampa que le pasa a todo el mundo:**

> **ERROR A PROPÓSITO:** tener seleccionada la capa (no la máscara) y pintar negro
> encima de la foto.
> "Acabo de pintar un brochazo negro sobre mi producto. Es que tenía seleccionada la
> **capa**, no la **máscara**. Fíjate en el borde blanco: el recuadro te dice en cuál
> estás parado. Antes de pintar en una máscara, clic en la máscara. **Ctrl+Z**."

### 6:30-12:00 · Práctica: la ficha de producto

> "Vamos a armar la entrega. Cuatro capas, y cada una con un trabajo."

1. **Ctrl+N**, 1080x1920, 72 ppp, RGB. **Ctrl+S** como `02-ficha.psd`. (Repetido de la
   clase 1, a propósito, sin disculparse: "esto lo vas a hacer treinta veces.")
2. **El fondo:** capa nueva (**Ctrl+Shift+N**), rellenar de color de marca con la
   herramienta de bote o **Alt+Supr** con el color frontal puesto. "Nombra la capa:
   doble clic en el nombre, 'fondo'. En veinte capas vas a agradecerlo."
3. **El producto:** arrastrar la foto, **Ctrl+T** para acomodar, **Enter**. Máscara, y
   pintar de negro el fondo de la foto. "Zoom con Alt+rueda para los bordes, pincel
   chico. No tiene que quedar perfecto: en la clase tres lo hacemos en dos clics con
   Seleccionar sujeto. Hoy lo hacemos a mano para que entiendas qué está pasando
   cuando esos dos clics lo hagan por ti."
4. **El texto:** **T**, el nombre del producto, **Ctrl+Enter** para cerrar. Segunda capa
   de texto con el precio o el material. "Dos textos, dos capas. Nunca los dos en la
   misma: si van en la misma, no puedes mover uno sin mover el otro."
5. **El logo:** arrastrar el PNG. Opacidad al 70%. "Un logo al cien por ciento compite
   con tu producto. Al setenta acompaña."
6. **Ctrl+G** sobre las capas de texto: una carpeta llamada "textos". "Con cinco capas
   parece exagerado. En la clase veintiuno vas a tener treinta."
7. **Guardar los dos archivos:** **Ctrl+S** para el PSD (el que puedes seguir
   editando), **Ctrl+Shift+Alt+W** para el JPG (el que se sube). "El PSD no se sube a
   ningún lado y no se borra nunca. Es tu original."

> **ERROR A PROPÓSITO:** intentar mover el producto con la capa de texto seleccionada y
> mover el texto. "Capa equivocada. Otra vez. Te va a pasar mil veces y siempre se
> arregla igual: mira el panel."

### 12:00-13:30 · Tres cosas que valen oro

> "Tres cosas que no te va a decir un tutorial de treinta segundos:"

> "**Una:** nombra las capas. Cuesta tres segundos. 'Capa 14 copia 3 copia' es la razón
> por la que la gente abandona sus propios archivos."

> "**Dos:** duplica antes de arriesgar. **Ctrl+J**, y experimenta en la copia. Si sale
> mal, borras la copia y no perdiste nada."

> "**Tres:** Alt más clic en el ojo de una capa te la deja ver sola, con todo lo demás
> apagado, y otro Alt más clic lo devuelve todo. Para saber qué capa es cuál cuando ya
> tienes veinte, esto vale más que ordenarlas."

### Cierre (últimos 20 s)

> "Tu reto: sube tu ficha a los comentarios y dime cuántas capas usaste. Si usaste una
> sola, vuelve al minuto seis."

> "Suscríbete y la clase tres te llega mañana: selecciones. Ahí vas a quitar ese fondo
> en dos clics, y vas a entender lo que esos dos clics están haciendo porque hoy lo
> hiciste a mano."

> **PANTALLA FINAL:** Clase 3.

---

## Shorts de esta clase

```
SHORT 1: gancho="Deja de borrar|en Photoshop"                → borrador vs máscara, 20 s
SHORT 2: gancho="Negro tapa, blanco muestra|ya sabes máscaras" → la regla, 15 s
SHORT 3: gancho="Alt + clic en el ojo|nadie te dijo esto"     → ver una capa sola, 14 s
```

## Descripción

```
Capas y máscaras, el único concepto que de verdad hay que entender de Photoshop. Al
final tienes tu ficha de producto en capas separadas.

PSD de la clase (a medias y terminado): [link]
Lista completa del curso: [link]
Clase anterior (Clase 1 — Interfaz y atajos): [link]  ·  Clase siguiente (Clase 3 — Selecciones): [link]

Minutos:
00:00 Lo que vas a tener al final
00:15 Qué es una capa (y por qué "no me sale" casi siempre es esto)
02:30 Máscaras: negro tapa, blanco muestra
04:40 Por qué el borrador destruye y la máscara no
06:30 Armamos la ficha de producto, capa por capa
12:00 Tres costumbres que te van a ahorrar horas

Esta clase se puede hacer completa en Photopea, gratis, desde el navegador.

#photoshop #cursodephotoshop #capas #mascaras
```

## Comentario fijado

```
PSD de la clase + logo + fotos: [link]
Viene en dos estados: a medias (para que lo termines conmigo) y terminado (para
comparar). Sube tu ficha aquí.
```
