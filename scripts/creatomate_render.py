"""Motor en la nube (opcional): Creatomate por API REST, sin Node ni SDK.

Cuando conviene sobre el motor local:
  - Las fotos ya viven en una URL publica (CDN de Shopify) y no quieres bajarlas.
  - Quieres render desde el celular/iPad, sin la PC encendida.
  - Necesitas una plantilla con animaciones que libass no puede hacer.

Cuando NO conviene: es de paga por minuto renderizado y sube tu material a un
tercero. Para el trabajo diario de la tienda, el motor local es gratis.

Requiere la variable de entorno CREATOMATE_API_KEY.

Uso:
    python creatomate_render.py --fuente escena.json --esperar --descargar reel.mp4
    python creatomate_render.py --plantilla ID --mods '{"Title":"Anillo dona"}' --esperar
    python creatomate_render.py --fotos-url "https://cdn/1.jpg,https://cdn/2.jpg" \
        --textos "Anillo dona|Envio gratis" --esperar --descargar reel.mp4
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

API = "https://api.creatomate.com/v1/renders"


def _pedir(url: str, metodo: str = "GET", cuerpo: dict | None = None) -> dict | list:
    clave = os.environ.get("CREATOMATE_API_KEY")
    if not clave:
        print("ERROR: falta la variable de entorno CREATOMATE_API_KEY.\n"
              "       Consigue la llave en creatomate.com > Project Settings > API key.\n"
              "       El motor local (slideshow.py / render_clip.py) no necesita ninguna llave.",
              file=sys.stderr)
        sys.exit(2)
    datos = json.dumps(cuerpo).encode("utf-8") if cuerpo is not None else None
    req = urllib.request.Request(url, data=datos, method=metodo, headers={
        "Authorization": f"Bearer {clave}",
        "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detalle = e.read().decode("utf-8", "replace")[:500]
        print(f"ERROR HTTP {e.code} de Creatomate: {detalle}", file=sys.stderr)
        sys.exit(1)


def escena_fotos(urls: list, textos: list, segundos: float, cta: str) -> dict:
    """RenderScript 9:16 con Ken Burns, cruces y textos: el equivalente en nube
    de lo que hace slideshow.py en local."""
    elementos = []
    animaciones = ["pan_center", "pan_left", "pan_right"]
    for i, u in enumerate(urls):
        elementos.append({
            "type": "image", "track": 1, "duration": segundos, "source": u,
            "animations": [{"type": animaciones[i % 3], "start_scale": "100%",
                            "end_scale": "120%", "easing": "linear"}],
            **({"transition": {"type": "fade", "duration": 0.4}} if i else {}),
        })
        if i < len(textos) and textos[i].strip():
            elementos.append({
                "type": "text", "track": 2, "time": round(i * segundos, 2),
                "duration": segundos, "text": textos[i].strip(),
                "y": "82%", "width": "88%", "x_alignment": "50%",
                "font_family": "Montserrat", "font_weight": "800",
                "font_size": "6 vmin", "fill_color": "#f5f2e9",
                "stroke_color": "#5a6640", "stroke_width": "1.2 vmin",
                "shadow_color": "rgba(0,0,0,0.45)", "shadow_blur": "12px",
            })
    if cta:
        elementos.append({
            "type": "text", "track": 3, "time": round(len(urls) * segundos - 2.5, 2),
            "duration": 2.5, "text": cta, "y": "12%", "width": "70%", "x_alignment": "50%",
            "font_family": "Montserrat", "font_weight": "800", "font_size": "5 vmin",
            "fill_color": "#f5f2e9", "background_color": "#5a6640",
            "background_x_padding": "40%", "background_y_padding": "30%",
        })
    return {"output_format": "mp4", "frame_rate": 30, "width": 1080, "height": 1920,
            "elements": elementos}


def esperar(ids: list, intervalo: float = 4.0, limite: float = 900) -> list:
    t0, resultados = time.time(), {}
    pendientes = set(ids)
    while pendientes and time.time() - t0 < limite:
        time.sleep(intervalo)
        for rid in list(pendientes):
            r = _pedir(f"{API}/{rid}")
            estado = r.get("status")
            print(f"  {rid[:8]}... {estado}")
            if estado in ("succeeded", "failed"):
                resultados[rid] = r
                pendientes.discard(rid)
    if pendientes:
        print("aviso: se agoto la espera para " + ", ".join(pendientes), file=sys.stderr)
    return list(resultados.values())


def main():
    ap = argparse.ArgumentParser(description="Render en la nube con Creatomate")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--fuente", help="archivo JSON con el RenderScript")
    g.add_argument("--plantilla", help="template_id de Creatomate")
    g.add_argument("--fotos-url", help="URLs de imagenes separadas por coma")
    ap.add_argument("--mods", help="JSON de modificaciones para la plantilla")
    ap.add_argument("--textos", default="", help="textos por foto separados por '|'")
    ap.add_argument("--segundos", type=float, default=2.6)
    ap.add_argument("--cta", default="")
    ap.add_argument("--esperar", action="store_true", help="espera a que termine el render")
    ap.add_argument("--descargar", help="guarda el resultado en esta ruta")
    args = ap.parse_args()

    if args.fuente:
        with open(args.fuente, "r", encoding="utf-8") as fh:
            cuerpo = {"source": json.load(fh)}
    elif args.plantilla:
        cuerpo = {"template_id": args.plantilla,
                  "modifications": json.loads(args.mods) if args.mods else {}}
    else:
        urls = [u.strip() for u in args.fotos_url.split(",") if u.strip()]
        cuerpo = {"source": escena_fotos(urls, args.textos.split("|"), args.segundos, args.cta)}

    respuesta = _pedir(API, "POST", cuerpo)
    renders = respuesta if isinstance(respuesta, list) else [respuesta]
    ids = [r["id"] for r in renders]
    print(f"{len(ids)} render(s) encolados: {', '.join(i[:8] for i in ids)}")

    if not args.esperar:
        print("consulta el estado con: python creatomate_render.py --fuente ... --esperar")
        return

    listos = esperar(ids)
    for r in listos:
        print(f"  {r['status']}: {r.get('url') or r.get('error_message')}")
    if args.descargar:
        ok = [r for r in listos if r.get("status") == "succeeded" and r.get("url")]
        if not ok:
            print("ningun render termino bien; no hay nada que descargar", file=sys.stderr)
            sys.exit(1)
        urllib.request.urlretrieve(ok[0]["url"], args.descargar)
        print(f"descargado -> {args.descargar}")


if __name__ == "__main__":
    main()
