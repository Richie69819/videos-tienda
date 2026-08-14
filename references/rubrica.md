# Rubrica para puntuar segmentos de un video largo

Cada dimension se puntua 0-100 y se pondera. Es la rubrica de claude-shorts con una
sexta dimension propia: en una tienda no basta con que el corte sea entretenido, tiene
que **acercar a la compra**.

```
puntaje = gancho*0.28 + coherencia*0.18 + emocion*0.15 + valor*0.12 + cierre*0.07 + compra*0.20
```

## 1. Gancho (0.28)

Los primeros 3 segundos deciden si te ven o te pasan.

| Arquetipo | Ejemplo | Rango |
|---|---|---|
| Contrario / rompe creencia | "Todo lo que te dijeron del PLA esta mal" | 80-100 |
| Hueco de curiosidad | "Nadie te dice esto antes de comprar una impresora" | 75-95 |
| Promesa concreta | "Asi saco el costo exacto de cada pieza" | 70-90 |
| Interrupcion de patron | "Espera, mira lo que le paso a esta pieza" | 70-90 |
| Anticipo del final | "Al final te enseno como quedo" | 65-85 |
| Arranque en accion | (empieza a media frase, con energia) | 60-80 |
| Generico | "Hoy les quiero platicar de..." | 10-40 |

Suman +5 a +10: un numero concreto ("4 horas", "$180"), una marca reconocible
("Ender 3", "PETG"), o experiencia propia ("llevo 2 anos imprimiendo").

## 2. Coherencia suelta (0.18)

Se entiende sin haber visto el resto del video.

| Criterio | Puntaje |
|---|---|
| Arco completo: planteo, desarrollo, cierre | 85-100 |
| Idea completa con huecos que se infieren | 65-84 |
| Menciona algo dicho antes ("como les decia") | 40-64 |
| Necesita contexto previo para entenderse | 10-39 |
| Fragmento cortado a media idea | 0-9 |

Bandera roja automatica: "como ya dijimos", "volviendo a lo de antes", pronombres sin
referente ("y entonces el me dijo"), o que corte a media frase.

## 3. Emocion (0.15)

| Senal | Rango |
|---|---|
| Opinion fuerte, con conviccion | 80-100 |
| Revelacion inesperada | 75-95 |
| Humor genuino / risa | 70-90 |
| Fracaso propio contado con honestidad | 70-90 |
| Entusiasmo explicando algo que le apasiona | 60-80 |
| Observacion tranquila pero interesante | 40-60 |
| Recitado plano | 10-30 |

## 4. Densidad de valor (0.12)

Cuanto se lleva el que ve, por segundo.

| Contenido | Rango |
|---|---|
| Paso a paso / metodo exacto | 80-100 |
| Marco mental con ejemplo | 75-95 |
| Datos duros, mediciones, costos reales | 70-90 |
| Idea contraintuitiva bien explicada | 65-85 |
| Consejo general con algo de concreto | 40-60 |
| Frases huecas ("hay que ser constante") | 10-30 |

Penaliza si mas del 30% del corte es relleno o tangente.

## 5. Cierre (0.07)

| Final | Rango |
|---|---|
| Remate o revelacion satisfactoria | 85-100 |
| Llamado a la accion concreto | 75-90 |
| Idea completa, punto natural para parar | 65-80 |
| Se diluye en el siguiente tema (se puede cortar limpio) | 40-60 |
| Corta a media idea | 10-30 |

## 6. Intencion de compra (0.20) — propia de tienda

Que tanto empuja a alguien a querer el producto.

| Senal | Rango |
|---|---|
| Muestra el resultado en uso real (el gato usandolo, la pieza montada) | 85-100 |
| Resuelve una objecion concreta (precio, resistencia, tamano, envio) | 80-95 |
| Comparacion visible contra la alternativa que ya usa el cliente | 75-90 |
| Detras de camara del proceso (impresion, armado, empaque) | 65-85 |
| Explica una caracteristica sin mostrarla | 40-60 |
| No se relaciona con ningun producto vendible | 0-20 |

Regla de Adrian Saenz que aplica aqui: **muestra el resultado, no el producto**. Un
corte donde se ve al gato usando la pieza vale mas que uno donde se explica la pieza.

## Como elegir los candidatos

1. Apunta a **8-12 candidatos** en un video de 30-60 min.
2. Duracion: **15-55 s**; el punto dulce esta en 21-34 s para TikTok.
3. Umbral: por debajo de **60** no lo propongas (bajalo a 50 si el video da poco).
4. Variedad: no propongas 5 cortes del mismo subtema.
5. Separacion: idealmente los cortes van a mas de 2 min de distancia entre si.
6. Fronteras: siempre alineados a frase, nunca a media palabra (de eso se encarga `snap.py`).

## Como escribir el gancho de cada corte

- **Linea 1**: 4-8 palabras, la afirmacion que frena el scroll (blanca, grande).
- **Linea 2**: 3-6 palabras, el contexto (naranja, mas chica).
- Las dos lineas **no repiten** las primeras palabras habladas: las complementan.
- Nada de social proof inventado.
