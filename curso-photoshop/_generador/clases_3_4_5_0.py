# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Pt, Cm
from guion_docx import (base, pie, titulo, parte, haces, dices, nota, h2,
                        parrafo, casillas, GRIS, AZUL, NARANJA, sombrear)

SALIDA = r"C:\Users\RICHO\Desktop\Curso Photoshop\guiones"


def nuevo(tit, sub, piecito):
    doc = Document()
    base(doc)
    pie(doc, piecito)
    titulo(doc, tit, sub)
    h2(doc, "C\u00f3mo se lee este gui\u00f3n")
    for etiqueta, resto, color in [
        ("LO QUE HACES EN PANTALLA", " \u2014 los clics, en orden. Es lo que se ve en pantalla.", NARANJA),
        ("LO QUE DICES", " \u2014 el texto hablado. Lo puedes leer tal cual o decirlo con tus palabras, "
                         "pero el orden no se cambia.", AZUL),
        ("NOTA PARA TI", " \u2014 recordatorio m\u00edo. Esto nunca se dice en voz alta.", GRIS),
    ]:
        pp = doc.add_paragraph()
        pp.paragraph_format.left_indent = Cm(0.6)
        pp.paragraph_format.space_after = Pt(4)
        r = pp.add_run(etiqueta); r.bold = True; r.font.size = Pt(10.5); r.font.color.rgb = color
        r2 = pp.add_run(resto); r2.font.size = Pt(10.5)
    return doc


def idea(doc, texto):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    sombrear(p, 'FFF4E5')
    r = p.add_run("  La idea de esta clase:  ")
    r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NARANJA
    r2 = p.add_run(texto + "  ")
    r2.font.size = Pt(11); r2.bold = True


def guardar(doc, nombre):
    ruta = os.path.join(SALIDA, nombre)
    doc.save(ruta)
    print("DOCX:", ruta)


# ==================================================================== CLASE 3
doc = nuevo("CLASE 3", "Selecciones: quitar el fondo  \u00b7  dura unos 14 minutos",
            "Curso de Photoshop desde cero  \u00b7  Clase 3  \u00b7  Selecciones")

h2(doc, "De qu\u00e9 va esta clase")
parrafo(doc, "Esta es la clase por la que te va a encontrar gente que no te conoce. \u201cC\u00f3mo quitar el "
             "fondo\u201d es de lo m\u00e1s buscado de Photoshop, as\u00ed que el t\u00edtulo y la miniatura de esta "
             "clase trabajan para el buscador, no para quien ya est\u00e1 siguiendo el curso.")
idea(doc, "seleccionar es decirle a Photoshop d\u00f3nde puede trabajar.")

h2(doc, "Antes de darle Rec")
casillas(doc, [
    "material\\figura-con-fondo.jpg: la figura con su fondo, el mismo archivo de la clase 2",
    "El PNG terminado guardado en plantillas\\, por si hay que repetir la toma",
    "Prueba antes de grabar que Seleccionar sujeto corra r\u00e1pido. Si tarda, lo dices en c\u00e1mara "
    "en vez de esperar callado",
    "Keyviz prendido, OBS grabando",
])

doc.add_page_break()

parte(doc, 1, "Presentaci\u00f3n y la promesa", "30 segundos")
haces(doc, [
    "Ten la figura con su fondo abierta.",
    "Dale a Seleccionar sujeto y ponle la m\u00e1scara, para que se vea quedar sola sobre el "
    "cuadriculado gris de la transparencia. Dos clics, delante de la c\u00e1mara.",
])
dices(doc, [
    "Qu\u00e9 tal, soy Richie, y seguimos con el curso de Photoshop desde cero.",
    "Hoy vamos a quitarle el fondo a la figura. Y lo vamos a hacer en dos clics, as\u00ed.",
    "Pero lo importante de esta clase no son los dos clics: es qu\u00e9 haces cuando los dos clics "
    "no alcanzan. Que pasa seguido, y es lo que casi ning\u00fan tutorial te ense\u00f1a.",
    "Al final vas a tener tu figura recortada, en PNG, con el fondo transparente.",
])

parte(doc, 2, "Qu\u00e9 es una selecci\u00f3n", "90 segundos")
haces(doc, [
    "Aprieta M y haz un rect\u00e1ngulo de selecci\u00f3n en medio del lienzo.",
    "Aprieta B y ponte a pintar por todos lados, dentro y fuera. Solo pinta adentro.",
    "Se\u00f1ala la l\u00ednea punteada que camina.",
    "Error a prop\u00f3sito: deja la selecci\u00f3n activa, cambia de zona e intenta pintar fuera. "
    "No pasa nada. Qu\u00e9date tres segundos insistiendo.",
    "Ctrl+D para deseleccionar, y ahora s\u00ed pinta.",
])
dices(doc, [
    "Una selecci\u00f3n no recorta nada. Una selecci\u00f3n le dice a Photoshop: de aqu\u00ed para dentro s\u00ed, "
    "de aqu\u00ed para fuera no.",
    "M\u00edralo: selecciono este cuadro, agarro el pincel, y pinto por todos lados. "
    "La pintura solo cae adentro. Lo de afuera est\u00e1 protegido.",
    "Esa l\u00ednea punteada que camina es el borde de la selecci\u00f3n. No es un dibujo, no se imprime, "
    "no existe en el archivo. Es un permiso.",
    "Y de ah\u00ed sale lo que vamos a hacer hoy: seleccionas, y de la selecci\u00f3n sacas una m\u00e1scara. "
    "La m\u00e1scara ya la vimos en la clase dos; hoy vemos c\u00f3mo conseguirla sin pintarla a mano.",
    "\u2014 (al no poder pintar) \u2014  Y este es el problema n\u00famero uno de todo Photoshop. "
    "Traigo una selecci\u00f3n activa de hace rato y no me acuerdo. Pinto, y no pasa nada.",
    "Control+D, deseleccionar. Ap\u00fantate esto: cuando Photoshop deje de obedecerte sin raz\u00f3n, "
    "Control+D primero, y despu\u00e9s te preguntas qu\u00e9 pas\u00f3.",
])

parte(doc, 3, "Las cuatro herramientas y cu\u00e1ndo usar cada una", "90 segundos")
haces(doc, [
    "Pon en pantalla la tarjeta con las cuatro. D\u00e9jala quieta 6 segundos al final.",
    "Aprieta cada tecla al nombrarla.",
])
dices(doc, [
    "Para seleccionar hay cuatro herramientas, y escoger la correcta te ahorra la mitad del trabajo.",
    "El marco, con M. Para cuadrados y c\u00edrculos. Sirve poco con cosas que tienen forma.",
    "El lazo, con L. A mano alzada. Sirve para arreglos r\u00e1pidos, no para precisi\u00f3n, "
    "porque te tiembla el pulso.",
    "La varita m\u00e1gica. Sirve cuando el fondo es de un solo color parejo.",
    "Y la selecci\u00f3n r\u00e1pida, con Seleccionar sujeto. Sirve para casi todo lo dem\u00e1s.",
    "Y el truco para escoger es al rev\u00e9s de como lo explican normalmente: mira el fondo, "
    "no el objeto.",
    "Si el fondo es parejo, selecciona el fondo con la varita y despu\u00e9s lo volteas. "
    "Si el fondo es un desorden, selecciona el objeto con Seleccionar sujeto. "
    "Es la misma decisi\u00f3n siempre, y te toma dos segundos.",
])

parte(doc, 4, "Seleccionar sujeto, y lo que siempre se le olvida", "2 minutos y medio")
haces(doc, [
    "Aprieta W y dale al bot\u00f3n Seleccionar sujeto de la barra de opciones.",
    "Alt+rueda para acercarte al hueco entre el brazo y el cuerpo. Ah\u00ed se ve que dej\u00f3 fondo adentro.",
    "Error a prop\u00f3sito: aprieta Shift y arrastra para quitar ese pedazo. Como Shift suma, "
    "se te mete media imagen. Ctrl+Z.",
    "Ahora con Alt arrastrado: resta. Quita el hueco bien.",
    "Revisa tambi\u00e9n los pies y la sombra. Quita la sombra de la selecci\u00f3n.",
])
dices(doc, [
    "Esta figura tiene el fondo complicado, as\u00ed que vamos con Seleccionar sujeto.",
    "W, y aqu\u00ed arriba en la barra de opciones: Seleccionar sujeto. Un clic.",
    "Esto corre un modelo entrenado para encontrar el objeto de la imagen, y con una figura as\u00ed "
    "le atina casi perfecto, porque es justo lo que espera encontrar: un objeto con silueta "
    "clara en el centro.",
    "Pero ahora acerqu\u00e9monos, porque aqu\u00ed est\u00e1 lo que no te ense\u00f1an.",
    "Se le olvid\u00f3 el hueco. Dej\u00f3 el pedazo de fondo que se mete entre el brazo y el cuerpo. "
    "Esto pasa siempre, con cualquier figura que tenga el brazo despegado del cuerpo.",
    "Se arregla con dos teclas, y estas dos las vas a usar toda la vida: Shift suma a la selecci\u00f3n, "
    "y Alt resta.",
    "\u2014 (tras sumar por error) \u2014  Le di Shift y ahora tengo fondo adentro. Control+Z. "
    "Shift suma, Alt resta. Lo voy a estar repitiendo todo el curso.",
    "Con Alt, quito el hueco.",
    "Y revisa los pies y la sombra. La sombra no es la figura: si la dejas dentro de la selecci\u00f3n, "
    "despu\u00e9s no puedes poner la figura sobre otro fondo. La sombra la vamos a hacer de nuevo, "
    "y mejor, m\u00e1s adelante en el curso.",
])

doc.add_page_break()

parte(doc, 5, "El paso que casi nadie da", "3 minutos")
haces(doc, [
    "Con la selecci\u00f3n activa, Ctrl+Alt+R: se abre Seleccionar y aplicar m\u00e1scara.",
    "Arriba a la derecha, cambia el modo de vista a Sobre negro.",
    "Alt+rueda al borde de la cabeza: se ve una l\u00ednea clara alrededor.",
    "Suavizar: 2 o 3.",
    "Desplazar borde: hacia dentro, entre \u22121 y \u22123.",
    "Enciende Descontaminar colores. Su\u00e9bele a 50.",
    "Apaga y prende esa casilla tres veces, despacio, con zoom al borde.",
    "Salida: Nueva capa con m\u00e1scara de capa. Aceptar.",
    "Se\u00f1ala en el panel: la capa original qued\u00f3 apagada e intacta, y arriba hay una nueva con m\u00e1scara.",
    "Selecci\u00f3n \u203a Guardar selecci\u00f3n. Le pones nombre. Luego abre Ventana \u203a Canales y ens\u00e9\u00f1ala ah\u00ed.",
])
dices(doc, [
    "Y ahora el minuto m\u00e1s importante de la clase. Casi todos los tutoriales se acaban en el paso "
    "anterior, y por eso casi todos los recortes de internet se ven recortados.",
    "Control+Alt+R. Se abre un espacio aparte que se llama Seleccionar y aplicar m\u00e1scara. "
    "Tiene como veinte controles y vamos a usar cuatro.",
    "Primero, para poder ver lo que estamos haciendo: aqu\u00ed arriba cambiamos el modo de vista "
    "a Sobre negro.",
    "Y ahora s\u00ed se ven los problemas. Mira esa l\u00ednea clara alrededor de toda la figura. "
    "Ese es el fondo de la imagen original, que se qued\u00f3 pegado en la orilla. Y eso es exactamente "
    "lo que hace que un recorte se vea pegado con tijeras.",
    "Suavizar le quita los escaloncitos al borde. Dos o tres es suficiente.",
    "Desplazar borde mete o saca la orilla. La metemos un poquito hacia dentro, uno o dos.",
    "Y este es el que nadie usa: Descontaminar colores. No mueve el borde. Lo que hace es quitarle "
    "el color del fondo viejo a los p\u00edxeles de la orilla y reemplazarlo por el color de la figura.",
    "M\u00edralo. Prendido. Apagado. Prendido.",
    "Esa es la diferencia entre un recorte que se nota y uno que no. Y son dos segundos.",
    "F\u00edjate que al prenderlo me cambi\u00f3 la salida de abajo a \u201cnueva capa con m\u00e1scara\u201d. "
    "Es a prop\u00f3sito: descontaminar necesita pintar p\u00edxeles nuevos.",
    "Aceptamos. Y mira lo que nos dio: la capa original intacta y apagada, y arriba una capa nueva "
    "con su m\u00e1scara. No se destruy\u00f3 nada. Es la misma l\u00f3gica de la clase dos.",
    "Y un paso de treinta segundos que vale la pena: si este recorte te cost\u00f3 trabajo, gu\u00e1rdalo. "
    "Selecci\u00f3n, Guardar selecci\u00f3n, le pones nombre.",
    "Se queda metido en el archivo, aqu\u00ed en Ventana, Canales. Y dentro de seis meses lo recuperas "
    "con Cargar selecci\u00f3n en vez de volver a recortar.",
])

parte(doc, 6, "Exportar, y el error del JPG", "90 segundos")
haces(doc, [
    "Ctrl+Shift+Alt+W.",
    "Formato: PNG. Gu\u00e1rdalo como 03-figura-recortada.png.",
    "Despu\u00e9s ens\u00e9\u00f1alo: exp\u00f3rtalo tambi\u00e9n en JPG y abre el archivo para que se vea el "
    "fondo blanco que apareci\u00f3.",
])
dices(doc, [
    "Control+Shift+Alt+W para exportar. Y aqu\u00ed hay una cosa que no tiene que ver con seleccionar, "
    "pero es de lo m\u00e1s importante de esta clase.",
    "El JPG no sabe hacer transparencia. No puede.",
    "Si exportas esto en JPG, el fondo transparente te va a salir blanco, y acabas de perder "
    "todo el trabajo. Te lo ense\u00f1o.",
    "\u2014 (ense\u00f1ando el JPG) \u2014  Ah\u00ed est\u00e1. Fondo blanco.",
    "Para algo recortado: PNG. Siempre. Si alguna vez subes un recorte y te sale con un cuadro "
    "blanco atr\u00e1s, es esto, y ya sabes por qu\u00e9.",
    "Pesa m\u00e1s que un JPG, y vale la pena.",
])

parte(doc, 7, "Lo que no se puede, y qu\u00e9 hacer entonces", "90 segundos")
haces(doc, ["Pon la tarjeta con los tres casos. D\u00e9jala 6 segundos."])
dices(doc, [
    "Y para que no pierdas una tarde: hay tres cosas que ninguna de estas herramientas resuelve "
    "bien de un clic.",
    "Pelo, pelusa y flecos, porque son miles de bordes medio transparentes. Eso se ve m\u00e1s adelante, "
    "con otra herramienta.",
    "Pl\u00e1stico transparente, como la ventana de una caja, porque el fondo se ve a trav\u00e9s del objeto.",
    "Y la tercera, que es la m\u00e1s com\u00fan: cuando el objeto es del mismo color que el fondo. "
    "Ah\u00ed no hay contraste de d\u00f3nde agarrarse.",
    "Y esa tercera no se arregla con una herramienta: se arregla antes de tomar la foto. "
    "Si pones la figura sobre una cartulina de un color que la figura no tenga, el recorte te toma "
    "dos clics en vez de veinte minutos.",
    "Y un adelanto: todo esto que acabamos de hacer a mano, m\u00e1s adelante en el curso lo vas a grabar "
    "como una acci\u00f3n, y se lo vas a aplicar a veinte im\u00e1genes de un jal\u00f3n. "
    "Hoy aprendes el movimiento; despu\u00e9s deja de ser tu trabajo.",
])

parte(doc, 8, "Cierre", "30 segundos")
haces(doc, ["Pantalla final apuntando a la Clase 4."])
dices(doc, [
    "Tu tarea: sube tu PNG recortado a los comentarios. Y si te sale con el cuadro blanco atr\u00e1s, "
    "ya sabes qu\u00e9 pas\u00f3.",
    "Suscr\u00edbete, y en la clase cuatro vemos transformar sin deformar: por qu\u00e9 la figura se ve "
    "apachurrada, por qu\u00e9 se pixelea al agrandarla, y el clic derecho que arregla las dos cosas. "
    "Ah\u00ed te veo.",
])

doc.add_page_break()
h2(doc, "Notas de producci\u00f3n")
parrafo(doc, "Todo lo de aqu\u00ed abajo es para ti. Nada se dice en c\u00e1mara.", 10)
h2(doc, "Ficha")
parrafo(doc, "T\u00edtulo: Curso de Photoshop desde cero \u2014 Clase 3: quitar el fondo de verdad "
             "(y lo que Seleccionar sujeto siempre falla)")
parrafo(doc, "Entrega: 03-figura-recortada.png, con fondo transparente y el borde limpio")
parrafo(doc, "Miniatura: texto \u201c2 CLICS\u201d. A la izquierda la figura con su fondo; a la derecha, "
             "sola sobre el cuadriculado gris de la transparencia.")
h2(doc, "Shorts que salen de esta grabaci\u00f3n")
for t in ["Parte 5, el Descontaminar colores \u2014 gancho: \u201cEsta casilla arregla / tu recorte en 2 segundos\u201d",
          "Parte 4, el hueco del brazo \u2014 gancho: \u201cSeleccionar sujeto / siempre olvida esto\u201d",
          "Parte 6, el JPG \u2014 gancho: \u201cTu recorte sale con / fondo blanco por esto\u201d"]:
    p = doc.add_paragraph(t, style='List Bullet'); p.paragraph_format.left_indent = Cm(0.8)
h2(doc, "Cap\u00edtulos para la descripci\u00f3n de YouTube")
for t in ["00:00 Presentaci\u00f3n", "00:30 Qu\u00e9 es una selecci\u00f3n (y el \u201cno me sale\u201d n\u00famero 1)",
          "02:00 Las 4 herramientas y cu\u00e1ndo usar cada una",
          "03:30 Seleccionar sujeto, y el hueco que siempre se le olvida",
          "06:00 Seleccionar y aplicar m\u00e1scara: los 4 controles que importan",
          "07:30 Descontaminar colores: el paso que casi nadie da",
          "08:30 Guardar la selecci\u00f3n para no volver a recortar",
          "09:00 Por qu\u00e9 tu recorte sale con fondo blanco (JPG vs PNG)",
          "11:00 Lo que no se puede recortar, y qu\u00e9 hacer entonces"]:
    p = doc.add_paragraph(t); p.paragraph_format.left_indent = Cm(0.8); p.paragraph_format.space_after = Pt(2)
guardar(doc, "Clase 03 - Selecciones.docx")


# ==================================================================== CLASE 4
doc = nuevo("CLASE 4", "Transformar sin deformar, y objetos inteligentes  \u00b7  dura unos 12 minutos",
            "Curso de Photoshop desde cero  \u00b7  Clase 4  \u00b7  Transformar")

h2(doc, "De qu\u00e9 va esta clase")
parrafo(doc, "Clase corta y mec\u00e1nica, y la que m\u00e1s verg\u00fcenzas evita. Deformar algo es lo que "
             "m\u00e1s delata a alguien que va empezando, porque el ojo detecta una proporci\u00f3n mal "
             "antes de poder explicar qu\u00e9 tiene.")
idea(doc, "reducir es gratis, agrandar se paga \u2014 y un objeto inteligente no paga ninguno de los dos.")

h2(doc, "Antes de darle Rec")
casillas(doc, [
    "03-figura-recortada.png, el PNG de la clase 3. Si esa toma no sali\u00f3, hay copia en plantillas\\",
    "Una segunda imagen de la figura lista, para el truco de Reemplazar contenido de la parte 5",
    "Decidido de antemano qu\u00e9 tres tama\u00f1os: 100%, 60% y 35%. No se piensa en c\u00e1mara",
    "Keyviz prendido, OBS grabando",
])

doc.add_page_break()

parte(doc, 1, "Presentaci\u00f3n", "25 segundos")
haces(doc, [
    "Ense\u00f1a la imagen terminada: las tres figuras alineadas, las tres con la cabeza redonda.",
    "Corta a una versi\u00f3n apachurrada, dos segundos, y regresa a la buena.",
])
dices(doc, [
    "Qu\u00e9 tal, soy Richie, seguimos con el curso de Photoshop desde cero.",
    "Hoy vamos a ver transformar: hacer algo m\u00e1s grande, m\u00e1s chico o girarlo. "
    "Suena simple y tiene dos trampas, y las dos se ven feo.",
    "Al final de este video vas a tener esta imagen con tu figura en tres tama\u00f1os, "
    "y no vas a volver a deformar ni a pixelear nada.",
])

parte(doc, 2, "Control+T y los ocho cuadritos", "90 segundos")
haces(doc, [
    "Abre el PNG de la clase 3. Ctrl+T.",
    "Se\u00f1ala los ocho cuadritos: cuatro en las esquinas, cuatro en los lados.",
    "Jala de una esquina (mantiene proporci\u00f3n). Esc.",
    "Jala de un lado (deforma). Esc.",
    "Ponte fuera del recuadro para girar. Esc.",
    "Se\u00f1ala la cadenita entre el ancho y el alto, en la barra de opciones.",
])
dices(doc, [
    "Control+T, transformar. Aparece un recuadro con ocho cuadritos: cuatro en las esquinas "
    "y cuatro en los lados. Esos ocho son toda la clase.",
    "Si jalas de una esquina, cambia de tama\u00f1o manteniendo la proporci\u00f3n.",
    "Si jalas de un lado, cambia solo el ancho o solo el alto. Eso deforma.",
    "Si te sales del recuadro, gira.",
    "Y con Alt apretado, escala desde el centro en vez de desde la esquina de enfrente.",
    "Tres teclas para terminar: Enter aplica, Esc cancela, y Control+Z deshace si ya aplicaste "
    "y no te gust\u00f3.",
    "Y f\u00edjate aqu\u00ed arriba en la barra de opciones: entre el ancho y el alto hay una cadenita. "
    "Con la cadena cerrada no se deforma, jales de donde jales. Si algo te sale deformado alguna vez, "
    "lo primero que revisas es esa cadena.",
])

parte(doc, 3, "La primera trampa: deformar", "2 minutos")
haces(doc, [
    "Ctrl+T y jala del cuadrito del lado hasta dejar la figura estirada de ancho.",
    "Qu\u00e9date ah\u00ed cinco segundos. Los primeros dos, callado.",
    "Aplica con Enter. Haz dos cosas m\u00e1s encima (mueve, agrega texto).",
    "Intenta arreglarlo con Ctrl+Z y ense\u00f1a que ya no alcanza c\u00f3modamente.",
    "Deshaz bien y hazlo de nuevo desde la esquina.",
])
dices(doc, [
    "M\u00edrala. \u00bfQu\u00e9 tiene de malo?",
    "Te apuesto que lo viste antes de que yo dijera nada, y que no sabr\u00edas explicar qu\u00e9 exactamente.",
    "Lo que tiene es que la cabeza ya no es redonda. Est\u00e1 de huevo.",
    "Y en una figura as\u00ed se nota mucho, porque la cabeza es m\u00e1s grande que el cuerpo. "
    "Esa proporci\u00f3n es la forma del mu\u00f1eco: si la cambias, deja de verse como lo que es.",
    "Y esto no pasa solo con figuras. Pasa igual con una cara, con un logo, con un envase. "
    "Todos tienen una proporci\u00f3n que la gente reconoce sin pensarlo.",
    "\u2014 (tras aplicar y seguir trabajando) \u2014  Y ya la apliqu\u00e9. Si sigo trabajando y a los diez "
    "minutos me doy cuenta, los Control+Z ya no me alcanzan.",
    "As\u00ed que te dejo una costumbre: antes de darle Enter a cualquier transformaci\u00f3n, "
    "una pregunta. \u00bfSigue siendo redondo lo que era redondo?",
    "Busca el c\u00edrculo de la imagen \u2014una cabeza, una rueda, un logo, un ojo\u2014 y m\u00edralo. "
    "Si est\u00e1 de huevo, est\u00e1 mal. Tres segundos, y te ahorra el rid\u00edculo.",
])

parte(doc, 4, "La segunda trampa: pixelear", "2 minutos")
haces(doc, [
    "Ctrl+T, reduce la figura al 35%. Enter.",
    "Ctrl+T otra vez, s\u00fabela de vuelta al 100%. Enter.",
    "Alt+rueda para acercarte: se ve borrosa y con la orilla sucia.",
])
dices(doc, [
    "Segunda trampa, y esta casi nadie te la explica.",
    "Acabo de reducir esta figura al treinta y cinco por ciento. Ahora la vuelvo a subir al cien.",
    "Y m\u00edrala. Est\u00e1 borrosa y tiene la orilla sucia.",
    "La raz\u00f3n es esta: cuando reduces, Photoshop tira p\u00edxeles, y tirar es f\u00e1cil. "
    "Cuando agrandas, tiene que inventar p\u00edxeles que nunca existieron, y los inventa promediando "
    "los de al lado. De ah\u00ed la borrosidad. No es que lo haga mal: es que no hay informaci\u00f3n "
    "que poner.",
    "La regla pr\u00e1ctica: nunca agrandes una imagen m\u00e1s de lo que mide. Si tu archivo es de mil "
    "p\u00edxeles de ancho y lo necesitas de dos mil, no lo agrandes: consigue el archivo grande. "
    "Y si de plano no hay otra, no pases del ciento diez por ciento.",
    "Y de ah\u00ed sale la costumbre m\u00e1s \u00fatil de todo este curso: trabaja siempre con el archivo "
    "m\u00e1s grande que tengas, y red\u00facelo. Nunca al rev\u00e9s.",
])

doc.add_page_break()

parte(doc, 5, "La soluci\u00f3n a las dos: objeto inteligente", "2 minutos y medio")
haces(doc, [
    "Clic derecho en la capa \u203a Convertir en objeto inteligente.",
    "Se\u00f1ala el cuadrito que le apareci\u00f3 a la miniatura.",
    "Ctrl+T, red\u00facela al 20%. Enter. Ctrl+T, s\u00fabela al 100%. Enter. Acerca el zoom: sigue n\u00edtida.",
    "Doble clic en la miniatura: se abre en su propia pesta\u00f1a. Cambia algo, Ctrl+S, cierra. "
    "Se actualiz\u00f3 en el documento.",
    "Clic derecho \u203a Reemplazar contenido. Escoge la segunda imagen de la figura.",
    "Se\u00f1ala que entr\u00f3 del mismo tama\u00f1o y en la misma posici\u00f3n, sin acomodar nada.",
])
dices(doc, [
    "Y ahora el truco que hace que las dos trampas dejen de importar.",
    "Clic derecho en la capa, Convertir en objeto inteligente. F\u00edjate que la miniatura cambi\u00f3: "
    "le apareci\u00f3 un cuadrito en la esquina.",
    "Lo que acabo de hacer es meter la imagen en una cajita. Lo que ves es una vista previa; "
    "el original est\u00e1 guardado completo adentro.",
    "Y por eso ahora puedo hacer esto: la reduzco al veinte, la aplico, y la vuelvo a subir al cien.",
    "Y est\u00e1 n\u00edtida. Porque no estaba escalando p\u00edxeles: estaba cambiando el tama\u00f1o de la vista "
    "previa. El original de adentro nunca se toc\u00f3.",
    "Dicho de otra forma: un objeto inteligente se puede escalar mil veces sin perder nada. "
    "Una capa normal, no.",
    "Y hace otras dos cosas que casi nadie usa.",
    "La primera: doble clic en la miniatura, y el original se abre en su propia pesta\u00f1a. "
    "Lo cambias, Control+S, cierras, y el documento de afuera se actualiza solo.",
    "Y la segunda, que es la buena: clic derecho, Reemplazar contenido. Le doy otra imagen...",
    "Y mira: entr\u00f3 del mismo tama\u00f1o, en la misma posici\u00f3n, con los mismos efectos que ten\u00eda "
    "la anterior. No acomod\u00e9 nada.",
    "Piensa en lo que eso significa cuando tengas una plantilla de caja con la figura en cuatro caras: "
    "cambias la imagen una vez y se actualizan las cuatro. Eso lo vemos m\u00e1s adelante en el curso. "
    "Por ahora qu\u00e9date con el clic derecho.",
    "Lo \u00fanico que cuestan: pesan m\u00e1s, y hay filtros que no se les pueden aplicar directo. "
    "Cuando topes con eso, clic derecho, Rasterizar. Pero rasteriza una copia, no el original.",
])

parte(doc, 6, "Armar la imagen de los tres tama\u00f1os", "2 minutos y medio")
haces(doc, [
    "Ctrl+N: 2000 x 1200 px, 72 ppp, RGB, fondo blanco. Ctrl+S como 04-tres-tamanos.psd.",
    "Arrastra el PNG. Enter. Clic derecho \u203a Convertir en objeto inteligente.",
    "Ctrl+J dos veces: tres capas.",
    "En la segunda: Ctrl+T y ESCRIBE 60% en el ancho y el alto, con la cadenita cerrada. Enter.",
    "En la tercera: 35%, igual.",
    "V, y acomoda las tres apoyadas en la misma l\u00ednea de abajo.",
    "Error a prop\u00f3sito: alin\u00e9alas primero por el centro, mira dos segundos, y rehazlo por la base.",
    "Usa las gu\u00edas rosas para que los espacios queden iguales.",
    "T, una etiqueta debajo de cada una con el tama\u00f1o en cent\u00edmetros.",
    "Ctrl+S y Ctrl+Shift+Alt+W como 04-tres-tamanos.jpg, calidad 80.",
])
dices(doc, [
    "Vamos a armar la imagen de los tres tama\u00f1os, que es lo que usar\u00edas para ense\u00f1ar las medidas "
    "de algo que vendes.",
    "Documento nuevo, dos mil por mil doscientos. Lo guardo.",
    "Meto el PNG, y lo primero: clic derecho, convertir en objeto inteligente. Siempre primero esto.",
    "Control+J dos veces, para tener tres capas con la misma figura.",
    "Y ahora, en vez de jalar con el rat\u00f3n, voy a escribir el n\u00famero. Control+T, y aqu\u00ed arriba "
    "escribo sesenta por ciento, con la cadenita cerrada. Enter.",
    "Escribir el n\u00famero es m\u00e1s preciso que jalar, y te deja repetirlo exacto. "
    "Y acu\u00e9rdate de esto: m\u00e1s adelante en el curso vamos a grabar estos pasos como una acci\u00f3n, "
    "y una acci\u00f3n graba el n\u00famero, no el movimiento del rat\u00f3n. Trabajar con n\u00fameros es "
    "lo que hace que tu trabajo se pueda automatizar despu\u00e9s.",
    "La tercera, al treinta y cinco.",
    "Y las acomodo apoyadas en la misma l\u00ednea de abajo.",
    "\u2014 (tras alinearlas por el centro) \u2014  As\u00ed no. Alineadas por el centro se ven flotando. "
    "Son objetos que se paran en una mesa, as\u00ed que coinciden por abajo.",
    "Y cuando los espacios entre las tres son iguales, Photoshop te ense\u00f1a unas flechitas rosas. "
    "Ah\u00ed suelto.",
    "Una etiqueta abajo de cada una con el tama\u00f1o en cent\u00edmetros, y exportamos.",
])

parte(doc, 7, "Las otras transformaciones y dos atajos de regalo", "90 segundos")
haces(doc, [
    "Abre el men\u00fa Edici\u00f3n \u203a Transformar y rec\u00f3rrelo.",
    "Haz Voltear horizontal sobre el grupo que tiene el texto: el nombre queda al rev\u00e9s. Ctrl+Z.",
    "Demuestra Ctrl+Shift+T repitiendo un giro.",
    "Demuestra Ctrl+Shift+Alt+T apret\u00e1ndolo varias veces seguidas para armar un abanico de copias.",
])
dices(doc, [
    "En el men\u00fa Edici\u00f3n, Transformar, est\u00e1n las dem\u00e1s.",
    "Voltear horizontal, para que la figura mire al otro lado. Rotar noventa grados, para cuando "
    "la foto del celular sale acostada.",
    "Y estas tres \u2014Distorsionar, Perspectiva y Deformar\u2014 son las que se usan para meter un dise\u00f1o "
    "plano sobre una superficie en \u00e1ngulo o con curva. Eso es lo que vamos a usar m\u00e1s adelante "
    "para ense\u00f1ar la caja sin haberla impreso.",
    "\u2014 (tras voltear el grupo) \u2014  Volte\u00e9 y se me volte\u00f3 el nombre tambi\u00e9n, porque volte\u00e9 el grupo "
    "y no la capa de la figura. Ojo con voltear cualquier cosa que tenga letras o un logo encima: "
    "el espejo se nota siempre.",
    "Y dos atajos de regalo. Control+Shift+T repite la \u00faltima transformaci\u00f3n tal cual en otra capa. "
    "Si acabas de girar algo doce grados y quieres girar otra cosa exactamente doce grados, es ese.",
    "Y Control+Shift+Alt+T duplica la capa y le aplica la transformaci\u00f3n otra vez, de un golpe. "
    "Si lo aprietas diez veces seguidas despu\u00e9s de haber girado algo, te armas un abanico de copias. "
    "Para rejillas y patrones, eso son treinta segundos en lugar de veinte minutos.",
])

parte(doc, 8, "Cierre", "25 segundos")
haces(doc, ["Pantalla final apuntando a la Clase 5."])
dices(doc, [
    "Tu tarea: sube tu imagen de tres tama\u00f1os. Y antes de subirla, m\u00edrale la cabeza: "
    "\u00bfsigue siendo redonda?",
    "Suscr\u00edbete, que en la clase cinco viene el error n\u00famero uno de todo Photoshop: "
    "la diferencia entre tama\u00f1o de imagen y tama\u00f1o de lienzo. Se confunden todo el tiempo, "
    "y confundirlos arruina m\u00e1s archivos que cualquier otra cosa. Ah\u00ed te veo.",
])

doc.add_page_break()
h2(doc, "Notas de producci\u00f3n")
parrafo(doc, "Todo lo de aqu\u00ed abajo es para ti. Nada se dice en c\u00e1mara.", 10)
h2(doc, "Ficha")
parrafo(doc, "T\u00edtulo: Curso de Photoshop desde cero \u2014 Clase 4: transformar sin deformar (y sin pixelear)")
parrafo(doc, "Entrega: 04-tres-tamanos.jpg \u2014 la misma figura en 3 tama\u00f1os, alineada, n\u00edtida")
parrafo(doc, "Miniatura: texto \u201cNO LA APACHURRES\u201d. La figura bien a la izquierda y apachurrada "
             "a la derecha, con una tacha.")
h2(doc, "Shorts que salen de esta grabaci\u00f3n")
for t in ["Parte 5, Reemplazar contenido \u2014 gancho: \u201cClic derecho, Reemplazar / y entra solo en su lugar\u201d",
          "Parte 3, la cabeza apachurrada \u2014 gancho: \u201c\u00bfVes qu\u00e9 tiene de malo? / la cabeza no es redonda\u201d",
          "Parte 7, el Ctrl+Shift+Alt+T \u2014 gancho: \u201cEl atajo que nadie usa / duplica y repite\u201d"]:
    p = doc.add_paragraph(t, style='List Bullet'); p.paragraph_format.left_indent = Cm(0.8)
guardar(doc, "Clase 04 - Transformar.docx")


# ==================================================================== CLASE 5
doc = nuevo("CLASE 5", "Tama\u00f1o de imagen contra tama\u00f1o de lienzo  \u00b7  dura unos 11 minutos",
            "Curso de Photoshop desde cero  \u00b7  Clase 5  \u00b7  Imagen contra lienzo")

h2(doc, "De qu\u00e9 va esta clase")
parrafo(doc, "Estos dos cuadros de di\u00e1logo se parecen, est\u00e1n uno debajo del otro en el men\u00fa, "
             "y confundirlos arruina m\u00e1s archivos que cualquier otra cosa. No es un error de "
             "principiante: hay gente con a\u00f1os encima que los sigue confundiendo.")
idea(doc, "el tama\u00f1o de imagen estira el contenido; el tama\u00f1o de lienzo cambia la hoja.")

h2(doc, "Antes de darle Rec")
casillas(doc, [
    "03-figura-recortada.png a la mano",
    "La cuenta ya hecha: 10 cm a 300 ppp son 1181 p\u00edxeles. No se calcula en c\u00e1mara",
    "Los dos JPG terminados en plantillas\\",
    "Keyviz prendido, OBS grabando",
])

doc.add_page_break()

parte(doc, 1, "Presentaci\u00f3n", "25 segundos")
haces(doc, [
    "Ense\u00f1a una imagen cuadrada con la figura.",
    "Corta a la versi\u00f3n vertical bien hecha.",
    "Corta a la versi\u00f3n vertical mal hecha: estirada, cabeza de huevo, pies cortados.",
])
dices(doc, [
    "Qu\u00e9 tal, soy Richie, y seguimos con el curso de Photoshop desde cero.",
    "Hoy vamos a ver dos cuadros de di\u00e1logo que se parecen, est\u00e1n uno debajo del otro en el men\u00fa, "
    "y que confundirlos arruina m\u00e1s archivos que cualquier otra cosa.",
    "Al final de este video no los vas a volver a confundir, y vas a tener tu figura en los dos "
    "formatos que de verdad se usan: cuadrado para la tienda y vertical para reel.",
])

parte(doc, 2, "Los dos cuadros", "2 minutos y medio")
haces(doc, [
    "Abre Imagen \u203a Tama\u00f1o de imagen (Ctrl+Alt+I). Ens\u00e9\u00f1alo y ci\u00e9rralo.",
    "Abre Imagen \u203a Tama\u00f1o de lienzo (Ctrl+Alt+C). Ens\u00e9\u00f1alo y ci\u00e9rralo.",
    "Vuelve a abrir Tama\u00f1o de imagen y ve se\u00f1alando campo por campo.",
    "Con Remuestrear APAGADO: cambia 72 a 300 ppp. Se\u00f1ala que los p\u00edxeles no se mueven "
    "y los cent\u00edmetros s\u00ed.",
    "Enciende Remuestrear y abre el desplegable.",
])
dices(doc, [
    "Imag\u00ednate que tu archivo es una foto pegada en una hoja de papel.",
    "Tama\u00f1o de imagen, que es Control+Alt+I, agarra la foto y la estira o la encoge. "
    "Todo lo que hay dentro cambia de tama\u00f1o.",
    "Tama\u00f1o de lienzo, Control+Alt+C, deja la foto exactamente igual y lo que cambia es la hoja "
    "de abajo. Si la haces m\u00e1s grande, aparece espacio vac\u00edo alrededor. Si la haces m\u00e1s chica, "
    "recorta: lo que se sale, se va.",
    "Y ya. Esa es la clase. Lo dem\u00e1s son los detalles que hacen que uno se equivoque.",
    "En el cuadro de tama\u00f1o de imagen hay tres cosas. Anchura y altura, que es el tama\u00f1o en p\u00edxeles. "
    "La resoluci\u00f3n, en ppp. Y la casilla de Remuestrear.",
    "Hablemos de la resoluci\u00f3n, porque hay mucha confusi\u00f3n suelta.",
    "Con la casilla de Remuestrear apagada, cambio setenta y dos por trescientos... y mira los p\u00edxeles: "
    "no se movieron. Lo \u00fanico que cambi\u00f3 fue cu\u00e1ntos cent\u00edmetros mide al imprimir.",
    "Porque los ppp no son calidad. Son una instrucci\u00f3n para la impresora de qu\u00e9 tan apretados "
    "poner los puntos.",
    "De ah\u00ed salen dos cosas que te van a ahorrar discusiones.",
    "La primera: para pantalla, los ppp no importan. Nada. Una imagen para Instagram a setenta y dos "
    "y la misma a trescientos se ven id\u00e9nticas, porque la pantalla solo cuenta p\u00edxeles.",
    "Y la segunda: para imprimir s\u00ed importan, y el n\u00famero es trescientos. Si vas a imprimir algo "
    "de diez cent\u00edmetros de ancho a trescientos ppp, necesitas mil ciento ochenta y un p\u00edxeles. "
    "Si solo tienes seiscientos, te va a salir borroso, y poner trescientos en esa casilla "
    "no lo arregla: no inventa informaci\u00f3n, solo cambia la etiqueta.",
    "Y con Remuestrear encendido s\u00ed se inventan o se tiran p\u00edxeles. De este desplegable, "
    "dos opciones y ya: Bic\u00fabica m\u00e1s enfocada cuando reduces, y Conservar detalles cuando agrandas. "
    "Si lo dejas en Autom\u00e1tico, le atina casi siempre.",
])

parte(doc, 3, "El error, en vivo", "90 segundos")
haces(doc, [
    "Con la imagen cuadrada de 2000x2000 abierta: Ctrl+Alt+I.",
    "Abre la cadenita y pon 1080 x 1920. Aceptar.",
    "Qu\u00e9date dos segundos viendo el desastre, callado.",
    "Ctrl+Z.",
])
dices(doc, [
    "Tengo esta imagen cuadrada y la quiero vertical, para un reel. "
    "Lo que hace uno la primera vez: tama\u00f1o de imagen, y escribo mil ochenta por mil novecientos "
    "veinte. Para que me deje, tengo que abrir la cadenita.",
    "\u2014 (viendo el resultado) \u2014  Y ah\u00ed est\u00e1 el desastre. La cabeza es un huevo.",
    "Estir\u00e9 la foto para que cupiera en una hoja de otra forma, que es justo lo que la clase cuatro "
    "dijo que no se hace nunca.",
    "Control+Z. Lo que yo quer\u00eda no era estirar la foto: era cambiar la hoja.",
])

parte(doc, 4, "El mismo archivo en dos formatos", "3 minutos y medio")
haces(doc, [
    "Ctrl+N: 2000 x 2000, 72 ppp, RGB, fondo blanco. Ctrl+S como 05-formatos.psd.",
    "Arrastra el PNG. Clic derecho \u203a Convertir en objeto inteligente.",
    "Ctrl+T, escala desde la esquina hasta que ocupe como el 75% del alto, centrada. Enter.",
    "Ctrl+Shift+Alt+W, JPG 80, como 05-tienda.jpg.",
    "Ctrl+Alt+C: anchura 1080, altura 1920, en p\u00edxeles.",
    "Se\u00f1ala la cuadr\u00edcula del ancla, abajo.",
    "Error a prop\u00f3sito: pon el ancla ARRIBA y ense\u00f1a que pierde los pies. Deshaz.",
    "Segundo error: pon el ancla ABAJO del todo y ense\u00f1a que le corta la cabeza. Deshaz.",
    "Ahora s\u00ed: ancla abajo al centro. Aceptar.",
    "Se\u00f1ala que la figura NO cambi\u00f3 de tama\u00f1o.",
    "Capa de fondo nueva hasta abajo, rellena con el color de tu biblioteca.",
    "V para recentrar. Ctrl+Shift+Alt+W como 05-reel.jpg.",
])
dices(doc, [
    "Ahora hagamos lo correcto, y de paso te queda el m\u00e9todo que vas a usar siempre: "
    "un archivo grande, varias salidas.",
    "Documento nuevo de dos mil por dos mil. Meto el PNG y lo convierto en objeto inteligente, "
    "como en la clase cuatro.",
    "Lo escalo desde la esquina hasta que ocupe como tres cuartas partes del alto, centrado.",
    "Dos mil por dos mil, cuadrado, es el formato que piden casi todas las tiendas, "
    "y es el que se ve bien en la cuadr\u00edcula de Instagram. Si solo vas a hacer un tama\u00f1o, "
    "haz este. Lo exporto.",
    "Y ahora el vertical, pero con el cuadro correcto: Control+Alt+C, tama\u00f1o de lienzo. "
    "Mil ochenta de ancho, mil novecientos veinte de alto, en p\u00edxeles.",
    "F\u00edjate en esta cuadr\u00edcula de abajo. Se llama ancla, y decide de d\u00f3nde crece o de d\u00f3nde "
    "recorta la hoja. Viene en el centro, as\u00ed que crece y recorta parejo por los cuatro lados.",
    "\u2014 (con el ancla arriba) \u2014  Si la pongo arriba, pierde los pies.",
    "\u2014 (con el ancla abajo) \u2014  Y si la pongo hasta abajo, le corta la cabeza. "
    "Y ah\u00ed est\u00e1 el error que cuesta caro: con una figura as\u00ed, la cabeza es media imagen. "
    "El ancla no es un detalle.",
    "Para algo que se para en el suelo, el ancla va abajo al centro: crece hacia arriba "
    "y le deja aire encima de la cabeza.",
    "Y mira lo importante: la figura no cambi\u00f3 de tama\u00f1o ni un p\u00edxel. Sigue igual. "
    "Lo \u00fanico que cambi\u00f3 es cu\u00e1nta hoja hay alrededor. Eso es el tama\u00f1o de lienzo.",
    "Relleno el espacio nuevo con el color de marca, que ya est\u00e1 en la biblioteca de la clase dos, "
    "a un clic. Recentro la figura, y exporto.",
    "Dos archivos, un solo original, cero deformaciones. Y como la figura es un objeto inteligente, "
    "si ma\u00f1ana le cambias la imagen de adentro, los dos se actualizan.",
])

parte(doc, 5, "La tercera que se confunde: recortar", "2 minutos")
haces(doc, [
    "Aprieta C. En la barra de opciones pon la proporci\u00f3n 9:16.",
    "Recorta a ojo y ense\u00f1a la diferencia con el cuadro de di\u00e1logo.",
    "Se\u00f1ala la casilla \u201cEliminar p\u00edxeles recortados\u201d y ap\u00e1gala.",
    "Con la misma herramienta, AGRANDA el lienzo m\u00e1s all\u00e1 de la imagen.",
    "Enciende la casilla \u201cRelleno seg\u00fan el contenido\u201d. Enter. Ense\u00f1a c\u00f3mo rellen\u00f3 el espacio nuevo.",
])
dices(doc, [
    "Y falta la tercera que se confunde con las otras dos: la herramienta de recorte, que es C.",
    "Hace lo mismo que cambiar el lienzo, pero a ojo y con el rat\u00f3n, y te deja poner una proporci\u00f3n "
    "fija aqu\u00ed arriba. Es la que vas a usar el noventa por ciento de las veces; los cuadros de "
    "di\u00e1logo son para cuando necesitas un n\u00famero exacto.",
    "Un detalle que importa: esta casilla que dice Eliminar p\u00edxeles recortados. D\u00e9jala apagada. "
    "Apagada, lo que recortas se queda guardado fuera del lienzo y puedes volver por ello. "
    "Encendida, se va para siempre. Es la misma idea de la clase dos: tapar, no borrar.",
    "Y un regalo, de las cosas que de verdad valen el programa: con esta misma herramienta "
    "tambi\u00e9n puedes agrandar el lienzo. Y si enciendes esta casilla de Relleno seg\u00fan el contenido, "
    "Photoshop te inventa el fondo que falta en el espacio nuevo.",
    "M\u00edralo: estiro el lienzo hacia arriba, Enter... y rellen\u00f3 solo.",
    "\u00dasalo para fondos: pared, mesa, cielo, madera. Pero no lo uses encima del producto. "
    "Lo que inventa ah\u00ed no es tu producto, y si eso se lo mandas a un cliente le est\u00e1s entregando "
    "algo que no existe.",
])

parte(doc, 6, "La tabla de tama\u00f1os", "90 segundos")
haces(doc, ["Pon la tabla completa en pantalla. D\u00e9jala quieta 10 segundos."])
dices(doc, [
    "Y te dejo la tabla de tama\u00f1os, para que la guardes.",
    "Ficha de tienda: dos mil por dos mil, RGB, setenta y dos.",
    "Reel, TikTok o Short: mil ochenta por mil novecientos veinte.",
    "Publicaci\u00f3n de feed: mil ochenta por mil trescientos cincuenta.",
    "Miniatura de YouTube: mil doscientos ochenta por setecientos veinte.",
    "Y para imprimir: seg\u00fan el tama\u00f1o f\u00edsico, en CMYK y a trescientos.",
    "Y la regla que resume la clase entera: trabaja en el m\u00e1s grande de la lista y de ah\u00ed saca "
    "los dem\u00e1s. Nunca al rev\u00e9s, porque agrandar inventa y se nota.",
    "Y si vas a imprimir alguna vez, el de imprenta le gana a todos en p\u00edxeles. "
    "Por eso los que trabajan con esto hacen el archivo madre a tama\u00f1o de impresi\u00f3n, "
    "y de ah\u00ed exportan las versiones de pantalla.",
    "Y para que no te suene a trabajo: sacar esas cinco versiones a mano son veinte minutos. "
    "M\u00e1s adelante en el curso se las vas a aventar al Procesador de im\u00e1genes y van a salir "
    "las cinco carpetas solas mientras te paras por un caf\u00e9.",
])

parte(doc, 7, "Cierre", "25 segundos")
haces(doc, ["Pantalla final apuntando a la Clase 6."])
dices(doc, [
    "Tu tarea: sube los dos archivos, el cuadrado y el vertical. "
    "Y dime en los comentarios cu\u00e1l de los dos cuadros usaste para pasar de uno a otro. "
    "Si me contestas \u201ctama\u00f1o de lienzo\u201d, esta clase funcion\u00f3.",
    "Suscr\u00edbete, que ya casi cerramos el primer bloque del curso. "
    "En la clase seis vemos guardar y exportar bien: los cuatro formatos y cu\u00e1l va en cada lugar. "
    "Ah\u00ed te veo.",
])

doc.add_page_break()
h2(doc, "Notas de producci\u00f3n")
parrafo(doc, "Todo lo de aqu\u00ed abajo es para ti. Nada se dice en c\u00e1mara.", 10)
h2(doc, "Ficha")
parrafo(doc, "T\u00edtulo: Curso de Photoshop desde cero \u2014 Clase 5: tama\u00f1o de imagen vs tama\u00f1o de lienzo "
             "(el error #1)")
parrafo(doc, "Entrega: 05-tienda.jpg (2000x2000) y 05-reel.jpg (1080x1920), del mismo archivo")
parrafo(doc, "Miniatura: texto \u201cIMAGEN NO ES LIENZO\u201d. La misma figura dos veces: una estirada "
             "hasta el borde, otra del mismo tama\u00f1o con aire alrededor.")
h2(doc, "Shorts que salen de esta grabaci\u00f3n")
for t in ["Parte 4, el ancla \u2014 gancho: \u201cAs\u00ed es como / le cortas la cabeza\u201d",
          "Parte 2, los ppp \u2014 gancho: \u201cLos 300 ppp no son / calidad de imagen\u201d",
          "Parte 5, el relleno al agrandar \u2014 gancho: \u201cAgranda el lienzo / y que invente el fondo\u201d"]:
    p = doc.add_paragraph(t, style='List Bullet'); p.paragraph_format.left_indent = Cm(0.8)
guardar(doc, "Clase 05 - Imagen contra lienzo.docx")


# ==================================================================== CLASE 0
doc = nuevo("CLASE 0", "La presentaci\u00f3n del curso  \u00b7  dura 4 minutos y medio",
            "Curso de Photoshop desde cero  \u00b7  Clase 0  \u00b7  Presentaci\u00f3n del curso")

h2(doc, "De qu\u00e9 va esta clase")
parrafo(doc, "Este es el video que vende el curso. Es el \u00fanico de los 31 que no ense\u00f1a nada: "
             "su trabajo es que alguien decida quedarse las 30 clases.")
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(6)
sombrear(p, 'FFF4E5')
r = p.add_run("  Se graba AL FINAL del d\u00eda,  ")
r.bold = True; r.font.size = Pt(11); r.font.color.rgb = NARANJA
r2 = p.add_run("cuando las clases 1 a 5 ya est\u00e9n grabadas. Si la grabas primero, "
               "est\u00e1s prometiendo algo que todav\u00eda no sabes si vas a cumplir, y eso se oye.  ")
r2.font.size = Pt(11)

h2(doc, "Antes de darle Rec")
casillas(doc, [
    "Las clases 1 a 5 ya grabadas. No es opcional: media presentaci\u00f3n se apoya en poder decir "
    "\u201cya est\u00e1n arriba\u201d",
    "Las tres pruebas del arranque, ya listas y en una carpeta, para pasarlas sin buscar nada",
    "La figura f\u00edsica en la mesa, a la mano, si vas a salir a c\u00e1mara",
    "NO decir precios de la licencia. Cambian por pa\u00eds y el video tiene que servir en dos a\u00f1os",
])
nota(doc, "Las tres pruebas son: (1) la imagen fea y la terminada, una tras otra; "
          "(2) una miniatura arm\u00e1ndose en acelerado; (3) una carpeta donde aparecen 200 im\u00e1genes "
          "de golpe con la barra de progreso corriendo.")

doc.add_page_break()

parte(doc, 1, "Las tres pruebas, antes de hablar", "20 segundos")
haces(doc, [
    "Prueba 1: la imagen cruda y, con un corte, la ficha terminada. 6 segundos.",
    "Prueba 2: la miniatura arm\u00e1ndose en acelerado. 6 segundos.",
    "Prueba 3: la carpeta donde aparecen 200 im\u00e1genes de golpe, con la barra de progreso. 6 segundos.",
    "Los primeros 4 segundos van SIN voz. Tu voz entra en el segundo 4.",
])
dices(doc, [
    "(entra en el segundo 4)  Esta es una imagen sin editar. Esta es la misma, veinte minutos despu\u00e9s.",
    "Esta miniatura la hace Photoshop con una plantilla y una hoja de c\u00e1lculo.",
    "Y estas doscientas im\u00e1genes no las hizo nadie: se hicieron solas.",
])

parte(doc, 2, "Qui\u00e9n eres y de qu\u00e9 va esto", "40 segundos")
haces(doc, [
    "A c\u00e1mara. Cuando digas \u201cesta figura\u201d, ens\u00e9\u00f1ala.",
])
dices(doc, [
    "Qu\u00e9 tal, soy Richie.",
    "Yo hago figuras y cajas personalizadas estilo Funko, y todo el dise\u00f1o lo hago en Photoshop. "
    "Llevo meses haciendo esto y he aprendido el programa haci\u00e9ndolo.",
    "En treinta clases te voy a ense\u00f1ar a usar Photoshop desde cero, hasta poder hacer "
    "las tres cosas que acabas de ver.",
    "Y no en teor\u00eda: cada clase termina con un archivo tuyo, exportado.",
    "Vamos a trabajar siempre con esta figura. Empezamos por abrir el programa, "
    "y terminamos armando la caja completa y haciendo que Photoshop la arme solo.",
    "Si lo que t\u00fa quieres es pintar o ilustrar, este no es tu curso, y te lo digo ahora "
    "para no hacerte perder el tiempo.",
])

parte(doc, 3, "Qu\u00e9 hace falta para seguirlo", "50 segundos")
haces(doc, [
    "Photoshop de escritorio abierto en pantalla. Nada de capturas de precios.",
])
dices(doc, [
    "Ahora lo que te tengo que decir de una vez, en vez de escond\u00e9rtelo hasta la clase veinte.",
    "Este curso se graba en Photoshop de escritorio, con licencia, y la pagu\u00e9 yo.",
    "No hay versi\u00f3n gratis de esto. Hay programas parecidos y est\u00e1n bien para las primeras clases, "
    "pero de la clase siete en adelante, y sobre todo cuando lleguemos a la parte donde el trabajo "
    "se empieza a hacer solo, lo que vamos a usar no existe en ning\u00fan otro lado.",
    "Prefiero dec\u00edrtelo ahora que engancharte con seis clases y dejarte en una pared.",
    "Tienes tres caminos.",
    "Uno: la prueba de siete d\u00edas de Adobe. Te alcanza para los dos primeros bloques del curso "
    "si te sientas a hacerlos. Pero es una sola prueba por persona, as\u00ed que no la actives hoy "
    "por curiosidad: act\u00edvala el d\u00eda que tengas la tarde libre.",
    "Dos: pagarla. Yo la pagu\u00e9 porque lleg\u00f3 el punto en que esto dej\u00f3 de ser un pasatiempo "
    "y le empiezo a entregar trabajo a gente. El precio cambia por pa\u00eds, as\u00ed que verif\u00edcalo "
    "en la p\u00e1gina de Adobe y no en este video, que lo vas a ver en dos a\u00f1os.",
    "Y tres: ver el curso sin tener el programa. Es v\u00e1lido. Mucha gente va a ver la parte "
    "de automatizaci\u00f3n y con eso va a decidir si le conviene pagarlo.",
    "Y una cosa m\u00e1s: no vamos a piratear nada. Siguiente tema.",
])
nota(doc, "La l\u00ednea de \u201cno actives la prueba hoy\u201d es la que m\u00e1s credibilidad te da de todo el video, "
          "porque va en contra de lo que le conviene a quien est\u00e1 vendiendo algo. No la quites.")

parte(doc, 4, "El mapa del curso", "90 segundos")
haces(doc, [
    "Seis tarjetas, una por bloque. La del bloque de automatizaci\u00f3n se queda m\u00e1s tiempo.",
    "Cuando hables de ese bloque, pon la barra de progreso del lote corriendo.",
])
dices(doc, [
    "El curso son seis bloques, y te digo desde ahorita cu\u00e1l es el que importa.",
    "El primero, los comandos. Seis clases para que tus manos sepan d\u00f3nde est\u00e1 todo sin pensarlo. "
    "Al final de la clase uno ya tienes tu primer archivo, y en la tres le quitas el fondo "
    "a la figura en dos clics.",
    "El segundo, la imagen. Revelado, fondo blanco de verdad, sombra que no parece pegada, "
    "color, y quitar lo que estorba.",
    "El tercero, y aqu\u00ed es donde este curso se separa de los dem\u00e1s.",
    "Para cuando llegues a la clase trece ya vas a haber editado seis im\u00e1genes a mano, "
    "una por una, y te va a haber dado flojera la sexta. Ese es justo el momento. "
    "En este bloque grabas una vez lo que haces, y se lo aplicas a doscientas.",
    "Casi todos los cursos de Photoshop dejan esto para el final, si es que lo dejan. "
    "Aqu\u00ed va a la mitad, porque es lo que de verdad te cambia el d\u00eda.",
    "El cuarto, el dise\u00f1o. Tipograf\u00eda, el logo en vectorial, la miniatura, y la caja lista "
    "para imprenta: CMYK, trescientos ppp, sangrado, y un PDF que la imprenta no te regrese.",
    "El quinto, automatizaci\u00f3n de verdad. Conectas un archivo de Photoshop con una hoja de c\u00e1lculo "
    "y salen veinte dise\u00f1os distintos. Y dos clases de scripts, para cuando ni la acci\u00f3n alcanza.",
    "Y el sexto, el oficio. El flujo completo de corrido, qu\u00e9 cuesta la licencia y c\u00f3mo se paga sola, "
    "y qu\u00e9 cobrar si decides hacerle esto a alguien m\u00e1s.",
])

parte(doc, 5, "El trato", "40 segundos")
dices(doc, [
    "Tres cosas de mi lado.",
    "Las clases uno a la cinco ya est\u00e1n arriba, en la lista, ahora mismo. No es una clase "
    "y una promesa: puedes seguir en cuanto termine este video y no te vas a topar con una pared.",
    "Despu\u00e9s sube una clase diaria hasta cerrar el primer bloque, y de ah\u00ed dos por semana, "
    "en d\u00edas fijos.",
    "Y en cada clase, el archivo con el que grab\u00e9 est\u00e1 en el comentario fijado. Gratis, "
    "sin pedirte correo. El PSD tal cual, con las capas sucias, para que trabajes con mi material "
    "y no te atores buscando el tuyo.",
    "Una cosa de tu lado: haz la clase, no la veas. Si solo la ves, en una semana no te vas "
    "a acordar de nada. Abre el programa, p\u00e1usale donde haga falta, y sube tu entrega "
    "a los comentarios. Yo los contesto.",
])

parte(doc, 6, "Cierre", "20 segundos")
haces(doc, ["Pantalla final apuntando SOLO a la Clase 1. Sin suscripci\u00f3n, sin otro video."])
dices(doc, [
    "Abre tu Photoshop, o activa esa prueba si hoy es el d\u00eda, y v\u00e1monos a la clase uno: "
    "la interfaz, los doce atajos que vas a usar siempre, y los tres ajustes que hay que cambiar "
    "el d\u00eda que instalas el programa.",
    "Es el siguiente video de la lista. Ah\u00ed te veo.",
])

doc.add_page_break()
h2(doc, "Notas de producci\u00f3n")
parrafo(doc, "Todo lo de aqu\u00ed abajo es para ti. Nada se dice en c\u00e1mara.", 10)
h2(doc, "Ficha")
parrafo(doc, "T\u00edtulo: Curso de Photoshop desde cero \u2014 Clase 0: lo que vas a poder hacer en 30 clases")
parrafo(doc, "Miniatura: texto \u201c30 CLASES\u201d sobre negro, y abajo chico \u201cde cero a 200 im\u00e1genes solas\u201d. "
             "A la izquierda la imagen cruda; a la derecha, la ficha terminada. "
             "Sin cara, sin flechas, sin c\u00edrculos rojos.")
h2(doc, "Shorts que salen de esta grabaci\u00f3n")
for t in ["Las 200 im\u00e1genes \u2014 gancho: \u201cEstas 200 im\u00e1genes / las hizo Photoshop solo\u201d",
          "El consejo de la prueba \u2014 gancho: \u201cNo actives hoy / tu prueba de 7 d\u00edas\u201d",
          "Las 12 herramientas \u2014 gancho: \u201cPhotoshop tiene 70 herramientas / vas a usar 12\u201d"]:
    p = doc.add_paragraph(t, style='List Bullet'); p.paragraph_format.left_indent = Cm(0.8)
guardar(doc, "Clase 00 - Presentacion del curso.docx")
