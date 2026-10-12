# Clase 4 — Transformar sin deformar, y objetos inteligentes

Clase corta y mecánica, y la que más vergüenzas evita. Deformar es el error que delata a un
principiante en medio segundo, porque el ojo humano detecta una proporción mal antes de
poder explicar por qué.

Dos ideas, y la segunda es la que vale el precio del programa: **escalar hacia abajo es
gratis, escalar hacia arriba cuesta** — y **un objeto inteligente no paga ninguno de los
dos costos**.

## Ficha

| | |
|---|---|
| Clase | 4 de 30 |
| Módulo | 1 — Los comandos |
| Título | `Curso de Photoshop desde cero — Clase 4: transformar sin deformar (y sin pixelear)` |
| Duración objetivo | 12:00 |
| Entrega | `04-tres-tamanos.jpg`: la misma figura en 3 tamaños, alineada, sin deformar ni pixelear |
| Requisitos | clase 3 (se parte del PNG recortado) |
| Archivos de la clase | `03-figura-recortada.png` y el PSD terminado |
| Atajos nuevos | Ctrl+T con Shift y con Alt, Ctrl+Shift+T, Ctrl+Shift+Alt+T, Esc |

## Miniatura

- Texto: **NO LA APLASTES**
- Color del módulo 1: naranja de marca
- Qué se ve: la figura bien a la izquierda y la misma achatada a la derecha, lado a lado, la
  achatada con una tacha. El contraste es el argumento; no hace falta explicarlo.

## Antes de grabar

- [ ] `03-figura-recortada.png` a mano. Si la clase 3 se grabó mal, hay copia en
      `plantillas/`
- [ ] El PSD terminado en `plantillas/`
- [ ] Decidido de antemano qué 3 tamaños: **100%, 60% y 35%**. No se piensa en cámara
- [ ] Una segunda foto de la figura lista para el truco de *Reemplazar contenido* del
      minuto 7

---

## Guion

### 0:00-0:15 · Gancho y promesa

> **PANTALLA:** las tres figuras alineadas, del mismo ancho de base, las tres con la cabeza
> perfectamente redonda. Luego, un corte a una versión achatada, dos segundos, y de vuelta.

> "Al final de este video tienes esta imagen con tu figura en tres tamaños, y no vas a
> volver a deformar ni a pixelear nada en tu vida. Doce minutos. Esta clase es corta y es la
> que más pena te va a ahorrar."

### 0:15-1:30 · Teoría: Ctrl+T y los nodos

> **PANTALLA:** **Ctrl+T** sobre la capa de la figura, y el recuadro con los ocho nodos
> apareciendo.

> "**Ctrl+T**, transformar. Aparece un recuadro con ocho nodos: cuatro en las esquinas y
> cuatro en los lados. Esos ocho nodos son toda la clase."

| Qué arrastras | Qué pasa |
|---|---|
| **Una esquina** | Escala manteniendo la proporción |
| **Un lado** | Escala **solo** ancho o **solo** alto → **deforma** |
| **Afuera del recuadro** | Rota |
| **Con Alt apretado** | Escala desde el centro, no desde la esquina opuesta |
| **Con Shift apretado** | **Libera** la proporción: deforma a propósito |

> "Y tres teclas que terminan la transformación: **Enter** aplica, **Esc** cancela, y
> **Ctrl+Z** deshace si ya aplicaste y no te gustó."

> "Fíjate en la barra de opciones, arriba: ahí está el ancho y el alto en porcentaje, y
> entre los dos **una cadenita**. Con la cadena cerrada —y viene cerrada— no se deforma
> nunca, hagas lo que hagas. Si alguna vez en tu vida te sale algo deformado, lo primero que
> miras es esa cadena."

### 1:30-3:30 · El error, en grande

> **PANTALLA:** arrastrar el nodo del lado derecho y dejar la figura estirada de ancho.
> Quedarse ahí cinco segundos, callado dos.

> "Mírala. ¿Qué tiene de malo? Te apuesto que lo viste antes de que yo dijera nada, y que no
> sabrías explicar qué exactamente."

> "Lo que tiene es que **la cabeza ya no es redonda**. Y con una figura de estas eso es
> fatal, porque la proporción de la cabeza contra el cuerpo **es el personaje**: es lo único
> que hace que esto se lea como una figura coleccionable y no como un muñeco cualquiera. Si
> le estiras la cabeza dos por ciento, deja de ser lo que es."

> "Y esto no es un problema de figuras. Es exactamente igual con una cara, con un logo y con
> un envase: todos tienen una proporción que la gente reconoce sin pensar, y deformarla es
> la cosa que más grita 'esto lo hizo alguien que empezó ayer'."

> **ERROR A PROPÓSITO:** aplicar la deformación con Enter, seguir trabajando dos pasos, y
> luego querer arreglarla. "Y ya la apliqué. Si sigo trabajando y a los diez minutos me doy
> cuenta, los Ctrl+Z ya no alcanzan. Ahora sí: deshacer, y lo hacemos bien."

**La prueba de los tres segundos:**

> "Antes de dar Enter en cualquier transformación, una pregunta: **¿sigue siendo redondo lo
> que era redondo?** Busca el círculo de la imagen —una cabeza, una rueda, un logo, un ojo—
> y míralo. Si está de huevo, está mal. Tres segundos y te ahorra el ridículo."

### 3:30-5:30 · La otra mitad: pixelear

> **PANTALLA:** tomar la figura ya reducida al 35% y volverla a subir al 100%.

> "Segunda mitad de la clase, y es la que casi nadie te explica. Acabo de reducir esta figura
> al treinta y cinco por ciento. Ahora la vuelvo a subir al cien... y mírala. Está borrosa y
> tiene la orilla sucia."

> **TEXTO EN PANTALLA:** `Reducir: gratis · Agrandar: se paga`

> "Por qué: cuando reduces, Photoshop **tira** píxeles, y tirar es fácil. Cuando agrandas,
> tiene que **inventar** píxeles que nunca existieron, y los inventa promediando los
> vecinos. De ahí la borrosidad. No es que lo haga mal: es que no hay información que
> poner."

> "La regla práctica: **nunca agrandes una imagen más de lo que mide.** Si tu foto es de mil
> píxeles de ancho y la necesitas de dos mil, no la agrandes: vuelve a tomar la foto, o
> consigue el archivo grande. Y si no hay más remedio, no pases del ciento diez por ciento."

> "Y de aquí sale la costumbre más útil de todo este curso: **trabaja siempre con la imagen
> más grande que tengas, y redúcela.** Nunca al revés."

### 5:30-7:30 · La solución a las dos cosas: objeto inteligente

> **PANTALLA:** clic derecho en la capa > Convertir en objeto inteligente. El icono cambia en
> la miniatura.

> "Y ahora el truco que hace que todo lo anterior deje de importar. Clic derecho en la capa,
> **Convertir en objeto inteligente**. Fíjate que la miniatura cambia: le aparece un
> cuadrito."

> "Qué acabo de hacer: metí la imagen en una cajita. Lo que ves es una **vista previa**; el
> original está guardado completo adentro. Y por eso ahora puedo hacer esto:"

> **PANTALLA:** reducir al 20%, aplicar, volver a subir al 100%, aplicar. Se ve nítida.

> "La reduje al veinte, la apliqué, y la volví a subir al cien. Y está **nítida**. Porque no
> estaba escalando píxeles: estaba cambiando el tamaño de la vista previa, y el original de
> adentro nunca se tocó."

> **TEXTO EN PANTALLA, grande:** `Un objeto inteligente se escala mil veces sin perder nada`

> "La costumbre que te vas a llevar de esta clase: antes de escalar algo que vas a escalar
> más de una vez, conviértelo en objeto inteligente. Cuesta un clic derecho."

**Las otras dos cosas que hace, y que casi nadie usa:**

> **PANTALLA:** doble clic en la miniatura del objeto inteligente: se abre en su propia
> ventana. Cambiar algo, **Ctrl+S**, y volver: se actualizó en el documento.

> "**Una: doble clic en la miniatura** y el original se abre en su propia pestaña. Lo
> cambias, **Ctrl+S**, cierras, y el documento de afuera se actualiza solo."

> **PANTALLA:** clic derecho > Reemplazar contenido, y elegir otra foto de la figura.

> "**Dos, y esta es la buena: clic derecho, Reemplazar contenido.** Le doy otra foto... y
> mira: entró **con el mismo tamaño, en la misma posición y con los mismos efectos** que
> tenía la anterior. No acomodé nada."

> "Piensa en lo que eso significa cuando tengas una plantilla con seis piezas: cambias la
> foto una vez y las seis se actualizan. Eso es la clase dieciocho, objetos inteligentes
> vinculados, y es la clase que te va a ahorrar más horas de todo el curso. Hoy quédate con
> el clic derecho."

> "Lo único que cuestan: pesan más, y hay filtros que no se les aplican directo. Cuando topes
> con eso, clic derecho, **Rasterizar**, y ya — pero rasteriza una **copia**, nunca el
> original."

### 7:30-10:00 · Práctica: la entrega

> "Vamos a hacer la imagen de los tres tamaños, que es lo que usarías para enseñar las
> medidas de algo que vendes."

1. **Ctrl+N**, 2000 x 1200 px, 72 ppp, RGB, fondo blanco. **Ctrl+S** como
   `04-tres-tamanos.psd`.
2. Arrastrar `03-figura-recortada.png`. **Enter**.
3. **Clic derecho > Convertir en objeto inteligente.** "Primero esto. Siempre primero esto."
4. **Ctrl+J** para duplicar, dos veces. "Tres capas, la misma figura."
5. En la segunda: **Ctrl+T**, y en la barra de opciones **escribir 60%** en ancho y alto
   —con la cadenita cerrada— en vez de arrastrar. **Enter**.

> "Escribir el número es más preciso que arrastrar, y te deja repetirlo exacto. Acuérdate de
> esto: en la clase trece vamos a **grabar** estos pasos como una acción, y una acción graba
> el número, no el arrastre del ratón. Trabajar con números es lo que hace que tu trabajo se
> pueda automatizar después."

6. En la tercera: **35%**, igual.
7. **V**, y acomodar las tres **apoyadas en la misma línea de base**. "Que coincidan por
   abajo, no por el centro. Son objetos que se paran en una mesa: si los alineas por el
   centro se ven flotando."
8. Las guías inteligentes para la separación. "Cuando los espacios entre las tres son
   iguales, Photoshop te enseña unas flechitas rosas. Suelta ahí."
9. **T**, una etiqueta debajo de cada una con el tamaño en centímetros reales.
10. **Ctrl+S** y **Ctrl+Shift+Alt+W** como `04-tres-tamanos.jpg`, calidad 80.

> **ERROR A PROPÓSITO:** alinear por el centro primero, mirarlo dos segundos y decir "se ven
> flotando", y rehacerlo por la base.

### 10:00-11:40 · Las otras transformaciones, y un atajo de regalo

> **PANTALLA:** el menú `Edición > Transformar` abierto.

| Comando | Para qué sirve de verdad |
|---|---|
| **Voltear horizontal** | Que la figura mire al otro lado |
| **Rotar 90°** | Foto del celular acostada |
| **Distorsionar** | Meter un diseño en una superficie en ángulo |
| **Perspectiva** | Lo mismo, con fuga |
| **Deformar** | Que un diseño siga una curva — el que se usa para mockups |

> "Estos tres últimos son la clase veintiuno, la del mockup: es lo que se usa para que un
> diseño plano se vea pegado sobre una caja de verdad, con su curva y su perspectiva."

> **ERROR A PROPÓSITO:** voltear la figura en horizontal con el texto encima dentro del grupo,
> y que el nombre quede espejeado.
> "Volteé y se me volteó el nombre también. Clásico: volteé el grupo, no la capa de la
> figura. Y ojo con voltear cualquier cosa que tenga letras, un logo o una marca encima: el
> espejo se nota siempre."

> "Y dos atajos de regalo, de los que casi nadie conoce:"

> "**Ctrl+Shift+T** repite la última transformación tal cual. Si acabas de girar algo doce
> grados y quieres girar otra cosa exactamente doce grados, es ese."

> "Y **Ctrl+Shift+Alt+T**: duplica la capa **y** le aplica la transformación otra vez, de un
> golpe. Si lo aprietas diez veces seguidas después de haber girado algo quince grados, te
> armas un abanico de diez copias en abanico. Para rejillas, patrones y círculos de
> elementos, eso es treinta segundos en lugar de veinte minutos."

### Cierre (últimos 20 s)

> "Tu reto: sube tu imagen de tres tamaños. Y mira la cabeza antes de subirla: ¿sigue siendo
> redonda?"

> "Suscríbete. La clase cinco es el error número uno de todo Photoshop: la diferencia entre
> tamaño de **imagen** y tamaño de **lienzo**. Se confunden, y confundirlas es lo que arruina
> más archivos que cualquier otra cosa. Once minutos. Ahí te veo."

> **PANTALLA FINAL:** Clase 5.

---

## Shorts de esta clase

```
SHORT 1: desde=06:40 hasta=07:05 gancho="Clic derecho, Reemplazar|y entra solo en su lugar"
SHORT 2: desde=01:50 hasta=02:10 gancho="¿Ves qué tiene de malo?|la cabeza no es redonda"
SHORT 3: desde=11:05 hasta=11:28 gancho="Ctrl+Shift+Alt+T|el atajo que nadie usa"
```

## Descripción

```
Transformar sin deformar y sin pixelear, y los objetos inteligentes: la cajita que te deja
escalar mil veces sin perder calidad y reemplazar una foto sin volver a acomodar nada.

PNG y PSD de la clase: [link]
Lista completa del curso: [link]
Clase anterior (Clase 3 — Selecciones): [link]  ·  Clase siguiente (Clase 5 — Imagen vs lienzo): [link]

Minutos:
00:00 Lo que vas a tener al final
00:15 Ctrl+T, los 8 nodos y la cadenita
01:30 El error: deformar (y la prueba de los 3 segundos)
03:30 Por qué agrandar pixelea y reducir no
05:30 Objetos inteligentes: escalar mil veces sin perder nada
06:40 Reemplazar contenido: cambiar la foto sin acomodar nada
07:30 Armamos la imagen de los 3 tamaños
10:00 Voltear, rotar, distorsionar y deformar
11:00 Ctrl+Shift+Alt+T: duplicar y repetir la transformación

#photoshop #cursodephotoshop #objetosinteligentes #funko
```

## Comentario fijado

```
El PNG recortado de la clase 3 + el PSD de los 3 tamaños terminado: [link]
Si tu clase 3 no te salió, agarra mi PNG y sigue sin problema.
Sube tu imagen de 3 tamaños aquí.
```
