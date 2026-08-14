"""Renderiza muchos clips de una sola pasada a partir de un plan en JSON.

Es la forma de trabajar cuando hay que sacar decenas de clips: se escribe el plan
(que corte, que gancho, que estilo), se revisa en texto, y se renderiza todo junto.
El plan va en UTF-8, asi que los acentos y signos de interrogacion llegan intactos
a los subtitulos sin pelearse con la consola de Windows.

Formato del plan:
{
  "comunes": { "estilo": "michilab", "cta": "michilab.store",
                "audio": "limpio", "nivel_audio": -18 },
  "clips": [
    { "nombre": "01-rojo-gato", "video": "C:/.../IMG_0362.MOV",
      "desde": 122, "hasta": 130, "gancho": "¿Se aburre solo?|Ya no" }
  ]
}

Cualquier clave de "comunes" se puede repisar clip por clip. Las claves aceptadas son
las opciones de render_clip.py con guion bajo (nivel_audio, sin_subtitulos, ...).

Uso:
    python lote.py --plan plan.json --salida "./Para publicar" [--validar]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

from common import ensure_dir, media_info

# clave del plan -> bandera de render_clip.py
BANDERAS = {
    "video": "--input", "desde": "--desde", "hasta": "--hasta",
    "estilo": "--estilo", "modo": "--modo", "contenido": "--contenido",
    "centro": "--centro", "gancho": "--gancho", "cta": "--cta",
    "plataforma": "--plataforma", "logo": "--logo", "musica": "--musica",
    "volumen_musica": "--volumen-musica", "audio": "--audio",
    "nivel_audio": "--nivel-audio", "velocidad": "--velocidad",
    "captions": "--captions",
}
BANDERAS_SOLAS = {"sin_subtitulos": "--sin-subtitulos", "cpu": "--cpu"}


def comando(clip: dict, destino: Path) -> tuple[list, Path]:
    salida = destino / f"{clip['nombre']}.mp4"
    cmd = [sys.executable, str(Path(__file__).parent / "render_clip.py"),
           "--out", str(salida)]
    for clave, bandera in BANDERAS.items():
        if clip.get(clave) not in (None, ""):
            cmd += [bandera, str(clip[clave])]
    for clave, bandera in BANDERAS_SOLAS.items():
        if clip.get(clave):
            cmd.append(bandera)
    return cmd, salida


def main():
    ap = argparse.ArgumentParser(description="Renderiza un lote de clips desde un plan JSON")
    ap.add_argument("--plan", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--validar", action="store_true", help="revisa los archivos al terminar")
    ap.add_argument("--seguir", action="store_true",
                    help="continua aunque un clip falle (por defecto tambien continua)")
    args = ap.parse_args()

    with open(args.plan, "r", encoding="utf-8") as fh:
        plan = json.load(fh)
    comunes = plan.get("comunes", {})
    clips = plan["clips"]
    destino = ensure_dir(args.salida)

    print(f"{len(clips)} clips -> {destino.resolve()}\n")
    t0 = time.time()
    hechos, fallidos = [], []

    for i, base in enumerate(clips, 1):
        clip = {**comunes, **base}
        cmd, salida = comando(clip, destino)
        print(f"[{i}/{len(clips)}] {clip['nombre']}  "
              f"{clip.get('desde', 0)}s -> {clip.get('hasta', '?')}s")
        proc = subprocess.run(cmd, capture_output=True, text=True,
                              encoding="utf-8", errors="replace")
        if proc.returncode != 0 or not salida.exists():
            cola = "\n".join((proc.stderr or proc.stdout or "").strip().splitlines()[-6:])
            print(f"    FALLO:\n{cola}\n")
            fallidos.append(clip["nombre"])
            continue
        info = media_info(salida)
        hechos.append({"nombre": clip["nombre"], "archivo": salida, "info": info,
                       "gancho": clip.get("gancho", "")})
        print(f"    ok  {info['duration']:.1f}s  {info['size']/1024**2:.1f} MB")

    print(f"\n{len(hechos)} clips en {time.time()-t0:.0f}s"
          + (f", {len(fallidos)} fallidos: {', '.join(fallidos)}" if fallidos else ""))

    if hechos:
        print(f"\n{'archivo':32s} {'dur':>6s} {'peso':>9s}  gancho")
        for h in hechos:
            print(f"{h['archivo'].name:32s} {h['info']['duration']:5.1f}s "
                  f"{h['info']['size']/1024**2:8.1f}M  {h['gancho'].replace('|', ' / ')}")

    if args.validar and hechos:
        print()
        subprocess.run([sys.executable, str(Path(__file__).parent / "validate.py"),
                        str(destino)])

    sys.exit(1 if fallidos else 0)


if __name__ == "__main__":
    main()
