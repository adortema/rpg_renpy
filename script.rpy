# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define p = " "
define enemigo = " "
define heroe_vida_max = 200
define heroe_hp = heroe_vida_max
define ataher= 100

# El juego comienza aquí.

label start:

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

    scene barmed

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    # Presenta las líneas del diálogo.
    # P espera un tiempo y luego baja a nueva linea

    e "hola aventurero,{p=2.0}¿cual es tu nombre?"
    $ p = renpy.input("¿cual es tu nombre?")

    e "%(p)s que estupido, te crees muy valiente no?,\nvienes a estas tierras
     aventurero con ansias de vino y prostitutas maldito enfermo."


    "el bar esta lleno y el ruido atesta el establecibimiento Ardio tu (amigo) te pasa una espada corta"

    $ d20 = renpy.random.randint(1, 20)

    menu:
     "la cogeras?"

     "si.":
         jump si

     "no.":
         jump no

    # esto termina el juego

    label si:
        "la agarras agilmente sin que aparentemente nadie lo note, Oros aquel
         ogro que se te encargo matar esta detras de ti"

        show ogro with dissolve

        "Ardio te pregunta -¿ %(p)s cuando crees que sera mejor atacar? "

        menu:
            "¿ cuando crees que sera mejor atacar?"

            "hacerlo ya.":
                jump ya

            "Esperar la noche":
                jump noche

            "Esperar un rató":
                jump rato

        label ya:
            "Los dos se levantan intentando no generar sospechas con sus movimientos"
            "y se dirigen hacia Oros, tu le dices a Ardio: "

            menu:
                "¿ que le dices a Ardio?"

                "hay que ser sigilosos intentemos atacarle por la espalda.":
                    jump sigi

                "Vamos de frente hombre":
                    jump fren

                "Tu ve Directo yo te cubro con la Ballesta":
                    jump dire

            label sigi:
                " El asiente y hace ademanes de caminar a la ventana y asi rodearle, tu te envuelves entre los salvajes que estan bebiendo a estas horas de la tarde"
                "mientras te diriges hacia el
                 Entonces, por fin llega un punto donde lo puedes atacar sin que lo note "

                menu:
                    "llegas a un punto donde lo puedes atacar sin que lo note "

                    " atacar sin que lo note ":

                        "lo atacas velozmente por la espalda, "
                        $ enemigo ="ogro"
                        $ x = renpy.random.randint(1, 20)
                        if x <= 6:
                             "pero intentando ser sigilosos no usas fuerza suficiente para atravezar su piel"
                             call combate
                             jump continuar_1
                        if x>=7 and x <= 18:
                             "encuentras un equlibrio en el ataque y logras acertarle
                              un buen golpe antes que se levante"
                             call combate
                        if x==19 or x==20:
                             "Logras clavarle la espada muy profunda, causando que este grite de dolor...
                              borbotones de sangre empiezan a salirle e intenta recuperarse para intentas pegarte"
                             "pero no lo logra "
                             call combate
                             
                             
                             

                    "llamarle con una line Epica ":

                        "Oros... Ogro estupido, Hoy sera el dia que perderas la cabeza por lo que hiciste 
					     en Amadore, y le atacas con un amplio corte en horizontal"
                         


                    " LLamarle e insultarle ":
                        "hola mama"

            label fren:
                "Ardio sonrie y los dos se lanzan a la mesa donde esta Oros"
            label dire:
                "Va, pero no falles cabron- te susurra mientras se dirige a la mesa,- tu te quedas a un poco de distancia 10 metros mas o menos"

        label noche:

            "Esperan que se haga de noche y Oros pasa todo el dia halli bebiendo, llegado al punto de incluso emborracharse;"
            "muy comveniente para ustedes... pero sin embargo Ardio a pesar de que tu intentaste que no bebiera se halla borracho tambien"
            return
        label rato:

            "Tu insiste en mejor esperar un rató"
            "Esperan unos 20 minutos y Ardio tan impaciente como siempre debido a que no dijiste un tiempo exacto se levanta derrepente, llamando un poco la atencion"

            menu:
                "¿te levantas?"

                "si.":
                    "te levantas tras el rapido, haciendolo todo un poco mas sospechoso"

                "no.":

                    "Tu disimulas quedandote, el te mira y sigue sin mas"
                    "-de todas formas tengo mi miniballesta y otro compañero no me vendria mal- te dices;"


    return

    label no:
        " Respondes en negativa, pretendes esperar un mejor momento para matar a Oros, aquel peligroso ogro que se les encargo"
        "pero aun asi este movimiento descuidado de tu compañero causa miradas de aquellos cercanos,el cantinero con su voz ronca te dice -ya vienen ustedes nuckheald a armar revuelo"

        menu:
            "que accion tomaras?"

            "intentar usar Carisma":
                "Le dices: mi amigo es algo maleducado, le pedi su espada corta para afeitarme y me la apasado asi nada mas con ese ruido, no tenemos encargo ahora mismo"

            "no responder":
                "Te quedas callado,cosa que normalmente seria incomoda, pero con el ruido no pasa por tal; ademas de que el caninero parece haber lidiado con muchos de tu calaña"


            "atemorizarlo":

                "Tu a esto le respondes con un seco -No me hables maldito cantinero, sirve y calla- el caninero escupe al frnte tuya y calla sin mas"






    # Finaliza el juego:

    return

    label continuar_1:


    return
