# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")
define p = " "
define enemigo = " "
define heroe_vida_max = 200
define heroe_hp = heroe_vida_max
define ataher= 100
define a = Character("Ardio")
define ck = Character("Cantinero")
define yo = Character("dices")

$ enemigo = "ogro"

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
                             #call combate
                             jump continuar_1
                        if x>=7 and x <= 18:
                             "encuentras un equlibrio en el ataque y logras acertarle
                              un buen golpe antes que se levante"
                             #call combate
                        if x==19 or x==20:
                             "Logras clavarle la espada muy profunda, causando que este grite de dolor...
                              borbotones de sangre empiezan a salirle e intenta recuperarse para intentas pegarte"
                             "pero no lo logra "
                             #call combate

                    "llamarle con una line Epica ":

                        "Oros... Ogro estupido, Hoy sera el dia que perderas la cabeza por lo que hiciste
					    en Amadore, y le atacas con un amplio corte en horizontal  "
                        $ x = rempy.random.randint(1, 20)

                        if x <= 3:
                             "Oros ya estando alerta esquiva tu ataque y con mucha fuerza arranca la espada
						      de tus manos  "
                              #call combate

                        if x>=4 and x<=20:
                             "el cual logra atravezar su armadura, marcando la linea del corte,
						      un buen golpe para empezar la pelea"
                              #call combate


                    " LLamarle e insultarle ":

                        "le dices: Oros... pedazo de mierda, Te voy a partir en trozos hijo de puta
					    esto viene de parte de la gente de Amadore,
					    y le atacas con un amplio corte en horizontal  "
                        $ x = rempy.random.randint(1, 20)

                        if x <= 2:
                             "Oros ya estando alerta esquiva tu ataque y con furia en su rostro, te golpea
						     dejandorte la cabeza dando vueltas y con una leve sensacion de vomito
						     por las cervesas que te habias tomado "

                             $ v = rempy.random.randit(1, 20)
                             if v<=10:
                                 "Esta sensacion se comvierte en necesidad y le vomitas encima a oros
							      que ahora esta mas enojado "

                        if x>=2 and x<=7:
                             "Oros ya estando alerta logra esquivar tu ataque "
                              #call combate


                        if x>=8 and x<=20:
                             "el cual logra atravezar su armadura, marcando la linea del corte
						      un buen golpe antes que se levante"
                              #call combate

                "Ardio mientras tu haces lo tuyo ataca a los acompañantes de Oros
                y empiza la revuelta"


            label fren:
                 "Ardio sonrie y los dos se lanzan a la mesa donde esta Oros
                 el esta distraido, por lo que inmediatamente atacan"

                 $ x = random.randit(1, 20)

                 if x <= 3:
                     "tu tomas la delantera como siempre
                      pero resbalas causando que Ardio lo haga tras de ti, causando la risa de varios
                      y causando que Oros se percate de su precensia"
                 else:
                     "acestando un buen primer golpe"
                      #call combate

            label dire:
                 "Va, pero no falles cabron- te susurra mientras se dirige a la mesa,- tu te quedas a un poco de distancia 10 metros mas o menos
                 el se adelanta y tu te quedas a un poco de distancia 10 metros mas o menos
			     El ataca, y tu desde atraz disparas con la ballesta"

                 $ x = random.randit(1, 20)

                 if x<=3:
                     "pero que mas suerte de todos le das a Ardio en la cabeza
					 - Bueno que mas da es hora de los golpes - dices tu "

                 if x>=4 and x<=18:
                     "golpeandolo con el perno en el brazo
					 - ahora es el momento de los golpes - dices tu "

                 if x>=19:
                      "el pernon viaja precisamente por el aire clavandosele a ardio
					  en el pecho, causandole daño evidente "

                 #call combat

        label noche:

            "Esperan que se haga de noche y Oros pasa todo el dia halli bebiendo, llegado al punto de incluso emborracharse;"
            "muy comveniente para ustedes... pero sin embargo Ardio a pesar de que tu intentaste que no bebiera se encuentra borracho tambien"
            menu:
                "hijo de puta":
                    jump hp

                "   cabron  ":
                    jump hp

                "pedazo de mierda":
                    jump hp

                "no decir nada...":
                    jump nada

            label hp:
                "le regañas y el te contesta:    "
                a "¿!!! vamos a matar a ese Ogro mierda ya, no¡¡¡? "
                "...............  "
                "...............  "
                "¡¡¡Si vamos a matar a ese ogro de mierda¡¡¡    grita todo el mundo"
                "se levanta todo el mundo y se le tiran encima a  Oros y los otros que lo acompañan "
                " ... esto es muy estupido piensas tu,  pero aprocehas los acontecimientos,  Oros esta borracho y es todo el bar
                contra él.... "
                "de todas formas Oros es fuerte y los derrota despues de un rató "
                "¡¡¡es tu momento, Oros esta cansado y herido, te lanzas al ataque  "
                #call combate

            label nada:
                "piensas -pedazo de mierda- pero no dices nada"
                menu:
                    "decirle que se quede ":
                         jump sinA
                    "vamos a por Oros ya... ":
                        jump Ar
                label sinA:

                     "el te responde -ughhhhhhhh - y se queda dormido.
                     bueno, ahora estas tu solo pero tienes la ventaja de estar osbrio,
                     ademas del factor sorpresa "
                     "recuerda aventurero que ademas de tu Espada corta, llevas una miniballesta"

                     menu:
                        "acercarte y usar espada corta  ":
                            jump ec
                        "usar la ballesta desde halli ":
                            jump mb


                     label mb:
                             "tranquilamente le disparas con la ballesta"
                             $ x= ramdon.randit (1, 20)

                             if x>=0 and x<=18:
                                 "golpeandolo con el perno en el brazo
							     El se voltea y te ve, con ojos perdidos de la borrachera"
                                 "- ahora es el momento de los golpes - piensas "

                                 #call combate

                             if x>=19:

                                 "el pernon viaja precisamente por el aire clavandosele a ardio
							     en la cabeza, haciendolo sangrar y estar confundido
							     tu aprovechas esta situacion para acercarte a el y acuchillarle"

                                 $ v= ramdon.randit (1, 20)

                                 if v>=10:

                                     "lo cual haces con suprema destreza degollandole por detras, llenando
								     asi todo el suelo con su sangre "
                                     "ahora todo es mas sencillo solo tienes que encargarte de los otros
                                     2 que le acompañaban "
                                      #call combate

                                 else:

                                     "lo cual haces con suprema destreza clavandole la espada por el costado
                                      haciendole un monton de daño
                                      pero ahora si empieza el manbo "
                                      #call combate
        label rato:

            "Tu insiste en mejor esperar un rató"
            "Esperan unos 20 minutos y Ardio tan impaciente como siempre, se levanta derrepente llamando un poco la atencion"

            menu:
                "¿te levantas?"

                "si.":
                    "te levantas tras el rapido, haciendolo todo un poco mas sospechoso"
                    "pero bien sabes que no lo podras comvencer asi que no gastas saliva intentandolo"
                    "mas bien la desicion que tienes que tomar es..."

                    menu:
                        "¿te quedas detras?":
                            "esta vez te quedas atras, de todas formas este movimiento tan poco elegante
                            es culpa del invecil de Ardio"
                            "y Ardio mientras tu piensas en esto, ataca a Oros asi nada mas, empezando una revuelta"
                            #call combate


                        "¿te adelantas?":
                            " tu tomas la delantera como siempre
        					Y ya estando en esta situacion lo unico que te queda es atacar"

                            $ x = random.randit(1, 20)

                            if x<=2:
                                "pero resbalas causando que Ardio lo haga tras de ti, causando la risa de varios
        						y causando que Oros se percate de su precensia"
                            else:
                                "y sorprendiendole le causas el primer golpe "
                                #call combate

                "no.":

                    "Tu disimulas quedandote, el te mira y sigue sin mas"
                    "-de todas formas tengo mi miniballesta y otro compañero no me vendria mal-    te dices;"
                    " El ataca, y tu desde atraz disparas con la ballesta"
                    $ x = random.randit (1, 20)

                    if x<=3:
                         "pero que cosa... de todos le das a Ardio en la espalda..
                    	  esa no era tu intencion pero,
                         -Bueno que mas da es hora de los golpes - dices tu "
                         #call combate
                    if x>=4 and x<=18:
                         "golpeando a Oros con un perno en el brazo
                          - ahora es el momento de los golpes - dices tu "
                          #call combate
                    if x>=19:
                         "el pernon viaja precisamente por el aire clavandosele a ardio
                		 en el pecho, causandole daño evidente "
                           #call combate

    return

    label no:
         "Respondes en negativa, pretendes esperar un mejor momento para matar a Oros, que es el encargo que les dejaron en Amadore"
         "pero aun asi este movimiento descuidado de tu compañero causa miradas de aquellos cercanos,el cantinero con su voz ronca te dice"
         ck"-ya vienen ustedes nuckheald a armar revuelo... dejen eso hombres  "

         menu:
            "que accion tomaras?"

            "intentas comvencerlo":
                 yo" mi amigo es algo maleducado, le pedi su espada corta para afeitarme y me la apasado asi nada mas con ese ruido, no tenemos encargo ahora mismo
                 el cantinero no se lo traga del todo, pero opta por una aptitud indiferente y no comenta nada mas..."
                 jump normal


            "no respondes":
                 yo"Te quedas callado,cosa que normalmente seria incomoda, pero con el ruido no pasa por tal; ademas de que el caninero parece haber lidiado con muchos de tu calaña"
                 "por lo que determinas que no hay problema "
                 jump normal



            "le atemorizas ":

                 yo"-No me hables maldito cantinero, sirve y calla- el caninero escupe al frnte tuya y calla sin mas"
                 jump tejo



         label normal:

             a"psshh.....psshhh....  {size=-5}cual es tu puto problema %(p)s me haces quedar como un estupido... vamos a matar a ese
             ogro estupido ya....{/size}  estupido....      "





    # Finaliza el juego:

    return

    label continuar_1:


    return
