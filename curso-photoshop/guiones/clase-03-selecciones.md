# Clase 3 — Selecciones

La clase que la gente viene buscando a YouTube. "Cómo quitar el fondo" es una de las
cosas más buscadas del programa, así que esta clase es la puerta de entrada de
desconocidos al curso: el título y la miniatura trabajan para el buscador, no para quien
ya está dentro.

La idea que hay que dejar clavada: **seleccionar es decirle a Photoshop dónde puede
trabajar.** Una selección no cambia nada por sí sola; delimita.

## Ficha

| | |
|---|---|
| Clase | 3 de 30 |
| Módulo | 1 — Los comandos |
| Título | `Curso de Photoshop desde cero — Clase 3: quitar el fondo de verdad (lazo, varita y Seleccionar sujeto)` |
| Duración objetivo | 13:00 |
| Entrega | `03-figura-recortada.png`: la figura sola, con fondo transparente |
| Requisitos | clases 1 y 2 (la máscara se da por sabida) |
| Dónde se puede hacer | Photopea, completo |
| Archivos de la clase | `01-mesa.jpg`, `05-fondo-claro.jpg` y el PNG terminado |
| Atajos nuevos | W, Shift+arrastrar (sumar), Alt+arrastrar (restar), Ctrl+Shift+I (invertir), Ctrl+clic en la miniatura, Ctrl+D |

## Miniatura

- Texto: **2 CLICS**
- Color del módulo 1: naranja de marca
- Qué se ve: a la izquierda la foto con la mesa desordenada; a la derecha la figura sola
  sobre el cuadriculado gris de la transparencia. El cuadriculado es la señal visual que
  cualquiera que ha usado Photoshop reconoce, y quien no, lo reconoce después.

## Antes de grabar

- [ ] `01-mesa.jpg` (fondo desordenado) y `05-fondo-claro.jpg` (fondo parejo) a mano:
      son dos fotos a propósito, porque cada una se recorta con una herramienta distinta
- [ ] El PNG terminado en `plantillas/`, por si hay que repetir la toma
- [ ] Panel de Capas abierto; nada más abierto

---

## Guion

### 0:00-0:15 · Gancho y promesa

> **PANTALLA:** la foto con la mesa desordenada. Dos clics. La figura queda sola sobre el
> cuadriculado de transparencia. Sin voz los primeros 4 segundos.

> "Dos clics. Al final de este video vas a poder quitarle el fondo a cualquier cosa, y
> —más importante— vas a saber qué hacer **cuando los dos clics no alcancen**, que es lo
> que ningún tutorial de treinta segundos te dice. Trece minutos."

> **TEXTO EN PANTALLA:** `03-figura-recortada.png`

### 0:15-1:30 · Teoría: qué es una selección

> **PANTALLA:** hacer una selección rectangular con **M** y, con ella activa, pintar con
> el pincel: la pintura solo cae dentro.

> "Una selección no recorta nada. Una selección le dice a Photoshop: **de aquí para
> dentro sí, de aquí para fuera no**. Mira: selecciono este cuadro, agarro el pincel, y
> pinto por todos lados... y la pintura solo cae adentro. Lo de afuera está protegido."

> "Esa línea que camina —las hormigas— es el borde de la selección. No es un dibujo, no
> se imprime, no existe en el archivo. Es un permiso."

> "Y de ahí sale la cadena entera de este curso: **seleccionas, y de la selección sacas
> una máscara.** Eso es todo lo que vas a hacer veinte veces en las próximas semanas.
> La clase dos fue la máscara, hoy es cómo conseguirla sin pintarla a mano."

> **ERROR A PROPÓSITO:** intentar pintar fuera de la selección y quedarse tres segundos
> dándole al pincel sin resultado.
> "Y este es el 'no me sale' número uno del curso: tengo una selección vieja activa y no
> me doy cuenta. Pinto, y no pasa nada. **Ctrl+D**, deseleccionar. Apúntatelo: cuando
> Photoshop deje de obedecer sin razón, **Ctrl+D** primero y pregunta después."

### 1:30-3:00 · Las cuatro formas, y cuándo usar cada una

> **PANTALLA:** tarjeta con las cuatro, se queda 6 segundos al final.

| Herramienta | Tecla | Cuándo sirve | Cuándo no |
|---|---|---|---|
| **Marco** | **M** | Cuadrados y círculos. Recortes rectos | Cualquier cosa con forma |
| **Lazo** | **L** | Zonas a mano alzada, arreglos rápidos | Para precisión: tiembla el pulso |
| **Varita mágica** | **W** (compartida) | Fondos de **un solo color parejo** | Fondos desordenados |
| **Selección rápida / Seleccionar sujeto** | **W** | Casi todo lo demás | Pelo, humo, cristal |

> "El orden en que hay que pensarlo es al revés de como lo enseñan: **primero mira el
> fondo, no el objeto.** Si el fondo es parejo —una pared blanca, un papel— seleccionas
> el fondo con la varita y lo invitas. Si el fondo es un desmadre, seleccionas el objeto
> con Seleccionar sujeto. Es la misma decisión que vas a tomar siempre, y toma dos
> segundos."

### 3:00-5:30 · Camino A: Seleccionar sujeto (el fondo difícil)

> **PANTALLA:** `01-mesa.jpg`, la de la mesa desordenada.

> "Esta foto tiene cable, tiene mesa, tiene sombra y tiene una taza cortada en la
> esquina. Fondo imposible para la varita. Aquí es donde Seleccionar sujeto se gana el
> sueldo."

1. **W**, y en la barra de opciones, arriba, el botón **Seleccionar sujeto**. "Un clic.
   Esto corre un modelo entrenado para encontrar 'la cosa' de la foto. Y con una figura
   así funciona casi perfecto, porque es exactamente lo que espera encontrar: un objeto
   con silueta clara en el centro."
2. Mirar el resultado de cerca: **Alt+rueda** al hueco entre el brazo y el cuerpo.

> "Y aquí está lo que ningún video de treinta segundos te enseña: **se le olvidó el
> hueco.** Dejó el pedazo de mesa que se mete entre el brazo y el torso. Esto pasa
> siempre, con cualquier figura que tenga un brazo separado del cuerpo, y es lo que
> delata un recorte mal hecho a un metro de distancia."

3. **Alt+arrastrar** con la selección rápida sobre ese hueco: **restar**. "Shift suma a
   la selección, **Alt resta**. Esas dos teclas son el ochenta por ciento del trabajo
   fino y se usan igual en todas las herramientas de selección."
4. Revisar también los pies y la sombra. "La sombra no es la figura. Si la dejas dentro,
   después no puedes poner la figura en otro fondo."

> **ERROR A PROPÓSITO:** sumar en lugar de restar (Shift en vez de Alt) y tragarse media
> mesa. "Le di Shift. Ahora tengo mesa adentro. **Ctrl+Z**. Shift suma, Alt resta. Lo voy
> a repetir las treinta clases."

### 5:30-7:30 · Camino B: la varita y la inversión (el fondo fácil)

> **PANTALLA:** `05-fondo-claro.jpg`, la del fondo parejo.

> "Ahora el camino corto, el que usa quien ya sabe. Esta foto tiene el fondo casi parejo.
> No voy a seleccionar la figura: voy a seleccionar **el fondo**, que es más fácil, y
> luego lo volteo."

1. **W**, varita mágica. Clic en el fondo.
2. **La tolerancia.** "Este número de la barra de opciones es lo único que hay que
   entender de la varita: **qué tan parecido tiene que ser un píxel para que también
   entre.** Tolerancia baja, agarra poquito. Tolerancia alta, agarra de más."

> **ERROR A PROPÓSITO:** tolerancia en 10, clic, y queda medio fondo fuera. Luego
> tolerancia en 100 y se traga la figura.
> "Diez: me dejó manchones de fondo. Cien: se comió la figura, porque la cabeza tiene
> un reflejo claro casi del mismo tono que la pared. En treinta y dos queda bien. No hay
> número correcto: se mueve, se prueba y se mira. Eso es trabajar en Photoshop."

3. **Shift+clic** en los manchones que faltaron. "Sumando, con Shift."
4. **Ctrl+Shift+I**, invertir la selección. "Tenía el fondo. Ahora tengo la figura. Este
   atajo es de los que cambian la vida: casi siempre es más fácil seleccionar el fondo
   y voltear."

> "Y una advertencia honesta sobre los ojos: estas figuras tienen los ojos negros y muy
> definidos, y si en vez de la varita usaras un ajuste automático de contraste se te
> van a tapar. Hoy no pasa porque estamos seleccionando el fondo, no el color de la
> figura — pero tenlo presente para la clase diez, cuando toquemos niveles."

### 7:30-10:30 · De la selección a la máscara (y el PNG)

> "Tengo la selección. Ahora lo de la clase dos: la convierto en máscara, que es
> reversible, en vez de borrar, que no lo es."

1. Con la selección activa, clic en el botón de máscara del panel de Capas. "Y listo: la
   selección se volvió máscara. Lo de adentro se ve, lo de afuera se tapó. **Nada se
   borró.**"
2. **Alt+rueda** al borde de la cabeza. "Mira el borde: tiene un filo duro, como de
   tijera. Se nota recortado."
3. **Seleccionar y aplicar máscara** (en la barra de opciones con una selección activa).
   "Aquí solo vamos a mover dos controles de todos los que hay: **Suavizar** un poquito,
   y **Desplazar borde** hacia dentro uno o dos. Eso le quita el filo de tijera y te come
   el píxel de fondo que siempre se queda pegado en la orilla. Los demás controles son
   para pelo y son la clase siete."

> **NOTA DE GRABACIÓN:** si grabas en Photoshop CS6 esto se llama **Perfeccionar borde**
> y vive en otro lugar. Decirlo en una línea para quien tenga una versión vieja, y
> seguir.

4. **Ctrl+clic en la miniatura de la máscara** para recuperar la selección si hace falta
   después. "Guarda ese atajo: una máscara se puede volver selección otra vez, cuando
   quieras."
5. **Ctrl+Shift+Alt+W**, exportar. **Formato PNG**, `03-figura-recortada.png`.

> **TEXTO EN PANTALLA, grande:** `JPG no guarda transparencia · PNG sí`

> "Y aquí la cosa más importante de la clase, que no tiene nada que ver con seleccionar:
> **el JPG no sabe hacer transparencia.** Si exportas esto en JPG, el fondo transparente
> te sale blanco y acabas de perder todo el trabajo. Para algo recortado: **PNG**.
> Siempre. Si alguna vez subes un recorte y te aparece con un cuadro blanco atrás, es
> esto, y ya sabes por qué."

> "Pesa más que un JPG, y vale la pena. En la clase siete vemos los cuatro formatos y
> cuál va en cada lugar."

### 10:30-12:00 · Lo que no se puede, y qué hacer entonces

> "Para que no pierdas una tarde: hay tres cosas que **ninguna** de estas herramientas
> resuelve bien de un clic."

| Caso | Por qué cuesta | Dónde se resuelve |
|---|---|---|
| Pelo, pelusa, flecos | Miles de bordes semitransparentes | Clase 7 |
| Plástico transparente, la ventana de una caja | El fondo se ve **a través** del objeto | Clase 7 |
| Objeto del mismo color que el fondo | No hay contraste de dónde agarrarse | Se resuelve con luz al tomar la foto, no en Photoshop |

> "Ese tercer caso es el que más importa, y la respuesta no es una herramienta: es que
> **la foto se arregla antes de tomarla**. Si pones la figura sobre una tela de un color
> que no tenga, el recorte te toma dos clics en vez de veinte minutos. La mejor
> herramienta de selección de Photoshop es una cartulina de diez pesos."

### Cierre (últimos 20 s)

> "Tu reto: sube tu PNG recortado a los comentarios. Si se ve el cuadrito blanco atrás,
> lo exportaste en JPG y ya sabes qué hacer."

> "Suscríbete, y la clase cuatro es transformar sin deformar: por qué tu figura se ve
> achatada y cómo escalarla a tres tamaños sin que pierda la forma. Ahí te veo."

> **PANTALLA FINAL:** Clase 4.

---

## Shorts de esta clase

```
SHORT 1: desde=09:40 hasta=09:58 gancho="Tu recorte sale con|fondo blanco por esto"
SHORT 2: desde=04:30 hasta=04:52 gancho="Seleccionar sujeto|siempre olvida esto"
SHORT 3: desde=07:05 hasta=07:22 gancho="Selecciona el fondo|no el objeto"
```

## Descripción

```
Cómo quitar el fondo de verdad: las 4 herramientas de selección, cuál usar según el
fondo, y qué hacer cuando "Seleccionar sujeto" no alcanza. Al final tienes tu figura
recortada en PNG con fondo transparente.

Fotos y PNG de la clase: [link]
Lista completa del curso: [link]
Clase anterior (Clase 2 — Capas y máscaras): [link]  ·  Clase siguiente (Clase 4 — Transformar): [link]

Minutos:
00:00 Dos clics (y cuándo no alcanzan)
00:15 Qué es una selección (y el "no me sale" número 1)
01:30 Las 4 herramientas y cuándo usar cada una
03:00 Seleccionar sujeto, y el hueco que siempre se le olvida
05:30 Varita, tolerancia e invertir la selección
07:30 De la selección a la máscara
09:30 Por qué tu recorte sale con fondo blanco (JPG vs PNG)
10:30 Lo que no se puede recortar, y qué hacer entonces

Esta clase se puede hacer completa en Photopea, gratis, desde el navegador.
Si usas Photoshop CS6, "Seleccionar y aplicar máscara" se llama "Perfeccionar borde".

#photoshop #cursodephotoshop #quitarfondo #seleccionarsujeto #funko
```

## Comentario fijado

```
Las 2 fotos de la clase + el PNG recortado terminado: [link]
Una tiene fondo desordenado y la otra fondo parejo, a propósito: se recortan con
herramientas distintas. Sube tu PNG aquí.
```
