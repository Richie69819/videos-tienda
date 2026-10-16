# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Pt, Cm
from guion_docx import (base, pie, titulo, parte, haces, dices, nota, h2,
                        parrafo, casillas, tabla_atajos, GRIS, AZUL, NARANJA,
                        sombrear, rotulo)

SALIDA = r"C:\Users\RICHO\Desktop\Curso Photoshop\guiones"

doc = Document()
base(doc)
pie(doc, "Curso de Photoshop desde cero  \u00b7  Clase 1  \u00b7  Interfaz y los 12 atajos")

titulo(doc, "CLASE 1",
       "La interfaz de Photoshop y los 12 atajos  \u00b7  dura unos 13 minutos")

# ---------- como se lee ----------
h2(doc, "C\u00f3mo se lee este gui\u00f3n")
for etiqueta, resto, color in [
    ("LO QUE HACES EN PANTALLA", " \u2014 los clics, en orden. Es lo que se ve en pantalla.", NARANJA),
    ("LO QUE DICES", " \u2014 el texto hablado. Lo puedes leer tal cual o decirlo con tus palabras, pero el orden no se cambia.", AZUL),
    ("NOTA PARA TI", " \u2014 recordatorio m\u00edo. Esto nunca se dice en voz alta.", GRIS),
]:
    pp = doc.add_paragraph()
    pp.paragraph_format.left_indent = Cm(0.6)
    pp.paragraph_format.space_after = Pt(4)
    r = pp.add_run(etiqueta); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = color
    r2 = pp.add_run(resto); r2.font.size = Pt(10.5)

parrafo(doc, "Las partes van numeradas, no por minuto. Grabas la PARTE 1, luego la 2, y as\u00ed. "
             "Los minutos que aparecen debajo de cada parte son solo para que sepas si te est\u00e1s alargando.")

# ---------- antes de rec ----------
h2(doc, "Antes de darle Rec")
casillas(doc, [
    "Photoshop abierto, con Ventana \u203a Espacio de trabajo \u203a Restablecer Aspectos esenciales",
    "La carpeta del material abierta en el explorador, a la vista, para arrastrar de ah\u00ed",
    "Keyviz prendido y el filtro en Off, para que se vean las teclas sueltas",
    "OBS grabando, 1920x1080",
    "Este gui\u00f3n impreso o en el segundo monitor",
])

p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(8)
sombrear(p, 'FFF4E5')
r = p.add_run("  Qu\u00e9 necesitas tener listo:  ")
r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NARANJA
r2 = p.add_run("el archivo de tu figura estilo Funko, en "
               "material\\figura.png  \u2014  el mismo mu\u00f1eco que vas a usar en las 30 clases.  ")
r2.font.size = Pt(11)

doc.add_page_break()

# ================= PARTE 1 =================
parte(doc, 1, "Presentaci\u00f3n", "25 segundos")
haces(doc, [
    "Nada todav\u00eda. Hablas a c\u00e1mara, o sobre la pantalla si no vas a salir t\u00fa.",
    "Cuando digas \u201cesta figura\u201d, ense\u00f1as el mu\u00f1eco: la figura f\u00edsica a c\u00e1mara, o el archivo abierto en pantalla. 2 o 3 segundos.",
])
dices(doc, [
    "Qu\u00e9 tal, soy Richie.",
    "Yo hago figuras y cajas personalizadas estilo Funko, y todo el dise\u00f1o lo hago en Photoshop.",
    "En este curso te voy a ense\u00f1ar a usar Photoshop desde cero. Y desde cero es literal: esta es la clase uno "
    "y vamos a empezar por abrir el programa y ver qu\u00e9 es cada cosa de la pantalla.",
    "Vamos a trabajar con esta figura. La vamos a usar en las treinta clases, y al final del curso vas a poder "
    "armar la caja completa y hacer que Photoshop te la arme solo.",
    "En esta clase vas a terminar con tu primer archivo hecho y exportado, y con doce atajos de teclado que "
    "vamos a usar en todo el curso.",
    "Empecemos.",
])
nota(doc, "No pidas suscripci\u00f3n aqu\u00ed. Va al final, cuando el archivo ya est\u00e9 hecho. "
          "Y no digas cu\u00e1nto dura el video: si despu\u00e9s cortas algo, el n\u00famero queda mal.")

# ================= PARTE 2 =================
parte(doc, 2, "Las cinco zonas de la pantalla", "2 minutos")
haces(doc, [
    "Photoshop abierto y vac\u00edo, sin ning\u00fan archivo.",
    "Vas se\u00f1alando con el rat\u00f3n cada zona justo cuando la nombras. Sin prisa.",
    "Cuando hables de la barra de opciones: aprieta B y luego T, para que se vea cambiar.",
    "Al final: cierra el panel de Capas con su X. Sigue hablando dos segundos como si no te hubieras dado cuenta.",
    "Aprieta F7 y el panel regresa.",
])
dices(doc, [
    "Esta es la pantalla de Photoshop. Son muchos botones, pero siempre son las mismas cinco zonas. "
    "Te las voy a se\u00f1alar una por una.",
    "Arriba est\u00e1n los men\u00fas. Ah\u00ed est\u00e1 todo lo que el programa puede hacer. Cuando no encuentres algo, "
    "b\u00fascalo ah\u00ed.",
    "Debajo est\u00e1 la barra de opciones. Esta cambia seg\u00fan la herramienta que tengas seleccionada. "
    "Te lo ense\u00f1o: si agarro el pincel, dice unas cosas. Si agarro el texto, dice otras. "
    "No est\u00e1 fallando: te est\u00e1 mostrando las opciones de la herramienta que traes activa.",
    "A la izquierda est\u00e1 la barra de herramientas. Son como setenta. En este curso vamos a usar doce.",
    "A la derecha est\u00e1n los paneles. De todos, el que vas a usar siempre es el de Capas. "
    "Ese es el importante, y la clase dos es completa sobre \u00e9l.",
    "Y en medio est\u00e1 el lienzo, que es donde va tu archivo.",
    "\u2014 (despu\u00e9s de cerrar el panel) \u2014  Acabo de cerrar el panel de capas. Esto te va a pasar.",
    "No se perdi\u00f3 nada. Le das F7 y regresa.",
    "Lo que ves en la pantalla no es tu archivo: es c\u00f3mo est\u00e1n acomodadas las ventanas. "
    "Si desordenas todo, vas a Ventana, Espacio de trabajo, Restablecer, y vuelve a como estaba.",
])

# ================= PARTE 3 =================
parte(doc, 3, "Los tres ajustes del primer d\u00eda", "2 minutos")
haces(doc, [
    "Ajuste 1 \u2014 Ventana \u203a Espacio de trabajo \u203a Nuevo espacio de trabajo. Le pones tu nombre y guardas.",
    "Ajuste 2 \u2014 Ctrl+K. Te vas a la pesta\u00f1a Rendimiento. Cambias Estados de historia de 50 a 100.",
    "Ajuste 3 \u2014 en las mismas preferencias, pesta\u00f1a Manejo de archivos. Pones la recuperaci\u00f3n autom\u00e1tica en 5 minutos.",
    "Aceptas y cierras.",
])
dices(doc, [
    "Antes de empezar a trabajar vamos a cambiar tres ajustes. Son dos minutos y no los vuelves a tocar.",
    "El primero. Cuando tengas los paneles acomodados como te gusten, vas a Ventana, Espacio de trabajo, "
    "Nuevo espacio de trabajo, y le pones tu nombre. A partir de ah\u00ed, si desordenas la pantalla, "
    "con un clic la regresas.",
    "El segundo. Control+K, que abre las preferencias. En Rendimiento hay una opci\u00f3n que dice "
    "Estados de historia. Viene en cincuenta y la vamos a subir a cien. "
    "Eso es cu\u00e1ntos pasos puedes deshacer hacia atr\u00e1s. Con cincuenta te puedes quedar corto "
    "en una sesi\u00f3n larga.",
    "Y el tercero, en Manejo de archivos: guardar informaci\u00f3n de recuperaci\u00f3n autom\u00e1ticamente. "
    "Ponlo en cada cinco minutos. Esto es para cuando el programa se cierre solo, que alguna vez va a pasar.",
])

# ================= PARTE 4 =================
parte(doc, 4, "Los 12 atajos", "90 segundos")
haces(doc, [
    "Pon en pantalla la tarjeta con los doce atajos.",
    "Aprieta cada tecla justo cuando la dices, para que se vea cambiar la herramienta y se vea en Keyviz.",
    "Al terminar, deja la tarjeta quieta unos 8 segundos para que se pueda pausar y fotografiar.",
])
dices(doc, [
    "Ahora los doce atajos. No te los aprendas de memoria ahorita: los vamos a usar en seguida "
    "y se quedan con el uso.",
    "Los primeros seis son de herramienta. Una tecla, una herramienta.",
    "V, mover.",
    "M, marco. Sirve para seleccionar un rect\u00e1ngulo.",
    "L, lazo.",
    "B, pincel.",
    "E, borrador.",
    "T, texto.",
    "Los otros seis son comandos, y van con la tecla Control.",
    "Control+N, documento nuevo.",
    "Control+T, transformar. Es para cambiar el tama\u00f1o de algo, o girarlo.",
    "Control+Z, deshacer. Se puede apretar varias veces seguidas.",
    "Control+cero, ajusta la imagen al tama\u00f1o de la pantalla.",
    "Control+S, guardar.",
    "Y Control+Shift+Alt+W, exportar. Es largo, pero es el que vas a usar para sacar el JPG.",
    "Si usas Mac, donde yo diga Control, t\u00fa usa Comando.",
    "Y dos cosas m\u00e1s que no son atajos, pero las vas a usar mucho. La barra espaciadora, apretada, "
    "te deja mover la imagen sin cambiar de herramienta. Y Alt con la rueda del rat\u00f3n hace zoom.",
])
nota(doc, "Esta tabla es tu referencia al grabar. No se lee en voz alta.")
tabla_atajos(doc, [
    ("V", "Mover", "la V de mo-V-er"),
    ("M", "Marco de selecci\u00f3n", "M de marco"),
    ("L", "Lazo", "L de lazo"),
    ("B", "Pincel", "brush"),
    ("E", "Borrador", "eraser"),
    ("T", "Texto", "T de texto"),
    ("Ctrl+N", "Documento nuevo", "nuevo"),
    ("Ctrl+T", "Transformar", "transformar"),
    ("Ctrl+Z", "Deshacer", "\u2014"),
    ("Ctrl+0", "Ajustar a la pantalla", "cero = todo"),
    ("Ctrl+S", "Guardar", "save"),
    ("Ctrl+Shift+Alt+W", "Exportar como", "el largo"),
])

doc.add_page_break()

# ================= PARTE 5 =================
parte(doc, 5, "Crear el documento", "2 minutos")
haces(doc, [
    "Ctrl+N.",
    "Anchura: 1080. Altura: 1920. Revisa que la unidad diga P\u00edxeles, no Cent\u00edmetros.",
    "Resoluci\u00f3n: 72.",
    "Modo de color: RGB, 8 bits.",
    "Contenido del fondo: Blanco.",
    "Antes de aceptar: se\u00f1ala el bot\u00f3n de guardar preajuste y gu\u00e1rdalo como \u201cvertical redes\u201d.",
    "Crear.",
    "Ctrl+S y lo guardas como 01-portada.psd.",
])
dices(doc, [
    "Ahora s\u00ed, vamos a crear el documento. Control+N.",
    "Aqu\u00ed es donde se arruinan la mitad de los dise\u00f1os, as\u00ed que vamos despacio.",
    "Anchura: mil ochenta. Altura: mil novecientos veinte. Y fíjate que la unidad diga p\u00edxeles, "
    "no cent\u00edmetros.",
    "Resoluci\u00f3n: setenta y dos.",
    "Modo de color: RGB, ocho bits.",
    "Y el fondo, blanco.",
    "Te explico esos n\u00fameros. Mil ochenta por mil novecientos veinte es el tama\u00f1o exacto de un reel, "
    "un TikTok y un Short. Es vertical.",
    "Y setenta y dos de resoluci\u00f3n con RGB es lo que se usa cuando algo va a verse en pantalla. "
    "Para imprimir son otros n\u00fameros, y eso lo vemos m\u00e1s adelante, cuando lleguemos a la caja.",
    "Antes de darle crear, mira este bot\u00f3n: guardar preajuste. Le ponemos \u201cvertical redes\u201d. "
    "Este documento lo vas a hacer muchas veces; m\u00e1s vale configurarlo una.",
    "Y lo guardamos de una vez, antes de hacer nada. Control+S, y le ponemos cero uno portada.",
    "Agarra la costumbre de darle Control+S cada vez que termines un paso.",
])

# ================= PARTE 6 =================
parte(doc, 6, "Meter la figura, moverla y escalarla", "3 minutos")
haces(doc, [
    "Arrastra figura.png de la carpeta al lienzo.",
    "Entra con un recuadro con cuadritos en las esquinas. Jalas una esquina para que quepa y das Enter.",
    "Se\u00f1ala el panel de capas: ahora hay dos.",
    "Aprieta V. Arrastra la figura al centro hasta que salgan las gu\u00edas rosas. Su\u00e9ltala ah\u00ed.",
    "Ctrl+T. Jala del cuadrito DEL LADO derecho y deja la figura achatada. Qu\u00e9date tres segundos sin hablar.",
    "Ctrl+Z.",
    "Ctrl+T otra vez, y ahora jala de la ESQUINA. Se\u00f1ala la cadenita de la barra de opciones. Enter.",
    "Alt+rueda para acercarte a la cara. Barra espaciadora para moverte. Ctrl+0 para volver a ver todo.",
])
dices(doc, [
    "Ahora metemos la figura. La agarras de la carpeta y la arrastras al lienzo. As\u00ed, directo.",
    "F\u00edjate que entr\u00f3 con un recuadro con cuadritos en las esquinas. Eso es Photoshop pregunt\u00e1ndote "
    "de qu\u00e9 tama\u00f1o la quieres. Jalas una esquina para que quepa, y Enter.",
    "Y mira el panel de capas: ahora hay dos. El fondo blanco, y la figura encima.",
    "Eso es Photoshop, en resumen: hojas encimadas. Y la clase dos es completa sobre eso.",
    "V, mover. Y la arrastras al centro.",
    "\u00bfVes esas l\u00edneas rosas que aparecieron? Son las gu\u00edas: te est\u00e1n diciendo que ya est\u00e1 centrado. "
    "Su\u00e9ltala ah\u00ed.",
    "Control+T, transformar. Ahora la puedo hacer m\u00e1s grande, m\u00e1s chica, o girarla.",
    "\u2014 (despu\u00e9s de achatarla, tras los tres segundos de silencio) \u2014  Mira lo que acabo de hacer. "
    "Le apachurr\u00e9 la cabeza.",
    "En una figura as\u00ed se nota mucho, porque la cabeza es m\u00e1s grande que el cuerpo. Esa proporci\u00f3n "
    "es la forma del mu\u00f1eco. Si la apachurras, deja de verse como lo que es.",
    "Control+Z y lo arreglamos.",
    "Lo que pas\u00f3 es esto: si jalas de la esquina, se mantiene la proporci\u00f3n. Si jalas del lado, "
    "lo deformas.",
    "Y si quieres estar seguro, mira arriba en la barra de opciones: entre el ancho y el alto hay una "
    "cadenita. Con la cadena cerrada no se deforma, jales de donde jales.",
    "Enter para aplicar.",
    "Y ya que estamos: Alt con la rueda para acercarme. Mira el detalle de la cara.",
    "La barra espaciadora apretada para moverme.",
    "Y Control+cero para volver a ver todo completo. Este atajo lo vas a usar todo el tiempo.",
])

# ================= PARTE 7 =================
parte(doc, 7, "Poner el texto", "90 segundos")
haces(doc, [
    "Aprieta T. Clic en el lienzo. Escribe el nombre de la figura.",
    "Si sale de un tama\u00f1o raro: Ctrl+T sobre el texto y lo ajustas.",
    "Se\u00f1ala arriba el tama\u00f1o, la fuente y el color en la barra de opciones.",
    "Aprieta Enter a prop\u00f3sito y ense\u00f1a que hace un rengl\u00f3n nuevo.",
    "Ctrl+Enter para cerrar el texto.",
])
dices(doc, [
    "T, de texto. Clic en el lienzo, y escribes el nombre de tu figura.",
    "Si sale enorme o muy chico, no te pelees con \u00e9l: Control+T tambi\u00e9n funciona en el texto.",
    "Y el tama\u00f1o, la letra y el color est\u00e1n aqu\u00ed arriba, en la barra de opciones, porque ahora "
    "la herramienta que traigo activa es el texto. Es lo que vimos al principio.",
    "Ahora, el error que comete todo el mundo. Para dejar de escribir le damos Enter... y no. "
    "Enter te hace un rengl\u00f3n nuevo.",
    "Se sale con Control+Enter. O cambiando de herramienta. O con la palomita de arriba.",
    "Control+Enter. Ap\u00fantatelo.",
])

# ================= PARTE 8 =================
parte(doc, 8, "Exportar el archivo", "90 segundos")
haces(doc, [
    "Ctrl+Shift+Alt+W.",
    "Formato: JPG. Calidad: 80.",
    "Se\u00f1ala el peso del archivo, abajo a la izquierda.",
    "Exportar, y lo guardas como 01-portada.jpg.",
    "Abre la carpeta y ense\u00f1a el archivo ya hecho.",
])
dices(doc, [
    "Ya tenemos el dise\u00f1o. Pero el PSD es tu archivo de trabajo: eso no se sube a internet. "
    "Para subirlo hay que exportarlo.",
    "Control+Shift+Alt+W. Ya te hab\u00eda dicho que era largo.",
    "Formato: JPG. Calidad: ochenta. Y la raz\u00f3n de ochenta es esta: de ah\u00ed para arriba el archivo "
    "pesa casi el doble y se ve pr\u00e1cticamente igual.",
    "Mira aqu\u00ed abajo a la izquierda, te dice cu\u00e1nto pesa.",
    "Exportar, y le ponemos cero uno portada.",
    "Y ah\u00ed est\u00e1 tu primer archivo de Photoshop. Ese ya lo puedes subir a donde quieras.",
])

# ================= PARTE 9 =================
parte(doc, 9, "Los seis \u201cno me sale\u201d", "90 segundos")
haces(doc, [
    "Provoca cada problema en pantalla y arr\u00e9glalo delante de la c\u00e1mara. Uno por uno, r\u00e1pido.",
    "Problema 1: selecciona la capa del fondo e intenta mover la figura.",
    "Problema 2: pon el Bloq May\u00fas y ense\u00f1a el cursor de cruz.",
    "Problema 3: haz una selecci\u00f3n con M, cambia a pincel e intenta pintar fuera. Luego Ctrl+D.",
    "Problema 4: Imagen \u203a Modo \u203a Color CMYK, ense\u00f1a el cambio, y reg\u00e9salo a RGB.",
    "Problema 5: cierra un panel y re\u00e1brelo desde el men\u00fa Ventana.",
    "Problema 6: ense\u00f1a Archivo \u203a Abrir recientes.",
])
dices(doc, [
    "Antes de cerrar, los seis problemas que te van a pasar esta semana. Te los ense\u00f1o y te los arreglo.",
    "Uno: haces algo y no pasa nada. Es que tienes seleccionada otra capa. Clic en la capa correcta, "
    "en el panel.",
    "Dos: el cursor se te hizo una cruz rara. Traes el Bloq May\u00fas puesto. Qu\u00edtalo.",
    "Tres: no puedes pintar nada. Tienes una selecci\u00f3n activa de antes. Control+D, deseleccionar.",
    "Cuatro: todo se ve raro de color. Est\u00e1s en modo CMYK. Imagen, Modo, Color RGB.",
    "Cinco: perdiste un panel. Lo cerraste. Ventana, y el que te falte.",
    "Seis: se cerr\u00f3 sin guardar. Archivo, Abrir recientes. Y ya configuramos la recuperaci\u00f3n "
    "autom\u00e1tica al principio del video, as\u00ed que est\u00e1s cubierto.",
    "Esos seis son casi todos los \u201cno me sale\u201d. Si quieres, pausa aqu\u00ed y toma captura.",
])

# ================= PARTE 10 =================
parte(doc, 10, "Cierre", "40 segundos")
haces(doc, [
    "Repasa los atajos apret\u00e1ndolos uno tras otro, r\u00e1pido, para que se vean en Keyviz.",
    "Pantalla final apuntando a la Clase 2. Nada m\u00e1s.",
])
dices(doc, [
    "Y para terminar, treinta segundos de pr\u00e1ctica. Conmigo, sin pensar:",
    "V. M. L. B. E. T. Control+Z. Control+cero.",
    "Otra vez, m\u00e1s r\u00e1pido.",
    "Haz esto tres minutos al d\u00eda esta semana y se te quedan en los dedos. Nadie se aprende "
    "los atajos ley\u00e9ndolos de una lista.",
    "Tu tarea: sube tu archivo a los comentarios. Tu figura, centrada, vertical. Los contesto todos.",
    "Y si no tienes una figura, te dej\u00e9 la m\u00eda en el comentario fijado para que trabajes con ella.",
    "Si te sirvi\u00f3, suscr\u00edbete, que ma\u00f1ana sube la clase dos.",
    "Y la clase dos es la importante: capas y m\u00e1scaras. Es el concepto en el que se apoya todo "
    "lo dem\u00e1s de Photoshop. Ah\u00ed te veo.",
])

doc.add_page_break()

# ---------- notas de produccion ----------
h2(doc, "Notas de producci\u00f3n")
parrafo(doc, "Todo lo de aqu\u00ed abajo es para ti. Nada se dice en c\u00e1mara.", 10)

h2(doc, "Los tres errores a prop\u00f3sito")
parrafo(doc, "Van a prop\u00f3sito y no se cortan. Son lo que hace que el que te ve no se sienta "
             "tonto cuando le pasen a \u00e9l:")
for t in ["Parte 2 \u2014 cerrar el panel de Capas.",
          "Parte 6 \u2014 apachurrarle la cabeza a la figura.",
          "Parte 7 \u2014 darle Enter al texto y que haga rengl\u00f3n nuevo."]:
    p = doc.add_paragraph(t, style='List Bullet')
    p.paragraph_format.left_indent = Cm(0.8)

h2(doc, "Ficha")
parrafo(doc, "T\u00edtulo: Curso de Photoshop desde cero \u2014 Clase 1: la interfaz y los 12 atajos "
             "que vas a usar siempre")
parrafo(doc, "Entrega: 01-portada.jpg, 1080x1920, con la figura centrada")
parrafo(doc, "Material: material\\figura.png")
parrafo(doc, "Miniatura: texto \u201c12 ATAJOS\u201d sobre fondo naranja. A un lado, un teclado con doce "
             "teclas iluminadas; al otro, el lienzo vertical terminado.")

h2(doc, "Shorts que salen de esta grabaci\u00f3n")
for t in ["Parte 6, el momento de la cabeza apachurrada \u2014 gancho: \u201cSi lo jalas del lado / "
          "le apachurras la cabeza\u201d",
          "Parte 7, el Control+Enter \u2014 gancho: \u201cTu texto no se cierra / con Enter\u201d",
          "Parte 3, los tres ajustes \u2014 gancho: \u201cCambia esto el d\u00eda / que instalas Photoshop\u201d"]:
    p = doc.add_paragraph(t, style='List Bullet')
    p.paragraph_format.left_indent = Cm(0.8)

h2(doc, "Capítulos para la descripci\u00f3n de YouTube")
for t in ["00:00 Presentaci\u00f3n", "00:25 Las 5 zonas de la pantalla",
          "02:25 Los 3 ajustes del primer d\u00eda", "04:25 Los 12 atajos",
          "06:00 Crear el documento: 1080x1920, 72 ppp, RGB",
          "08:00 Meter la figura, mover y escalar sin deformar",
          "11:00 El texto (y c\u00f3mo se cierra)", "12:00 Exportar en JPG",
          "13:00 Los 6 \u201cno me sale\u201d m\u00e1s comunes"]:
    p = doc.add_paragraph(t)
    p.paragraph_format.left_indent = Cm(0.8)
    p.paragraph_format.space_after = Pt(2)

ruta = os.path.join(SALIDA, "Clase 01 - Interfaz y 12 atajos.docx")
doc.save(ruta)
print("DOCX:", ruta)
