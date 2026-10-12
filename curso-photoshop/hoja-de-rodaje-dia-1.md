# Hoja de rodaje — el día 1: seis clases grabadas

Una sola página. El objetivo del día es cerrar **seis grabaciones**: las clases 1, 2, 3,
4 y 5, y al final la clase 0. En ese orden, que no es el orden del curso y hay una razón
para eso (paso 6).

Carpeta de trabajo: `C:\Users\RICHO\Desktop\Curso Photoshop`

```
Curso Photoshop/
  guiones/           los 6 guiones de hoy (ya están)
  material/
    base/            las 6 fotos del Funko, crudas, sin editar
  plantillas/        los PSD de la clase, ya terminados, para poder repetir toma
  entregas/          lo que exportas en cada clase (es lo que sube al comentario fijado)
  grabaciones/       la salida de OBS
```

---

## Lo que tiene que estar listo antes de hablar

Tres cosas. Nada más. Nada de luces, nada de micrófono nuevo, nada de comprar Photoshop.

### 1. Un solo Funko, seis fotos (30 min)

**Un** Funko, el mismo las 30 clases. Si a la mitad del curso cambias de figura, todas
las clases anteriores dejan de verse como el mismo curso. Que sea uno de los tuyos,
custom, con caja o sin ella — es tu mejor credencial y se ve en el minuto 0.

Con el celular, sin editar, sin filtro, sin luz de estudio. **Feas a propósito**: son
las fotos que tiene el espectador.

| # | Archivo | Qué es | En qué clase se usa |
|---|---|---|---|
| 1 | `01-mesa.jpg` | El Funko completo sobre una mesa cualquiera, fondo desordenado | 0, 1, 2, 8 |
| 2 | `02-mano.jpg` | El Funko en la mano, para que se vea el tamaño real | 13 |
| 3 | `03-caja.jpg` | El Funko con su caja, los dos en el cuadro | 14, 20 |
| 4 | `04-macro.jpg` | Detalle a 10 cm: la cara, la pintura, la textura | 13 |
| 5 | `05-fondo-claro.jpg` | Sobre fondo claro pero con sombras sucias | 8, 9 |
| 6 | `06-estorbo.jpg` | Con algo que estorbe: un cable, una mancha, otra figura cortada | 11 |

Van en `material/base/` con **esos nombres**. Los números al inicio importan: el
pipeline de video toma las fotos en orden alfabético.

- [ ] Las 6 fotos en `material/base/`, sin editar

### 2. El "después" (40 min)

Editar **una sola** —la número 1— hasta dejarla como portada terminada: fondo limpio,
color corregido, el nombre del Funko, tu logo al 70%.

Esa imagen sola es la prueba número uno del minuto 0 de la clase 0, y es el argumento
entero del curso: la misma foto, veinte minutos después.

- [ ] `material/antes-despues.jpg`: las dos versiones lado a lado, 1920x1080

### 3. Las otras dos pruebas de la clase 0 (30 min)

- [ ] **Prueba 2:** una miniatura construyéndose. Graba la pantalla mientras armas una
      miniatura cualquiera y acelera el clip 8x. No tiene que ser la definitiva.
- [ ] **Prueba 3:** las 200 imágenes. Esta es la única que pide Photoshop de escritorio.
      Si hoy no la tienes a mano: **graba la clase 0 sin ella** y deja la promesa en
      palabras ("en la clase 23 vas a poder soltarle 200 fotos"). No retrases el estreno
      por esto; el módulo 4 se graba en semanas.

---

## Paso 4 — Dónde se graba: Photopea, no tu Photoshop

Esto cambia respecto al plan original y es importante, así que va la razón:

1. **OBS no captura bien el CS6 portable.** Ese Photoshop abre como administrador; OBS,
   que corre sin elevar, no engancha la ventana ni ve las teclas que tecleas en ella. La
   barra de atajos en pantalla —que es media clase— se queda muda.
2. **Un CS6 crackeado en pantalla, en un canal, es un reclamo esperando.** Treinta clases
   es demasiado trabajo para montarlo sobre eso.
3. **CS6 le falta lo que la clase 3 necesita.** No tiene *Seleccionar sujeto* ni
   *Seleccionar y aplicar máscara*; tiene *Perfeccionar borde*, que es otra cosa y se
   llama distinto. Si grabas en CS6, el espectador con Photoshop de hoy no encuentra
   nada donde tú lo señalas.

Photopea abre los PSD, usa los mismos atajos, está en español y es gratis. Es también lo
que el espectador va a tener abierto. Cuando algo esté en otro lugar en el Photoshop de
paga, se dice en una línea y se sigue.

- [ ] `photopea.com` abierto, en español (`Más > Idioma > Español`), sin proyecto previo
- [ ] Probar **ahora, antes de grabar**: abrir `material/base/01-mesa.jpg`, hacer una
      selección, poner una máscara. Si el navegador se arrastra, cierra todo lo demás.

## Paso 5 — Preparar la grabación (20 min)

- [ ] OBS: captura de pantalla 1920x1080, 30 fps. Carpeta de salida: `grabaciones/`
- [ ] Zoom del navegador al 110-125%. Lo que no se lee en un celular, no sirve
- [ ] Fuente de **entrada de teclado** en pantalla, abajo a la derecha
- [ ] Micrófono a 15 cm de la boca, no en la mesa
- [ ] El guion de la clase abierto en el segundo monitor o impreso. **Nunca grabar sin
      guion**: el silencio pensando es lo que hace que la gente se vaya
- [ ] **Prueba de 30 segundos:** grabar, cerrar, abrir el archivo y confirmar dos cosas:
      que **se oye la voz** y que el texto de los paneles **se lee**. Esto se revisa
      antes de grabar 12 minutos, no después

## Paso 6 — Grabar, en este orden

| Orden | Clase | Dur. objetivo | Grabar en | Entrega |
|---|---|---|---|---|
| 1º | **Clase 1** — Interfaz y los 12 atajos | 12 min | Photopea | `entregas/01-portada.jpg` |
| 2º | **Clase 2** — Capas y máscaras | 14 min | Photopea | `entregas/02-ficha.jpg` |
| 3º | **Clase 3** — Selecciones | 13 min | Photopea | `entregas/03-funko-recortado.png` |
| 4º | **Clase 4** — Transformar sin deformar | 11 min | Photopea | `entregas/04-tres-tamanos.jpg` |
| 5º | **Clase 5** — Tamaño de imagen vs lienzo | 10 min | Photopea | `entregas/05-tienda.jpg` + `05-reel.jpg` |
| 6º | **Clase 0** — La promesa | 4:30 | pantalla + las 3 pruebas | nada que exportar |

**La clase 1 va primero** porque es la más mecánica y es donde vas a aprender a grabar.
Si sale mal, se regraba sin que duela.

**La clase 0 va al final.** Grabar la clase 0 primero es el error que hace que medio
canal se quede en la clase 0: prometes algo que todavía no sabes si vas a cumplir. Si la
grabas al final del día, dices "la clase 1 ya está arriba" porque de verdad está.

Reglas de grabación, las mismas las seis veces:

- **Una toma. Los errores se dejan dentro** y se arreglan en pantalla. Es la regla 3 del
  curso y es lo que lo separa de los cursos bonitos. Si te equivocas, no cortes: lo
  explicas y lo resuelves.
- **Cada atajo, en voz alta, cada vez.** "Ctrl+J, duplicar."
- **No editar hoy.** Hoy se graba. Mañana se sube.
- Entre clase y clase, **5 minutos de pie y agua**. Seis grabaciones seguidas cansan la
  voz, y se oye.

- [ ] Clase 1 grabada
- [ ] Clase 2 grabada
- [ ] Clase 3 grabada
- [ ] Clase 4 grabada
- [ ] Clase 5 grabada
- [ ] Clase 0 grabada

### El reloj, contado desde que arrancas

| Desde | Qué |
|---|---|
| T+0:00 | Las 6 fotos del Funko |
| T+0:30 | El "después" y las 2 pruebas |
| T+1:40 | OBS, Photopea, prueba de 30 segundos |
| T+2:00 | Clase 1 |
| T+2:25 | Clase 2 |
| T+2:55 | Clase 3 |
| T+3:25 | Clase 4 |
| T+3:50 | Clase 5 |
| T+4:10 | Clase 0 |
| T+4:25 | Hecho |

Cuatro horas y media, sin editar nada. Si el día no alcanza, el corte honesto es
**grabar 1, 2 y 3 hoy** y 4, 5 y 0 mañana temprano — pero no subas nada hasta tener las
seis. Una lista con seis clases se lee como curso; con una, se lee como intento.

## Paso 7 — Subir (mañana, no hoy)

Las seis el mismo día, con los capítulos en la descripción y el comentario fijado en
cada una. Después, la lista configurada como **Curso** en YouTube Studio. El detalle
completo en [`00-lanzamiento.md`](00-lanzamiento.md).

Con seis clases el día del estreno, el módulo 1 queda casi completo de entrada. Eso mata
la duda de "esto lo van a dejar a medias" mejor que cualquier promesa en el video.

---

## Lo que NO hay que hacer hoy

- Comprar luces, micrófono ni Photoshop. Nada de eso es el cuello de botella.
- Diseñar una intro animada.
- Grabar la clase 0 antes de las otras cinco.
- Editar. Hoy se graba.
- Cambiar de Funko a media tarde.
- Esperar a tener las 30 clases escritas al detalle. Están planeadas; el resto se
  escribe sobre la marcha con `guiones/_plantilla.md`.
- Comprar un dominio, hacer un logo nuevo ni abrir un canal aparte para el curso. El
  curso vive en el canal que ya tienes.
