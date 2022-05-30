label route_H:
    narrateur """La cloche sonne trois fois, ce qui signifie que les cours sont terminés.

    Tu te lèves pour s'étirer après une longue journée de travail, lorsque ton téléphone sonne dans ta poche."""
    playerName "Hmm"
    call phone_start(usrh, "17:05")
    call message_start(tph, "Retrouve-moi au parc dès que possible, je sais que tu as fini tes cours <3")
    pause 2.0
    window show
    call phone_end(False)
    playerName """Je me demande ce qu'elle veut.
    
    Le soleil se couchait juste derrière le bâtiment de l'école.
    
    Cette première journée était assez agréable."""
    narrateur "Tu trouves Himeno à l'arrière du parc assis à l'ombre."
    c_himeno "Hey [Player]"
    menu:
        c_himeno "Tu es prêt à ruiner des vies ?"

        "Tu parles d’expérience ?":
            c_akane "Peut-être"

        "J'allais le supprimer de toute façon.":
            c_akane "..."
            c_akane "... Mouai ..."
    return