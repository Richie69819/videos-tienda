# Hojas de QR para imprimir

QR de `https://unit.link/richieland`, dibujado como vectores desde su matriz de
modulos (`qr-richieland.matrix.txt`, 29x29, version 3). No es un PNG escalado:
sale nitido a cualquier resolucion de impresora.

## Archivos

| Archivo | Bloque total | Cuadro negro | Por hoja |
|---|---|---|---|
| `QR-richieland-44mm-A4.pdf` | 44,0 mm | 38,7 mm | 24 |
| `QR-richieland-44mm-Carta.pdf` | 44,0 mm | 38,7 mm | 20 |
| `QR-richieland-codigo-44mm-A4.pdf` | 50,1 mm | 44,0 mm | 15 |
| `QR-richieland-codigo-44mm-Carta.pdf` | 50,1 mm | 44,0 mm | 20 |

Los dos primeros son la opcion segura: **todo** (codigo mas margen blanco) cabe
dentro de 44 mm, con 1 mm de tolerancia contra un area de 45 mm.

Los dos ultimos hacen el cuadro negro de 44 mm exactos y dejan el margen blanco
por fuera (bloque de 50,1 mm). Solo sirven si lo que rodea al area de 45 mm ya
es blanco.

## Al imprimir

Escala **100 %** / "Tamano real". Si sale "Ajustar a la pagina" o "Reducir al
area de impresion", el tamano fisico cambia y deja de medir 44 mm.

Las lineas grises finas son guias de corte.

## Regenerar

    pip install reportlab
    python3 scripts/qr_hoja.py                        # 44 mm de bloque total
    python3 scripts/qr_hoja.py --mm 30                # otro tamano
    python3 scripts/qr_hoja.py --modo codigo          # 44 mm = solo el negro
