# Clase 5 — Tamaño de imagen vs tamaño de lienzo

El error número uno de Photoshop, y no es un error de principiante: hay gente con años
encima que sigue confundiendo estos dos cuadros de diálogo. Clase corta, once minutos, y de
las que más comentarios de "no sabía esto" va a traer.

La idea que hay que dejar clavada: **el tamaño de imagen estira el contenido. El tamaño de
lienzo cambia el papel.**

## Ficha

| | |
|---|---|
| Clase | 5 de 30 |
| Módulo | 1 — Los comandos |
| Título | `Curso de Photoshop desde cero — Clase 5: tamaño de imagen vs tamaño de lienzo (el error #1)` |
| Duración objetivo | 11:00 |
| Entrega | `05-tienda.jpg` (2000x2000) y `05-reel.jpg` (1080x1920): la misma figura, dos formatos, sin deformar y sin perder la cabeza |
| Requisitos | clases 1 a 4 |
| Archivos de la clase | `03-figura-recortada.png` y los dos JPG terminados |
| Atajos nuevos | Ctrl+Alt+I (tamaño de imagen), Ctrl+Alt+C (tamaño de lienzo), C (recortar) |

## Miniatura

- Texto: **IMAGEN ≠ LIENZO**
- Color del módulo 1: naranja de marca
- Qué se ve: la misma figura dos veces. En una, estirada hasta el borde de un cuadro
  vertical. En la otra, del mismo tamaño pero con más espacio alrededor. La diferencia entre
  las dos **es** la clase.

## Antes de grabar

- [ ] `03-figura-recortada.png` a mano
- [ ] Los dos JPG terminados en `plantillas/`
- [ ] La cuenta de los píxeles de impresión ya hecha: **10 cm a 300 ppp = 1181 px**. No se
      calcula en cámara
- [ ] Confirmar **antes de grabar** si en esta versión *Conservar detalles 2.0* aparece en el
      desplegable de remuestreo o si hay que encenderlo en `Ctrl+K > Previsualizaciones de
      tecnología`. Lo que salga, se dice; lo que no, no se menciona

---

## Guion

### 0:00-0:15 · Gancho y promesa

> **PANTALLA:** una imagen cuadrada con la figura. Dos cortes seguidos: la misma pasada a
> vertical **bien**, y la misma pasada a vertical **mal** (estirada, con la cabeza de huevo y
> los pies cortados).

> "Estos dos cuadros de diálogo se parecen, están uno debajo del otro en el menú, y
> confundirlos arruina más archivos que cualquier otra cosa en Photoshop. En once minutos no
> los vas a volver a confundir, y vas a tener tu figura en los dos formatos que de verdad se
> usan: cuadrado para la tienda y vertical para reel."

### 0:15-2:30 · Teoría: los dos cuadros

> **PANTALLA:** abrir `Imagen > Tamaño de imagen` (**Ctrl+Alt+I**) y, al lado, `Imagen >
> Tamaño de lienzo` (**Ctrl+Alt+C**).

> "Imagínate que tu archivo es una foto pegada en una hoja de papel."

> **TEXTO EN PANTALLA, grande, 6 segundos:**
> `TAMAÑO DE IMAGEN → estira la foto`
> `TAMAÑO DE LIENZO → cambia la hoja`

> "**Tamaño de imagen**, Ctrl+Alt+I: agarra la foto y la estira o la encoge. Todo lo que hay
> dentro cambia de tamaño."

> "**Tamaño de lienzo**, Ctrl+Alt+C: la foto se queda exactamente igual, y lo que cambia es
> la hoja de abajo. Si la haces más grande, aparece espacio vacío alrededor. Si la haces más
> chica, **recortas**: lo que se sale, se va."

> "Y ya está. Esa es la clase. Lo demás son los detalles que hacen que te equivoques."

**El cuadro de Tamaño de imagen, campo por campo:**

| Campo | Qué es | El detalle que importa |
|---|---|---|
| **Anchura / Altura** | El tamaño en píxeles | Con la cadenita cerrada no deformas |
| **Resolución (ppp)** | Píxeles por pulgada **al imprimir** | Para pantalla **no significa nada** |
| **Remuestrear** | Si se inventan o se tiran píxeles | Es la casilla que lo cambia todo |

> "Hablemos de los ppp, porque hay mucha confusión suelta en internet."

> **PANTALLA:** con Remuestrear **apagado**, cambiar 72 a 300 ppp y señalar que los píxeles
> **no se mueven** y el tamaño en centímetros **sí**.

> "Con la casilla de Remuestrear apagada, cambio setenta y dos por trescientos... y mira los
> píxeles: **no se movieron**. Lo único que cambió fue cuántos centímetros mide al imprimir.
> Porque los ppp no son calidad: son **una instrucción para la impresora** de qué tan
> apretados poner los puntos."

> "Entonces, dos frases que te van a ahorrar discusiones:"

> "**Una:** para pantalla, los ppp no importan. Nada. Una imagen para Instagram a setenta y
> dos y la misma a trescientos se ven idénticas, porque la pantalla solo cuenta píxeles."

> "**Dos:** para imprimir, sí importan, y el número es trescientos. Si vas a imprimir algo
> de diez centímetros de ancho a trescientos ppp, necesitas **mil ciento ochenta y un
> píxeles**. Si solo tienes seiscientos, te va a salir borroso y **ningún** ajuste de ppp lo
> arregla: poner trescientos en esa casilla no inventa información, solo cambia la etiqueta.
> Esto es la clase veinte completa, la de la imprenta."

> **TEXTO EN PANTALLA:** `10 cm a 300 ppp = 1181 px`

> **PANTALLA:** encender Remuestrear y mostrar el desplegable.

> "Y con Remuestrear encendido, sí se inventan o se tiran píxeles. Del desplegable, dos
> opciones y ya: **Bicúbica más enfocada** cuando reduces, **Conservar detalles** cuando
> agrandas. Si lo dejas en Automático, acierta casi siempre."

> "Y hay una versión mejor de *Conservar detalles* para ampliar, que usa un modelo entrenado
> y hace un trabajo notablemente mejor con los bordes. Si no te aparece en la lista, está en
> `Ctrl+K`, `Previsualizaciones de tecnología`. Vale la pena encenderla el día que tengas que
> ampliar algo en serio — pero sigue sin inventar lo que no está. Ampliar siempre es el plan
> B."

### 2:30-4:00 · El error, en vivo

> **PANTALLA:** la imagen cuadrada de 2000x2000. Abrir **Tamaño de imagen**, abrir la
> cadenita, y poner 1080 x 1920.

> "Tengo esta imagen cuadrada y la quiero vertical para un reel. Lo que hace todo el mundo la
> primera vez: tamaño de imagen, y escribo mil ochenta por mil novecientos veinte. Para que
> me deje, tengo que abrir la cadenita. Enter."

> **PANTALLA:** el resultado, estirado, la cabeza ovalada. Quedarse callado dos segundos.

> "Y ahí está el desastre. La cabeza es un huevo. Estiré la foto para que cupiera en una hoja
> de otra forma, y eso es justo lo que la clase cuatro dijo que no se hace nunca."

> "**Ctrl+Z**. Lo que yo quería no era estirar la foto: era **cambiar la hoja**."

### 4:00-7:30 · Práctica: el mismo archivo en dos formatos

> "Vamos a hacerlo bien, y de paso te queda el método que vas a usar toda la vida: **un
> archivo grande, dos salidas.**"

**Paso 1 — El cuadrado de la tienda.**

1. **Ctrl+N**, 2000 x 2000 px, 72 ppp, RGB, fondo blanco. **Ctrl+S** como `05-formatos.psd`.
2. Arrastrar `03-figura-recortada.png`. **Clic derecho > Convertir en objeto inteligente** (la
   costumbre de la clase 4).
3. **Ctrl+T**, escalar desde la esquina hasta que la figura ocupe como el setenta y cinco por
   ciento del alto, centrada. **Enter**.

> "Dos mil por dos mil, cuadrado, es el formato que piden casi todas las tiendas y
> marketplaces, y es el que se ve bien en la cuadrícula de Instagram. Si solo vas a hacer un
> tamaño, haz este."

4. **Ctrl+Shift+Alt+W**, JPG calidad 80, `05-tienda.jpg`.

**Paso 2 — El vertical, con Tamaño de lienzo.**

5. **Ctrl+Alt+C**, Tamaño de lienzo. Anchura 1080, Altura 1920, en píxeles.

> "Fíjate en la cuadrícula del **ancla**, abajo. Esos nueve cuadritos deciden **de dónde**
> crece o se recorta la hoja. Por defecto está en el centro: crece y recorta parejo por los
> cuatro lados."

> **ERROR A PROPÓSITO:** dejar el ancla en el centro bajando de 2000 a 1080 de ancho, luego
> ponerla arriba y perder los pies, y después abajo y **cortarle la cabeza**.
> "Y ahí está el error que cuesta caro: le corté la cabeza. Con una figura así, la cabeza es
> media imagen; el ancla no es un detalle. Para algo que se para en el suelo, el ancla va
> **abajo al centro**: crece hacia arriba y le deja aire sobre la cabeza."

6. Ancla abajo al centro. **OK**.

> "Y mira lo importante: **la figura no cambió de tamaño ni un píxel.** Sigue igual. Lo único
> que cambió es cuánta hoja hay alrededor. Eso es el tamaño de lienzo."

7. Si quedó espacio transparente, capa de fondo nueva al fondo, rellenada del color de marca
   —que ya está en tu biblioteca de la clase 2, a un clic.
8. **V** para recentrar la figura, con las guías inteligentes.
9. **Ctrl+Shift+Alt+W**, `05-reel.jpg`.

> "Dos archivos, un original, cero deformaciones. Y como la figura es un objeto inteligente,
> si mañana le cambias la foto de adentro con *Reemplazar contenido*, los dos se actualizan."

**Paso 3 — La tercera herramienta que se confunde: recortar (C).**

10. **C**, herramienta de recorte. En la barra de opciones, poner la proporción **9:16**.

> "Y falta la tercera que se confunde con las otras dos: **C**, recortar. Hace lo mismo que
> cambiar el lienzo, pero a ojo y con el ratón, y te deja poner una proporción fija arriba.
> Es la que vas a usar el noventa por ciento de las veces en la vida real; los cuadros de
> diálogo son para cuando necesitas un número exacto."

> "Un detalle que importa: la casilla que dice **Eliminar píxeles recortados**. Déjala
> **apagada**. Apagada, lo que recortas se queda guardado fuera del lienzo y puedes volver
> por él; encendida, se va para siempre. Es la misma idea de la clase dos: tapar, no borrar."

> **PANTALLA:** con la herramienta de recorte, **agrandar** el lienzo más allá de la imagen y
> encender **Relleno según el contenido**.

> "Y un regalo, que es de las cosas que justifican el programa: con la herramienta de recorte
> puedes también **agrandar** el lienzo, y si enciendes esta casilla de **Relleno según el
> contenido**, Photoshop te **inventa** el fondo que falta en el espacio nuevo. Mira: le
> estiro el lienzo hacia arriba, Enter... y rellenó la mesa y la pared solas."

> "Úsalo para fondos: pared, mesa, cielo, madera. **No lo uses nunca sobre el producto**: lo
> que inventa ahí no es tu producto, y si lo mandas a un cliente estás entregando algo que no
> existe. Esa frontera se la vamos a ver bien en la clase once."

### 7:30-9:30 · La tabla que hay que guardar

> **PANTALLA:** la tabla completa, 10 segundos fijos, para pausar y fotografiar.

| Para qué | Tamaño | Modo | ppp |
|---|---|---|---|
| Ficha de tienda / marketplace | 2000 x 2000 | RGB | 72 |
| Reel, TikTok, Short | 1080 x 1920 | RGB | 72 |
| Publicación de feed | 1080 x 1350 | RGB | 72 |
| Miniatura de YouTube | 1280 x 720 | RGB | 72 |
| Para imprimir (clase 20) | según el tamaño físico | **CMYK** | **300** |

> "Y la regla que resume la clase entera: **trabaja en el más grande de la lista y de ahí saca
> los demás.** Nunca al revés, porque agrandar inventa y se nota."

> "¿Cuál es el más grande? Cuenta píxeles totales, no lados. Y si vas a imprimir alguna vez,
> el de imprenta le gana a todos: una caja a trescientos ppp tiene más píxeles que cualquier
> cosa de pantalla. De ahí sale la costumbre de los que trabajan así: **el archivo madre se
> hace a tamaño de impresión**, y las versiones de pantalla se exportan de ahí. Eso es la
> clase veintidós, la de la plantilla maestra."

> "Y para que no te suene a trabajo: sacar esas cinco versiones de un archivo, a mano, son
> veinte minutos. En la clase catorce se lo vas a aventar al **Procesador de imágenes** y van
> a salir las cinco carpetas solas mientras te paras por un café. Eso es el módulo tres."

### Cierre (últimos 20 s)

> "Tu reto: sube los dos archivos, el cuadrado y el vertical. Y dime en los comentarios cuál
> de los dos cuadros de diálogo usaste para pasar de uno a otro. Si contestas 'tamaño de
> lienzo', esta clase funcionó."

> "Suscríbete, que con esta ya casi cerramos el módulo uno. La clase seis es guardar y
> exportar bien: los cuatro formatos, cuál va en cada lugar, y cómo dejar guardado un
> preajuste para no volver a pensarlo. Ahí te veo."

> **PANTALLA FINAL:** Clase 6.

---

## Shorts de esta clase

```
SHORT 1: desde=05:40 hasta=06:02 gancho="Así es como le|cortas la cabeza"
SHORT 2: desde=01:40 hasta=02:05 gancho="Los 300 ppp no son|calidad de imagen"
SHORT 3: desde=06:50 hasta=07:15 gancho="Agranda el lienzo|y que invente el fondo"
```

## Descripción

```
Tamaño de imagen vs tamaño de lienzo: los dos cuadros que todo el mundo confunde, y el mito
de los 300 ppp. Al final tienes la misma imagen en formato de tienda (2000x2000) y en
vertical para reel (1080x1920), sin deformar nada.

PNG y PSD de la clase: [link]
Lista completa del curso: [link]
Clase anterior (Clase 4 — Transformar): [link]  ·  Clase siguiente (Clase 6 — Guardar y exportar): [link]

Minutos:
00:00 Lo que vas a tener al final
00:15 Tamaño de imagen estira la foto; tamaño de lienzo cambia la hoja
01:30 Los 300 ppp no son calidad (y cuándo sí importan)
02:30 El error, en vivo
04:00 El cuadrado de tienda y el vertical de reel desde un solo archivo
05:30 El ancla del lienzo (y cómo NO cortarle la cabeza)
06:30 Recortar con C, la casilla que hay que apagar, y rellenar el lienzo nuevo
07:30 La tabla de tamaños que hay que guardar

#photoshop #cursodephotoshop #tamañodeimagen #300ppp #funko
```

## Comentario fijado

```
El PNG de la figura + el PSD con los dos formatos: [link]
Sube tus dos archivos aquí y dime cuál cuadro de diálogo usaste para pasar de uno a otro.
```
