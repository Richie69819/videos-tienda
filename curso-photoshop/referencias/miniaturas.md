# El sistema de miniaturas del curso

Las miniaturas de un curso no se ven de una en una: se ven **las treinta juntas** en la
página de la lista. Ahí es donde el espectador decide si esto es un plan o un montón de
videos sueltos. Por eso no son treinta diseños, es un sistema con treinta datos.

Y por eso se generan con Variables en la clase 26, no a mano: hacer treinta a mano
garantiza que la número veinte ya no se parezca a la número dos.

## Especificaciones

| | |
|---|---|
| Tamaño | 1280 x 720 px |
| Peso | bajo 2 MB (JPG calidad 80 suele dar 300-600 KB) |
| Modo | RGB, 72 ppp |
| Texto | máximo 3 palabras |
| Legibilidad | tiene que leerse al 10% del tamaño: si se achica a 128 px de ancho y no se lee, no sirve |

La prueba del 10% va en la clase 18, en pantalla: se achica la miniatura al tamaño de
una uña y se pregunta en voz alta "¿se lee?". Es la única prueba que importa, porque es
el tamaño al que la gente la va a ver en el celular.

## Rejilla fija

```
┌──────────────────────────────────────────┐  1280 x 720
│ ███                                      │  número de clase: esquina superior
│ ███  ← 01            [ resultado    ]    │  izquierda, 180 px de alto, siempre
│                      [ terminado    ]    │
│   PALABRA            [ ocupando la  ]    │  texto: izquierda, 2-3 palabras,
│   CLAVE              [ mitad derecha]    │  Montserrat ExtraBold
│                                          │
│ ▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁ │  franja del módulo: 24 px abajo
└──────────────────────────────────────────┘
```

Reglas de la rejilla, que son las que hacen que la lista se vea como curso:

1. **El número de clase siempre en el mismo lugar**, mismo tamaño, misma tipografía.
   Es lo que convierte treinta imágenes en una secuencia.
2. **El resultado terminado a la derecha, no la interfaz de Photoshop.** Nadie hace clic
   en una captura de paneles grises. Se hace clic en la foto bonita del producto.
3. **Un color por módulo**, en la franja de abajo y en el número. Al ver la lista
   completa se distinguen los cinco bloques de un vistazo.
4. **Sin cara, sin flechas rojas, sin círculos, sin signos de admiración.** El canal
   vende producto; esa estética no corresponde y además ya la usan todos.
5. **Sin logos grandes.** El logo chico, abajo a la derecha, al 70% de opacidad.

## Colores por módulo

| Módulo | Color | Clases |
|---|---|---|
| 0 — El pacto | negro | 0 |
| 1 — Los comandos | naranja de marca | 1-7 |
| 2 — Foto de producto | olivo de marca | 8-14 |
| 3 — Diseño | crema de marca | 15-21 |
| 4 — Automatización | negro con filo naranja | 22-28 |
| 5 — Cerrar | olivo oscuro | 29-30 |

Los valores exactos salen del kit de marca, los mismos que usa `pantalla_final.py`. No
inventar colores nuevos para el curso: el curso es parte del canal.

## La plantilla con variables

El PSD `miniatura-curso.psd` se construye en la clase 18 y se le definen las variables
en la clase 26:

| Capa | Variable | Tipo |
|---|---|---|
| `numero` | `numero` | sustitución de texto |
| `palabra-clave` | `palabra` | sustitución de texto |
| `resultado` | `imagen` | sustitución de píxeles, método **Ajustar** |
| `franja-modulo` | `color-modulo` | sustitución de píxeles (una tira de color plano por módulo) |
| `insignia-escritorio` | `solo-escritorio` | visibilidad (el sello chico de "requiere Photoshop") |

## El CSV de las 30 miniaturas

Se guarda en UTF-8. La primera columna da el nombre del archivo de salida.

```csv
numero,palabra,imagen,color-modulo,solo-escritorio
00,30 CLASES,res/00-antes-despues.jpg,color/negro.png,FALSO
01,12 ATAJOS,res/01-teclado.jpg,color/naranja.png,FALSO
02,NO BORRES,res/02-mascara.jpg,color/naranja.png,FALSO
03,DOS CLICS,res/03-recorte.jpg,color/naranja.png,FALSO
04,SIN DEFORMAR,res/04-escala.jpg,color/naranja.png,FALSO
05,EL ERROR 1,res/05-tamanos.jpg,color/naranja.png,FALSO
06,BORRAR SIN BORRAR,res/06-pincel.jpg,color/naranja.png,FALSO
07,4 FORMATOS,res/07-exportar.jpg,color/naranja.png,FALSO
08,FONDO BLANCO,res/08-fondo.jpg,color/olivo.png,FALSO
09,SOMBRA REAL,res/09-sombra.jpg,color/olivo.png,FALSO
10,TU NARANJA,res/10-color.jpg,color/olivo.png,FALSO
11,QUITA ESO,res/11-tampon.jpg,color/olivo.png,FALSO
12,CAMERA RAW,res/12-raw.jpg,color/olivo.png,VERDADERO
13,LA TEXTURA,res/13-enfoque.jpg,color/olivo.png,FALSO
14,3 FONDOS,res/14-marca.jpg,color/olivo.png,FALSO
15,NO SE LEE,res/15-texto.jpg,color/crema.png,FALSO
16,NUNCA PIXELEA,res/16-vector.jpg,color/crema.png,FALSO
17,10 HORAS MENOS,res/17-inteligente.jpg,color/crema.png,FALSO
18,ESTA MINIATURA,res/18-miniatura.jpg,color/crema.png,FALSO
19,PARA IMPRENTA,res/19-etiqueta.jpg,color/crema.png,VERDADERO
20,SIN EMPACAR,res/20-mockup.jpg,color/crema.png,FALSO
21,6 FORMATOS,res/21-plantilla.jpg,color/crema.png,FALSO
22,GRABA UNA VEZ,res/22-acciones.jpg,color/negro-naranja.png,VERDADERO
23,200 FOTOS,res/23-lote.jpg,color/negro-naranja.png,VERDADERO
24,3 TAMANOS,res/24-procesador.jpg,color/negro-naranja.png,VERDADERO
25,UN CSV,res/25-variables.jpg,color/negro-naranja.png,VERDADERO
26,ESTAS 30,res/26-miniaturas.jpg,color/negro-naranja.png,VERDADERO
27,CODIGO,res/27-script.jpg,color/negro-naranja.png,VERDADERO
28,AL REEL,res/28-video.jpg,color/negro-naranja.png,VERDADERO
29,TODO SEGUIDO,res/29-flujo.jpg,color/olivo-oscuro.png,FALSO
30,QUE COBRAR,res/30-precios.jpg,color/olivo-oscuro.png,FALSO
```

Después de `Archivo > Exportar > Conjuntos de datos como archivos` salen 31 **PSD**
(la exportación no da JPG, ver [`automatizacion.md`](automatizacion.md)), así que el
segundo paso es el Procesador de imágenes con JPG calidad 80 y ancho máximo 1280. El
resultado son 31 archivos de medio mega, listos para subir.

## Lo que se cambia después del estreno

Las miniaturas no son definitivas. A las dos semanas:

1. Mirar el CTR por video en la lista.
2. Tomar las **tres peores** y cambiarles **una sola cosa**: la palabra clave. No el
   diseño, no el color, no la foto. Una variable, que es justo lo que la plantilla
   permite cambiar en treinta segundos.
3. Esperar una semana y comparar contra la mediana del canal, no contra números de
   blogs.

Esa es la ventaja escondida de generar las miniaturas con variables: rehacer tres no
cuesta una tarde, cuesta editar tres renglones del CSV y volver a exportar.
