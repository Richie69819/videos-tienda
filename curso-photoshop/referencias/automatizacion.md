# Los módulos 3 y 5 a detalle — la automatización

La automatización está partida en dos: el **módulo 3** (clases 13 a 15) llega a la mitad
del curso, cuando al alumno ya le dolió repetir seis fotos a mano, y enseña lo que resuelve
el noventa por ciento de la repetición. El **módulo 5** (clases 23 a 27) es lo que ya pide
un archivo alimentado por datos.

Este módulo es la razón de ser del curso. Todo lo anterior lo enseñan cien canales;
esto lo enseñan muy pocos en español, y es lo único que de verdad cambia cuánto tiempo
le toma a alguien atender su tienda.

Rutas de menú con la interfaz **en español**. Entre paréntesis, el nombre en inglés,
porque la mitad de los tutoriales que el espectador va a encontrar después están así.

Todo esto necesita **Photoshop de escritorio**, y es la razón de la licencia. Acciones
y carga `.atn`, pero no tiene Lote por carpetas, ni Droplets, ni Variables.

---

## Clase 13 — Acciones

`Ventana > Acciones` (Window > Actions), **Alt+F9**.

Una acción es una grabadora de pasos. Se graba una vez, se reproduce mil.

**El guion de la clase, en orden:**

1. Botón de carpeta: crear un **conjunto** propio ("Michilab"). No grabar nunca dentro
   de los conjuntos que vienen de fábrica.
2. Botón de hoja: **acción nueva**. Darle nombre y, aquí sí, asignarle una tecla de
   función (**F2** a **F12**). Es lo que convierte la acción en reflejo.
3. Grabar. El círculo rojo se enciende. Hacer los pasos **limpios**: nada de clics de
   más, nada de deshacer a medias.
4. Cuadrado: detener. Reproducir sobre otra foto.

**Lo que hay que enseñar y nadie enseña:**

- **No todo se graba.** Lo que se hace con el ratón a pulso —una pincelada, un lazo a
  mano— se graba como coordenadas, y en otra foto cae en el lugar equivocado. Las
  acciones son para comandos de menú y de cuadro de diálogo, no para pulso.
- **Insertar detención** (menú del panel): la acción se detiene y muestra un mensaje
  escrito por ti ("ahora selecciona el producto y dale continuar"). Así se automatiza un
  flujo que tiene un paso humano en medio. Es la función que vuelve útiles las acciones
  de verdad.
- **Insertar elemento de menú**: mete al guion un comando que la grabadora no alcanzó.
- **Los diálogos:** el cuadrito al lado de cada paso hace que la acción **pare** y
  muestre ese diálogo al reproducirse. Con él apagado, usa los valores grabados. Para un
  lote de 200 fotos: todos apagados, o la computadora espera a que alguien le dé
  Aceptar doscientas veces.
- **Exportar:** seleccionar el conjunto y, en el menú del panel, Guardar acciones →
  archivo **`.atn`**. Ese archivo se respalda, se pasa a otra computadora y **se abre en
  Photopea**. La entrega de la clase son 3 `.atn`.

**Las 3 acciones que se graban en la clase** (las que de verdad se usan en una tienda):

| Acción | Qué hace | Tecla |
|---|---|---|
| `tienda-2000` | Convierte a RGB 8 bits, ajusta a 2000x2000 sobre fondo blanco, enfoca y guarda JPG calidad 80 | F2 |
| `reel-1080x1920` | Lienzo vertical, producto centrado, franja de marca abajo | F3 |
| `miniatura-1280x720` | Recorta a 16:9, aplica la plantilla de texto, exporta bajo 2 MB | F4 |

**Por qué se rompe una acción** (va como tabla en pantalla): la capa no se llama igual
que cuando se grabó, el archivo venía en CMYK o en 16 bits y la acción esperaba RGB 8
bits, o la foto es vertical y la acción se grabó sobre una horizontal. Las tres se
previenen metiendo al principio de la acción `Imagen > Modo > Color RGB` y 8 bits.

---

## Clases 14 y 15 — Lote, Procesador y Droplet

Esto era una sola clase y se partió en dos: la **14** es Procesador de imágenes y Lote
(dentro de Photoshop), y la **15** es el Droplet (el icono del escritorio). El contenido de
abajo sirve para las dos; el corte va donde empieza *Droplet*.

### Lote

`Archivo > Automatizar > Lote` (File > Automate > Batch).

| Campo | Qué poner | La trampa |
|---|---|---|
| Conjunto / Acción | la acción grabada | una sola acción por lote |
| Origen: Carpeta | la carpeta de fotos crudas | tiene que ser **disco local o de red**, no una carpeta sincronizada de nube |
| Incluir todos los subdirectorios | según el caso | — |
| Suprimir cuadros de diálogo de apertura | **sí** | si no, pregunta por cada archivo |
| Omitir comandos "Abrir" de la acción | **sí**, si la acción empieza abriendo un archivo | es el error que más cuelga el lote |
| Destino: Carpeta | carpeta de salida, **distinta** a la de origen | misma carpeta = sobrescribes los originales |
| Anular comandos "Guardar como" de la acción | **sí** | si no, los 200 archivos se guardan con el nombre del archivo con que grabaste |
| Nombres de archivo | nombre del documento + número de serie de 3 dígitos + extensión | — |
| Errores | "Registrar errores en archivo" | así el lote no se detiene en el archivo 37 y te deja un reporte |

**La demostración de la clase:** una carpeta con 200 fotos, el lote corriendo, y el
cronómetro en pantalla. Ese plano es el que se recorta como Short y es el mejor anuncio
que va a tener el curso.

### Droplet

`Archivo > Automatizar > Crear droplet` (Create Droplet).

Genera un **ejecutable** al que se le arrastra una carpeta o un montón de archivos
encima. Mismos campos que el lote. Qué resuelve: ya no hay que abrir Photoshop ni
acordarse de los ajustes; el droplet vive en el escritorio y procesa con doble gesto.

Advertencias para la clase: el droplet hecho en Windows no corre en Mac ni al revés, y
si se mueve la acción o se renombra el conjunto, el droplet queda huérfano. Se regenera
en diez segundos, no se repara.

---

## Clase 14 (segunda mitad) — Procesador de imágenes

`Archivo > Secuencias de comandos > Procesador de imágenes` (File > Scripts > Image
Processor).

La herramienta más desaprovechada de Photoshop. En una pasada: toma una carpeta,
guarda en **JPG, PSD y TIFF a la vez**, cada uno con su tamaño máximo, y además puede
aplicar una acción encima.

El caso de la tienda, que es la entrega de la clase: de una carpeta de fotos editadas
salen tres carpetas solas —`tienda/` a 2000 px, `reel/` a 1080 px, `miniatura/` a 1280
px— sin tocar nada más.

Dato que hay que decir: el Procesador de imágenes **crea sus propias subcarpetas** por
formato. No hay que crearlas antes.

---

## Clase 23 — Variables y conjuntos de datos I

Aquí es donde el espectador se queda con la boca abierta, así que el orden importa:
primero el resultado, luego el cómo.

**La idea:** un PSD de plantilla + una hoja de cálculo = tantas imágenes como filas
tenga la hoja. Un diseño, veinte productos.

### Paso 1 — Preparar el PSD

Cada cosa que vaya a cambiar, en **su propia capa** y con **nombre claro**:
`nombre-producto`, `precio`, `foto`, `sello-envio`.

### Paso 2 — Definir las variables

`Imagen > Variables > Definir` (Image > Variables > Define).

Se elige una capa y se le asigna un tipo:

| Tipo | Qué cambia | Para qué en la tienda |
|---|---|---|
| **Sustitución de texto** | el contenido de una capa de texto | nombre, precio, material |
| **Sustitución de píxeles** | la imagen dentro de la capa | la foto del producto |
| **Visibilidad** | si la capa se ve o no | el sello de "envío gratis", solo en algunos |

En sustitución de píxeles importa el **método**: *Ajustar* mantiene la proporción dentro
del cuadro; *Rellenar* llena el cuadro y recorta; *Conformar* deforma. Para fotos de
producto, **Ajustar**, siempre, o los productos salen estirados y nadie entiende por qué.

### Paso 3 — La hoja de cálculo

Un `.csv` o un `.txt` delimitado por tabulaciones, en UTF-8, **primera fila con los
nombres exactos de las variables**:

```csv
nombre-producto,precio,foto,sello-envio
Anillo dona,180,fotos/anillo.jpg,VERDADERO
Rascador esquinero,420,fotos/rascador.jpg,VERDADERO
Soporte de audífonos,150,fotos/soporte.jpg,FALSO
```

Para visibilidad se escribe `VERDADERO` / `FALSO` (en la interfaz en español) y para
píxeles, la **ruta** al archivo. Rutas relativas al CSV para que todo sea portátil.

### Paso 4 — Importar y exportar

1. `Archivo > Importar > Conjuntos de datos variables` (File > Import > Variable Data
   Sets). Marcar "usar la primera columna para nombres de los conjuntos de datos" y
   "sustituir conjuntos de datos existentes".
2. Revisar uno por uno con `Imagen > Variables > Conjuntos de datos` y el botón de
   **aplicar**, para ver en el lienzo que la fila cayó donde debía.
3. `Archivo > Exportar > Conjuntos de datos como archivos` (Export > Data Sets as
   Files). Carpeta de destino y, en el nombre, "nombre del conjunto de datos" para que
   cada archivo salga con el nombre de su producto.

### El detalle que tira a todo el mundo

**La exportación de conjuntos de datos sale en PSD, siempre.** No hay opción de JPG ni
de PNG en ese cuadro de diálogo. Es un límite de la función, no un error de
configuración, y es la razón por la que la mitad de la gente abandona las variables
creyendo que no sirven.

La solución es de dos pasos y es exactamente el cierre de la clase:

```
Exportar conjuntos de datos  →  carpeta de PSD
        ↓
Archivo > Secuencias de comandos > Procesador de imágenes  →  JPG en los 3 tamaños
```

Esa cadena —CSV → PSD → Procesador de imágenes → JPG— es el flujo profesional completo
y cabe en una diapositiva. Vale la pena dejarla en pantalla 10 segundos y repetirla al
final.

---

## Clase 24 — Variables II: las miniaturas del curso

La clase donde el curso se ilustra a sí mismo: se generan **las 30 miniaturas de este
curso** desde un CSV, en vivo, con la plantilla de la clase 18. El CSV y el detalle de
la plantilla están en [`miniaturas.md`](miniaturas.md).

Es la mejor prueba posible de que la técnica sirve, porque el espectador ya vio esas 30
miniaturas al entrar a la lista.

---

## Clases 25 y 26 — Scripts `.jsx`

Cuándo una acción ya no alcanza: cuando hay que **decidir** algo (si la foto es vertical
haz esto, si no, lo otro), cuando hay que **recorrer** una lista, o cuando hay que leer
el nombre de las capas.

`Archivo > Secuencias de comandos > Explorar` (File > Scripts > Browse) para correr un
`.jsx`. Si el `.jsx` se guarda en la carpeta `Presets/Scripts` de Photoshop, aparece en
ese mismo menú al reiniciar.

El script de la clase: **exportar cada grupo de capas como un JPG distinto**. Es el caso
real de quien tiene un PSD con las 6 variantes de color de un producto, cada una en su
grupo.

```javascript
// exportar-grupos.jsx — un JPG por cada grupo de capas del documento abierto
#target photoshop

var doc = app.activeDocument;
var carpeta = Folder.selectDialog("¿Dónde guardo los JPG?");

if (carpeta != null) {
    var grupos = doc.layerSets;

    // apagar todos los grupos; lo que no sea grupo (fondo, marca) se queda visible
    for (var i = 0; i < grupos.length; i++) {
        grupos[i].visible = false;
    }

    for (var i = 0; i < grupos.length; i++) {
        grupos[i].visible = true;

        var opciones = new JPEGSaveOptions();
        opciones.quality = 9;

        var archivo = new File(carpeta + "/" + grupos[i].name + ".jpg");
        doc.saveAs(archivo, opciones, true, Extension.LOWERCASE);

        grupos[i].visible = false;
    }

    alert("Listos " + grupos.length + " archivos.");
}
```

Cómo se enseña, en este orden exacto:

1. Correrlo primero y ver el resultado. Nadie aguanta código sin haber visto para qué.
2. Leerlo línea por línea. Son tres ideas: `doc.layerSets` es la lista de grupos, el
   `for` las recorre, `saveAs` con `true` guarda **una copia** sin tocar el archivo
   abierto.
3. Cambiar **un** número en pantalla: `quality = 9` a `quality = 6`, y comparar el peso.
   Que el espectador vea que el código se puede tocar sin romperlo.
4. Decir qué hacer cuando marque error: el renglón donde falla sale en el aviso, y el
   error más común es tener el documento sin guardar o un grupo con un nombre que lleva
   `/` o `:`, que no son caracteres válidos para un nombre de archivo.

**Probar el script en la máquina de grabación antes de grabar.** Las versiones cambian
cosas chicas y un script que falla en cámara es la única toma que no se puede salvar
hablando.

Mención al cierre, sin profundizar: Adobe empuja **UXP** y los plugins modernos para lo
que antes se hacía con ExtendScript. Para el trabajo de una tienda, `.jsx` sigue siendo
la relación esfuerzo/resultado más alta. Decirlo así, en una frase, y seguir.

---

## Clase 27 — Imposición, y la salida hacia el reel

El cierre del módulo y lo que conecta el curso con el resto del canal: la carpeta que
sale de Photoshop entra directo al pipeline de video de este repositorio.

```bash
# las fotos del Procesador de imágenes, ya a 1080 px, se vuelven un reel
python scripts/slideshow.py --imagenes "salida/reel" --out "reel.mp4" \
    --segundos 2.6 --estilo michilab \
    --textos "Anillo dona||PETG resistente||Envío gratis" \
    --gancho "Tu gato ya tiene|donde rascarse" --cta "michilab.store"
```

Lo que hay que respetar desde Photoshop para que el video salga bien, y que es la parte
que a nadie se le ocurre:

| En Photoshop | Por qué |
|---|---|
| Lienzo 1080x1920 | es el tamaño exacto del reel; cualquier otra cosa se reescala y pierde nitidez |
| Nada importante arriba de y=210 ni abajo de y=1470 | la interfaz de la red tapa esas franjas (ver `../../references/plataformas.md`) |
| JPG calidad 80, no 100 | el 100 pesa el doble y la red lo recomprime igual |
| Nombres con número al inicio (`01-`, `02-`) | `slideshow.py` toma las fotos en orden alfabético: el orden del reel se decide con el nombre del archivo |
| RGB, 72 ppp | si va en CMYK los colores salen apagados en el video |

Esa última tabla es la clase entera: **el archivo se diseña para su destino**. Es la
idea con la que se cierra el módulo.
