# -*- coding: utf-8 -*-
"""Curso corto: presentacion + clases 1 a 3."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curso_corto_base import (nuevo, regla, reloj, antes, cierre_notas, guardar,
                              DISCIPLINA)
from guion_docx import parte, haces, dices, nota, h2, parrafo

# =========================================================== 0. PRESENTACION
doc = nuevo("PRESENTACI\u00d3N", "El video que abre el curso  \u00b7  2 minutos",
            "Curso de Photoshop para cajas  \u00b7  Presentaci\u00f3n")
regla(doc, "Se graba AL FINAL, cuando las 8 clases ya est\u00e9n grabadas.")
parrafo(doc, "Si lo grabas primero est\u00e1s prometiendo algo que todav\u00eda no sabes si vas a cumplir, "
             "y eso se oye. Grabado al final, puedes decir \u201cya est\u00e1n arriba\u201d porque de verdad lo est\u00e1n.")
antes(doc, [
    "Las 8 clases ya grabadas",
    "La caja terminada en pantalla, y el PDF abierto",
    "El lote corriendo, grabado, para los 5 segundos del arranque",
    "NO decir precios de la licencia. Cambian por pa\u00eds",
])

parte(doc, 1, "El arranque", "20 segundos")
haces(doc, [
    "Sin hablar los primeros 4 segundos.",
    "Ense\u00f1a la figura suelta. Corte. La caja armada con esa figura dentro.",
    "Corte. El lote corriendo sobre una carpeta, con la barra de progreso.",
])
dices(doc, [
    "(entra en el segundo 4)  Esta es una figura. Esta es la caja hecha para ella, "
    "lista para imprimir.",
    "Y estas no las hice yo: las hizo Photoshop solo, mientras me tomaba un caf\u00e9.",
])

parte(doc, 2, "Qui\u00e9n eres y qu\u00e9 es esto", "50 segundos")
haces(doc, ["A c\u00e1mara."])
dices(doc, [
    "Qu\u00e9 tal, soy Richie.",
    "Yo hago figuras y cajas personalizadas estilo Funko, y todo el dise\u00f1o lo hago en Photoshop. "
    "Llevo meses en esto y aprend\u00ed el programa haci\u00e9ndolo.",
    "Este curso son ocho clases, hora y media en total, y al final vas a tener tu caja "
    "lista para imprimir. Empezamos abriendo Photoshop por primera vez.",
    "No es un curso de todo Photoshop. Es el camino corto: lo que de verdad necesitas "
    "para sacar un trabajo, sin las cincuenta cosas que no vas a usar.",
    "Cada clase deja un archivo terminado. Si haces las ocho, acabas con la caja.",
])

parte(doc, 3, "Qu\u00e9 hace falta", "30 segundos")
dices(doc, [
    "Lo \u00fanico que necesitas es Photoshop de escritorio. Y te lo digo de una vez en vez "
    "de escond\u00e9rtelo: cuesta dinero, y lo pagu\u00e9 yo.",
    "Adobe te da siete d\u00edas de prueba, y con siete d\u00edas te alcanza para hacer este curso "
    "completo. Pero es una sola prueba por persona, as\u00ed que no la actives hoy por curiosidad: "
    "act\u00edvala el d\u00eda que te vayas a sentar.",
    "Y no, no vamos a piratear nada.",
])
nota(doc, "La l\u00ednea de \u201cno la actives hoy\u201d es la que m\u00e1s credibilidad te da del video entero, "
          "porque va en contra de lo que le conviene a quien vende algo. No la quites.")

parte(doc, 4, "Cierre", "20 segundos")
haces(doc, ["Pantalla final apuntando SOLO a la Clase 1."])
dices(doc, [
    "Las ocho clases ya est\u00e1n arriba, en la lista. Puedes hacerlas de corrido hoy mismo.",
    "El archivo con el que grabo est\u00e1 en el comentario fijado de cada clase, gratis.",
    "Nada m\u00e1s te pido una cosa: haz la clase, no la veas. Si solo la ves, en una semana "
    "no te vas a acordar de nada.",
    "V\u00e1monos a la clase uno.",
])
cierre_notas(doc,
    "Curso de Photoshop desde cero para hacer cajas \u2014 Presentaci\u00f3n",
    "nada; es el video que abre",
    "texto \u201c8 CLASES\u201d sobre negro. A la izquierda la figura suelta, a la derecha la caja armada.",
    ["El lote corriendo \u2014 \u201cEstas cajas / las hizo Photoshop solo\u201d",
     "El consejo de la prueba \u2014 \u201cNo actives hoy / tu prueba de 7 d\u00edas\u201d"])
guardar(doc, "00 - Presentacion.docx")


# =========================================================== 1
doc = nuevo("CLASE 1", "La pantalla y los 7 atajos  \u00b7  8 minutos",
            "Curso de Photoshop para cajas  \u00b7  Clase 1")
regla(doc, DISCIPLINA.format(dur="8 minutos", tope="10"))
antes(doc, [
    "Photoshop abierto, Ventana \u203a Espacio de trabajo \u203a Restablecer Aspectos esenciales",
    "material\\figura-con-fondo.jpg a la vista en el explorador",
    "Keyviz prendido, OBS grabando",
])

parte(doc, 1, "Arranque", "15 segundos")
haces(doc, ["Ense\u00f1a el archivo terminado: el lienzo vertical con la figura centrada."])
dices(doc, [
    "Qu\u00e9 tal, soy Richie. Esta es la clase uno del curso.",
    "En ocho minutos vas a tener este archivo hecho por ti, y siete atajos de teclado "
    "que vamos a usar en las ocho clases.",
    "Si nunca has abierto Photoshop, estamos empezando exactamente donde t\u00fa.",
])

parte(doc, 2, "Las cinco zonas", "90 segundos")
haces(doc, [
    "Se\u00f1ala cada zona con el rat\u00f3n al nombrarla. Sin detenerte.",
    "Al hablar de la barra de opciones: aprieta B y luego T, para que se vea cambiar.",
    "Cierra el panel de Capas con su X. Sigue hablando dos segundos. Aprieta F7 y regresa.",
])
dices(doc, [
    "Photoshop son muchos botones, pero siempre son las mismas cinco zonas.",
    "Arriba, los men\u00fas: ah\u00ed est\u00e1 todo. Cuando no encuentres algo, b\u00fascalo ah\u00ed.",
    "Debajo, la barra de opciones. Esta cambia seg\u00fan la herramienta que traigas. "
    "Con el pincel dice una cosa, con el texto dice otra. No est\u00e1 fallando.",
    "A la izquierda, las herramientas. A la derecha, los paneles: el que importa es Capas.",
    "Y en medio, el lienzo, que es tu archivo.",
    "\u2014 (tras cerrar Capas) \u2014  Y ya cerr\u00e9 el panel de capas. Esto te va a pasar. "
    "F7 y regresa. Lo que ves en pantalla no es tu archivo: es c\u00f3mo est\u00e1n acomodadas "
    "las ventanas.",
])
reloj(doc, "al terminar esta parte deber\u00edas ir en 1:45.")

parte(doc, 3, "Los 7 atajos", "90 segundos")
haces(doc, [
    "Tarjeta en pantalla con los siete.",
    "Aprieta cada tecla al decirla, para que se vea en Keyviz.",
    "Deja la tarjeta quieta 6 segundos al final.",
])
dices(doc, [
    "Siete atajos. No te los aprendas ahorita, los vamos a usar en seguida.",
    "V, mover.",
    "T, texto.",
    "Control+N, documento nuevo.",
    "Control+T, transformar: cambiar de tama\u00f1o o girar.",
    "Control+Z, deshacer.",
    "Control+S, guardar.",
    "Y Control+Shift+Alt+W, exportar. Es largo, pero es el que saca el JPG.",
    "Si usas Mac, donde yo diga Control, t\u00fa usa Comando.",
])
reloj(doc, "deber\u00edas ir en 3:15.")

parte(doc, 4, "El documento y la figura", "3 minutos")
haces(doc, [
    "Ctrl+N. Anchura 1080, altura 1920, en p\u00edxeles. Resoluci\u00f3n 72. RGB 8 bits. Fondo blanco.",
    "Antes de aceptar: guarda el preajuste como \u201cvertical redes\u201d.",
    "Crear. Ctrl+S como 01-portada.psd.",
    "Arrastra figura-con-fondo.jpg al lienzo. Jala una esquina y Enter.",
    "V, y arrastra al centro hasta que salgan las gu\u00edas rosas.",
])
dices(doc, [
    "Control+N. Aqu\u00ed es donde se arruinan la mitad de los dise\u00f1os, as\u00ed que despacio.",
    "Mil ochenta de ancho, mil novecientos veinte de alto. Y que diga p\u00edxeles, no cent\u00edmetros.",
    "Resoluci\u00f3n setenta y dos, color RGB, fondo blanco.",
    "Ese tama\u00f1o es el de un reel, un TikTok y un Short. Y setenta y dos con RGB es lo que "
    "se usa para pantalla. Para imprimir son otros n\u00fameros, y eso es la clase siete.",
    "Antes de crear: guarda el preajuste. Este documento lo vas a hacer muchas veces.",
    "Y gu\u00e1rdalo antes de hacer nada. Control+S.",
    "Ahora arrastro la figura desde la carpeta al lienzo. Jalo una esquina para que quepa, Enter.",
    "Mira el panel de capas: hay dos. El fondo, y la figura encima. Eso es Photoshop: "
    "hojas encimadas. Y la clase dos es sobre eso.",
    "V, mover, y la llevo al centro. Esas l\u00edneas rosas son las gu\u00edas: ya est\u00e1 centrada.",
])
reloj(doc, "deber\u00edas ir en 6:15.")

parte(doc, 5, "El texto y exportar", "100 segundos")
haces(doc, [
    "T, clic, escribe el nombre de la figura.",
    "Aprieta Enter a prop\u00f3sito: hace un rengl\u00f3n nuevo. Ctrl+Enter para cerrar bien.",
    "Ctrl+Shift+Alt+W. JPG, calidad 80. Exportar como 01-portada.jpg.",
])
dices(doc, [
    "T, de texto. Clic, y escribo el nombre de la figura. El tama\u00f1o y la letra est\u00e1n "
    "arriba, en la barra de opciones.",
    "\u2014 (tras darle Enter) \u2014  Y aqu\u00ed el error de todos: para cerrar el texto, Enter no sirve. "
    "Enter hace un rengl\u00f3n nuevo. Se cierra con Control+Enter.",
    "Y ya exportamos. Control+Shift+Alt+W. JPG, calidad ochenta: de ah\u00ed para arriba "
    "pesa el doble y se ve igual.",
    "Ah\u00ed est\u00e1 tu primer archivo de Photoshop.",
])

parte(doc, 6, "Cierre", "15 segundos")
haces(doc, ["Pantalla final a la Clase 2."])
dices(doc, [
    "Sube tu archivo a los comentarios, los contesto todos.",
    "En la clase dos vemos capas y m\u00e1scaras, que es el concepto en el que se apoya "
    "todo lo dem\u00e1s. Ah\u00ed te veo.",
])
cierre_notas(doc,
    "Curso de Photoshop desde cero \u2014 Clase 1: la pantalla y los 7 atajos",
    "01-portada.jpg, 1080x1920 con la figura centrada",
    "texto \u201c7 ATAJOS\u201d sobre naranja, con el lienzo terminado al lado.",
    ["El Ctrl+Enter \u2014 \u201cTu texto no se cierra / con Enter\u201d",
     "El panel cerrado \u2014 \u201cSe te fue el panel de capas / F7\u201d"])
guardar(doc, "01 - La pantalla y los 7 atajos.docx")


# =========================================================== 2
doc = nuevo("CLASE 2", "Capas y m\u00e1scaras  \u00b7  9 minutos",
            "Curso de Photoshop para cajas  \u00b7  Clase 2")
regla(doc, "Esta es LA clase del curso. Si se entiende la m\u00e1scara, las seis que siguen "
           "son cuesta abajo. Por eso dura 9 y no 6.")
antes(doc, [
    "material\\figura-con-fondo.jpg abierta",
    "Una versi\u00f3n fea, borrada a mordidas con el borrador, para ense\u00f1arla al arrancar",
    "Keyviz prendido, OBS grabando",
])

parte(doc, 1, "Arranque", "20 segundos")
haces(doc, [
    "Ense\u00f1a la versi\u00f3n fea, mordida.",
    "Ense\u00f1a la buena. Y en la buena, apaga la m\u00e1scara con Shift+clic: el fondo REGRESA.",
])
dices(doc, [
    "Soy Richie, seguimos con el curso.",
    "Mira estas dos. En esta le quit\u00e9 el fondo con el borrador. En esta us\u00e9 una m\u00e1scara.",
    "Y la diferencia de verdad es esta: en la de la m\u00e1scara el fondo sigue ah\u00ed. "
    "Lo puedo regresar cuando quiera.",
    "En nueve minutos vas a entender por qu\u00e9, y eso es lo m\u00e1s importante que vas a aprender "
    "de Photoshop.",
])

parte(doc, 2, "Qu\u00e9 es una capa", "2 minutos")
haces(doc, [
    "F7 para abrir el panel. Se\u00f1ala las capas de arriba abajo.",
    "Apaga y prende el ojo de la figura dos veces.",
    "Selecciona a prop\u00f3sito la capa de abajo y ponte a pintar con el pincel. No pasa nada. "
    "Qu\u00e9date dos segundos.",
    "Se\u00f1ala en el panel cu\u00e1l ten\u00edas seleccionada. Ctrl+Z.",
])
dices(doc, [
    "Una capa es una hoja transparente. Tu archivo es un mont\u00f3n de hojas encimadas, "
    "y lo que ves es lo que se alcanza a ver desde arriba. Ya est\u00e1, eso es todo.",
    "De ah\u00ed salen dos cosas. La primera: lo de arriba tapa lo de abajo.",
    "Y la segunda, que es de donde sale casi todo lo que se le complica a uno: "
    "solo le haces cosas a la capa que tengas seleccionada. M\u00edrame.",
    "\u2014 (pintando sin resultado) \u2014  Estoy pintando y no pasa nada, porque estoy pintando "
    "debajo de la figura. Nos pasa a todos, seguido.",
    "Antes de pensar que el programa est\u00e1 fallando, mira el panel de capas.",
    "Y una costumbre: ponle nombre a las capas. Doble clic. Cuesta tres segundos y "
    "es lo que hace que puedas abrir tu propio archivo dentro de un mes.",
])
reloj(doc, "deber\u00edas ir en 2:20.")

parte(doc, 3, "La m\u00e1scara", "4 minutos")
haces(doc, [
    "E, borrador. Borra fondo y mu\u00e9rdele un pedazo a la cabeza. Qu\u00e9date dos segundos. Ctrl+Z.",
    "Con la capa seleccionada, clic en el bot\u00f3n de m\u00e1scara, abajo del panel.",
    "Se\u00f1ala el cuadrito blanco nuevo.",
    "Clic en ese cuadrito. D, luego B.",
    "Pinta negro sobre el fondo. Mu\u00e9rdele la cabeza otra vez a prop\u00f3sito.",
    "X para cambiar a blanco. Pinta encima: la cabeza regresa.",
    "Shift+clic en la m\u00e1scara para apagarla: la imagen completa sigue ah\u00ed. Otro Shift+clic.",
    "Alt+rueda al hueco entre el brazo y el cuerpo. Tapa ese hueco con pincel chico.",
])
dices(doc, [
    "Quiero quitarle el fondo. Lo que hace uno la primera vez es agarrar el borrador. "
    "Lo voy a hacer para que veas por qu\u00e9 no.",
    "\u2014 (tras morder la cabeza) \u2014  Le mord\u00ed la cabeza. Y lo malo no es eso: lo malo es que "
    "esos p\u00edxeles ya no est\u00e1n. Si guardo y cierro, los perd\u00ed.",
    "La forma correcta es una m\u00e1scara. Con la capa seleccionada, este bot\u00f3n de abajo. "
    "Y f\u00edjate que apareci\u00f3 un cuadrito blanco junto a la miniatura. Esa es la m\u00e1scara.",
    "Y toda la m\u00e1scara se resume en una frase: lo que pintas de negro se tapa, "
    "y lo que pintas de blanco se vuelve a ver.",
    "La m\u00e1scara no es la imagen. Es una instrucci\u00f3n de qu\u00e9 se muestra.",
    "Clic en el cuadrito. D para poner negro y blanco. B, pincel. Y pinto negro sobre el fondo.",
    "Se va. Pero me pas\u00e9 y le mord\u00ed la cabeza otra vez. X, que cambia a blanco. Pinto encima...",
    "Y regresa. No la recuper\u00e9 de ning\u00fan lado: nunca se fue.",
    "El borrador destruye. La m\u00e1scara tapa. Y tapar se puede deshacer siempre.",
    "Te lo compruebo: Shift con clic en la m\u00e1scara, y la apago. La imagen est\u00e1 completa.",
    "\u2014 (en el hueco del brazo) \u2014  Y aqu\u00ed est\u00e1 el \u00fanico lugar que cuesta. Este hueco entre "
    "el brazo y el cuerpo, donde el fondo se mete dentro de la silueta. Si no lo tapas "
    "te queda un pedazo de fondo colgando, y eso delata un recorte mal hecho.",
    "Si te queda imperfecto no importa: en la clase tres esto se hace en dos clics.",
])
reloj(doc, "deber\u00edas ir en 6:20. Si vas en 8, te alargaste aqu\u00ed.")

parte(doc, 4, "La trampa de la m\u00e1scara", "90 segundos")
haces(doc, [
    "Selecciona la CAPA en vez de la m\u00e1scara y pinta negro encima de la figura.",
    "Se\u00f1ala el borde blanco del recuadro que te dice en cu\u00e1l est\u00e1s. Ctrl+Z.",
    "Ctrl+S.",
])
dices(doc, [
    "Y antes de cerrar, la trampa que nos pasa a todos.",
    "\u2014 (tras el brochazo) \u2014  Acabo de pintar negro encima de la figura. Ten\u00eda seleccionada "
    "la capa, no la m\u00e1scara.",
    "F\u00edjate en el borde blanco: ese recuadro te dice en cu\u00e1l de las dos est\u00e1s parado. "
    "Antes de pintar en una m\u00e1scara, clic en la m\u00e1scara.",
])

parte(doc, 5, "Cierre", "15 segundos")
haces(doc, ["Pantalla final a la Clase 3."])
dices(doc, [
    "Sube tu figura con el fondo tapado a los comentarios.",
    "En la clase tres quitamos ese fondo en dos clics. Y lo vas a entender, "
    "porque hoy lo hiciste a mano. Ah\u00ed te veo.",
])
cierre_notas(doc,
    "Curso de Photoshop desde cero \u2014 Clase 2: capas y m\u00e1scaras explicadas de una vez",
    "la figura con el fondo tapado con m\u00e1scara, guardada en PSD",
    "texto \u201cNO BORRES\u201d. La figura mordida y la limpia, con el borrador tachado.",
    ["El borrador contra la m\u00e1scara \u2014 \u201cDeja de borrar / en Photoshop\u201d",
     "La regla \u2014 \u201cNegro tapa, blanco muestra / ya sabes m\u00e1scaras\u201d"])
guardar(doc, "02 - Capas y mascaras.docx")


# =========================================================== 3
doc = nuevo("CLASE 3", "Recortar la figura  \u00b7  8 minutos",
            "Curso de Photoshop para cajas  \u00b7  Clase 3")
regla(doc, "Esta es la clase que te va a traer gente de la b\u00fasqueda. \u201cQuitar el fondo\u201d "
           "es de lo m\u00e1s buscado del programa: cuida el t\u00edtulo y la miniatura m\u00e1s que en las otras.")
antes(doc, [
    "material\\figura-con-fondo.jpg abierta",
    "El PNG terminado guardado en plantillas\\, por si la toma sale mal",
    "Prueba antes de grabar que Seleccionar sujeto corra r\u00e1pido en tu m\u00e1quina",
])

parte(doc, 1, "Arranque", "20 segundos")
haces(doc, ["Dale a Seleccionar sujeto y ponle la m\u00e1scara. Dos clics, a c\u00e1mara. "
            "La figura queda sola sobre el cuadriculado de transparencia."])
dices(doc, [
    "Soy Richie, seguimos.",
    "Hoy le quitamos el fondo a la figura, y se hace en dos clics. As\u00ed.",
    "Pero lo importante de esta clase no son los dos clics: es qu\u00e9 haces cuando "
    "no alcanzan, que pasa siempre.",
])

parte(doc, 2, "Seleccionar sujeto, y lo que se le olvida", "3 minutos")
haces(doc, [
    "W, y el bot\u00f3n Seleccionar sujeto de la barra de opciones.",
    "Alt+rueda al hueco entre el brazo y el cuerpo: dej\u00f3 fondo adentro.",
    "Error: aprieta Shift y arrastra para quitarlo. Como Shift suma, se mete media imagen. Ctrl+Z.",
    "Ahora con Alt arrastrado: resta. Quita el hueco bien.",
    "Revisa la sombra y qu\u00edtala tambi\u00e9n de la selecci\u00f3n.",
])
dices(doc, [
    "Antes de nada, qu\u00e9 es una selecci\u00f3n: es decirle a Photoshop de aqu\u00ed para dentro s\u00ed, "
    "de aqu\u00ed para fuera no. Esa l\u00ednea punteada que camina es un permiso, no un dibujo.",
    "W, y aqu\u00ed arriba, Seleccionar sujeto. Un clic. Esto busca el objeto de la imagen, "
    "y con una figura as\u00ed le atina casi perfecto.",
    "Casi. Vamos a acercarnos.",
    "Se le olvid\u00f3 el hueco. Dej\u00f3 el pedazo de fondo que se mete entre el brazo y el cuerpo. "
    "Esto pasa siempre.",
    "Se arregla con dos teclas que vas a usar toda la vida: Shift suma a la selecci\u00f3n, "
    "y Alt resta.",
    "\u2014 (tras sumar por error) \u2014  Le di Shift y ahora tengo fondo adentro. Control+Z. "
    "Shift suma, Alt resta.",
    "Con Alt, quito el hueco. Y quito tambi\u00e9n la sombra: la sombra no es la figura, "
    "y si la dejas no puedes poner la figura sobre otro fondo.",
])
reloj(doc, "deber\u00edas ir en 3:20.")

parte(doc, 3, "El paso que casi nadie da", "3 minutos")
haces(doc, [
    "Ctrl+Alt+R: se abre Seleccionar y aplicar m\u00e1scara.",
    "Modo de vista: Sobre negro.",
    "Alt+rueda al borde de la cabeza: se ve una l\u00ednea clara alrededor.",
    "Suavizar 2. Desplazar borde \u22122.",
    "Enciende Descontaminar colores, s\u00fabelo a 50.",
    "Apaga y prende esa casilla tres veces, despacio, con zoom al borde.",
    "Salida: Nueva capa con m\u00e1scara de capa. Aceptar.",
])
dices(doc, [
    "Y ahora el minuto m\u00e1s importante. Casi todos los tutoriales se acaban en el paso anterior, "
    "y por eso casi todos los recortes de internet se ven recortados.",
    "Control+Alt+R. Tiene veinte controles y vamos a usar tres.",
    "Primero, para poder ver: el modo de vista, aqu\u00ed arriba, a Sobre negro.",
    "Y ahora s\u00ed se ve el problema. Esa l\u00ednea clara alrededor de la figura es el fondo viejo "
    "que se qued\u00f3 pegado en la orilla. Eso es lo que hace que un recorte se vea "
    "pegado con tijeras.",
    "Suavizar le quita los escaloncitos: dos. Desplazar borde lo mete un poco hacia dentro: "
    "menos dos.",
    "Y este es el que nadie usa: Descontaminar colores. Le quita el color del fondo viejo "
    "a los p\u00edxeles de la orilla.",
    "M\u00edralo. Prendido. Apagado. Prendido.",
    "Esa es la diferencia entre un recorte que se nota y uno que no. Dos segundos.",
    "Aceptamos. Y mira: la capa original qued\u00f3 intacta y apagada, y arriba hay una nueva "
    "con su m\u00e1scara. No se destruy\u00f3 nada, igual que en la clase dos.",
])
reloj(doc, "deber\u00edas ir en 6:20.")

parte(doc, 4, "Exportar, y el error del JPG", "80 segundos")
haces(doc, [
    "Ctrl+Shift+Alt+W. Formato PNG. Guardar como figura.png.",
    "Expórtalo tambi\u00e9n en JPG y \u00e1brelo: sale con fondo blanco.",
])
dices(doc, [
    "Exportamos. Y aqu\u00ed una cosa que no tiene que ver con seleccionar, pero es de lo m\u00e1s "
    "importante de la clase.",
    "El JPG no sabe hacer transparencia. No puede.",
    "Si exportas esto en JPG, el fondo transparente te sale blanco y perdiste el trabajo. "
    "Te lo ense\u00f1o. Ah\u00ed est\u00e1.",
    "Para algo recortado: PNG. Siempre.",
    "Y guarda este archivo bien, porque es con el que vamos a armar la caja.",
])

parte(doc, 5, "Cierre", "15 segundos")
haces(doc, ["Pantalla final a la Clase 4."])
dices(doc, [
    "Sube tu PNG recortado a los comentarios. Si te sale con el cuadro blanco atr\u00e1s, "
    "ya sabes qu\u00e9 pas\u00f3.",
    "En la clase cuatro vemos c\u00f3mo escalarla sin deformarla, y un clic derecho que "
    "te va a ahorrar horas. Ah\u00ed te veo.",
])
cierre_notas(doc,
    "Curso de Photoshop desde cero \u2014 Clase 3: quitar el fondo de verdad",
    "figura.png, con fondo transparente y el borde limpio",
    "texto \u201c2 CLICS\u201d. La figura con fondo a la izquierda; sola sobre el cuadriculado gris "
    "a la derecha.",
    ["Descontaminar colores \u2014 \u201cEsta casilla arregla / tu recorte en 2 segundos\u201d",
     "El hueco del brazo \u2014 \u201cSeleccionar sujeto / siempre olvida esto\u201d",
     "El JPG \u2014 \u201cTu recorte sale con / fondo blanco por esto\u201d"])
guardar(doc, "03 - Recortar la figura.docx")
print("--- parte 1 lista ---")
