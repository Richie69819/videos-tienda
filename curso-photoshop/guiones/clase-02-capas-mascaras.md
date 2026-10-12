# Clase 2 — Capas y máscaras

La clase bisagra. Si el espectador entiende la máscara, las 28 clases que siguen son
cuesta abajo; si no la entiende, va a sufrir en todas. Por eso va en el día 1 y por eso
dura 14 minutos y no 8.

La idea que hay que dejar clavada: **en Photoshop no se borra. Se tapa.**

## Ficha

| | |
|---|---|
| Clase | 2 de 30 |
| Módulo | 1 — Los comandos |
| Título | `Curso de Photoshop desde cero — Clase 2: capas y máscaras explicadas de una vez` |
| Duración objetivo | 14:00 |
| Entrega | `02-ficha.jpg`: el Funko + nombre + número + logo en capas separadas, con el fondo tapado con máscara (no borrado) |
| Requisitos | clase 1 |
| Dónde se puede hacer | Photopea, completo |
| Archivos de la clase | `material/base/`, tu logo en PNG, y el PSD en dos estados: a medias y terminado |
| Atajos nuevos | Ctrl+J, Ctrl+G, Ctrl+Shift+N, Alt+clic, Ctrl+D, F7, X, D, Ctrl+Shift+S |

## Miniatura

- Texto: **NO BORRES**
- Color del módulo 1: naranja de marca
- Qué se ve: el mismo Funko dos veces, uno con el fondo borrado a mordidas (con un
  pedazo de oreja comido) y otro limpio con la máscara. El borrador tachado.

## Antes de grabar

- [ ] `02-ficha.psd` **a medias** guardado en `plantillas/`: fondo de color y la foto
      metida, nada más. Es el punto de partida que se ofrece en el comentario fijado
- [ ] `02-ficha.psd` **terminado** guardado en `plantillas/`, por si hay que repetir
- [ ] Tu logo en PNG con fondo transparente, a mano
- [ ] El nombre y el número que le vas a poner a la figura, ya decididos (no se piensa
      en cámara)

---

## Guion

### 0:00-0:15 · Gancho y promesa

> **PANTALLA:** el Funko con el fondo borrado con el borrador, feo, con una mordida en
> la cabeza. Al lado, el mismo con máscara, perfecto, y el fondo **volviendo a
> aparecer** de un clic.

> "Al final de este video vas a entender lo único que de verdad hay que entender de
> Photoshop, y vas a tener esta ficha hecha por ti. Catorce minutos. Si siempre has
> borrado con el borrador, esto te va a cambiar la forma de trabajar."

### 0:15-2:30 · Teoría: capas

> **PANTALLA:** tres acetatos de verdad, en la mano, encimados frente a la cámara. Si no
> hay cámara, tres rectángulos en pantalla que se separan en perspectiva.

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

> "**Tres:** cada cosa en su capa. La figura en una, el nombre en otra, el número en
> otra, el logo en otra. Cuesta diez segundos más y te permite cambiar una cosa sin
> rehacer el resto. Y cuando lleguemos a la clase veinticinco y te enseñe a sacar veinte
> fichas distintas de un solo archivo, eso solo funciona si cada cosa está en su capa."

**Los controles del panel (F7):**

| Control | Qué hace | Para qué sirve de verdad |
|---|---|---|
| El ojo | Enciende y apaga la capa | Comparar antes y después en un clic |
| Opacidad | Transparencia de la capa | Bajar el logo al 60% para que no grite |
| Bloqueo | Candado | Que no muevas el fondo sin querer |
| Modo de fusión | Cómo se mezcla con la de abajo | De los ~27, se usan 3: **Multiplicar**, **Trama**, **Luz suave** |

> "Los modos de fusión los vas a ver en todos los tutoriales de internet y en todos
> suenan a brujería. Son esto: Multiplicar oscurece y deja pasar lo blanco. Trama aclara
> y deja pasar lo negro. Luz suave sube el contraste. Esos tres, el resto cuando tengas
> tiempo libre."

**Atajos de capas:**

| Atajo | Qué hace |
|---|---|
| **Ctrl+J** | Duplicar la capa. Antes de arriesgar algo, duplica |
| **Ctrl+Shift+N** | Capa nueva vacía |
| **Ctrl+G** | Agrupar las seleccionadas (carpetas, para no perderte en 20 capas) |
| **F7** | Mostrar u ocultar el panel |
| **Alt+clic en el ojo** | Ver **solo** esa capa. El mejor atajo del panel y casi nadie lo sabe |

### 2:30-6:30 · Teoría y práctica: la máscara

> **PANTALLA:** `01-mesa.jpg` abierta, con todo el desorden de la mesa alrededor del
> Funko. El botón de máscara marcado.

> "Ahora lo importante. Quiero quitarle el fondo a esta foto: la mesa, el cable, todo lo
> que no es la figura. La forma en que lo hace un principiante es con el borrador: **E**,
> y a tallar. Lo voy a hacer para que veas por qué no."

> **ERROR A PROPÓSITO:** borrar un pedazo del fondo con el borrador y comerse un pedazo
> de la cabeza del Funko.
> "Le mordí la cabeza. Y lo peor: eso ya no está. Si guardo y cierro, perdí esos píxeles
> para siempre. **Ctrl+Z**."

> "Y fíjate dónde me la comí: en la curva de la cabeza. Con un Funko eso es lo más
> delicado que hay, porque la cabeza es una bola perfecta y el ojo humano detecta
> cualquier abolladura en un círculo a un metro de distancia. Una mordida en el pie no
> la ve nadie; una en la cabeza se ve siempre."

> "La forma correcta: una máscara. Con la capa seleccionada, este botón de abajo del
> panel —el rectángulo con el círculo— agrega una máscara de capa. Fíjate que aparece un
> cuadrito blanco al lado de la miniatura de la capa."

> **TEXTO EN PANTALLA, grande, 5 segundos:** `NEGRO TAPA · BLANCO MUESTRA`

> "Esa es la regla completa, y es lo único que tienes que memorizar hoy: en una máscara,
> **lo que pintas de negro se tapa, y lo que pintas de blanco se vuelve a ver**. La
> máscara no es la imagen: es una instrucción de qué se muestra."

> "Entonces: clic en el cuadrito blanco de la máscara, **B** de pincel, **D** para poner
> los colores en negro y blanco por defecto, y **X** para intercambiar entre uno y otro.
> Pinto de negro sobre la mesa... y se va. Pero mira: me pasé y me comí otra vez la
> cabeza. **X**, ahora tengo blanco, pinto encima... y **regresa**. No lo recuperé de la
> basura: nunca se fue."

> "Eso es la diferencia. El borrador destruye; la máscara tapa. Y tapar es reversible
> para siempre, hasta dentro de dos años cuando abras el archivo."

> **PANTALLA:** apagar la máscara con Shift+clic en su miniatura para mostrar que la
> foto sigue completa debajo.

> "Shift más clic en la máscara la apaga: la foto está entera, intacta. Siempre estuvo."

**El hueco entre el brazo y el cuerpo:**

> **PANTALLA:** zoom al espacio entre el brazo y el torso de la figura.

> "Y aquí tienes el único lugar difícil de esta figura. La cabeza es fácil, es una
> curva; los pies son fáciles, son rectos. Lo que cuesta es **este hueco** entre el brazo
> y el cuerpo, porque ahí el fondo se mete dentro de la silueta. Si no lo tapas, te queda
> un parche de mesa colgando del sobaco de la figura, y eso es lo que delata un recorte
> mal hecho más que cualquier otra cosa."

> "Pincel chico, **Alt+rueda** para acercarte, y con calma. Y si lo dejas imperfecto hoy,
> no pasa nada: en la clase tres lo hacemos en dos clics."

**La trampa que le pasa a todo el mundo:**

> **ERROR A PROPÓSITO:** tener seleccionada la capa (no la máscara) y pintar negro encima
> de la figura.
> "Acabo de pintar un brochazo negro sobre mi figura. Es que tenía seleccionada la
> **capa**, no la **máscara**. Fíjate en el borde blanco: el recuadro te dice en cuál
> estás parado. Antes de pintar en una máscara, clic en la máscara. **Ctrl+Z**."

### 6:30-12:00 · Práctica: la ficha

> "Vamos a armar la entrega. Cinco capas, y cada una con un trabajo."

1. **Ctrl+N**, 1080x1920, 72 ppp, RGB. **Ctrl+S** como `02-ficha.psd`. (Repetido de la
   clase 1, a propósito, sin disculparse: "esto lo vas a hacer treinta veces.")
2. **El fondo:** capa nueva (**Ctrl+Shift+N**), rellenar de color con el bote o con
   **Alt+Supr** teniendo el color frontal puesto. "Nombra la capa: doble clic en el
   nombre, 'fondo'. En veinte capas vas a agradecerlo."
3. **La figura:** arrastrar `01-mesa.jpg`, **Ctrl+T** para acomodar, **Enter**. Máscara,
   y pintar de negro todo lo que no es la figura. "No tiene que quedar perfecto: en la
   clase tres lo hacemos en dos clics con Seleccionar sujeto. Hoy lo hacemos a mano para
   que entiendas qué está pasando cuando esos dos clics lo hagan por ti."
4. **El nombre:** **T**, el nombre de la figura, **Ctrl+Enter** para cerrar.
5. **El número:** otra capa de texto, el número de la figura, chico, arriba a la
   izquierda. "Dos textos, dos capas. Nunca los dos en la misma: si van en la misma, no
   puedes mover uno sin mover el otro. Y ese número no es decoración: en la clase
   veintiséis, cuando saquemos las fichas desde una hoja de cálculo, el nombre y el
   número van a ser dos columnas de esa hoja. Hoy los pones a mano; en la veintiséis se
   ponen solos."
6. **El logo:** arrastrar el PNG. Opacidad al 70%. "Un logo al cien por ciento compite
   con tu figura. Al setenta acompaña."
7. **Ctrl+G** sobre las dos capas de texto: una carpeta llamada "textos". "Con cinco
   capas parece exagerado. En la clase veintiuno vas a tener treinta."
8. **Guardar los dos archivos:** **Ctrl+S** para el PSD (el que puedes seguir editando),
   **Ctrl+Shift+Alt+W** para el JPG (el que se sube). "El PSD no se sube a ningún lado y
   no se borra nunca. Es tu original."

> **ERROR A PROPÓSITO:** intentar mover la figura con la capa de texto seleccionada y
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

> "Suscríbete y la clase tres te llega mañana: selecciones. Ahí vas a quitar ese fondo en
> dos clics, y vas a entender lo que esos dos clics están haciendo porque hoy lo hiciste
> a mano."

> **PANTALLA FINAL:** Clase 3.

---

## Shorts de esta clase

```
SHORT 1: desde=04:20 hasta=04:40 gancho="Deja de borrar|en Photoshop"
SHORT 2: desde=03:30 hasta=03:45 gancho="Negro tapa, blanco muestra|ya sabes máscaras"
SHORT 3: desde=13:05 hasta=13:19 gancho="Alt + clic en el ojo|nadie te dijo esto"
```

## Descripción

```
Capas y máscaras, el único concepto que de verdad hay que entender de Photoshop. Al
final tienes tu ficha en capas separadas.

PSD de la clase (a medias y terminado): [link]
Lista completa del curso: [link]
Clase anterior (Clase 1 — Interfaz y atajos): [link]  ·  Clase siguiente (Clase 3 — Selecciones): [link]

Minutos:
00:00 Lo que vas a tener al final
00:15 Qué es una capa (y por qué "no me sale" casi siempre es esto)
02:30 Máscaras: negro tapa, blanco muestra
04:40 Por qué el borrador destruye y la máscara no
05:50 El hueco entre el brazo y el cuerpo
06:30 Armamos la ficha, capa por capa
12:00 Tres costumbres que te van a ahorrar horas

Esta clase se puede hacer completa en Photopea, gratis, desde el navegador.

#photoshop #cursodephotoshop #capas #mascaras #funko
```

## Comentario fijado

```
PSD de la clase + logo + fotos: [link]
Viene en dos estados: a medias (para que lo termines conmigo) y terminado (para
comparar). Sube tu ficha aquí.
```
