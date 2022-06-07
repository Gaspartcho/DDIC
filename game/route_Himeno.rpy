label RH1:
    define ptsh1 = 0
    narrateur """{i}La cloche sonne trois fois, ce qui signifie que les cours sont terminés.{/i}

    {i}Tu vois le soleil se coucher juste derrière le bâtiment de l'école.{/i}"""

    "{i}Cette première journée était assez agréable."

    narrateur "Tu te lèves pour t'étirer après une longue journée de travail, lorsque ton téléphone sonne dans ta poche."
    playerName "Hmm?"

    call phone_start(usrh, "17:05")
    call message_start(tph, "Retrouve-moi au parc dès que possible, je sais que tu as fini tes cours <3")
    call phone_end
    "{i}..."
    
    "{i}Je me demande ce qu'elle veut."

    scene park with fade

    narrateur "Tu trouves Himeno à l'arrière du parc assis à l'ombre."
    show screen cexp("hpw", "heb", "hml", "hbn")

    c_himeno "Hey [playerName]"
    show screen cexp("hph", "hel", "hms", "hbn")
    menu:
        c_himeno "Tu es prêt à ruiner des vies ?"
        "On fait quoi? j'espère rien de mal":
            playerName "On fait quoi? j'espère rien de mal"
            show screen cexp("hph", "heb", "hmt", "hbn")
            c_himeno """Mais bien sûr! 

            On va exécuter le plan le plus diabolique de l'humanité"""

        "C’est sûr et certain qu'on ne va pas faire de bonnes choses.":
            playerName "C’est sûr et certain qu'on ne va pas faire de bonnes choses."
            $ ptsh1 += 1
            show screen cexp("hph", "heb", "hmt", "hbn")
            c_himeno "Ne sois pas bête c'est pour le plus grand bien"
    show screen cexp("hph", "hel", "hms", "hbn")
    c_himeno """Mon maquillage est superbe aujourd'hui.

    Je te fais prendre des photos de moi pour ma page instargam."""
    show screen cexp("hph", "hes", "hmm", "hbn")
    c_himeno "On va ruiner la vie des gens en leur montrant ce qu'ils ratent."

    menu:
        c_himeno "Tu peux le faire, n'est-ce pas ?"
        "Je suis le meilleur photographe que vous trouverez":
            playerName "Je suis le meilleur photographe que vous trouverez"
            $ ptsh1 += 1
            show screen cexp("hph", "heb", "hms", "hbn")
            c_himeno """C'est parfait!

            Tu vois? On est un pair parfait"""

        "Je ne suis pas très doué avec l'appareil photo":
            playerName "Je ne suis pas très doué avec l'appareil photo"
            show screen cexp("hpw", "hes", "hmt", "hbn")
            c_himeno "C'est pas grave, je vais te guider"
    show screen cexp("hph", "heb", "hms", "hbn")
    narrateur "Tu prends des photos de Himeno dans diverses poses."
    show screen cexp("hpw", "hel", "hms", "hbn")
    narrateur "Elle demande finalement à voir comment ils sont sortis après quelques minutes"
    show screen cexp("hph", "hea", "hmf", "hba")
    c_himeno "Hé! N'est-ce pas…"
    show screen cexp("hph", "hea", "hmn", "hba")

    """{i}Quoi{/i}

    {i}Est-ce que j'ai mal fait ça ?{/i}

    {i}J'ai suivi des règles de photographie que j'ai vues en ligne.{/i}

    {i}Elle exagère sûrement-{/i}"""
    show screen cexp("hph", "hel", "hmf", "hba")
    c_himeno "C'est Bomi à l'arrière."

    narrateur "Tu te rapproche du tel de Himeno et il y avait une silhouette rose à l'arrière d’une des photos qui se cachait derrière l'un des arbres."

    "{i}Hein...{/i}"
    show screen cexp("hph", "hea", "hml", "hba")
    c_himeno "Pfft"
    show screen cexp("hph", "hel", "hml", "hba")
    c_himeno """Elle ressemble à un harceleur.

    Qu'est-ce qu'elle fout ?"""
    show screen cexp("hpw", "hel", "hml", "hba")
    narrateur "Himeno agite son bras, essayant d'attirer l'attention de Bomi."

    c_himeno """Hey! 

    Je vais dire à tout le monde que tu es un harceleur !"""

    menu:
        c_himeno "Laisse-moi tranquille !"
        "Je ne pense pas que tu devrais faire ça… On ne connaît pas toute l'histoire.":
            playerName "Je ne pense pas que tu devrais faire ça… On ne connaît pas toute l'histoire."
            show screen cexp("hph", "hel", "hmn", "hba")
            $ ptsh1 += 1
            c_himeno "Elle me suit, je pense que c'est suffisant pour la punir"

        "Elle s'en ira, ignore-la.":
            playerName "Elle s'en ira, ignore-la."
            show screen cexp("hph", "hel", "hmf", "hba")
            c_himeno """Quoi et la laisser me suivre? 

            Certainement pas."""
    c_himeno "Je refuse d'accepter et d'endurer un événement aussi effrayant."
    show screen cexp("hpw", "hel", "hmn", "hba")
    menu:
        c_himeno "Surtout d’elle."
        "Elle apprendra les conséquences de ses actes":
            playerName "Elle apprendra les conséquences de ses actes"
            show screen cexp("hph", "hea", "hmn", "hba")
            c_himeno "Ouais, évidemment."

        "On pourrait juste lui demander pourquoi elle te suit. Est-ce la seule chose qu'elle t'ait faite qui te dérange ? ":
            playerName "On pourrait juste lui demander pourquoi elle te suit."
            playerName "Est-ce la seule chose qu'elle t'ait faite qui te dérange ? "
            $ ptsh1 += 1
            show screen cexp("hph", "hea", "hmn", "hba")
            c_himeno """…

            Ouais"""
    show screen cexp("hph", "hea", "hmf", "hba")
    c_himeno """Et elle a toujours pris ma place au sommet du classement

    comme je l'ai dit,"""
    show screen cexp("hph", "hel", "hmf", "hba")
    menu:
        c_himeno "Je suis tellement sûr qu'elle triche."
        "Comment le sais-tu ? Je suis sûr qu'elle a travaillé dur pour être là où elle est maintenant. Je crois que tu peux la battre aussi.":
            playerName """Comment le sais-tu ? 
            
            Je suis sûr qu'elle a travaillé dur pour être là où elle est maintenant. 
            
            Je crois que tu peux la battre aussi."""
            show screen cexp("hph", "hea", "hmn", "hba")
            $ ptsh1 += 1
            c_himeno "…"

        "Peut-être qu'elle est juste plus intelligente que toi. ":
            playerName "Peut-être qu'elle est juste plus intelligente que toi. "
            show screen cexp("hph", "hea", "hmn", "hba")
            c_himeno "..."

    """{i}Himeno a l'air énervé.{/i}

    {i}Peut-être que je n'aurais pas dû dire ça.{/i}"""
    show screen cexp("hph", "hel", "hmf", "hba", "hlc")
    c_himeno "… Tais-toi…"
    show screen cexp("hph", "hel", "hmn", "hba", "hlc")
    playerName "Hein?"
    show screen cexp("hph", "hea", "hmf", "hba", "hlc")
    c_himeno "De quel droit tu me dis cela ?"
    show screen cexp("hph", "hel", "hmf", "hba", "hlc")
    c_himeno "tu penses que je n'essaie pas?"
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno """tout ce que je veux

    c'est que mon père me remarque"""
    show screen cexp("hph", "hea", "hmf", "hbs", "hlc")
    c_himeno """il est jamais a la maison

    et même si je vais du bien ou du mal"""
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno "il ne me regarde jamais "
    show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
    c_himeno "…"
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno """ah

    t’es nul

    t’as ruiné mon maquillage"""
    show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
    "…"

    menu:
        "{i}Je devrais peut-être dire quelque chose{/i}"
        "Il te verra un jour. C'est pour ca que tu devras rester bon pour le jour où il le fera.":
            show screen cexp("hph", "hel", "hmn", "hbs", "hlc")
            playerName "Il te verra un jour. C'est pour ca que tu devras rester bon pour le jour où il le fera."
            $ ptsh1 += 1

        "... ":
            playerName "... "
    
    show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
    c_himeno "..."
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno "Je vais rentrer à la maison."
    hide screen cexp with fade
    narrateur """Elle se lève du banc et se dirige vers l'entrée du parc.

    Tu jetes un coup d'œil à la direction où Bomi Park était censé être mais elle n'était plus là"""

    "{i}Elle a dû partir quand Himeno l'a appelée.{/i}"
    scene black with fade
    narrateur "Tu rentres aussi chez toi."

    "{i}Je me demande ce que va faire Himeno.{/i}"
    pause 5

    if ptsh1>=4: 
        jump RH2
    else:
        jump HB1

label HB1:
    pause 5
    scene classroom late with fade
    """{i}Ça fait une semaine que j’étais au parc avec Himeno.{/i}

    {i}Himeno a fini par publier cette photo et a répandu beaucoup de haine.{/i}

    {i}Bomi a fini par subir beaucoup d'intimidation depuis que la cyberintimidation est devenue physique.{/i}"""
    show screen cexp("hpw", "hel", "hmf", "hbn")
    c_himeno "Hey [playerName]"
    
    "{i}Le regard de Himeno semble devenir froid chaque fois qu'elle me regarde.{/i}"
    show screen cexp("hph", "hel", "hmf", "hbn")
    c_himeno "Viens avec moi."
    show screen cexp("hph", "hea", "hmn", "hbn")
    """{i}Pour être juste, ce n'est pas comme si je pouvais aller contre elle.{/i}

    {i}Elle a fini par trouver des secrets sur moi.{/i}"""

    scene hallway late with fade
    narrateur "Tu la suis dans le couloir quand une silhouette rose sortie de nulle part et attaque à Himeno"
    show screen cexp("hph", "hel", "hmf", "hbs")
    c_bomi """Tu!

    As!

    Fais!

    Ca!

    T’es terrible!

    Tu m’as ruine!"""

    """{i}Himeno et Bomi se sont battus l'un contre l'autre.{/i}

    {i}Il ne semblait pas y avoir de limites.{/i}"""

    c_himeno "Lâche-moi espèce de - !"

    narrateur "Tu remarques que Himeno recule sur le bord de l'escalier"

    playerName "Attends--"
    scene black with fade

    """{i}C'était trop tard.{/i}

    {i}Avant que je ne puisse faire quoi que ce soit, Himeno tombe à la renverse dans deux volées d'escaliers.{/i}"""

    c_bomi "..."

    """{i}Avant que je puisse attraper Bomi et lui demander de l'aider, elle s'est enfuie.{/i}

    {i}Quelques heures plus tard.{/i}

    {i}Himeno a été transportée d'urgence à l'hôpital car elle ne se réveillait pas après sa chute.{/i}"""

    scene HB1 with fade
    """{i}Je suis allé lui rendre visite une fois qu'elle s'était réveillée quelques heures plus tard mais elle avait vraiment mal partout.{/i}

    {i}Selon les médecins, les escaliers l'ont vraiment frappé.{/i}

    {i}Je ne pense pas qu'elle s'en remettra mentalement puisque sa vie était basée sur son apparence.{/i}"""

    jump game_over


label RH2:
    define ptsh2 =0
    """{i}Cela fait une semaine que je n'étais pas au parc avec Himeno.{/i}

    {i}Himeno a posté les photos que nous avons prises d'elle et elles ont explosé.{/i}

    {i}Heureusement, Himeno a été miséricordieux et l'a supprimée.{/i}"""
    scene classroom day with fade
    show screen cexp("hpw", "heb", "hml", "hbn")
    c_himeno "Hey! [playerName]! T’as vraiment bien travaillé avec la caméra."
    show screen cexp("hph", "hes", "hml", "hbn")
    c_himeno """T’as si bien réussi que j’ai reçu des offres d'entreprises !"""
    show screen cexp("hph", "heb", "hml", "hbn")
    c_himeno """Je peux gagner de l'argent maintenant!"""
    show screen cexp("hph", "hea", "hms", "hbn")
    "{i}Himeno me montre ses demandes sur instargam.{/i}"
    show screen cexp("hph", "hes", "hml", "hbn")
    c_himeno "C'est fou ici. Ta pote devient populaire ~~"
    show screen cexp("hph", "hea", "hms", "hbn")
    menu:
        "{i}C'était un mélange de bijoux, de vêtements et de maquillage. Certains d'entre eux étaient des cadeaux gratuits et beaucoup d'entre eux étaient des compliments de fans.{/i}"
        "Haha c'est super ! En T’en as accepté ?":
            playerName "Haha c'est super ! En T’en as accepté ?"
            $ ptsh2 += 1
            show screen cexp("hpw", "hes", "hmt", "hbn")
            c_himeno "Non, je voulais te montrer tout avant d'accepter l'un d'eux!"

        "C'est incroyable Himeno ! ":
            playerName "C'est incroyable Himeno ! "
            show screen cexp("hpw", "heb", "hml", "hbn")
            c_himeno "Ha ha ! Attends que j'accepte les offres et que je devienne le visage de grandes marques !!"
    show screen cexp("hph", "hea", "hms", "hbn")
    """{i}Elle a ouvert un des messages.{/i}

    {i}C'était une demande de guzzi.{/i}

    {i}Une marque très connue de pratiquement tout le monde.{/i}"""

    menu:
        "{i}Mais le site officiel n'était-il pas guzzi.com et non guzzi_official.com ?{/i}"

        "Hey… certains ne semblent pas corrects.":
            playerName "Hey… certains ne semblent pas corrects."
            $ ptsh2 += 1
            show screen cexp("hph", "hel", "hmt", "hbn")
            c_himeno "Que veux-tu dire?"

        "T’as une demande d'une marque de luxe ?":
            playerName "T’as une demande d'une marque de luxe ?"
            show screen cexp("hph", "hel", "hmf", "hbn")
            c_himeno "Que veux-tu dire par là?"

    playerName "Je dis ça comme ça…"
    show screen cexp("hph", "hea", "hmn", "hbn")
    """{i}Himeno roule des yeux et ouvre quand même le lien.{/i}

    {i}Le site Web s'ouvre sur une section où on devait entrer nos coordonnées Guugle.{/i}

    {i}mais pourquoi?{/i}"""
    show screen cexp("hph", "hel", "hmn", "hbn")
    playerName "Attends"
    show screen cexp("hph", "hel", "hmt", "hbn")
    c_himeno "Hein?"

    menu:
        c_himeno "Qu’est-ce qu’il y a?"
        "Ne mets pas tes coordonnées pendant que je suis à côté de toi !":
            playerName "Ne mets pas tes coordonnées pendant que je suis à côté de toi !"
            show screen cexp("hph", "hea", "hml", "hbn")
            c_himeno "C'est pas comme si ça me dérangeait de toute façon"

        "J'ai l'impression qu'on devrait les vérifier.":
            playerName "J'ai l'impression qu'on devrait les vérifier."
            $ ptsh2 += 1
            show screen cexp("hph", "hea", "hmt", "hbn")
            c_himeno "Comment?"
    show screen cexp("hph", "hea", "hmn", "hbn")
    """{i}Un doux sonnerie vient du téléphone de Himeno{/i}

    {i}Un email.{/i}"""
    show screen cexp("hph", "hea", "hmt", "hbs")
    c_himeno """Eh?! 
    Il dit que mon compte bancaire a été compromis…"""
    show screen cexp("hph", "hel", "hmt", "hbs")
    menu:
        c_himeno "Pour récupérer mon compte, je dois me reconnecter avec ce lien."
        "Himeno, je pense que tu devrais les vérifier avant de faire quoi que ce soit.":
            show screen cexp("hph", "hel", "hmn", "hbs")
            playerName "Himeno, je pense que tu devrais les vérifier avant de faire quoi que ce soit."
            $ ptsh2 += 1
            playerName """C'est hyper sus.

            Je vais chercher une boisson. 

            Juste attends moi."""
            show screen cexp("hph", "hea", "hmf", "hbs")
            c_himeno "Wahhhh ! Que devrais-je faire…"

        "Appelle-moi si tu as besoin de quoi que ce soit, j'irai chercher du banana milk.":
            show screen cexp("hph", "hel", "hmn", "hbs")
            playerName "Appelle-moi si tu as besoin de quoi que ce soit, j'irai chercher du banana milk."
            show screen cexp("hph", "heb", "hml", "hbs")
            c_himeno "Ok ~ Ce sera fait."
    show screen cexp("hpw", "hel", "hmt", "hbn")
    c_himeno "Attends! Peux-tu me chercher un thé glacé ?"
    show screen cexp("hph", "heb", "hms", "hbn")
    playerName "Okay"
    hide screen cexp

    if ptsh2>2:
        jump HGE
    else: 
        jump HB2
        
label HB2:
    scene hallway day with fade
    """{i}Hmm…{/i}

    {i}C’est est tellement bizarre.{/i}

    {i}J'ai l'impression que j'aurais dû m'assurer qu'elle ne fasse rien.{/i}"""
    
    narrateur "Tu sens ton téléphone vibrer lorsque tu prends le thé glacé et le banana milk."
    call phone_start(usrh, "10:12")
    call message_start(tph, "Reviens! J’ai soif!!")
    call reply_message("Okay okay!")
    call message(tph, "Je l'ai fait! J'espère qu'ils envoient les articles bientôt!")
    call phone_end(False)
    scene black with fade
    """{i}...{/i}

    {i}Ça fait 2 semaines que j' ai parlé à Himeno de ses offres.{/i}

    {i}La fille a juste arrêté de venir en cours.{/i}

    {i}Ce qui est plus inquiétant, c'est que des adultes sont venus dans notre classe pour demander où elle se trouvait.{/i}

    {i}Je devrais aller lui rendre visite.{/i}"""

    narrateur "Tu vas lui dire que tu as eu de l'école."

    """{i}Huh??? {/i}

    {i}Pourquoi les gens sortent-ils ses meubles ?{/i}"""

    narrateur "Une foule séparée de personnes scandait son nom."

    """{i}Sont-ce des fans ?{/i}

    {i}… {/i}

    {i}Je ne pense pas que les fans soient censés savoir où vous vivez.{/i}"""

    narrateur "Tu regardes autour de toi pour voir si tu peux repérer Himeno mais tu ne la vois pas."

    """{i}…{/i}

    {i}Je vais aller chercher quelque chose à manger avant de rentrer à la maison. {/i}"""

    narrateur "Tu vas au 7-11 le plus proche et tu t'achètes un onigiri au saumon, des sandwichs japonais au riz."

    """{i}Zut.{/i}

    {i}J'ai oublié mon porte-monnaie.{/i}"""

    narrateur "Tu regardes la caissière."
    scene HB2 with fade
    "{i}…{/i}"

    c_himeno """???
    
    Ah!?? [playerName]?! N-non! Ne me regarde pas !
    
    Ils ont tout pris ! Mon argent, ma maison, et ma vie."""

    """{i}Des larmes commencent à se former dans ses yeux fatigués.{/i}
    
    {i}Je n'aurais jamais pensé voir Himeno dans cet état.{/i}"""
    pause 5

    jump game_over

label HGE:
    scene hallway day with fade
    """{i}Hmm…{/i}

    {i}C’est est tellement bizarre.{/i}

    {i}J'ai l'impression que j'aurais dû m'assurer qu'elle ne fasse rien.{/i}"""
    
    narrateur "Tu sens ton téléphone vibrer lorsque tu prends le thé glacé et le banana milk."
    call phone_start(usrh, "10:12")
    call message_start(tph, "Reviens! J’ai soif!!")
    call reply_message("Okay okay!")
    call message(tph, "Je l'ai fait! J'espère qu'ils envoient les articles bientôt!")
    call phone_end(False)
    scene black with fade
    """{i}...{/i}

    {i}Ça fait 2 semaines que j'ai parlé à Himeno de ses offres.{/i}"""

    """{i}Avec le mannequinat et les sponsors qu'elle a continué à obtenir, Himeno n'avait plus vraiment besoin de venir à l'école.{/i}

    {i}Malgré cela, elle est toujours venue m'accompagner tout au long des journée.{/i}"""

    c_himeno "[playerName]!"
    scene HGE with fade
    c_himeno """Concentre-toi!
    
    Il faut finir la séance pour ce soir."""

    """{i}Wow{/i}

    {i}Elle est vraiment faite pour le public.{/i}"""

    return