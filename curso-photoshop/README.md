# Curso de Photoshop desde cero — plan del curso

Curso gratuito en YouTube, 30 clases, de abrir el programa por primera vez a generar
200 imágenes sin tocar el ratón.

**La diferencia con los otros cursos de Photoshop de YouTube:** aquí no se enseña
Photoshop en abstracto. Las 30 clases se trabajan **con la misma figura estilo Funko**,
y Photoshop es la herramienta con la que se resuelve lo que esa figura necesita: el
recorte, el fondo, la sombra, el color, la ficha, la miniatura, la caja para imprenta y
las 200 variantes cuando ya hay catálogo. Cada clase termina con un archivo exportado.
Ninguna clase termina con "y aquí ven que esta herramienta hace este efecto".

**Por qué una figura y no una foto de ejemplo cualquiera:** porque es el peor caso de
casi todo. Cabeza redonda (ahí se ve cualquier deformación), brillos de plástico (ahí
se rompen los recortes), hueco entre el brazo y el cuerpo (ahí fallan las selecciones
automáticas) y una cara (ahí el ojo humano revisa más duro). Si le sale con eso, le
sale con lo que sea. Y de paso el curso lo graba alguien trabajando en lo suyo, que se
nota y se cree.

Eso es también lo que lo hace atractivo desde el día 1: el espectador no viene a
aprender un programa, viene a ver cómo se hace eso. El plan de lanzamiento está en
[`00-lanzamiento.md`](00-lanzamiento.md), y lo que hay que hacer **hoy**, paso a paso,
en [`hoja-de-rodaje-dia-1.md`](hoja-de-rodaje-dia-1.md).

## Las reglas del curso

1. **Una clase, una entrega.** Si la clase no produce un archivo que se sube a algún
   lado, la clase no existe. La entrega va anunciada en el primer minuto.
2. **Promesa en los primeros 15 segundos**, mostrando el resultado terminado. Sin
   intro animada, sin "hola, bienvenidos a mi canal", sin presentarse.
3. **Se graba con errores dentro.** Cuando una selección sale mal, se deja y se
   arregla en pantalla. Es lo que separa este curso de los que se graban en limpio: el
   espectador va a cometer ese error y necesita verlo resuelto, no evitado.
4. **Los atajos se dicen en voz alta cada vez**, las 30 clases. "Ctrl+J, duplicar."
   La repetición es el método; no hay una clase de atajos, hay 30.
5. **Nada de cifras inventadas.** Ni alumnos, ni ventas, ni "el 90% de los diseñadores".
   Lo único que se promete es lo que se entrega en pantalla. Misma regla de marca que
   el resto del canal.
6. **El archivo de la clase va gratis en el comentario fijado.** El PSD con el que se
   graba, tal cual, con las capas sucias.
7. **Cada clase apunta a la siguiente, no a suscribirse.** La pantalla final es la
   Clase N+1.

## Dónde se abre Photoshop (y cuándo toca pagar)

El curso está partido para que las primeras 21 clases se puedan hacer **gratis y
legalmente** en Photopea, que corre en el navegador y usa los mismos atajos y la misma
lógica de capas y máscaras. A partir de la clase 22 ya no alcanza: la automatización
—Acciones, Lote, Droplets, Variables, Procesador de imágenes, scripts— solo existe en
el Photoshop de escritorio. Ese corte es honesto y además es el mejor argumento del
curso: el espectador llega a la clase 22 ya sabiendo trabajar, y entonces entiende qué
está pagando. Detalle en [`referencias/acceso-legal.md`](referencias/acceso-legal.md).

| Clases | Dónde | Costo |
|---|---|---|
| 0-21 | Photopea (navegador), con **dos excepciones**: la 12 (Camera Raw) y la 19 (CMYK para imprenta) piden escritorio | $0 |
| 22-30 | Photoshop de escritorio, obligatorio | plan de paga |

Photopea sí tiene panel de Acciones y carga archivos `.atn`, así que parte de la clase
22 se puede seguir ahí. Lo que no tiene es **Lote sobre carpetas, Droplets, Variables y
conjuntos de datos, Procesador de imágenes, CMYK y 16 bits**, que es justo el contenido
de las clases 23 a 28.

## La malla

Duraciones objetivo. Si una clase se pasa 4 minutos del objetivo, se parte en dos.

### Módulo 0 — El pacto

| # | Clase | Dur | Te llevas |
|---|---|---|---|
| 0 | Lo que vas a poder hacer en 30 clases | 4:30 | Photoshop abierto, gratis y legal |

### Módulo 1 — Los comandos (gratis)

| # | Clase | Dur | Te llevas |
|---|---|---|---|
| 1 | Interfaz y los 12 atajos que son el 90% del trabajo | 12 min | Lienzo 1080x1920 con la figura centrada, exportado bajo 2 MB |
| 2 | Capas y máscaras: el único concepto que importa | 14 min | Ficha con la figura + nombre + número + logo en capas separadas |
| 3 | Selecciones: lazo, varita y Seleccionar sujeto | 13 min | `03-figura-recortada.png`, con fondo transparente |
| 4 | Transformar sin deformar | 11 min | La misma figura en 3 tamaños, sin deformar ni pixelear |
| 5 | Tamaño de imagen vs tamaño de lienzo (el error #1) | 10 min | 2000x2000 para tienda y 1080x1920 para reel, del mismo archivo |
| 6 | Pincel, borrador y el truco de borrar sin borrar | 12 min | 3 fotos de la figura limpias |
| 7 | Guardar y exportar: PSD, JPG, PNG, WebP | 10 min | El mismo diseño en los 4 formatos, con sus pesos comparados |

### Módulo 2 — Foto de producto que vende

| # | Clase | Dur | Te llevas |
|---|---|---|---|
| 8 | Fondo blanco real: bordes, pelo y plástico translúcido | 15 min | Foto que pasa el filtro de cualquier marketplace |
| 9 | Sombra que no parece pegada: contacto, caída y reflejo | 14 min | La misma foto con sombra creíble |
| 10 | Color: niveles, curvas y por qué tu naranja se ve lavado | 15 min | Las 3 fotos con el color de marca igualado |
| 11 | Quitar lo que estorba: Tampón, Parche, Eliminar | 13 min | Mesa sin cables, figura sin rayones ni brillos de más |
| 12 | Camera Raw como filtro: la base de toda foto de celular (escritorio) | 14 min | Preajuste propio aplicable a todo lo que grabes |
| 13 | Enfoque y ruido: que se vea la textura de la pieza | 11 min | Macro de la pintura de la cara que aguanta zoom |
| 14 | La figura sobre fondo de marca, en 3 variantes | 14 min | 3 fotos listas para la ficha del producto |

### Módulo 3 — Lo que la gente ve antes de leer

| # | Clase | Dur | Te llevas |
|---|---|---|---|
| 15 | Texto: jerarquía, tracking y por qué el nombre no cabe | 13 min | Los 4 textos de la ficha legibles a tamaño real |
| 16 | Formas vectoriales y el logo que nunca pixelea | 12 min | Tu logo en SVG + PNG en 5 tamaños |
| 17 | Objetos inteligentes: el concepto que ahorra 10 horas al mes | 14 min | Plantilla donde cambias una foto y se actualizan 6 piezas |
| 18 | La miniatura de este curso, hecha en vivo | 16 min | Plantilla 1280x720 bajo 2 MB, con tu sistema de color |
| 19 | La caja para imprenta: CMYK, sangrado, 300 ppp y marcas de corte (escritorio) | 15 min | PDF que la imprenta acepta sin regresártelo |
| 20 | Mockup: tu diseño sobre la caja real | 14 min | Foto de la caja sin haber impreso nada |
| 21 | Plantilla maestra: un PSD que escupe los 6 formatos | 15 min | El PSD maestro |

### Módulo 4 — Automatización (Photoshop de paga)

| # | Clase | Dur | Te llevas |
|---|---|---|---|
| 22 | Acciones: graba una vez, úsalo mil | 14 min | 3 acciones tuyas, exportadas en .atn |
| 23 | Lote y Droplet: arrastra 200 fotos y vete a dormir | 15 min | Un .exe al que le tiras una carpeta |
| 24 | Procesador de imágenes: 3 tamaños de cada foto en una pasada | 11 min | Carpetas tienda/ reel/ miniatura/ generadas solas |
| 25 | Variables y conjuntos de datos I: un PSD + un CSV | 16 min | 20 fichas de producto desde una hoja de cálculo |
| 26 | Variables II: las 30 miniaturas de este curso desde el CSV | 15 min | Las 30 miniaturas reales del curso |
| 27 | Scripts .jsx: cuando la acción ya no alcanza | 16 min | Script que exporta cada grupo de capas como JPG |
| 28 | De Photoshop al reel: enlazar la salida con el pipeline de video | 15 min | Carpeta de fotos que entra directo a `slideshow.py` |

### Módulo 5 — Cerrar el círculo

| # | Clase | Dur | Te llevas |
|---|---|---|---|
| 29 | El flujo completo en una sentada: 40 fotos crudas a tienda publicada | 20 min | Un producto entero publicado |
| 30 | Qué cobrar por esto y cómo entregarlo | 14 min | Lista de precios y de entregables |

Total: unas 6 h 30 min de clase.

## Qué hay en esta carpeta

```
README.md                         este plan
hoja-de-rodaje-dia-1.md           QUÉ HACER HOY, paso a paso, para grabar 6 clases
00-lanzamiento.md                 el plan de subida: títulos, miniaturas, cadencia, Cursos de YouTube
guiones/
  _plantilla.md                   molde de guion, con los tiempos y las marcas de pantalla
  clase-00-promesa.md             guion completo del video 0 (el que vende el curso)
  clase-01-interfaz-atajos.md     guion completo
  clase-02-capas-mascaras.md      guion completo
  clase-03-selecciones.md         guion completo
  clase-04-transformar.md         guion completo
  clase-05-imagen-vs-lienzo.md    guion completo
  shorts-lanzamiento.md           Shorts del día 1 + el plan JSON para lote.py
referencias/
  acceso-legal.md                 cómo abrir Photoshop sin pagar y cuándo ya no se puede
  atajos.md                       la chuleta: qué atajo se enseña en qué clase
  automatizacion.md               el módulo 4 a detalle, con rutas de menú exactas
  miniaturas.md                   el sistema de miniaturas del curso
  metricas.md                     qué medir y qué decidir con cada número
```

Y en la carpeta de trabajo (`Desktop\Curso Photoshop`), además:

```
material/base/                    las 6 fotos de la figura, crudas. El material de las 30 clases
plantillas/                       los PSD terminados de cada clase, para poder repetir toma
entregas/                         lo que se exporta en cada clase (es lo que va al comentario fijado)
grabaciones/                      la salida de OBS
```

## Cómo se produce cada clase

El canal ya tiene el pipeline de video ([`../SKILL.md`](../SKILL.md)), así que la
producción de la clase es:

1. Escribir el guion desde `guiones/_plantilla.md`. **Nunca grabar sin guion**: el
   silencio pensando es lo que hace que la gente se vaya.
2. Grabar pantalla a 1920x1080, 30 fps, **en Photopea**, en español, con la barra de
   atajos visible (OBS: fuente de entrada de teclado en la esquina). Por qué en Photopea
   y no en Photoshop: el único Photoshop de esta máquina es un CS6 portable que abre
   como administrador, y OBS no engancha una ventana elevada ni ve las teclas que se
   teclean en ella; además CS6 no tiene *Seleccionar sujeto*, que la clase 3 necesita.
   Grabar en Photopea tiene además la ventaja de que lo que se ve en pantalla es
   exactamente lo que el espectador tiene abierto.
3. Subir la clase larga a YouTube.
4. Sacar 3 Shorts verticales de esa misma clase con el pipeline del repo:
   `momentos.py` no sirve aquí (es material de pantalla, no de movimiento), así que se
   marcan los tiempos a mano en el guion —cada guion trae la línea `SHORT:`— y se
   renderizan con `lote.py`.
5. Publicar los Shorts en los 3 días siguientes, cada uno apuntando a la clase.
