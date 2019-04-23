label combate:

    scene pabar
    show pabar2 behind pabar
    show pabar2 behind ogro

    call enemigos

    $ cookies_left = 13

    jump inicio

    screen pantalla:
        frame:
            xalign 0.18 yalign 0.7
            xminimum 220 xmaximum 220
            vbox:
                text p size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 130
                        value heroe_hp
                        range heroe_vida_max
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None


                    null width 5

                    text "[heroe_hp] / [heroe_vida_max]" size 16


        frame:
            xalign 0.8 yalign 0.05
            xminimum 220 xmaximum 220
            vbox:
                text "[enemigo]" size 22 xalign 0.5
                null height 5
                hbox:
                    bar:
                        xmaximum 130
                        value enemigo_hp
                        range enemigo_vida_max
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None

                    null width 5

                    text "[enemigo_hp] / [enemigo_vida_max]" size 16

        text  p + " vs. ogro" xalign 0.5 yalign 0.05 size 30



#inicio del combate
label inicio:

    show ogro:
        ypos 100 xpos 270
        linear 1 xzoom 1 yzoom 1
        linear 1 xzoom 1.02 yzoom 1.005
        repeat

    e "vamos a pelar puto"

    e "cara de monda"

    #play music "pelea00.1.mp3"
    play music "pelea002.mpeg"


    show screen pantalla

    while (enemigo_hp >= 1) and (heroe_hp >= 1):

        menu:
            "Atacar!":
                $ enemigo_hp = enemigo_hp - ataher
                play sound "ataque.ogg"
                p "tomaaaaaa!!!11 ( daño de [ataher] )"

            "magia tienes [cookies_left] poderes )" if cookies_left > 0:
                $ heroe_hp = min(heroe_hp+50, heroe_vida_max)
                $ cookies_left -= 1
                p "Mira como me curo puto, assss... (restore 50hp)"

        if enemigo_hp <=0:
            jump fin_batalla

        $ wolf_damage = renpy.random.randint(ataque_enemigo-5, ataque_enemigo)

        $ heroe_hp -= wolf_damage

        show ogro with hpunch

        "RrrrrRRrrrr! {i}*ogro te da un manducaso*{/i} (daño de - [wolf_damage]hp)"
    #
    ####

    hide screen pantalla

label fin_batalla:

    if enemigo_hp <= 0:

        p "ganeeeee gegege"
        p "que [enemigo] tan perro y dificil."
        "(te quedan [cookies_left] curas)"

    else:
        "Om-nom-nom-nom {i}*wolf ate you all up*{/i} (along with the basket, of course...)"

    jump battle_1_ending

label battle_1_ending:
    "The end."
    return
