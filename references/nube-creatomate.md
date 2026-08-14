# Motor en la nube: Creatomate

El motor local (FFmpeg) cubre el trabajo diario y es gratis. Creatomate es la segunda
opcion, por API REST, sin instalar el SDK de Node.

## Cuando conviene

- Las fotos **ya viven en una URL publica** (el CDN de Shopify, por ejemplo) y no quieres bajarlas.
- Quieres render **desde el celular o el iPad**, con la PC apagada.
- Necesitas una **plantilla** con animaciones que libass no puede hacer.
- Vas a generar **muchas variantes** del mismo video cambiando solo textos.

## Cuando no

Cobra por minuto renderizado y sube tu material a un tercero. Para un reel de fotos o
un corte con subtitulos, el motor local hace lo mismo gratis y sin salir de la PC.

## Configuracion

La llave se saca en creatomate.com > Project Settings > API key y se pasa por variable
de entorno (nunca en el codigo ni en el repo):

```powershell
$env:CREATOMATE_API_KEY = "tu-llave"
```

## Uso

Slideshow desde URLs (equivalente en nube de `slideshow.py`):

```
python scripts/creatomate_render.py --fotos-url "https://cdn.shopify.com/a.jpg,https://cdn.shopify.com/b.jpg" --textos "Anillo dona|Envio gratis" --cta "michilab.store" --esperar --descargar reel.mp4
```

Plantilla con modificaciones:

```
python scripts/creatomate_render.py --plantilla TEMPLATE_ID --mods "{\"Title\":\"Anillo dona\",\"Price\":\"$180\"}" --esperar
```

Escena propia en JSON (RenderScript):

```
python scripts/creatomate_render.py --fuente escena.json --esperar --descargar reel.mp4
```

## RenderScript en corto

Es un JSON con `output_format`, `width`, `height` y una lista de `elements`. Cada
elemento tiene un `track` (los numeros altos van encima) y opcionalmente `time` y
`duration`.

```json
{
  "output_format": "mp4", "frame_rate": 30, "width": 1080, "height": 1920,
  "elements": [
    { "type": "image", "track": 1, "duration": 3, "source": "https://...",
      "animations": [{ "type": "pan_center", "start_scale": "100%", "end_scale": "120%" }] },
    { "type": "text", "track": 2, "time": 0.5, "duration": 2.5, "text": "Anillo dona",
      "y": "82%", "font_family": "Montserrat", "font_weight": "800",
      "fill_color": "#f5f2e9", "stroke_color": "#5a6640" }
  ]
}
```

Tipos utiles: `video`, `image`, `text`, `audio`, `composition` (agrupa elementos como
una escena anidada). Transiciones entre elementos del mismo track con
`"transition": {"type": "fade", "duration": 0.4}`.

Colores de marca Michilab para cualquier plantilla: olivo `#5a6640`, crema `#f5f2e9`,
naranja `#e08a5b`.

## Flujo

`POST /v1/renders` encola y responde con uno o varios renders con su `id` y `status`
(`planned` → `rendering` → `succeeded` / `failed`). `GET /v1/renders/{id}` consulta el
estado; cuando termina trae la `url` del archivo. `--esperar` hace ese sondeo solo y
`--descargar` guarda el resultado.

Mas ejemplos oficiales: https://github.com/Creatomate/node-examples
