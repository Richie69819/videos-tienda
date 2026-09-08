"""Genera hojas de QR listas para imprimir a un tamano fisico exacto.

El QR se dibuja como vectores a partir de su matriz de modulos, no se escala
un PNG, asi que sale nitido a cualquier tamano y a cualquier resolucion de
impresora.

Uso:
    python3 scripts/qr_hoja.py                      # 44 mm, A4 y Carta
    python3 scripts/qr_hoja.py --mm 30              # otro tamano
    python3 scripts/qr_hoja.py --modo codigo        # 44 mm = solo el negro
"""

import argparse
from pathlib import Path

from reportlab.lib.colors import Color, black
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "imprimir" / "qr"

GUIA = Color(0.78, 0.78, 0.78)  # gris claro para las lineas de corte
QUIET = 2  # modulos de zona blanca a cada lado


def leer_matriz(ruta):
    filas = [l.strip() for l in ruta.read_text().splitlines() if l.strip()]
    if any(len(f) != len(filas) for f in filas):
        raise ValueError(f"{ruta}: la matriz no es cuadrada")
    return filas


def dibujar_qr(c, x, y, lado_mm, filas):
    """Dibuja el simbolo con su esquina inferior izquierda en (x, y)."""
    n = len(filas)
    m = lado_mm * mm / n
    c.setFillColor(black)
    for r in range(n):
        col = 0
        while col < n:
            if filas[r][col] == "#":
                ini = col
                while col < n and filas[r][col] == "#":
                    col += 1
                # el +0.02 evita lineas blancas finas entre modulos en algunos RIP
                c.rect(x + ini * m, y + (n - 1 - r) * m,
                       (col - ini) * m + 0.02, m + 0.02, stroke=0, fill=1)
            else:
                col += 1


def hoja(c, pagina, lado_mm, filas, titulo):
    """Rellena la pagina con todos los bloques que quepan. Devuelve (cols, rens)."""
    ancho, alto = pagina
    n = len(filas)
    modulo_mm = lado_mm / n
    blanco_mm = QUIET * modulo_mm
    bloque_mm = lado_mm + 2 * blanco_mm

    cabecera = 9 * mm
    margen = 5 * mm

    cols = int((ancho - 2 * margen) // (bloque_mm * mm))
    rens = int((alto - cabecera - 2 * margen) // (bloque_mm * mm))
    if cols < 1 or rens < 1:
        raise ValueError("el bloque no cabe en la pagina")

    rejilla_w = cols * bloque_mm * mm
    rejilla_h = rens * bloque_mm * mm
    ox = (ancho - rejilla_w) / 2
    oy = (alto - cabecera - rejilla_h) / 2

    c.setFillColor(Color(0.45, 0.45, 0.45))
    c.setFont("Helvetica", 7)
    c.drawCentredString(ancho / 2, alto - cabecera + 2.5 * mm, titulo)

    c.setStrokeColor(GUIA)
    c.setLineWidth(0.25)
    for i in range(cols + 1):
        gx = ox + i * bloque_mm * mm
        c.line(gx, oy, gx, oy + rejilla_h)
    for j in range(rens + 1):
        gy = oy + j * bloque_mm * mm
        c.line(ox, gy, ox + rejilla_w, gy)

    for j in range(rens):
        for i in range(cols):
            dibujar_qr(c,
                       ox + i * bloque_mm * mm + blanco_mm * mm,
                       oy + j * bloque_mm * mm + blanco_mm * mm,
                       lado_mm, filas)
    return cols, rens


def construir(pagina, nombre_pagina, destino, objetivo_mm, filas, modo, etiqueta):
    n = len(filas)
    # "bloque": los objetivo_mm incluyen la zona blanca. "codigo": solo el negro.
    if modo == "bloque":
        lado_mm = objetivo_mm * n / (n + 2 * QUIET)
    else:
        lado_mm = objetivo_mm
    blanco_mm = (lado_mm / n) * QUIET
    bloque_mm = lado_mm + 2 * blanco_mm

    titulo = (f"bloque total {bloque_mm:.1f} mm  (codigo {lado_mm:.1f} mm "
              f"+ margen blanco {blanco_mm:.1f} mm)   |   {etiqueta}")

    c = canvas.Canvas(str(destino), pagesize=pagina)
    c.setTitle(destino.stem)
    cols, rens = hoja(c, pagina, lado_mm, filas, titulo)
    c.showPage()
    c.save()

    print(f"{destino.name}: {nombre_pagina}, {cols}x{rens} = {cols * rens} QR/hoja | "
          f"bloque {bloque_mm:.1f} mm | codigo {lado_mm:.1f} mm | modulo {lado_mm / n:.3f} mm")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--matriz", type=Path,
                   default=SALIDA / "qr-richieland.matrix.txt",
                   help="archivo con la matriz de modulos (# y .)")
    p.add_argument("--mm", type=float, default=44.0, help="tamano objetivo en mm")
    p.add_argument("--modo", choices=("bloque", "codigo"), default="bloque",
                   help="bloque: --mm incluye el margen blanco (por defecto). "
                        "codigo: --mm es solo el cuadro negro")
    p.add_argument("--etiqueta", default="https://unit.link/richieland",
                   help="texto de referencia en la cabecera")
    p.add_argument("--nombre", default="QR-richieland", help="prefijo del archivo")
    args = p.parse_args()

    filas = leer_matriz(args.matriz)
    SALIDA.mkdir(parents=True, exist_ok=True)

    base = f"{args.nombre}-{args.mm:g}mm"
    for pagina, nombre, sufijo in ((A4, "A4", "A4"), (LETTER, "Carta", "Carta")):
        construir(pagina, nombre, SALIDA / f"{base}-{sufijo}.pdf",
                  args.mm, filas, args.modo, args.etiqueta)


if __name__ == "__main__":
    main()
