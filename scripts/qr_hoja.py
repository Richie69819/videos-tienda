"""Genera hojas de QR listas para imprimir a un tamano fisico exacto.

El QR se dibuja como vectores, no se escala un PNG, asi que el tamano fisico
es exacto y los bordes salen nitidos a cualquier resolucion de impresora.

Uso:
    python3 scripts/qr_hoja.py --texto "https://ejemplo.com"
    python3 scripts/qr_hoja.py --matriz imprimir/qr/algo.matrix.txt
    python3 scripts/qr_hoja.py --texto "..." --estilo puntos --logo instagram
    python3 scripts/qr_hoja.py --mm 30 --modo codigo
"""

import argparse
from pathlib import Path

from reportlab.lib.colors import Color, black, white
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "imprimir" / "qr"

GUIA = Color(0.78, 0.78, 0.78)  # gris claro para las lineas de corte
QUIET = 2                       # modulos de zona blanca a cada lado
LOGO_MODULOS = 9                # lado del hueco del logo, en modulos


# ---------------------------------------------------------------- matriz

def matriz_desde_texto(texto, ec="H"):
    import qrcode
    from qrcode.constants import (ERROR_CORRECT_H, ERROR_CORRECT_L,
                                  ERROR_CORRECT_M, ERROR_CORRECT_Q)
    niveles = {"L": ERROR_CORRECT_L, "M": ERROR_CORRECT_M,
               "Q": ERROR_CORRECT_Q, "H": ERROR_CORRECT_H}
    q = qrcode.QRCode(error_correction=niveles[ec], border=0)
    q.add_data(texto)
    q.make(fit=True)
    return ["".join("#" if v else "." for v in fila) for fila in q.get_matrix()]


def matriz_desde_archivo(ruta):
    filas = [l.strip() for l in ruta.read_text().splitlines() if l.strip()]
    if any(len(f) != len(filas) for f in filas):
        raise ValueError(f"{ruta}: la matriz no es cuadrada")
    return filas


def hueco_logo(n):
    """Rango [ini, fin) de filas/columnas que ocupa el logo, centrado."""
    ini = (n - LOGO_MODULOS) // 2
    return ini, ini + LOGO_MODULOS


# ---------------------------------------------------------------- dibujo

def _finder_puntos(c, x, y, m):
    """Finder al estilo Instagram: anillo redondeado mas centro redondeado."""
    c.setStrokeColor(black)
    c.setFillColor(black)
    c.setLineWidth(m)
    c.roundRect(x + m / 2, y + m / 2, 6 * m, 6 * m, 2 * m, stroke=1, fill=0)
    c.roundRect(x + 2 * m, y + 2 * m, 3 * m, 3 * m, m, stroke=0, fill=1)


def _glifo_instagram(c, x, y, lado):
    """Camara de Instagram dentro del cuadrado (x, y, lado)."""
    c.setFillColor(white)
    c.rect(x, y, lado, lado, stroke=0, fill=1)          # limpia el hueco
    g = lado * 0.74                                      # glifo dentro del hueco
    gx, gy = x + (lado - g) / 2, y + (lado - g) / 2
    c.setStrokeColor(black)
    c.setFillColor(black)
    c.setLineWidth(g * 0.115)
    c.roundRect(gx + g * 0.06, gy + g * 0.06, g * 0.88, g * 0.88,
                g * 0.27, stroke=1, fill=0)
    c.circle(gx + g / 2, gy + g / 2, g * 0.235, stroke=1, fill=0)
    c.circle(gx + g * 0.75, gy + g * 0.75, g * 0.062, stroke=0, fill=1)


def dibujar_qr(c, x, y, lado_mm, filas, estilo="cuadrado", logo=None):
    """Dibuja el simbolo con su esquina inferior izquierda en (x, y)."""
    n = len(filas)
    m = lado_mm * mm / n
    li, lf = hueco_logo(n) if logo else (0, 0)
    finders = {(0, 0), (0, n - 7), (n - 7, 0)}

    c.setFillColor(black)
    if estilo == "cuadrado":
        for r in range(n):
            col = 0
            while col < n:
                if filas[r][col] == "#" and not (logo and li <= r < lf and li <= col < lf):
                    ini = col
                    while (col < n and filas[r][col] == "#"
                           and not (logo and li <= r < lf and li <= col < lf)):
                        col += 1
                    # el +0.02 evita lineas blancas finas entre modulos en algunos RIP
                    c.rect(x + ini * m, y + (n - 1 - r) * m,
                           (col - ini) * m + 0.02, m + 0.02, stroke=0, fill=1)
                else:
                    col += 1
    else:  # puntos
        for r in range(n):
            for col in range(n):
                if filas[r][col] != "#":
                    continue
                if logo and li <= r < lf and li <= col < lf:
                    continue
                # los finders se dibujan aparte, con su forma propia
                if any(fr <= r < fr + 7 and fc <= col < fc + 7 for fr, fc in finders):
                    continue
                c.circle(x + (col + 0.5) * m, y + (n - 1 - r + 0.5) * m,
                         m * 0.46, stroke=0, fill=1)
        for fr, fc in finders:
            _finder_puntos(c, x + fc * m, y + (n - 7 - fr) * m, m)

    if logo:
        _glifo_instagram(c, x + li * m, y + (n - lf) * m, LOGO_MODULOS * m)


# ---------------------------------------------------------------- hoja

def hoja(c, pagina, lado_mm, filas, titulo, estilo, logo):
    """Rellena la pagina con todos los bloques que quepan."""
    ancho, alto = pagina
    n = len(filas)
    blanco_mm = QUIET * (lado_mm / n)
    bloque_mm = lado_mm + 2 * blanco_mm

    cabecera, margen = 9 * mm, 5 * mm
    cols = int((ancho - 2 * margen) // (bloque_mm * mm))
    rens = int((alto - cabecera - 2 * margen) // (bloque_mm * mm))
    if cols < 1 or rens < 1:
        raise ValueError("el bloque no cabe en la pagina")

    ox = (ancho - cols * bloque_mm * mm) / 2
    oy = (alto - cabecera - rens * bloque_mm * mm) / 2

    c.setFillColor(Color(0.45, 0.45, 0.45))
    c.setFont("Helvetica", 7)
    c.drawCentredString(ancho / 2, alto - cabecera + 2.5 * mm, titulo)

    c.setStrokeColor(GUIA)
    c.setLineWidth(0.25)
    for i in range(cols + 1):
        gx = ox + i * bloque_mm * mm
        c.line(gx, oy, gx, oy + rens * bloque_mm * mm)
    for j in range(rens + 1):
        gy = oy + j * bloque_mm * mm
        c.line(ox, gy, ox + cols * bloque_mm * mm, gy)

    for j in range(rens):
        for i in range(cols):
            dibujar_qr(c,
                       ox + i * bloque_mm * mm + blanco_mm * mm,
                       oy + j * bloque_mm * mm + blanco_mm * mm,
                       lado_mm, filas, estilo, logo)
    return cols, rens


def construir(pagina, nombre_pagina, destino, objetivo_mm, filas, modo,
              etiqueta, estilo="cuadrado", logo=None):
    n = len(filas)
    # "bloque": los objetivo_mm incluyen la zona blanca. "codigo": solo el negro.
    lado_mm = objetivo_mm * n / (n + 2 * QUIET) if modo == "bloque" else objetivo_mm
    blanco_mm = (lado_mm / n) * QUIET
    bloque_mm = lado_mm + 2 * blanco_mm
    modulo_mm = lado_mm / n

    titulo = (f"bloque total {bloque_mm:.1f} mm  (codigo {lado_mm:.1f} mm "
              f"+ margen blanco {blanco_mm:.1f} mm)   |   modulo {modulo_mm:.2f} mm"
              f"   |   {etiqueta}")

    c = canvas.Canvas(str(destino), pagesize=pagina)
    c.setTitle(destino.stem)
    cols, rens = hoja(c, pagina, lado_mm, filas, titulo, estilo, logo)
    c.showPage()
    c.save()

    print(f"{destino.name}: {nombre_pagina}, {cols}x{rens} = {cols * rens} QR/hoja | "
          f"bloque {bloque_mm:.1f} mm | codigo {lado_mm:.1f} mm | "
          f"{n}x{n} modulos | modulo {modulo_mm:.3f} mm")
    if modulo_mm < 0.6:
        print(f"  AVISO: modulo de {modulo_mm:.2f} mm, por debajo de 0,6 mm. "
              f"Riesgo de que no lea segun la impresora.")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    fuente = p.add_mutually_exclusive_group(required=True)
    fuente.add_argument("--texto", help="contenido a codificar (genera el QR)")
    fuente.add_argument("--matriz", type=Path, help="matriz ya extraida (# y .)")
    p.add_argument("--mm", type=float, default=44.0, help="tamano objetivo en mm")
    p.add_argument("--modo", choices=("bloque", "codigo"), default="bloque",
                   help="bloque: --mm incluye el margen blanco (por defecto). "
                        "codigo: --mm es solo el cuadro negro")
    p.add_argument("--ec", choices=("L", "M", "Q", "H"), default="H",
                   help="nivel de correccion de errores (por defecto H, el maximo)")
    p.add_argument("--estilo", choices=("cuadrado", "puntos"), default="cuadrado")
    p.add_argument("--logo", choices=("instagram",), default=None)
    p.add_argument("--etiqueta", default=None, help="texto de referencia en la cabecera")
    p.add_argument("--nombre", default="QR", help="prefijo del archivo")
    args = p.parse_args()

    filas = (matriz_desde_texto(args.texto, args.ec) if args.texto
             else matriz_desde_archivo(args.matriz))
    etiqueta = args.etiqueta or (args.texto if args.texto else args.matriz.stem)
    if len(etiqueta) > 70:
        etiqueta = etiqueta[:67] + "..."

    SALIDA.mkdir(parents=True, exist_ok=True)
    base = f"{args.nombre}-{args.mm:g}mm"
    for pagina, nombre, sufijo in ((A4, "A4", "A4"), (LETTER, "Carta", "Carta")):
        construir(pagina, nombre, SALIDA / f"{base}-{sufijo}.pdf", args.mm,
                  filas, args.modo, etiqueta, args.estilo, args.logo)


if __name__ == "__main__":
    main()
