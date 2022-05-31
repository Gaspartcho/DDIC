label route_H1:
    define pts = 0
    narrateur """La cloche sonne trois fois, ce qui signifie que les cours sont terminés.

    Tu te lèves pour s'étirer après une longue journée de travail, lorsque ton téléphone sonne dans ta poche."""
    playerName "Hmm"
    call phone_start(usrh, "17:05")
    call message_start(tph, "Retrouve-moi au parc dès que possible, je sais que tu as fini tes cours <3")
    pause 2.0
    window show
    call phone_end(False)
    """{i}Je me demande ce qu'elle veut.{/i}

    {i}Le soleil se couchait juste derrière le bâtiment de l'école.{/i}

    {i}Cette première journée était assez agréable.{/i}"""
    scene park with fade

    narrateur "Tu trouves Himeno à l'arrière du parc assis à l'ombre."

    c_himeno "Hey [playerName]"

    menu:
        c_himeno "Tu es prêt à ruiner des vies ?"
        "On fait quoi? j'espère rien de mal":
            c_himeno """Mais bien sûr! 
            On va exécuter le plan le plus diabolique de l'humanité"""

        "C’est sûr et certain qu'on ne va pas faire de bonnes choses.":
            $ pts += 1
            c_himeno "Ne sois pas bête c'est pour le plus grand bien"

    c_himeno """Mon maquillage est superbe aujourd'hui.

    Je te fais prendre des photos de moi pour ma page instargam.

    On va ruiner la vie des gens en leur montrant ce qu'ils ratent."""

    menu:
        c_himeno "Tu peux le faire, n'est-ce pas ?"
        "Je suis le meilleur photographe que vous trouverez":
            $ pts += 1
            c_himeno """C'est parfait!

            Tu vois? On est un pair parfait"""

        "Je ne suis pas très doué avec l'appareil photo":
            c_himeno "C'est pas grave, je vais te guider"

    narrateur """Tu prends des photos de Himeno dans diverses poses.

    Elle demande finalement à voir comment ils sont sortis après quelques minutes"""

    c_himeno "Hé! N'est-ce pas…"

    """{i}Quoi{/i}

    {i}Est-ce que j'ai mal fait ça ?{/i}

    {i}J'ai suivi des règles de photographie que j'ai vues en ligne.{/i}

    {i}Elle exagère sûrement-{/i}"""

    c_himeno "C'est Bomi à l'arrière."

    narrateur "Tu te rapproche du tel de Himeno et il y avait une silhouette rose à l'arrière d’une des photos qui se cachait derrière l'un des arbres."

    "{i}Hein...{/i}"

    c_himeno """Pfft

    Elle ressemble à un harceleur.

    Qu'est-ce qu'elle fout ?"""

    narrateur "Himeno agite son bras, essayant d'attirer l'attention de Bomi."

    c_himeno """Hey! 

    Je vais dire à tout le monde que tu es un harceleur !"""

    menu:
        c_himeno "Laisse-moi tranquille !"
        "Je ne pense pas que tu devrais faire ça… On ne connaît pas toute l'histoire.":
            $ pts += 1
            c_himeno "Elle me suit, je pense que c'est suffisant pour la punir"

        "Elle s'en ira, ignore-la.":
            c_himeno """Quoi et la laisser me suivre? 

            Certainement pas."""
    c_himeno "Je refuse d'accepter et d'endurer un événement aussi effrayant."

    menu:
        c_himeno "Surtout d’elle."
        "Elle apprendra les conséquences de ses actes":
            c_himeno "Ouais, évidemment."

        "On pourrait juste lui demander pourquoi elle te suit. Est-ce la seule chose qu'elle t'ait faite qui te dérange ? ":
            $ pts += 1
            c_himeno """…
            Ouais"""

    c_himeno """Et elle a toujours pris ma place au sommet du classement

    comme je l'ai dit,"""

    menu:
        c_himeno "Je suis tellement sûr qu'elle triche."
        "Comment le sais-tu ? Je suis sûr qu'elle a travaillé dur pour être là où elle est maintenant. Je crois que tu peux la battre aussi.":
            $ pts += 1
            c_himeno """…

            Vraiment?"""

        "Peut-être qu'elle est juste plus intelligente que toi. ":
            c_himeno "..."

    """{i}Himeno a l'air énervé.{/i}

    {i}Peut-être que je n'aurais pas dû dire ça.{/i}"""

    c_himeno "… Tais-toi…"

    playerName "Hein?"

    c_himeno """De quel droit tu me dis cela ?

    tu penses que je n'essaie pas?

    tout ce que je veux

    c'est que mon père me remarque

    il est jamais a la maison

    et même si je vais du bien ou du mal

    il ne me regarde jamais 

    …

    ah

    t’es nul

    t’as ruiné mon maquillage"""

    "…"

    menu:
        "{i}Je devrais peut-être dire quelque chose{/i}"
        "Il te verra un jour. C'est pour ca que tu devras rester bon pour le jour où il le fera.":
            $ pts += 1

        "... ":
            c_himeno "..."

    c_himeno "Je vais rentrer à la maison."

    narrateur """Elle se lève du banc et se dirige vers l'entrée du parc.

    Tu jetes un coup d'œil à la direction où Bomi Park était censé être mais elle n'était plus là"""

    "{i}Elle a dû partir quand Himeno l'a appelée.{/i}"
    scene black with fade
    narrateur "Tu rentres aussi chez toi."

    "{i}Je me demande ce que va faire Himeno.{/i}"

    if pts>=4: 
        jump route_H2
    else:
        jump HBad1

label HBad1:
    pause 5
    scene classroom late with fade
    """{i}Ça fait une semaine que j’étais au parc avec Himeno.{/i}

    {i}Himeno a fini par publier cette photo et a répandu beaucoup de haine.{/i}

    {i}Bomi a fini par subir beaucoup d'intimidation depuis que la cyberintimidation est devenue physique.{/i}"""

    c_himeno "Hey [playerName]"

    "{i}Le regard de Himeno semble devenir froid chaque fois qu'elle me regarde.{/i}"

    c_himeno "Viens avec moi."

    """{i}Pour être juste, ce n'est pas comme si je pouvais aller contre elle.{/i}

    {i}Elle a fini par trouver des secrets sur moi.{/i}"""

    scene hallway late with fade
    narrateur "Tu la suis dans le couloir quand une silhouette rose sortie de nulle part et attaque à Himeno"

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

    scene BH1 with fade
    """{i}Je suis allé lui rendre visite une fois qu'elle s'était réveillée quelques heures plus tard mais elle avait vraiment mal partout.{/i}

    {i}Selon les médecins, les escaliers l'ont vraiment frappé.{/i}

    {i}Je ne pense pas qu'elle s'en remettra mentalement puisque sa vie était basée sur son apparence.{/i}"""

    jump game_over


label route_H2:
    """{i}Cela fait une semaine que je n'étais pas au parc avec Himeno.{/i}

    {i}Himeno a posté les photos que nous avons prises d'elle et elles ont explosé.{/i}

    {i}Heureusement, Himeno a été miséricordieux et l'a supprimée.{/i}"""
    scene classroom day with fade

    c_himeno "Hey! [playerName]! T’as vraiment bien travaillé avec la caméra."

    "{i}Elle attrape mon bras.{/i}"

    c_himeno """T’as si bien réussi que j’ai reçu des offres d'entreprises !

    Je peux gagner de l'argent maintenant!"""

    "{i}Himeno sort son téléphone et me montre ses demandes sur instargam.{/i}"

    c_himeno "C'est fou ici. Ta pote devient populaire ~~"

    menu:
        "{i}C'était un mélange de bijoux, de vêtements et de maquillage. Certains d'entre eux étaient des cadeaux gratuits et beaucoup d'entre eux étaient des compliments de fans.{/i}"
        "Haha c'est super ! En T’en as accepté ?":
            $ pts += 1
            c_himeno "Non, je voulais te montrer tout avant d'accepter l'un d'eux!"

        "C'est incroyable Himeno ! ":
            c_himeno "Ha ha ! Attends que j'accepte les offres et que je devienne le visage de grandes marques !!"

    """{i}Elle a ouvert un des messages.{/i}

    {i}C'était une demande de guzzi.{/i}

    {i}Une marque très connue de pratiquement tout le monde.{/i}"""

    menu:
        "{i}Mais le site officiel n'était-il pas guzzi.com et non guzzi_official.com ?{/i}"

        "Hey… certains ne semblent pas corrects.":
            $ pts += 1
            c_himeno "Que veux-tu dire?"

        "T’as une demande d'une marque de luxe ?":
            c_himeno "Que veux-tu dire par là?"

    playerName "Je dis ça comme ça…"

    """{i}Himeno roule des yeux et ouvre quand même le lien.{/i}

    {i}Le site Web s'ouvre sur une section où on devait entrer nos coordonnées Guugle.{/i}

    {i}mais pourquoi?{/i}"""

    playerName "Attends"

    c_himeno "Hein?"

    menu:
        c_himeno "Qu’est-ce qu’il y a?"
        "Ne mets pas tes coordonnées pendant que je suis à côté de toi !":
            c_himeno "C'est pas comme si ça me dérangeait de toute façon"

        "J'ai l'impression qu'on devrait les vérifier.":
            $ pts += 1
            c_himeno "Comment?"

    """{i}Un doux sonnerie vient du téléphone de Himeno{/i}

    {i}Un email.{/i}"""

    c_himeno """Eh?! 
    Il dit que mon compte bancaire a été compromis…"""

    menu:
        c_himeno "Pour récupérer mon compte, je dois me reconnecter avec ce lien."
        "Himeno, je pense que tu devrais les vérifier avant de faire quoi que ce soit.":

            playerName """C'est hyper sus.
            Je vais chercher une boisson. 
            Juste attends moi."""

            c_himeno "Wahhhh ! Que devrais-je faire…"

        "Appelle-moi si tu as besoin de quoi que ce soit, j'irai chercher du banana milk.":
            $ pts += 1
            c_himeno "Ok ~ Ce sera fait."
    
    c_himeno "Attends! Peux-tu me chercher un thé glacé ?"

    playerName "Okay"

    if pts >2:
        jump HGE
    else: 
        jump HBad2
        
label HBad2:
    scene hallway day with fade
    """{i}Hmm…{/i}

    {i}C’est est tellement bizarre.{/i}

    {i}J'ai l'impression que j'aurais dû m'assurer qu'elle ne fasse rien.{/i}"""
    
    narrateur "Tu sens ton téléphone vibrer lorsque tu prends le thé glacé et le banana milk."
    call phone_start(usrh, "10:12")
    call message_start(tph, "Reviens! J’ai soif!!")
    call reply_message(playerName, "Okay okay!")
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

    narrateur "Tu regardes autour de toi pour voir si tu peux repérer Himeno mais tu ne le fais pas."

    """{i}…{/i}

    {i}Je suppose que je vais aller chercher quelque chose à manger avant de rentrer à la maison. {/i}"""

    narrateur "Tu vas au 7-12 le plus proche et tu achètes un onigiri au saumon, des sandwichs japonais au riz."

    """{i}Zut.{/i}

    {i}J'ai oublié mon porte-monnaie.{/i}"""

    narrateur "Tu regardes la caissière."

    "{i}…{/i}"

    c_himeno """???
    
    Ah!?? [playerName]?! N-non! Ne me regarde pas !
    
    Ils ont tout pris ! Mon argent, ma maison, et ma vie."""

    """{i}Des larmes commencent à se former dans ses yeux fatigués.{/i}
    
    {i}Je n'aurais jamais pensé voir Himeno dans cet état.{/i}"""

    jump game_over

label HGE:





    




    

