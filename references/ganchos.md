# Ganchos, guiones y copy para video de tienda

El cuello de botella de una tienda nueva no es la tienda, es el **alcance**. Estos son
los moldes que funcionan para producto impreso en 3D.

## Los primeros 3 segundos

El gancho se escribe en dos lineas y va en pantalla, arriba, sobre el video. Se pasa
al render como `--gancho "linea 1|linea 2"`.

### Moldes que jalan

| Molde | Ejemplo para Michilab |
|---|---|
| Objecion de frente | `"Cuesta menos que|una lata de atun al mes"` |
| Resultado antes que producto | `"Dejo de rascar el sillon|en 3 dias"` |
| Numero concreto | `"4 horas de impresion|y aguanta 6 kilos"` |
| Antes / despues | `"Asi tenia el sillon|y asi lo tiene hoy"` |
| Curiosidad de proceso | `"Nadie te dice esto|de imprimir en PETG"` |
| Error comun | `"Si tu gato hace esto|le falta esto"` |
| Comparacion honesta | `"El de tienda vs|el que imprimi yo"` |
| Pregunta directa | `"Tu gato tambien|se sube a la mesa?"` |

### Lo que NO funciona

- "Hola, bienvenidos a mi canal" — se pasan de largo.
- "Hoy les traigo un nuevo producto" — no promete nada.
- Cifras inventadas de clientes o ventas — regla de marca: prohibido.
- El nombre del producto solo, sin beneficio.

## Estructura de un reel de 15-25 s

```
0.0 - 3.0 s   GANCHO      texto en pantalla + la imagen mas llamativa
3.0 - 6.0 s   PROBLEMA    lo que le pasa hoy al cliente
6.0 - 14.0 s  RESULTADO   el producto EN USO, no en la mesa
14.0 - 20.0 s PRUEBA      material, resistencia, tamano real (mano al lado)
20.0 - 23.0 s CTA         "michilab.store" + envio gratis
```

Para el flujo de fotos (`slideshow.py`), el mismo orden: foto llamativa primero, foto
en uso al centro, foto de detalle o empaque al final.

## Angulos por tipo de producto

- **Producto para gatos:** el gato usandolo. Siempre. Es el video que mas vende.
- **Pieza funcional (soportes, organizadores):** el antes y despues del escritorio.
- **Timelapse de impresion:** acelerado, con la pieza terminada en los primeros 2 s como anticipo. Nunca empieces por la cama vacia.
- **Empaque:** manos, papel, sticker. Va bien como cierre, no como gancho.

## Texto sobre las fotos

Corto y en mayusculas solo si es una palabra clave. Un texto por foto, maximo 4-5
palabras. Ejemplos: "PETG, no PLA", "Aguanta garras", "Envio gratis", "Hecho en CDMX".

## Copy para publicar

Estructura de 3 lineas + hashtags:

```
[Beneficio en una linea, mismo tono que el gancho]
[Detalle concreto: material, medida, tiempo de entrega]
[CTA: link en bio / michilab.store · envio gratis nacional]

#gatos #michilab #impresion3d #petg #cdmx #productosparagatos
```

Reglas: sin emojis de corazon (la marca usa 🐾), sin testimonios inventados, y el mismo
video se sube a TikTok, Reels y Shorts el mismo dia.

## Cadencia

3-5 videos al dia durante 2-3 semanas para testear angulos. Del lote, se repite el
angulo que retuvo, no el que mas gusto internamente.
