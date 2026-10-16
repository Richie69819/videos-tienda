# Shorts del lanzamiento

Los Shorts no son adelantos del curso: son clases de 20 segundos que se entienden
solas. El que resuelve un problema en 20 segundos gana el derecho a que lo escuchen 12
minutos.

Regla: **un Short, un truco completo**. Si no cabe entero en 20 segundos, no es Short,
es clase.

## Cómo se producen (con el pipeline del repo)

El material es captura de pantalla con voz, así que hay transcripción y conviene
quemar subtítulos: en Shorts se ve mucho sin sonido.

```bash
# 1. Transcribir la clase ya grabada
python scripts/transcribe.py "clases/clase-01.mp4" --output "%TEMP%/videos-tienda/c01.json" --idioma es

# 2. Renderizar los 3 Shorts de una pasada
python scripts/lote.py --plan curso-photoshop/plan-shorts-clase-01.json --salida "./Para publicar" --validar

# 3. Una variante por red
python scripts/export.py --entrada "./Para publicar" --plataforma todas --salida "./videos"
python scripts/validate.py "./videos"
```

**Lo que cambia respecto a un reel de producto:** la captura de pantalla es 16:9 y al
pasarla a 9:16 queda una franja ilegible en el celular. Dos reglas:

1. Grabar la clase con la **interfaz de Photoshop al 125%** (`Edición > Preferencias >
   Interfaz > Escala de IU`). Lo que no se lee en un celular, no sirve.
2. Para el Short, no meter la pantalla completa: usar `--centro` para encuadrar la zona
   que importa (el panel de capas, el cuadro de diálogo) y dejar que `reframe.py` haga
   el resto. `--contenido pantalla` pone la banda de marca arriba y abajo en lugar de
   estirar la imagen.

## Plan listo para `lote.py`

Guardar como `curso-photoshop/plan-shorts-clase-01.json`, **en UTF-8** (si se pasan los
ganchos como argumento en la consola de Windows, los acentos y los signos de
interrogación se rompen; por eso van en el archivo).

```json
{
  "comunes": {
    "estilo": "bold",
    "contenido": "pantalla",
    "cta": "Curso completo: Clase 1",
    "captions": "C:/Users/richie/AppData/Local/Temp/videos-tienda/c01.json",
    "audio": "limpio",
    "nivel_audio": -18,
    "plataforma": "todas"
  },
  "clips": [
    {
      "nombre": "c01-s1-texto-enter",
      "video": "clases/clase-01.mp4",
      "desde": 455,
      "hasta": 470,
      "gancho": "Tu texto no se cierra|con Enter"
    },
    {
      "nombre": "c01-s2-deformar",
      "video": "clases/clase-01.mp4",
      "desde": 362,
      "hasta": 380,
      "gancho": "Si lo escalas del lado|lo deformas"
    },
    {
      "nombre": "c01-s3-documento-nuevo",
      "video": "clases/clase-01.mp4",
      "desde": 212,
      "hasta": 234,
      "gancho": "1080 x 1920, 72 ppp, RGB|apúntalo"
    }
  ]
}
```

Los segundos de `desde` y `hasta` salen del guion: cada guion de clase trae su línea
`SHORT:` con los tiempos marcados mientras se graba. Marcarlos en el momento ahorra
media hora de buscar después.

## Los 9 Shorts del día 1 al día 3

Tres por clase estrenada. El gancho va en dos líneas, igual que en el resto del canal.

| Día | Gancho | De dónde sale | Dur |
|---|---|---|---|
| 1 | `Estas 200 imágenes\|las hizo Photoshop solo` | Clase 0, el lote corriendo | 18 s |
| 1 | `Tu texto no se cierra\|con Enter` | Clase 1 | 15 s |
| 1 | `Deja de borrar\|en Photoshop` | Clase 2, borrador vs máscara | 20 s |
| 2 | `Photoshop gratis y legal\|existe, es esto` | Clase 0, Photopea | 20 s |
| 2 | `Si lo escalas del lado\|lo deformas` | Clase 1 | 18 s |
| 2 | `Negro tapa, blanco muestra\|ya sabes máscaras` | Clase 2 | 15 s |
| 3 | `Photoshop tiene 70 herramientas\|vas a usar 12` | Clase 0 | 15 s |
| 3 | `1080 x 1920, 72 ppp, RGB\|apúntalo` | Clase 1 | 22 s |
| 3 | `Alt + clic en el ojo\|nadie te dijo esto` | Clase 2 | 14 s |

Los tres mejores ganchos para abrir son, en orden: **"Deja de borrar en Photoshop"**
(contradice algo que el espectador hace hoy), **"Estas 200 imágenes las hizo Photoshop
solo"** (resultado imposible de ignorar) y **"Tu texto no se cierra con Enter"**
(problema que tuvo ayer). Los tres caben en los moldes del canal: contradicción,
resultado antes que producto, y error común (ver `../references/ganchos.md`).

## Lo que no se hace en los Shorts

- Decir "link en la descripción". En Shorts nadie baja. Se dice "está en mi canal,
  clase uno".
- Meter el curso completo en 20 segundos.
- Subir el Short el mismo día que la clase y no volver a mencionarla. Cada Short se
  reutiliza: el del día 1 se vuelve a subir en el día 40 con otro gancho. Las clases no
  caducan, los Shorts tampoco.
- Música al volumen del original. Con voz encima, la música va al 0.12 que trae
  `render_clip.py` por defecto.
