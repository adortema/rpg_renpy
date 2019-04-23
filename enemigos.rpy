# en este script esta el listado de enemigos a vencer
#ogro#
label enemigos:

    define enemigo_vida_max = 100
    define enemigo_hp = enemigo_vida_max

    if enemigo == "ogro":

        $ enemigo_vida_max = 500
        $ enemigo_hp = enemigo_vida_max
        $ ataque_enemigo= 25

return
