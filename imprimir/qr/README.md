# Hojas de QR para imprimir

Los QR se dibujan como **vectores**, no son PNG escalados: el tamano fisico es
exacto y los bordes salen nitidos a cualquier resolucion de impresora.

Todas las hojas usan bloques de **44,0 mm** (codigo mas margen blanco), pensados
para un area de 45 mm con 1 mm de tolerancia. Salvo las marcadas como `-codigo`,
donde los 44 mm son solo el cuadro negro y el margen blanco queda por fuera.

## unit.link/richieland

| Archivo | Bloque | Codigo | Modulo | Por hoja A4 |
|---|---|---|---|---|
| `QR-richieland-44mm-*` | 44,0 mm | 38,7 mm | 1,33 mm | 24 |
| `QR-richieland-codigo-44mm-*` | 50,1 mm | 44,0 mm | 1,52 mm | 15 |

## Instagram (@inquebrantablemx_)

| Archivo | URL | Estilo | Modulos | Modulo | Por hoja A4 |
|---|---|---|---|---|---|
| `QR-instagram-44mm-*` | corta | cuadrado | 37x37 | 1,07 mm | 24 |
| `QR-instagram-logo-44mm-*` | corta | puntos + logo | 37x37 | 1,07 mm | 24 |
| `QR-instagram-original-44mm-*` | con token | cuadrado | 49x49 | 0,83 mm | 24 |

**URL corta** es `https://www.instagram.com/inquebrantablemx_`, sin el parametro
`stkn=` que Instagram agrega al QR que genera la app. Ese token puede caducar,
y en papel impreso eso no se puede corregir despues. La URL corta ademas ocupa
37x37 modulos en vez de 49x49, asi que cada modulo es un 29 % mas grande y se
lee mejor a este tamano.

`-original` conserva la URL completa con el token, por si hace falta el
comportamiento exacto del QR de la app.

### Sobre la variante con logo

Reproduce el aspecto de Instagram (puntos redondos, finders redondeados y el
glifo de la camara al centro). Se verifico que los datos son identicos a los del
QR plano: 0 diferencias en los 1141 modulos comparables.

Lo que **no** se pudo verificar automaticamente es la lectura: el detector de
OpenCV no lee QR de puntos, y tampoco lee el QR original que genera Instagram.
No es senal de que este mal, pero **conviene escanear una prueba con el telefono
antes de mandar a imprimir la hoja completa.** Si hay dudas, usar la variante
plana, que si esta verificada.

## Al imprimir

Escala **100 %** / "Tamano real". Si sale "Ajustar a la pagina" o "Reducir al
area de impresion", el tamano fisico cambia y deja de medir 44 mm.

Las lineas grises finas son guias de corte.

## Regenerar

    pip install reportlab qrcode
    python3 scripts/qr_hoja.py --texto "https://ejemplo.com"
    python3 scripts/qr_hoja.py --texto "..." --estilo puntos --logo instagram
    python3 scripts/qr_hoja.py --mm 30 --modo codigo --texto "..."
    python3 scripts/qr_hoja.py --matriz imprimir/qr/qr-richieland.matrix.txt

Cada ejecucion produce la version A4 y la Carta. Avisa si el modulo baja de
0,6 mm, que es donde la impresion empieza a fallar.
