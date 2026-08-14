"""Motor de subtitulos animados: genera un archivo .ass (libass) sin Node ni Remotion.

Sustituye al render de Remotion de claude-shorts: los mismos tres estilos
(bold / bounce / clean) resueltos con overrides de ASS que FFmpeg quema con
el filtro `subtitles`. Palabra activa resaltada, pop de entrada, zonas seguras
de cada plataforma y capas de gancho (hook) y CTA de marca.

Uso tipico:
    python make_ass.py --captions transcript.json --estilo bold --out subs.ass \
        --desde 262.0 --hasta 301.0 --gancho "Nadie te dice esto|del PETG" \
        --cta "michilab.store" --duracion 39.0

Modo tarjetas (para slideshows de fotos, sin transcripcion):
    python make_ass.py --tarjetas tarjetas.json --out subs.ass --duracion 15
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from common import CREMA, NARANJA, OLIVO, load_json

# --------------------------------------------------------------------------- #
# Estilos (equivalentes a los presets de Remotion de claude-shorts)
# --------------------------------------------------------------------------- #
ESTILOS = {
    # Ojo: el nombre de familia real de Montserrat-Bold.ttf es "Montserrat ExtraBold"
    # (subfamilia Regular). libass empareja por familia, no por nombre de archivo.
    "bold": {
        "fuente": "Montserrat ExtraBold", "tam": 72, "negrita": False, "mayusculas": True,
        "color": "#FFFFFF", "activo": "#FFD700", "borde": 6, "sombra": 0,
        "palabras": 3, "chars_linea": 18, "ventana_ms": 800,
        "anim": "pop", "descripcion": "ALL CAPS, palabra activa amarilla. Educativo, negocio, motivacion.",
    },
    "bounce": {
        "fuente": "Bangers", "tam": 88, "negrita": False, "mayusculas": True,
        "color": "#FFFFFF", "activo": None, "borde": 8, "sombra": 0,
        "palabras": 2, "chars_linea": 14, "ventana_ms": 600,
        "anim": "bounce", "descripcion": "Colores rotando y rebote. Entretenimiento, reacciones, energia.",
        "rotacion": ["#00FFFF", "#FF00FF", "#00FF00", "#FFFF00", "#FF6600", "#FF0066"],
    },
    "clean": {
        "fuente": "Inter", "tam": 56, "negrita": True, "mayusculas": False,
        "color": "#FFFFFF", "activo": "#E0E0E0", "borde": 2, "sombra": 3,
        "palabras": 5, "chars_linea": 26, "ventana_ms": 1500,
        "anim": "fade", "descripcion": "Minimalista, blanco con sombra suave. Entrevistas, profesional.",
    },
    # Estilo propio de la combinacion: identidad Michilab
    "michilab": {
        "fuente": "Montserrat ExtraBold", "tam": 66, "negrita": False, "mayusculas": True,
        "color": CREMA, "activo": NARANJA, "borde": 6, "sombra": 0,
        "palabras": 3, "chars_linea": 18, "ventana_ms": 800,
        "anim": "pop", "descripcion": "Crema con palabra activa naranja sobre contorno olivo. Marca Michilab.",
        "color_borde": OLIVO,
    },
}

# Margen inferior de los subtitulos por plataforma (px desde el borde inferior
# en un lienzo de 1920). Ver references/plataformas.md.
MARGEN_INFERIOR = {"tiktok": 380, "instagram": 400, "youtube": 420, "todas": 450}


def hex_ass(color: str, alpha: int = 0) -> str:
    """'#RRGGBB' -> '&HAABBGGRR&' (ASS invierte el orden y antepone alfa)."""
    c = color.lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    r, g, b = c[0:2], c[2:4], c[4:6]
    return f"&H{alpha:02X}{b}{g}{r}&".upper()


def esc(texto: str) -> str:
    """Neutraliza los caracteres que ASS interpreta como codigo."""
    return (texto.replace("\\", "/").replace("{", "(").replace("}", ")")
            .replace("\r", " ").replace("\n", " ").strip())


def ts(segundos: float) -> str:
    """Timestamp ASS: h:mm:ss.cc"""
    segundos = max(0.0, float(segundos))
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = segundos % 60
    return f"{h:d}:{m:02d}:{s:05.2f}"


# --------------------------------------------------------------------------- #
# Agrupado de palabras en "paginas"
# --------------------------------------------------------------------------- #
def cargar_palabras(transcripcion: dict, desde: float, hasta: float) -> list:
    """Extrae palabras con tiempo, recortadas al rango y con el origen en 0."""
    palabras = []
    for seg in transcripcion.get("segments", []):
        for w in seg.get("words", []) or []:
            ini, fin = float(w.get("start", 0)), float(w.get("end", 0))
            txt = (w.get("word") or w.get("text") or "").strip()
            if txt and fin > desde and ini < hasta:
                palabras.append({"t": txt,
                                 "ini": max(0.0, ini - desde),
                                 "fin": max(0.0, min(fin, hasta) - desde)})
    if palabras:
        return palabras
    # Sin timestamps por palabra: repartimos cada caption entre sus palabras.
    for c in transcripcion.get("captions", []):
        ini, fin = c["startMs"] / 1000.0, c["endMs"] / 1000.0
        if fin <= desde or ini >= hasta:
            continue
        trozos = (c.get("text") or "").split()
        if not trozos:
            continue
        paso = (fin - ini) / len(trozos)
        for i, t in enumerate(trozos):
            palabras.append({"t": t,
                             "ini": max(0.0, ini + i * paso - desde),
                             "fin": max(0.0, ini + (i + 1) * paso - desde)})
    return palabras


def paginar(palabras: list, max_palabras: int, ventana_ms: int) -> list:
    """Agrupa palabras en paginas: corta por numero, pausa larga o fin de frase."""
    paginas, actual = [], []
    for w in palabras:
        if actual:
            hueco = (w["ini"] - actual[-1]["fin"]) * 1000
            fin_frase = bool(re.search(r"[.!?]$", actual[-1]["t"]))
            if len(actual) >= max_palabras or hueco > ventana_ms or fin_frase:
                paginas.append(actual)
                actual = []
        actual.append(w)
    if actual:
        paginas.append(actual)
    return paginas


def repartir_lineas(pagina: list, chars_linea: int) -> list:
    """Distribuye las palabras de una pagina en lineas (indices)."""
    lineas, actual, largo = [], [], 0
    for i, w in enumerate(pagina):
        n = len(w["t"])
        if actual and largo + n + 1 > chars_linea:
            lineas.append(actual)
            actual, largo = [], 0
        actual.append(i)
        largo += n + 1
    if actual:
        lineas.append(actual)
    return lineas


# --------------------------------------------------------------------------- #
# Construccion del archivo ASS
# --------------------------------------------------------------------------- #
def cabecera(est: dict, margen_v: int, ancho: int, alto: int) -> list:
    borde_col = hex_ass(est.get("color_borde", "#000000"))
    negrita = -1 if est["negrita"] else 0
    return [
        "[Script Info]",
        "; Generado por videos-tienda (motor local FFmpeg + libass)",
        "ScriptType: v4.00+",
        f"PlayResX: {ancho}",
        f"PlayResY: {alto}",
        "WrapStyle: 2",
        "ScaledBorderAndShadow: yes",
        "YCbCr Matrix: TV.709",
        "",
        "[V4+ Styles]",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, "
        "BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, "
        "BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
        # Subtitulos: abajo centrado (alineacion 2)
        f"Style: cap,{est['fuente']},{est['tam']},{hex_ass(est['color'])},{hex_ass(est['color'])},"
        f"{borde_col},&H80000000,{negrita},0,0,0,100,100,0,0,1,{est['borde']},{est['sombra']},"
        f"2,60,60,{margen_v},1",
        # Gancho, linea 1: blanca con contorno grueso y sombra. Legible sobre
        # cualquier fondo, que es lo que pasa en video real (madera, pelo negro, sol).
        f"Style: hook,{est['fuente']},78,{hex_ass('#FFFFFF')},{hex_ass('#FFFFFF')},"
        f"{hex_ass('#000000')},&H60000000,-1,0,0,0,100,100,0,0,1,8,3,8,60,60,210,1",
        # Gancho, linea 2: caja solida olivo con texto crema (BorderStyle 3). El
        # texto naranja suelto se perdia sobre la madera; la caja no falla nunca.
        f"Style: hook2,{est['fuente']},50,{hex_ass(CREMA)},{hex_ass(CREMA)},"
        f"{hex_ass(OLIVO)},{hex_ass(OLIVO)},-1,0,0,0,100,100,0,0,3,13,0,8,60,60,210,1",
        # CTA de marca: arriba, caja solida olivo (BorderStyle 3)
        f"Style: cta,{est['fuente']},58,{hex_ass(CREMA)},{hex_ass(CREMA)},"
        f"{hex_ass(OLIVO)},{hex_ass(OLIVO)},-1,0,0,0,100,100,0,0,3,14,0,8,60,60,240,1",
        # Tarjetas de slideshow
        f"Style: card,{est['fuente']},68,{hex_ass('#FFFFFF')},{hex_ass('#FFFFFF')},"
        f"{hex_ass('#000000')},&H80000000,-1,0,0,0,100,100,0,0,1,6,0,2,70,70,{margen_v},1",
        f"Style: cardtop,{est['fuente']},68,{hex_ass('#FFFFFF')},{hex_ass('#FFFFFF')},"
        f"{hex_ass('#000000')},&H80000000,-1,0,0,0,100,100,0,0,1,6,0,8,70,70,240,1",
        "",
        "[Events]",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text",
    ]


def dialog(ini: float, fin: float, estilo: str, texto: str, capa: int = 0) -> str:
    return f"Dialogue: {capa},{ts(ini)},{ts(fin)},{estilo},,0,0,0,,{texto}"


def eventos_subtitulos(palabras: list, est: dict) -> list:
    """Un evento por palabra: la pagina completa con la palabra activa resaltada."""
    eventos = []
    paginas = paginar(palabras, est["palabras"], est["ventana_ms"])
    rotacion = est.get("rotacion")

    for idx_pag, pagina in enumerate(paginas):
        # Tope duro: la pagina desaparece antes de que arranque la siguiente.
        # Sin esto, dos paginas se dibujan encimadas cuando no hay pausa entre ellas.
        siguiente = paginas[idx_pag + 1][0]["ini"] if idx_pag + 1 < len(paginas) else float("inf")
        lineas = repartir_lineas(pagina, est["chars_linea"])
        base = est["color"]
        activo = est.get("activo") or (rotacion[idx_pag % len(rotacion)] if rotacion else "#FFD700")
        c_base, c_activo = hex_ass(base), hex_ass(activo)

        for i, palabra in enumerate(pagina):
            partes = []
            for linea in lineas:
                trozo = []
                for j in linea:
                    t = pagina[j]["t"]
                    t = t.upper() if est["mayusculas"] else t
                    t = esc(t)
                    if j == i:
                        if est["anim"] == "bounce":
                            trozo.append(f"{{\\c{c_activo}\\fscx116\\fscy116}}{t}{{\\c{c_base}\\fscx100\\fscy100}}")
                        else:
                            trozo.append(f"{{\\c{c_activo}}}{t}{{\\c{c_base}}}")
                    else:
                        trozo.append(t)
                partes.append(" ".join(trozo))
            texto = "\\N".join(partes)

            # La animacion de entrada solo corre en la primera palabra de la pagina;
            # si no, la pagina entera saltaria en cada palabra.
            prefijo = ""
            if i == 0:
                if est["anim"] == "pop":
                    prefijo = "{\\fscx86\\fscy86\\t(0,90,\\fscx104\\fscy104)\\t(90,170,\\fscx100\\fscy100)}"
                elif est["anim"] == "bounce":
                    prefijo = "{\\fscx70\\fscy70\\t(0,110,\\fscx120\\fscy120)\\t(110,230,\\fscx100\\fscy100)}"
                elif est["anim"] == "fade":
                    prefijo = "{\\fad(160,0)}"

            fin = pagina[i + 1]["ini"] if i + 1 < len(pagina) else palabra["fin"] + 0.12
            fin = min(fin, siguiente - 0.02)
            fin = max(fin, palabra["ini"] + 0.05)
            eventos.append(dialog(palabra["ini"], fin, "cap", prefijo + texto))
    return eventos


def eventos_gancho(gancho: str, duracion: float) -> list:
    """Gancho de los primeros segundos: linea 1 blanca grande, linea 2 naranja."""
    if not gancho:
        return []
    l1, _, l2 = gancho.partition("|")
    fin = min(3.5, max(1.5, duracion * 0.35))
    ev = [dialog(0.15, fin, "hook", "{\\fad(200,250)\\fscx90\\fscy90\\t(0,140,\\fscx100\\fscy100)}" + esc(l1), capa=2)]
    if l2.strip():
        ev.append(dialog(0.35, fin, "hook2", "{\\fad(260,250)\\pos(540,335)}" + esc(l2.strip()), capa=2))
    return ev


def eventos_cta(cta: str, duracion: float, segundos: float = 2.6) -> list:
    if not cta:
        return []
    ini = max(0.0, duracion - segundos)
    return [dialog(ini, duracion, "cta", "{\\fad(250,0)}" + esc(cta), capa=3)]


def eventos_tarjetas(tarjetas: list) -> list:
    ev = []
    for t in tarjetas:
        estilo = "cardtop" if t.get("pos", "abajo") == "arriba" else "card"
        texto = esc(t.get("text") or t.get("texto") or "")
        if not texto:
            continue
        texto = texto.replace(" // ", "\\N")
        ev.append(dialog(float(t["start"]), float(t["end"]), estilo,
                         "{\\fad(220,220)\\fscx92\\fscy92\\t(0,180,\\fscx100\\fscy100)}" + texto, capa=1))
    return ev


def main():
    ap = argparse.ArgumentParser(description="Genera subtitulos animados .ass")
    ap.add_argument("--captions", help="transcript.json con palabras cronometradas")
    ap.add_argument("--tarjetas", help="JSON con tarjetas de texto [{text,start,end,pos}]")
    ap.add_argument("--estilo", default="michilab", choices=list(ESTILOS))
    ap.add_argument("--out", required=True)
    ap.add_argument("--desde", type=float, default=0.0, help="inicio del recorte en el video original")
    ap.add_argument("--hasta", type=float, default=1e9, help="fin del recorte en el video original")
    ap.add_argument("--duracion", type=float, default=0.0, help="duracion del clip resultante (para gancho y CTA)")
    ap.add_argument("--gancho", default="", help='texto del gancho, "linea 1|linea 2"')
    ap.add_argument("--cta", default="", help="texto de cierre de marca")
    ap.add_argument("--plataforma", default="todas", choices=list(MARGEN_INFERIOR))
    ap.add_argument("--margen", type=int, help="margen inferior manual en px")
    ap.add_argument("--ancho", type=int, default=1080)
    ap.add_argument("--alto", type=int, default=1920)
    args = ap.parse_args()

    est = ESTILOS[args.estilo]
    margen = args.margen or MARGEN_INFERIOR[args.plataforma]
    lineas = cabecera(est, margen, args.ancho, args.alto)

    duracion = args.duracion or max(0.0, min(args.hasta, 1e6) - args.desde)

    if args.captions:
        palabras = cargar_palabras(load_json(args.captions), args.desde, args.hasta)
        lineas += eventos_subtitulos(palabras, est)
    if args.tarjetas:
        lineas += eventos_tarjetas(load_json(args.tarjetas))
    lineas += eventos_gancho(args.gancho, duracion)
    lineas += eventos_cta(args.cta, duracion)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n".join(lineas) + "\n", encoding="utf-8")
    n = sum(1 for l in lineas if l.startswith("Dialogue:"))
    print(f"subtitulos -> {args.out} ({n} eventos, estilo {args.estilo}, margen {margen}px)")


if __name__ == "__main__":
    main()
