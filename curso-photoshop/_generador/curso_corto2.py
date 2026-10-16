# -*- coding: utf-8 -*-
"""Curso corto, clases 4 a 8."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from curso_corto_base import (nuevo, regla, reloj, antes, cierre_notas, guardar,
                              DISCIPLINA)
from guion_docx import parte, haces, dices, nota, h2, parrafo

# =========================================================== 4
doc = nuevo("CLASE 4", "Escalar sin deformar, y objetos inteligentes  ·  7 minutos",
            "Curso de Photoshop para cajas  ·  Clase 4")
regla(doc, DISCIPLINA.format(dur="7 minutos", tope="9"))
antes(doc, [
    "figura.png, el recorte de la clase 3. Si esa toma salió mal, hay copia en plantillas\\",
    "Una segunda imagen de figura lista, para el truco de Reemplazar contenido",
])

parte(doc, 1, "Arranque", "15 segundos")
haces(doc, ["Enseña la figura bien, y al lado la misma apachurrada. Dos segundos cada una."])
dices(doc, [
    "Soy Richie, seguimos.",
    "Hoy: cómo cambiarle el tamaño a algo sin arruinarlo. Suena simple y tiene dos trampas, "
    "y las dos se ven feo.",
    "Son siete minutos y te vas con un clic derecho que te va a ahorrar horas.",
])

parte(doc, 2, "Control+T y la trampa de deformar", "2 minutos y medio")
haces(doc, [
    "Ctrl+T sobre la figura. Señala los ocho cuadritos.",
    "Jala del cuadrito DEL LADO hasta dejarla estirada. Quédate 4 segundos; los dos primeros, callado.",
    "Ctrl+Z.",
    "Ctrl+T otra vez y jala de la ESQUINA. Señala la cadenita de la barra de opciones. Enter.",
])
dices(doc, [
    "Control+T, transformar. Sale un recuadro con ocho cuadritos: cuatro en las esquinas "
    "y cuatro en los lados.",
    "— (tras estirarla, después del silencio) —  Mira lo que acabo de hacer. "
    "Le apachurré la cabeza.",
    "En una figura así se nota mucho, porque la cabeza es más grande que el cuerpo. "
    "Esa proporción es la forma del muñeco: si la cambias, deja de verse como lo que es.",
    "Control+Z. Y lo que pasó es esto: si jalas de la esquina, se mantiene la proporción. "
    "Si jalas del lado, lo deformas.",
    "Y si quieres estar seguro, aquí arriba entre el ancho y el alto hay una cadenita. "
    "Con la cadena cerrada no se deforma, jales de donde jales.",
    "Una costumbre que te dejo: antes de darle Enter a cualquier transformación, "
    "mira si lo que era redondo sigue siendo redondo. Tres segundos, y te ahorra el ridículo.",
])
reloj(doc, "deberías ir en 2:45.")

parte(doc, 3, "La trampa de agrandar", "90 segundos")
haces(doc, [
    "Ctrl+T, reduce al 30%. Enter.",
    "Ctrl+T, súbela de vuelta al 100%. Enter.",
    "Alt+rueda para acercarte: borrosa y con la orilla sucia.",
])
dices(doc, [
    "Segunda trampa. Reduzco la figura al treinta por ciento, y la vuelvo a subir al cien.",
    "Y mírala: borrosa.",
    "La razón es que al reducir, Photoshop tira píxeles, y tirar es fácil. Al agrandar tiene "
    "que inventar píxeles que nunca existieron. No es que lo haga mal: es que no hay "
    "información que poner.",
    "La regla: nunca agrandes una imagen más de lo que mide. Trabaja siempre con el archivo "
    "más grande que tengas y redúcelo. Nunca al revés.",
])
reloj(doc, "deberías ir en 4:15.")

parte(doc, 4, "La solución a las dos", "2 minutos")
haces(doc, [
    "Clic derecho en la capa › Convertir en objeto inteligente. Señala el cuadrito de la miniatura.",
    "Ctrl+T, redúcela al 20%. Enter. Ctrl+T, súbela al 100%. Enter. Zoom: sigue nítida.",
    "Clic derecho › Reemplazar contenido. Escoge la otra imagen de figura.",
    "Señala que entró del mismo tamaño y en la misma posición.",
])
dices(doc, [
    "Y ahora el truco que hace que las dos trampas dejen de importar.",
    "Clic derecho en la capa, Convertir en objeto inteligente. Fíjate que a la miniatura "
    "le apareció un cuadrito.",
    "Lo que acabo de hacer es meter la imagen en una cajita. Lo que ves es una vista previa; "
    "el original está guardado completo adentro.",
    "Y por eso ahora puedo reducirla al veinte, aplicar, y subirla otra vez al cien...",
    "Y sigue nítida. Porque no estaba escalando píxeles: estaba cambiando el tamaño de la "
    "vista previa. El original nunca se tocó.",
    "Y hace otra cosa, que es la buena. Clic derecho, Reemplazar contenido. Le doy otra imagen...",
    "Y entró del mismo tamaño, en la misma posición. No acomodé nada.",
    "Quédate con eso, porque en la clase seis vamos a meter la figura en las cuatro caras "
    "de la caja. Y gracias a esto, cuando cambies de figura, se cambian las cuatro solas.",
])

parte(doc, 5, "Cierre", "15 segundos")
haces(doc, ["Guarda. Pantalla final a la Clase 5."])
dices(doc, [
    "Deja tu figura convertida en objeto inteligente y guardada, porque de ahí partimos.",
    "En la clase cinco le ponemos el nombre y el número. Ahí te veo.",
])
cierre_notas(doc,
    "Curso de Photoshop desde cero — Clase 4: escalar sin deformar (y sin pixelear)",
    "la figura convertida en objeto inteligente, guardada",
    "texto “NO LA APACHURRES”. La figura bien y la apachurrada, con una tacha.",
    ["Reemplazar contenido — “Clic derecho, Reemplazar / y entra solo en su lugar”",
     "La cabeza apachurrada — “¿Ves qué tiene de malo? / la cabeza no es redonda”"])
guardar(doc, "04 - Escalar sin deformar.docx")


# =========================================================== 5
doc = nuevo("CLASE 5", "El texto de la caja  ·  7 minutos",
            "Curso de Photoshop para cajas  ·  Clase 5")
regla(doc, DISCIPLINA.format(dur="7 minutos", tope="9"))
antes(doc, [
    "El archivo de la clase 4 abierto",
    "Decidido el nombre y el número que le vas a poner. No se piensa en cámara",
    "Si vas a usar una fuente de Adobe Fonts, actívala ANTES de grabar",
])

parte(doc, 1, "Arranque", "15 segundos")
haces(doc, ["Enseña el nombre puesto en la caja, bien, y luego una versión ilegible de tan chica."])
dices(doc, [
    "Soy Richie, seguimos.",
    "Hoy ponemos el texto: el nombre y el número. Y el objetivo no es que se vea bonito, "
    "es que se lea cuando la caja esté en tu mano.",
])

parte(doc, 2, "Poner el texto", "2 minutos y medio")
haces(doc, [
    "T, clic en el lienzo, escribe el nombre.",
    "Error: aprieta Enter. Hace un renglón nuevo. Ctrl+Enter para cerrar.",
    "Señala arriba el tamaño, la fuente y el color.",
    "T otra vez, escribe el número, chico. Ctrl+Enter.",
    "Señala en el panel que son dos capas distintas.",
])
dices(doc, [
    "T, de texto. Clic, y escribo el nombre.",
    "— (tras el Enter) —  Y aquí el error de todos: para cerrar el texto, Enter no sirve. "
    "Enter hace un renglón nuevo. Se cierra con Control+Enter.",
    "El tamaño, la letra y el color están aquí arriba, porque ahora la herramienta "
    "que traigo es el texto.",
    "Ahora el número, en otra capa. Dos textos, dos capas. Nunca los dos en la misma: "
    "si están juntos no puedes mover uno sin mover el otro.",
    "Y ese número no es adorno: en la clase ocho, cuando hagamos que esto se arme solo, "
    "el nombre y el número van a ser los dos datos que cambian en cada caja.",
])
reloj(doc, "deberías ir en 2:45.")

parte(doc, 3, "Que se lea de verdad", "2 minutos y medio")
haces(doc, [
    "Baja el zoom al 25% para ver la caja al tamaño aproximado que tiene en la mano.",
    "Enseña que el nombre no se lee. Súbele el tamaño.",
    "Abre el panel Carácter y enseña el tracking. Súbelo un poco en el nombre.",
    "Prueba una fuente gruesa contra una delgada: enseña cuál aguanta.",
])
dices(doc, [
    "Y ahora la parte que de verdad importa, porque esto se va a imprimir.",
    "Bajo el zoom para verlo más o menos del tamaño que va a tener en la mano. Y mira: "
    "el nombre casi no se lee.",
    "Esa es la única prueba que vale. No lo veas al cien por ciento en tu monitor de "
    "veinticuatro pulgadas: veío chiquito, como lo va a ver quien lo tenga.",
    "Dos cosas lo arreglan. La primera, obvia: más grande.",
    "Y la segunda, que casi nadie usa: el tracking, que es el espacio entre las letras. "
    "Está en el panel Carácter. Si le subes un poco al nombre, se lee mucho mejor "
    "a tamaño chico.",
    "Y de fuente, en algo que se va a imprimir chico, una gruesa aguanta y una delgada "
    "se pierde. No es cuestión de gusto.",
])
reloj(doc, "deberías ir en 5:15.")

parte(doc, 4, "Agrupar y guardar", "80 segundos")
haces(doc, [
    "Selecciona las dos capas de texto y Ctrl+G. Nombra la carpeta “textos”.",
    "Error: con la capa de texto seleccionada, intenta mover la figura. Se mueve el texto.",
    "Ctrl+S.",
])
dices(doc, [
    "Agrupo los dos textos con Control+G, en una carpeta que diga textos. Con dos capas "
    "parece exagerado; cuando tengas quince, no.",
    "— (al mover el texto por error) —  Capa equivocada, otra vez. Siempre se arregla igual: "
    "mira el panel.",
    "Guardamos.",
])

parte(doc, 5, "Cierre", "15 segundos")
haces(doc, ["Pantalla final a la Clase 6."])
dices(doc, [
    "Sube tu nombre y tu número puestos. Y mirálo chiquito antes de subirlo: ¿se lee?",
    "En la clase seis armamos la caja completa. Ahí te veo.",
])
cierre_notas(doc,
    "Curso de Photoshop desde cero — Clase 5: el texto, y que se lea de verdad",
    "el nombre y el número puestos, legibles a tamaño real",
    "texto “¿SE LEE?”. El nombre grande y el mismo chiquito e ilegible.",
    ["El Ctrl+Enter — “Tu texto no se cierra / con Enter”",
     "El tracking — “Si tu texto no se lee / no es el tamaño”"])
guardar(doc, "05 - El texto de la caja.docx")


# =========================================================== 6
doc = nuevo("CLASE 6", "Armar la caja  ·  9 minutos",
            "Curso de Photoshop para cajas  ·  Clase 6")
regla(doc, "Esta es la clase donde el curso cumple lo que prometió. Al terminarla hay una caja "
           "en pantalla. Vale la pena que dure 9.")
antes(doc, [
    "plantillas\\plantilla-caja.psd: TU plantilla, con TU marca. Ningún logo ni nombre de cliente",
    "La plantilla ya limpia: borra lo que no se vaya a usar en la clase, para que el panel "
    "de capas no asuste",
    "figura.png de la clase 3",
    "La caja terminada guardada aparte, por si hay que repetir la toma",
])

parte(doc, 1, "Arranque", "20 segundos")
haces(doc, ["Enseña la caja terminada, girando o en mockup si lo tienes. 4 segundos."])
dices(doc, [
    "Soy Richie, y esta es la clase donde armamos la caja.",
    "Todo lo que vimos en las cinco anteriores —capas, máscaras, el recorte, los objetos "
    "inteligentes, el texto— era para llegar aquí.",
    "En nueve minutos vas a tener esto.",
])

parte(doc, 2, "Cómo está hecha una plantilla de caja", "2 minutos")
haces(doc, [
    "Abre plantilla-caja.psd. Ctrl+0 para verla completa.",
    "Señala las caras: frente, lados, arriba, atrás.",
    "Señala las líneas de doblez y las de corte.",
    "Abre y cierra los grupos del panel de capas, señalando qué hay en cada uno.",
])
dices(doc, [
    "Esto es una caja desarmada, plana. Cuando se imprime y se dobla, cada uno de estos "
    "pedazos es una cara.",
    "El frente, los dos lados, la de arriba y la de atrás.",
    "Y estas líneas son por dónde se dobla y por dónde se corta. Esas no se imprimen: "
    "son guías, y en la clase siete las vamos a apagar antes de mandar el archivo.",
    "En el panel de capas está todo agrupado por lo que hace: los fondos, la figura, "
    "los textos. Así es como se trabaja un archivo que tiene muchas partes: "
    "en carpetas, no en cuarenta capas sueltas.",
])

parte(doc, 3, "Meter la figura en las cuatro caras", "3 minutos y medio")
haces(doc, [
    "Arrastra figura.png a la plantilla.",
    "Clic derecho › Convertir en objeto inteligente.",
    "Ctrl+T, escala desde la esquina para que entre en la cara del frente. Enter.",
    "Ctrl+J para duplicar. Mueve la copia a otra cara y ajústala.",
    "Repite hasta tener la figura en las caras que lleven figura.",
    "Nombra cada capa: figura frente, figura lado, etc.",
    "Ctrl+S.",
])
dices(doc, [
    "Meto la figura, y lo primero que hago es convertirla en objeto inteligente, "
    "como en la clase cuatro.",
    "Control+T para que entre en la cara del frente. Desde la esquina, siempre.",
    "Y ahora Control+J para duplicarla, y la llevo a la otra cara.",
    "Fíjate en lo que estoy haciendo: cada cara es su propia capa, con su propio tamaño. "
    "No estoy estirando una sola figura por toda la caja.",
    "Y les pongo nombre conforme las voy haciendo. Figura frente, figura lado. "
    "Diez segundos ahora, media hora menos después.",
])
reloj(doc, "deberías ir en 6:00.")

parte(doc, 4, "El pago de haber usado objetos inteligentes", "90 segundos")
haces(doc, [
    "Clic derecho en una de las capas de figura › Reemplazar contenido. Pon otra figura.",
    "Enseña que entró en su lugar, del mismo tamaño.",
    "Hazlo en una segunda cara para que se vea el patrón.",
])
dices(doc, [
    "Y aquí está el pago de haber hecho objetos inteligentes en la clase cuatro.",
    "Si mañana te llega otro pedido con otra figura, no rehaces la caja. Clic derecho, "
    "Reemplazar contenido, y ya.",
    "Entra del mismo tamaño, en el mismo lugar, en cada cara.",
    "Esto es lo que convierte una caja de dos horas en una caja de diez minutos. "
    "Y en la clase ocho lo vamos a llevar todavía más lejos.",
])

parte(doc, 5, "Cierre", "20 segundos")
haces(doc, ["Ctrl+S. Pantalla final a la Clase 7."])
dices(doc, [
    "Guarda el PSD y no lo borres nunca: ese es tu original, y es la plantilla con la que "
    "vas a hacer la siguiente.",
    "Sube tu caja a los comentarios.",
    "En la clase siete la dejamos lista para la imprenta: trescientos ppp, CMYK, sangrado, "
    "y un PDF que no te regresen. Ahí te veo.",
])
cierre_notas(doc,
    "Curso de Photoshop desde cero — Clase 6: armamos la caja completa",
    "la caja armada en pantalla, guardada en PSD",
    "texto “LA CAJA”. La plantilla plana a la izquierda, la caja armada a la derecha.",
    ["Reemplazar contenido en las 4 caras — “Cambia la figura una vez / y se cambian las cuatro”",
     "La plantilla plana — “Así se ve una caja / antes de doblarse”"])
guardar(doc, "06 - Armar la caja.docx")


# =========================================================== 7
doc = nuevo("CLASE 7", "El PDF para la imprenta  ·  7 minutos",
            "Curso de Photoshop para cajas  ·  Clase 7")
regla(doc, "Esta clase es la que separa un diseño de un trabajo entregable. Es poco "
           "espectacular y es la que más te van a agradecer.")
antes(doc, [
    "La caja de la clase 6 abierta",
    "Un PDF bueno ya exportado en plantillas\\, por si hay que repetir",
    "Si tu imprenta te pidió algo específico, ténlo a la mano para decirlo en cámara",
])

parte(doc, 1, "Arranque", "15 segundos")
haces(doc, ["Enseña el PDF abierto, con las marcas de corte."])
dices(doc, [
    "Soy Richie, seguimos.",
    "Hoy convertimos la caja en un archivo que la imprenta acepte a la primera. "
    "Son cuatro cosas, y si te falta una, te lo regresan.",
])

parte(doc, 2, "Las cuatro cosas", "3 minutos")
haces(doc, [
    "Ctrl+Alt+I: enseña la resolución. Con Remuestrear APAGADO, enseña 72 contra 300.",
    "Imagen › Modo › Color CMYK. Enseña cómo cambian los colores más vivos.",
    "Señala el sangrado de la plantilla: el diseño que se pasa de la línea de corte.",
    "Apaga las capas de guías, líneas de doblez y cualquier cosa que no se imprima.",
])
dices(doc, [
    "Primero: la resolución. Para pantalla usamos setenta y dos, y para imprimir se usan "
    "trescientos.",
    "Y aquí hay una confusión muy común: los ppp no son calidad. Son una instrucción para "
    "la impresora de qué tan apretados poner los puntos. Si tu imagen es chica, "
    "poner trescientos no la arregla: no inventa información.",
    "Segundo: el color. En pantalla trabajamos en RGB, que es luz. La impresora trabaja "
    "con tinta, y eso es CMYK. Imagen, Modo, Color CMYK.",
    "Y fíjate que algunos colores se apagaron un poco. No se dañó nada: es que esos tonos "
    "no existen en tinta. Mejor que lo veas tú ahora a que te sorprenda impreso.",
    "Tercero: el sangrado. ¿Ves que el diseño se pasa un poco de la línea de corte? "
    "Eso es a propósito. Las guillotinas no cortan exacto, y si el color llega justo "
    "a la línea, te va a quedar un filo blanco. Tres milímetros de más lo resuelven.",
    "Y cuarto: apagar lo que no se imprime. Las guías, las líneas de doblez, cualquier "
    "nota que tengas. Si se queda prendido, se imprime.",
])
reloj(doc, "deberías ir en 3:15.")

parte(doc, 3, "Guardar el PDF", "2 minutos")
haces(doc, [
    "Archivo › Guardar como › Photoshop PDF.",
    "Preajuste: Calidad de prensa.",
    "Desmarca la compresión agresiva si la trae.",
    "Guardar. Abre el PDF y recórrelo en pantalla.",
])
dices(doc, [
    "Archivo, Guardar como, y escoges PDF de Photoshop.",
    "En preajuste, Calidad de prensa. Ese ya trae puestas las opciones correctas "
    "para imprimir.",
    "Y lo guardamos.",
    "Ahora ábrelo y revísalo tú, antes de mandarlo. Mira que esté completo, que no "
    "se haya quedado una capa apagada que sí debía ir, y que el texto esté donde lo dejaste.",
    "Esa revisión de treinta segundos te ahorra un reimpreso.",
])

parte(doc, 4, "Qué preguntarle a tu imprenta", "90 segundos")
haces(doc, ["A cámara o sobre el PDF abierto."])
dices(doc, [
    "Y un consejo que vale más que todo lo anterior: antes de mandar nada, pregúntale "
    "a tu imprenta tres cosas.",
    "Cuánto sangrado quieren. Tres milímetros es lo normal, pero cada quien pide lo suyo.",
    "Si lo quieren en CMYK o si ellos lo convierten. Algunas prefieren convertirlo "
    "con su propio perfil.",
    "Y en qué material y a qué tamaño lo van a imprimir, para que tu archivo salga "
    "de ese tamaño desde el principio.",
    "Preguntar eso una vez te ahorra tres idas y vueltas. Y si eres tú quien imprime, "
    "haz una prueba en papel normal antes de gastar el material bueno.",
])

parte(doc, 5, "Cierre", "15 segundos")
haces(doc, ["Pantalla final a la Clase 8."])
dices(doc, [
    "Ya tienes tu caja lista para imprimir. Si la imprimes, mándame la foto.",
    "Y en la clase ocho, la última, vamos a hacer que Photoshop haga todo esto solo. "
    "Ahí te veo.",
])
cierre_notas(doc,
    "Curso de Photoshop desde cero — Clase 7: el PDF que la imprenta acepta",
    "caja.pdf a 300 ppp, en CMYK, con sangrado",
    "texto “300 PPP”. El PDF con sus marcas de corte.",
    ["Los ppp — “Los 300 ppp no son / calidad de imagen”",
     "El sangrado — “Por esto te sale / un filo blanco al cortar”"])
guardar(doc, "07 - El PDF para la imprenta.docx")


# =========================================================== 8
doc = nuevo("CLASE 8", "Que Photoshop lo haga solo  ·  9 minutos",
            "Curso de Photoshop para cajas  ·  Clase 8")
regla(doc, "La clase que separa este curso de todos los demás. Llega cuando el alumno "
           "ya hizo una caja a mano y sabe cuánto cuesta. Vale la pena que dure 9.")
antes(doc, [
    "Una carpeta con 10 o 20 imágenes de figura, para el lote",
    "La acción ya probada ANTES de grabar: que corra sin errores",
    "La carpeta de salida vacía, para que se vea llenarse",
])

parte(doc, 1, "Arranque", "20 segundos")
haces(doc, ["Arranca el lote y deja correr la barra de progreso 4 segundos, sin hablar. "
            "Después enseña la carpeta llenándose."])
dices(doc, [
    "(entra a los 4 segundos)  Soy Richie, y esta es la última clase del curso.",
    "Esto que estás viendo no lo estoy haciendo yo. Lo está haciendo Photoshop solo, "
    "con lo que le enseñé una vez.",
    "Y en nueve minutos vas a poder hacerlo tú.",
])

parte(doc, 2, "Qué es una acción", "3 minutos")
haces(doc, [
    "Ventana › Acciones. Crea un conjunto nuevo con tu nombre.",
    "Crea una acción nueva. Dale Grabar.",
    "Haz una secuencia corta y útil: por ejemplo abrir, cambiar tamaño a 2000x2000, "
    "convertir a RGB, exportar JPG calidad 80, cerrar.",
    "Dale Detener.",
    "Señala la lista de pasos que quedó grabada, y abre uno para enseñar que guardó el número.",
    "Abre otra imagen y dale Reproducir. Enséñalo correr.",
])
dices(doc, [
    "Una acción es una grabadora. Le das grabar, haces algo una vez, y le das detener. "
    "A partir de ahí lo puede repetir.",
    "Ventana, Acciones. Creo un conjunto con mi nombre, y adentro una acción nueva.",
    "Grabar. Y ahora hago lo que quiero que aprenda.",
    "— (al terminar) —  Detener.",
    "Y mira lo que quedó: cada paso que hice, en orden. Y si abro uno, guardó "
    "el número exacto.",
    "Por eso en las clases anteriores insistí en escribir los números en vez de jalar "
    "con el ratón: una acción graba el número, no el movimiento del ratón.",
    "Ahora abro otra imagen, y le doy Reproducir. Y lo hace solo.",
])
reloj(doc, "deberías ir en 3:20.")

parte(doc, 3, "El lote: una carpeta entera", "3 minutos")
haces(doc, [
    "Archivo › Automatizar › Lote.",
    "Conjunto y acción: los que acabas de hacer.",
    "Origen: Carpeta, y escoges la de las 20 imágenes.",
    "Destino: Carpeta, y escoges la de salida vacía.",
    "Aceptar. Deja correr y enseña la carpeta de salida llenándose.",
])
dices(doc, [
    "Y ahora lo bueno. Archivo, Automatizar, Lote.",
    "Le digo qué acción quiero, de qué carpeta tomar las imágenes, y en qué carpeta "
    "dejar las terminadas.",
    "Y aceptar.",
    "— (mientras corre) —  Eso que está pasando ahí, hecho a mano, son veinte minutos. "
    "Así son cuarenta segundos.",
    "Y no es que vaya más rápido que tú: es que no se cansa, no se distrae y no se equivoca "
    "en la número diecisiete.",
])
reloj(doc, "deberías ir en 6:30.")

parte(doc, 4, "Qué sí y qué no automatizar", "90 segundos")
dices(doc, [
    "Pero no todo se automatiza, y conviene que lo sepas antes de frustrarte.",
    "Se automatiza bien lo que es siempre igual: cambiar de tamaño, convertir a un modo "
    "de color, exportar, poner una marca de agua, renombrar.",
    "No se automatiza bien lo que necesita criterio: recortar una figura, acomodar algo "
    "para que se vea bien, decidir un color.",
    "Y la trampa clásica: una acción se rompe si el archivo no es como el que usaste "
    "al grabarla. Si grabaste con una imagen horizontal y le pasas una vertical, "
    "te la va a dejar mal.",
    "Así que prueba tu acción con dos o tres antes de soltarle doscientas.",
])

parte(doc, 5, "Cierre del curso", "60 segundos")
haces(doc, [
    "Enseña la caja terminada, el PDF y la carpeta llena, uno tras otro.",
    "Pantalla final: la lista completa del curso, no un video suelto.",
])
dices(doc, [
    "Y con esto cerramos el curso.",
    "En ocho clases pasaste de abrir Photoshop por primera vez a tener una caja lista "
    "para imprimir, y a que el programa te haga el trabajo repetido.",
    "No viste todo Photoshop. Viste lo que se usa. Las demás herramientas existen "
    "y las vas a ir encontrando cuando las necesites.",
    "Lo que sí te pido: haz una caja tuya. Con tu figura, tu nombre, tu marca. "
    "Y súbela a los comentarios, que las quiero ver.",
    "Si este curso te sirvió, lo mejor que puedes hacer es dejarlo en los comentarios "
    "o pasárselo a alguien que esté empezando.",
    "Yo sigo subiendo cosas de esto al canal. Gracias por llegar hasta aquí.",
])
nota(doc, "Si más adelante quieres vender tu script de armado de cajas, este es el video "
          "donde la gente ya entendió qué problema resuelve. No lo menciones todavía: "
          "se agrega después, en la descripción y en un comentario fijado.")
cierre_notas(doc,
    "Curso de Photoshop desde cero — Clase 8: que Photoshop haga el trabajo solo",
    "una acción propia y una carpeta procesada en lote",
    "texto “SOLO” sobre negro, con la barra de progreso y la carpeta llenándose.",
    ["El lote corriendo — “Estas 20 las hizo / Photoshop solo”",
     "Grabar la acción — “Photoshop tiene grabadora / y casi nadie la usa”",
     "Qué no automatizar — “Esto NO lo automatices / nunca”"])
guardar(doc, "08 - Que Photoshop lo haga solo.docx")
print("--- parte 2 lista ---")
