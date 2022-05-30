label route_H:
    narrateur """La cloche sonne trois fois, ce qui signifie que les cours sont terminés.

    Tu te lèves pour s'étirer après une longue journée de travail, lorsque ton téléphone sonne dans ta poche."""
    playerName "Hmm"
    call phone_start(usrh, "17:05")
    call message_start(tph, "Retrouve-moi au parc dès que possible, je sais que tu as fini tes cours <3")
    pause 2.0
    window show
    call phone_end(False)
    """{i}Je me demande ce qu'elle veut.
    
    Le soleil se couchait juste derrière le bâtiment de l'école.
    
    Cette première journée était assez agréable.{/i}"""
    narrateur "Tu trouves Himeno à l'arrière du parc assis à l'ombre."
    c_himeno "Hey [Player]"
    menu:
        c_himeno "Tu es prêt à ruiner des vies ?"
        "On fait quoi? j'espère rien de mal":
            c_himeno """Mais bien sûr! 
            On va exécuter le plan le plus diabolique de l'humanité"""

        "C’est sûr et certain qu'on ne va pas faire de bonnes choses.":
            c_himeno "Ne sois pas bête c'est pour le plus grand bien"
    c_himeno """Mon maquillage est superbe aujourd'hui.
    Je te fais prendre des photos de moi pour ma page instargam.
    On va ruiner la vie des gens en leur montrant ce qu'ils ratent."""
    menu:
        c_himeno "Tu peux le faire, n'est-ce pas ?"
        "Je suis le meilleur photographe que vous trouverez":
            c_himeno """C'est parfait!
            Tu vois? On est un pair parfait"""

        "Je ne suis pas très doué avec l'appareil photo":
            c_himeno "C'est pas grave, je vais te guider"
    narrateur """Tu prends des photos de Himeno dans diverses poses.
    Elle demande finalement à voir comment ils sont sortis après quelques minutes"""
    c_himeno "Hé! N'est-ce pas…"
    """{i}Quoi
    Est-ce que j'ai mal fait ça ?
    J'ai suivi des règles de photographie que j'ai vues en ligne.
    Elle exagère sûrement-{/i}"""
    c_himeno "C'est Bomi à l'arrière."
    narrateur "Tu te rapproche du tel de Himeno et il y avait une silhouette rose à l'arrière d’une des photos qui se cachait derrière l'un des arbres."
    "{i}Hein...{/i}"
    c_himeno """Pfft
    Elle ressemble à un harceleur.
    Qu'est-ce qu'elle fout ?"""
    narrateur "Himeno agite son bras, essayant d'attirer l'attention de Bomi."\
    c_himeno """Hey! 
    Je vais dire à tout le monde que tu es un harceleur !"""
    menu:
        c_akane "Laisse-moi tranquille !"
        "Je ne pense pas que tu devrais faire ça… On ne connaît pas toute l'histoire.":
            c_himeno "Elle me suit, je pense que c'est suffisant pour la punir"

        "Elle s'en ira, ignore-la.":
            c_himeno "C'est pas grave, je vais te guider"

    
    return