# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Pt, Cm
from guion_docx import (base, pie, titulo, parte, haces, dices, nota, h2,
                        parrafo, casillas, GRIS, AZUL, NARANJA, sombrear)

SALIDA = r"C:\Users\RICHO\Desktop\Curso Photoshop\guiones"

doc = Document()
base(doc)
pie(doc, "Curso de Photoshop desde cero  \u00b7  Clase 2  \u00b7  Capas y m\u00e1scaras")

titulo(doc, "CLASE 2", "Capas y m\u00e1scaras  \u00b7  dura unos 14 minutos")

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

h2(doc, "De qu\u00e9 va esta clase")
parrafo(doc, "Esta es la clase bisagra del curso. Si el que te ve entiende la m\u00e1scara, las 28 clases "
             "que siguen son cuesta abajo. Si no la entiende, va a batallar en todas. Por eso dura "
             "14 minutos y no 8, y por eso va en el primer d\u00eda.")
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(6)
sombrear(p, 'FFF4E5')
r = p.add_run("  La idea que hay que dejar clavada:  ")
r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NARANJA
r2 = p.add_run("en Photoshop no se borra, se tapa.  ")
r2.font.size = Pt(11); r2.bold = True

h2(doc, "Antes de darle Rec")
casillas(doc, [
    "material\\figura-con-fondo.jpg a la mano: la figura ANTES de recortarse, con su fondo. "
    "Es lo que le vas a tapar con la m\u00e1scara",
    "Tu logo en PNG con fondo transparente",
    "El nombre y el n\u00famero que le vas a poner a la figura, ya decididos (no se piensa en c\u00e1mara)",
    "02-ficha.psd a medias guardado en plantillas\\ (fondo de color y la figura metida, nada m\u00e1s)",
    "02-ficha.psd terminado guardado en plantillas\\, por si hay que repetir la toma",
    "Keyviz prendido, OBS grabando",
])
nota(doc, "Si tu figura solo la tienes ya recortada, dime y te genero la versi\u00f3n con fondo. "
          "Sin fondo que tapar, esta clase no se puede grabar.")

doc.add_page_break()

# ===== PARTE 1 =====
parte(doc, 1, "Presentaci\u00f3n y lo que se va a hacer", "30 segundos")
haces(doc, [
    "Ten abiertas dos versiones de la figura: una con el fondo borrado a mordidas con el borrador, "
    "fea, y otra limpia hecha con m\u00e1scara.",
    "Ense\u00f1a la fea. Luego la buena.",
    "En la buena, apaga la m\u00e1scara con Shift+clic para que el fondo REGRESE. Ese es el momento.",
])
dices(doc, [
    "Qu\u00e9 tal, soy Richie. Seguimos con el curso de Photoshop desde cero.",
    "En la clase uno vimos la pantalla y los atajos, y sacamos el primer archivo. "
    "Si no la has visto, te la dejo aqu\u00ed arriba.",
    "Hoy vamos a ver capas y m\u00e1scaras. Y esta es la clase importante del curso, te lo digo de una vez: "
    "es el concepto en el que se apoya todo lo dem\u00e1s.",
    "Mira estas dos. En esta le quit\u00e9 el fondo con el borrador, y se ve mordida. "
    "En esta lo hice con una m\u00e1scara.",
    "Y la diferencia de verdad es esta: en la de la m\u00e1scara, el fondo sigue ah\u00ed. Lo puedo regresar "
    "cuando quiera.",
    "Al final de este video vas a entender por qu\u00e9, y vas a tener esta ficha hecha por ti.",
])

# ===== PARTE 2 =====
parte(doc, 2, "Qu\u00e9 es una capa", "2 minutos y medio")
haces(doc, [
    "Si tienes tres acetatos o tres hojas transparentes, ens\u00e9\u00f1alos a c\u00e1mara encimados. "
    "Si no, haz tres rect\u00e1ngulos en pantalla y s\u00e9paralos.",
    "Abre el panel de capas con F7 y se\u00f1ala las capas de arriba abajo.",
    "Selecciona a prop\u00f3sito la capa de abajo y ponte a pintar con el pincel. No va a pasar nada visible. "
    "Qu\u00e9date dos segundos as\u00ed.",
    "Se\u00f1ala en el panel qu\u00e9 capa ten\u00edas seleccionada. Ctrl+Z.",
])
dices(doc, [
    "Una capa es una hoja transparente. Tu archivo es un mont\u00f3n de hojas encimadas, y lo que ves "
    "es lo que se alcanza a ver desde arriba. Eso es todo.",
    "De ah\u00ed salen tres cosas, y de esas tres sale casi todo lo que se le complica a alguien "
    "que va empezando.",
    "La primera: el orden importa. Lo de arriba tapa lo de abajo. En el panel, arriba es arriba.",
    "La segunda: solo le haces cosas a la capa que tengas seleccionada. Y esto es importante, "
    "porque cuando algo no funcione, casi siempre es esto. M\u00edrame.",
    "\u2014 (pintando sin resultado) \u2014  Estoy pintando y no pasa nada. Y es porque estoy pintando "
    "debajo de la figura. Ten\u00eda seleccionada la capa de abajo.",
    "Esto nos pasa a todos, seguido. Antes de pensar que el programa est\u00e1 fallando, mira "
    "el panel de capas.",
    "Y la tercera: cada cosa en su capa. La figura en una, el nombre en otra, el n\u00famero en otra, "
    "el logo en otra. Te cuesta diez segundos m\u00e1s y te deja cambiar una cosa sin rehacer el resto.",
    "Y hay otra raz\u00f3n, que la vas a ver m\u00e1s adelante en el curso: cuando lleguemos a sacar varias "
    "cajas de un solo archivo, eso solo funciona si cada cosa est\u00e1 en su capa y tiene nombre. "
    "La ficha que hagamos hoy va a ser esa plantilla.",
])

# ===== PARTE 3 =====
parte(doc, 3, "Los controles del panel de capas", "2 minutos")
haces(doc, [
    "Se\u00f1ala y usa cada control conforme lo nombras: el ojo, la opacidad, el candado, el modo de fusi\u00f3n.",
    "Con el ojo: apaga y prende la capa de la figura dos veces, para que se vea el antes y despu\u00e9s.",
    "Con la opacidad: baja el logo a 70 y s\u00fabelo otra vez.",
    "Abre el desplegable de modos de fusi\u00f3n y ens\u00e9\u00f1alo. Prueba Multiplicar.",
    "Demuestra los atajos: Ctrl+J duplica, Ctrl+Shift+N capa nueva, Ctrl+G agrupa.",
    "Alt+clic en el ojo de una capa, para dejarla sola. Otro Alt+clic para regresar.",
])
dices(doc, [
    "Estos son los controles del panel, y son cuatro.",
    "El ojo prende y apaga la capa. Sirve para comparar el antes y el despu\u00e9s de un clic.",
    "La opacidad es qu\u00e9 tan transparente est\u00e1 la capa. Al logo normalmente le bajo a setenta, "
    "para que no compita con la figura.",
    "El candado es para que no muevas algo sin querer. Al fondo se lo pongo siempre.",
    "Y el modo de fusi\u00f3n es c\u00f3mo se mezcla una capa con la de abajo. Hay como veintisiete y "
    "suenan a brujer\u00eda, pero en la pr\u00e1ctica se usan tres: Multiplicar oscurece y deja pasar lo blanco. "
    "Trama aclara y deja pasar lo negro. Luz suave sube el contraste.",
    "Esos tres. Multiplicar es el que vamos a usar cuando hagamos la sombra de la figura.",
    "Y cuatro atajos del panel que vas a usar siempre:",
    "Control+J duplica la capa. Antes de arriesgar algo, duplica.",
    "Control+Shift+N hace una capa nueva vac\u00eda.",
    "Control+G las agrupa en una carpeta, para no perderte cuando tengas veinte.",
    "Y este casi nadie lo sabe: Alt con clic en el ojo de una capa te deja ver esa sola, "
    "y apaga todas las dem\u00e1s. Otro Alt con clic y regresan. Cuando tengas veinte capas y no sepas "
    "cu\u00e1l es cu\u00e1l, esto sirve m\u00e1s que ordenarlas.",
])

doc.add_page_break()

# ===== PARTE 4 =====
parte(doc, 4, "La m\u00e1scara: negro tapa, blanco muestra", "4 minutos")
haces(doc, [
    "Abre figura-con-fondo.jpg.",
    "Aprieta E, borrador, y ponte a borrar el fondo. A prop\u00f3sito, mu\u00e9rdele un pedazo a la cabeza.",
    "Qu\u00e9date dos segundos viendo la mordida. Ctrl+Z.",
    "Ahora s\u00ed: con la capa seleccionada, clic en el bot\u00f3n de m\u00e1scara, abajo del panel "
    "(el rect\u00e1ngulo con el c\u00edrculo adentro).",
    "Se\u00f1ala el cuadrito blanco que apareci\u00f3 junto a la miniatura.",
    "Clic en ese cuadrito. Aprieta D, luego B.",
    "Pinta de negro sobre el fondo. Mu\u00e9rdele otra vez la cabeza a prop\u00f3sito.",
    "Aprieta X para cambiar a blanco. Pinta encima de la mordida y ens\u00e9\u00f1ala regresando.",
    "Shift+clic en la miniatura de la m\u00e1scara para apagarla: la foto completa sigue ah\u00ed. "
    "Otro Shift+clic para volver.",
    "Zoom con Alt+rueda al hueco entre el brazo y el cuerpo. Tapa ese hueco con pincel chico.",
    "\u00daltimo error: selecciona la CAPA en vez de la m\u00e1scara y pinta negro encima de la figura. Ctrl+Z.",
])
dices(doc, [
    "Ahora lo importante. Le quiero quitar el fondo a esta figura.",
    "Lo que hace uno la primera vez es agarrar el borrador. E, y a tallar. Lo voy a hacer para que "
    "veas por qu\u00e9 no conviene.",
    "\u2014 (tras morder la cabeza) \u2014  Le mord\u00ed la cabeza. Y lo malo no es eso: lo malo es que esos "
    "p\u00edxeles ya no est\u00e1n. Si guardo y cierro, los perd\u00ed.",
    "Control+Z.",
    "La forma correcta es una m\u00e1scara. Con la capa seleccionada, este bot\u00f3n de abajo del panel, "
    "el rect\u00e1ngulo con el c\u00edrculo. Y f\u00edjate que apareci\u00f3 un cuadrito blanco junto a la miniatura "
    "de la capa. Esa es la m\u00e1scara.",
    "Y toda la m\u00e1scara se resume en una frase: lo que pintas de negro se tapa, y lo que pintas "
    "de blanco se vuelve a ver.",
    "La m\u00e1scara no es la imagen. Es una instrucci\u00f3n de qu\u00e9 se muestra y qu\u00e9 no.",
    "Entonces: clic en el cuadrito de la m\u00e1scara. D, para poner los colores en negro y blanco. "
    "B, pincel. Y pinto de negro sobre el fondo.",
    "Se va. Pero mira, me pas\u00e9 y le mord\u00ed la cabeza otra vez.",
    "X, que cambia de negro a blanco. Pinto encima... y regresa.",
    "Y ah\u00ed est\u00e1 la diferencia. No lo recuper\u00e9 de ning\u00fan lado: nunca se fue. El borrador destruye; "
    "la m\u00e1scara tapa. Y tapar se puede deshacer siempre, hasta dentro de dos a\u00f1os cuando "
    "abras el archivo.",
    "Te lo compruebo: Shift con clic en la m\u00e1scara, y la apago. La imagen est\u00e1 completa. "
    "Siempre estuvo ah\u00ed.",
    "\u2014 (en el hueco del brazo) \u2014  Y aqu\u00ed est\u00e1 el \u00fanico lugar que cuesta en esta figura. "
    "La cabeza es f\u00e1cil, es una curva. Los pies son f\u00e1ciles. Lo que cuesta es este hueco "
    "entre el brazo y el cuerpo, porque ah\u00ed el fondo se mete dentro de la silueta.",
    "Si no lo tapas te queda un pedazo de fondo colgando, y eso es lo que delata un recorte "
    "mal hecho. Pincel chico, Alt con la rueda para acercarte, y con calma.",
    "Si te queda imperfecto hoy no pasa nada: en la clase tres esto se hace en dos clics.",
    "\u2014 (al pintar en la capa por error) \u2014  Acabo de pintar un brochazo negro encima de la figura. "
    "Ten\u00eda seleccionada la capa, no la m\u00e1scara.",
    "F\u00edjate en el borde blanco: el recuadro te dice en cu\u00e1l de las dos est\u00e1s parado. "
    "Antes de pintar en una m\u00e1scara, clic en la m\u00e1scara. Control+Z.",
])
nota(doc, "Si solo te acuerdas de una frase de esta clase al grabar, que sea \u201cnegro tapa, "
          "blanco muestra\u201d. D\u00edcela dos veces y d\u00e9jala en pantalla cinco segundos.")

doc.add_page_break()

# ===== PARTE 5 =====
parte(doc, 5, "Armar la ficha, capa por capa", "5 minutos")
haces(doc, [
    "Ctrl+N y usa el preajuste \u201cvertical redes\u201d de la clase 1. Ctrl+S como 02-ficha.psd.",
    "Capa nueva con Ctrl+Shift+N. Rell\u00e9nala con Alt+Supr. Nombra la capa \u201cfondo\u201d con doble clic.",
    "Abre Ventana \u203a Bibliotecas. Crea una biblioteca con el nombre de tu marca y arrastra el color ah\u00ed.",
    "Arrastra figura-con-fondo.jpg. Ctrl+T para acomodar. Enter.",
    "P\u00f3nle m\u00e1scara y tapa el fondo con negro, como en la parte 4.",
    "T, escribe el nombre de la figura. Ctrl+Enter.",
    "T otra vez, escribe el n\u00famero, chico, arriba a la izquierda. Ctrl+Enter.",
    "Arrastra el logo en PNG. B\u00e1jale la opacidad a 70.",
    "Selecciona las dos capas de texto y Ctrl+G. Nombra la carpeta \u201ctextos\u201d.",
    "Error a prop\u00f3sito: con la capa de texto seleccionada, intenta mover la figura. Se mueve el texto.",
    "Ctrl+S, y luego Ctrl+Shift+Alt+W para sacar el JPG.",
])
dices(doc, [
    "Vamos a armar la ficha. Son cinco capas, y cada una hace una cosa.",
    "Control+N, y aqu\u00ed uso el preajuste que guardamos en la clase uno. Control+S, cero dos ficha.",
    "Primero el fondo. Capa nueva con Control+Shift+N, y la relleno con Alt y Suprimir, "
    "que rellena del color que tengas al frente.",
    "Y le pongo nombre: doble clic, \u201cfondo\u201d. Cuando tengas veinte capas vas a agradecer esto.",
    "Un minuto para algo que te va a servir siempre: Ventana, Bibliotecas. Creas una biblioteca, "
    "le pones el nombre de tu marca, y guardas ah\u00ed tu color.",
    "A partir de ah\u00ed ese color est\u00e1 a un clic en todos tus archivos, en vez de que lo andes "
    "copiando a mano y que la quinta ficha te salga de otro tono.",
    "Ahora la figura. La arrastro, Control+T para acomodarla, Enter. Y le pongo su m\u00e1scara "
    "y le tapo el fondo, igual que hace rato.",
    "El nombre. T, escribo, Control+Enter para cerrar.",
    "Y el n\u00famero, en otra capa de texto. Chiquito, arriba.",
    "Dos textos, dos capas. Nunca los dos en la misma: si est\u00e1n juntos no puedes mover uno "
    "sin mover el otro.",
    "Y ese n\u00famero no es adorno. M\u00e1s adelante en el curso, cuando saquemos varias fichas de golpe "
    "desde una hoja de c\u00e1lculo, el nombre y el n\u00famero van a ser dos columnas de esa hoja. "
    "Hoy los ponemos a mano.",
    "El logo. Lo arrastro y le bajo la opacidad a setenta.",
    "Y agrupo los dos textos con Control+G, en una carpeta que diga \u201ctextos\u201d. "
    "Con cinco capas parece exagerado; m\u00e1s adelante vas a tener treinta.",
    "\u2014 (al mover el texto por error) \u2014  Capa equivocada, otra vez. Te va a pasar mil veces "
    "y siempre se arregla igual: mira el panel.",
    "Y guardamos los dos archivos. Control+S para el PSD, que es con el que puedes seguir editando. "
    "Y Control+Shift+Alt+W para el JPG, que es el que se sube.",
    "El PSD no se sube a ning\u00fan lado y no se borra nunca. Ese es tu original.",
])

# ===== PARTE 6 =====
parte(doc, 6, "Tres costumbres que valen oro", "90 segundos")
haces(doc, [
    "Ense\u00f1a una capa mal nombrada tipo \u201cCapa 14 copia 3 copia\u201d.",
    "Ctrl+J sobre una capa, y pinta sobre la copia para demostrar.",
    "Alt+clic en el ojo otra vez.",
])
dices(doc, [
    "Y antes de cerrar, tres costumbres que no te va a decir un tutorial de treinta segundos.",
    "La primera: ponle nombre a las capas. Cuesta tres segundos. \u201cCapa catorce copia tres copia\u201d "
    "es la raz\u00f3n por la que uno termina abandonando sus propios archivos.",
    "La segunda: duplica antes de arriesgar. Control+J, y experimentas en la copia. "
    "Si sale mal, borras la copia y no perdiste nada.",
    "Y la tercera, que ya la vimos pero la repito porque es la m\u00e1s \u00fatil: Alt con clic en el ojo "
    "para ver una capa sola.",
])

# ===== PARTE 7 =====
parte(doc, 7, "Cierre", "30 segundos")
haces(doc, ["Pantalla final apuntando a la Clase 3."])
dices(doc, [
    "Tu tarea: sube tu ficha a los comentarios, y dime cu\u00e1ntas capas usaste. "
    "Si usaste una sola, reg\u00e1late otra vez la parte de la m\u00e1scara.",
    "Si te sirvi\u00f3, suscr\u00edbete.",
    "Y en la clase tres vamos a quitar ese fondo en dos clics. Y lo vas a entender, "
    "porque hoy lo hiciste a mano. Ah\u00ed te veo.",
])

doc.add_page_break()
h2(doc, "Notas de producci\u00f3n")
parrafo(doc, "Todo lo de aqu\u00ed abajo es para ti. Nada se dice en c\u00e1mara.", 10)

h2(doc, "Los tres errores a prop\u00f3sito")
for t in ["Parte 2 \u2014 pintar en la capa equivocada y que no pase nada.",
          "Parte 4 \u2014 morder la cabeza con el borrador, y despu\u00e9s pintar en la capa en vez de en la m\u00e1scara.",
          "Parte 5 \u2014 mover el texto creyendo que mueves la figura."]:
    p = doc.add_paragraph(t, style='List Bullet'); p.paragraph_format.left_indent = Cm(0.8)

h2(doc, "Ficha")
parrafo(doc, "T\u00edtulo: Curso de Photoshop desde cero \u2014 Clase 2: capas y m\u00e1scaras explicadas de una vez")
parrafo(doc, "Entrega: 02-ficha.jpg \u2014 figura, nombre, n\u00famero y logo en capas separadas, "
             "con el fondo tapado con m\u00e1scara")
parrafo(doc, "Miniatura: texto \u201cNO BORRES\u201d. La misma figura dos veces: una mordida por el borrador, "
             "otra limpia. El borrador tachado.")

h2(doc, "Shorts que salen de esta grabaci\u00f3n")
for t in ["Parte 4, el borrador contra la m\u00e1scara \u2014 gancho: \u201cDeja de borrar / en Photoshop\u201d",
          "Parte 4, la regla \u2014 gancho: \u201cNegro tapa, blanco muestra / ya sabes m\u00e1scaras\u201d",
          "Parte 3, el Alt+clic en el ojo \u2014 gancho: \u201cAlt + clic en el ojo / nadie te dijo esto\u201d"]:
    p = doc.add_paragraph(t, style='List Bullet'); p.paragraph_format.left_indent = Cm(0.8)

h2(doc, "Cap\u00edtulos para la descripci\u00f3n de YouTube")
for t in ["00:00 Presentaci\u00f3n y lo que vas a tener al final", "00:30 Qu\u00e9 es una capa",
          "03:00 Los controles del panel de capas", "05:00 La m\u00e1scara: negro tapa, blanco muestra",
          "06:30 Por qu\u00e9 el borrador destruye y la m\u00e1scara no",
          "08:00 El hueco entre el brazo y el cuerpo",
          "09:00 Armamos la ficha, capa por capa",
          "10:00 Bibliotecas: tu color de marca a un clic",
          "13:00 Tres costumbres que te van a ahorrar horas"]:
    p = doc.add_paragraph(t); p.paragraph_format.left_indent = Cm(0.8); p.paragraph_format.space_after = Pt(2)

ruta = os.path.join(SALIDA, "Clase 02 - Capas y mascaras.docx")
doc.save(ruta)
print("DOCX:", ruta)
