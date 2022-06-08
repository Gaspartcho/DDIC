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
    
    "{i}Je me demande ce qu'elle me veut."

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
            c_himeno """Mais bien sûr que si! 

            On va exécuter le plan le plus diabolique de l'humanité"""

        "C'est sûr et certain qu'on ne va pas faire de bonnes choses.":
            playerName "C'est sûr et certain qu'on ne va pas faire de bonnes choses."
            $ ptsh1 += 1
            show screen cexp("hph", "heb", "hmt", "hbn")
            c_himeno "Ne sois pas bête c'est pour le plus grand bien"
    
    playerName "..."
    show screen cexp("hph", "hel", "hms", "hbn")
    c_himeno """Mon maquillage est superbe aujourd'hui.

    Donc mon plan, c'est que je t'engage pour faire mes photos de ma page instargam."""
    show screen cexp("hph", "hes", "hmm", "hbn")
    c_himeno """Tu vas voir, ça vas être marant
        
    On va ruiner la vie des gens en leur montrant ce qu'ils ratent."""

    menu:
        c_himeno "Tu peux le faire, n'est-ce pas ?"
        "Je suis le meilleur photographe que tu trouveras":
            playerName "Je suis le meilleur photographe que tu trouveras ici."
            $ ptsh1 += 1
            define himeno_help = False
            show screen cexp("hph", "heb", "hms", "hbn")
            c_himeno """C'est parfait!

            Tu vois? On est une paire parfaite"""

        "Je ne suis pas très doué avec l'appareil photo":
            define himeno_help = True
            playerName "Je ne suis pas très doué avec l'appareil photo"
            show screen cexp("hpw", "hes", "hmt", "hbn")
            c_himeno "C'est pas grave, je vais te guider"
    
    show screen cexp("hph", "heb", "hms", "hbn")

    play sound camera_effect
    with Fade(0.1, 0.0, 0.5, color="#fff")
    play sound camera_effect
    with Fade(0.1, 0.0, 0.5, color="#fff")
    play sound camera_effect
    with Fade(0.1, 0.0, 0.5, color="#fff")
    play sound camera_effect
    with Fade(0.1, 0.0, 0.5, color="#fff")

    narrateur "Tu prends des photos de Himeno dans diverses poses."
    show screen cexp("hpw", "hel", "hms", "hbn")
    c_himeno "Je me demande comment elles rendent..."
    show screen cexp("hph", "hea", "hmf", "hba")
    c_himeno "Hé! Mais ce n'est pas..."
    show screen cexp("hph", "hea", "hmn", "hba")

    """{i}Quoi{/i}{nw}

    {i}Est-ce que j'ai mal fait ça ?{/i}{nw}"""

    if himeno_help:
        "{i}J'ai pourtant tout fait comme elle m'as dit...{/i}{nw}"
    else:
        "{i}J'ai pourtant suivi les règles de photographie que j'ai vues en ligne...{/i}{nw}"

    "{i}Elle exagère sûrement-{/i}{nw}"
    show screen cexp("hph", "hel", "hmf", "hba")
    c_himeno "C'est Bomi à l'arrière."

    narrateur "Tu te rapproche du tel de Himeno et tu vois qu'il y avait une silhouette rose à l'arrière d'une des photos qui se cachait derrière l'un des arbres."

    playerName "Hein?"
    show screen cexp("hph", "hea", "hml", "hba")
    c_himeno "Pfft!"
    show screen cexp("hph", "hel", "hml", "hba")
    c_himeno "Elle ressemble à une harceleuse."
    show screen cexp("hph", "hea", "hml", "hba")
    c_himeno "Qu'est-ce qu'elle fout ?"
    show screen cexp("hpw", "hel", "hml", "hba")

    c_himeno """(A Bomi) Hey! 

    Je vais dire à tout le monde que tu es une harceleuse !"""

    menu:
        c_himeno "Laisse-la tranquille !"
        "Je ne pense pas que tu devrais faire ça... Elle est sûrement là par hasard":
            playerName "Je ne pense pas que tu devrais faire ça... On ne connaît pas toute l'histoire."
            playerName "Si ça se trouve, elle est sûrement là par hasard..."
            show screen cexp("hph", "hel", "hmn", "hba")
            $ ptsh1 += 1
            c_himeno "Elle me suit, je pense que c'est suffisant pour la punir"

        "Elle s'en ira, ignore-la.":
            playerName "Elle s'en ira, ignore-la."
            show screen cexp("hph", "hel", "hmf", "hba")
            c_himeno """Quoi et la laisser continuer de me suivre?

            Certainement pas."""
    c_himeno "Je refuse d'accepter et d'endurer un événement aussi effrayant."
    show screen cexp("hpw", "hel", "hmn", "hba")
    menu:
        c_himeno "Surtout d'elle."
        "Elle apprendra les conséquences de ses actes":
            playerName "Elle apprendra les conséquences de ses actes"
            show screen cexp("hph", "hea", "hmn", "hba")
            c_himeno "Ouais, évidemment."
            c_himeno "Et puis zut! Elle fais tout pour m'énerver celle-là!"

        "On pourrait juste lui demander pourquoi elle te suit":
            playerName "On pourrait juste lui demander pourquoi elle te suit..."
            playerName "Est-ce qu'elle t'as fais d'autres choses qui te dérangent?"
            $ ptsh1 += 1
            show screen cexp("hph", "hea", "hmn", "hba")
            c_himeno """...

            Ouais"""

    show screen cexp("hph", "hea", "hmf", "hba")
    c_himeno """Et elle occupe {b}ma{/b} place au sommet du classement.

    Comme je l'ai dit,"""
    show screen cexp("hph", "hel", "hmf", "hba")
    menu:
        c_himeno "Je suis certaine qu'elle triche."
        "Je suis sûr qu'elle a travaillé dur pour être là où elle est maintenant.":
            playerName """Comment le sais-tu ? 
            
            Je suis sûr qu'elle a travaillé dur pour être là où elle est maintenant. 
            
            Je crois que tu peux la battre aussi."""
            show screen cexp("hph", "hea", "hmn", "hba")
            $ ptsh1 += 1
            c_himeno "..."

        "Peut-être qu'elle est juste plus intelligente que toi. ":
            playerName "Peut-être qu'elle est juste plus intelligente que toi. "
            show screen cexp("hph", "hea", "hmn", "hba")
            c_himeno "..."

    """{i}Himeno a l'air énervé.{/i}

    {i}Peut-être que je n'aurais pas dû dire ça.{/i}"""
    show screen cexp("hph", "hel", "hmf", "hba", "hlc")
    c_himeno "... Tais-toi..."
    show screen cexp("hph", "hel", "hmn", "hba", "hlc")
    playerName "Hein?"
    show screen cexp("hph", "hea", "hmf", "hba", "hlc")
    c_himeno "De quel droit tu me dis cela ?"
    show screen cexp("hph", "hel", "hmf", "hba", "hlc")
    c_himeno "Tu penses que je n'essaie pas?"
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno """Tout ce que je veux...

    ... c'est que mon père me remarque"""
    show screen cexp("hph", "hea", "hmf", "hbs", "hlc")
    c_himeno """Il est jamais a la maison.

    Que je fasse tout pour faire le bien ou le mal..."""
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno "... Il ne me regarde jamais."
    show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
    c_himeno "..."
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno """ah

    t'es nul"""
    show screen cexp("hph", "heb", "hmf", "hbs", "hlc")
    c_himeno "t'as ruiné mon maquillage"
    show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
    "..."

    menu:
        "{i}Je devrais peut-être dire quelque chose{/i}"
        "Il te verra un jour.":
            show screen cexp("hph", "hel", "hmn", "hbs", "hlc")
            playerName "Il te verra un jour, ne t'inquiète pas."
            playerName "C'est pour ça que tu devras rester gentille,"
            playerName "... pour que le jour où il le fera,"
            playerName "... il te voie sous le plus beau jour possible."
            $ ptsh1 += 1
            show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
            c_himeno "Merci."

        "... ":
            playerName "... "
            show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
            c_himeno "..."
    

    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno "Je pense que je vais rentrer chez moi..."
    hide screen cexp with fade
    pause 2.0
    narrateur "Tu jetes un coup d'œil à la direction où Bomi Park était censé être mais elle n'était plus là"

    "{i}Elle a dû partir quand Himeno l'a appelée.{/i}"
    narrateur "Tu décide également de rentrer chez toi."
    scene black with fade

    "{i}Je me demande ce que va faire Himeno.{/i}"
    pause 5

    if ptsh1 >= 4: 
        jump RH2
    else:
        jump HB1

label HB1:
    pause 5
    scene classroom late with fade
    """{i}Ça fait une semaine que j'étais allé au parc avec Himeno.{/i}

    {i}Himeno a fini par publier cette photo en accusant bomi d'arcellement et a répandu beaucoup de haine.{/i}

    {i}Bomi a fini par subir de plus en plus de violence{/i}
    
    {i}C'étais d'autant pire que ces violences étaient passées du téléphone au monde réel...{/i}"""
    show screen cexp("hpw", "hel", "hmf", "hbn")
    c_himeno "Hey [playerName]."
    
    "{i}Le regard de Himeno semble devenir froid chaque fois qu'elle me regarde.{/i}"
    show screen cexp("hph", "hel", "hmf", "hbn")
    c_himeno "Viens avec moi."
    show screen cexp("hph", "hea", "hmn", "hbn")
    playerName "Ok."

    """{i}Pour être honnête, ce n'est pas comme si je pouvais dire non...{/i}

    {i}Elle est de plus en plus intimidante.{/i}"""
    hide screen cexp
    scene hallway late with fade
    show screen cexp("hph", "hel", "hmf", "hbs", p=p_right)
    narrateur "Tu la suis dans le couloir quand une silhouette rose sortie de nulle part et attaque à Himeno"
    hide screen cexp
    show screen h_and_bomi
    c_bomi """Tu!

    As!

    Fais!

    Ca!

    T'es terrible!

    Tu m'as ruinée!"""

    hide screen h_and_bomi

    """{i}Himeno et Bomi ont comencées à se battre l'une contre l'autre.{/i}

    {i}Il ne semblait pas y avoir de limites.{/i}"""

    c_himeno "Lâche-moi espèce de - !"

    narrateur "Tu remarques que Himeno recule sur le bord de l'escalier"

    playerName "Attention--"
    scene black with fade

    """{i}C'était trop tard.{/i}

    {i}Avant que je ne puisse faire quoi que ce soit, Himeno tombe à la renverse dans deux volées d'escaliers.{/i}"""

    c_bomi "..."

    """{i}Avant que je puisse attraper Bomi et lui demander de l'aider, elle s'est enfuie.{/i}

    {i}Je n'ai rien pu faire...{/i}

    {i}Quelques heures plus tard, Himeno a été transportée d'urgence à l'hôpital car elle ne se réveillait pas après sa chute.{/i}"""

    scene HB1 with fade
    """{i}Je suis allé lui rendre visite après qu'elle s'était réveillée un peut plus tard mais elle avait vraiment mal partout.{/i}

    {i}Selon les médecins, \"les escaliers ne l'ont pas épargnée\"...{/i}

    {i}Je ne pense pas qu'elle s'en remettra mentalement, sa vie était trop basée sur son apparence.{/i}"""

    window hide
    pause

    jump game_over


label RH2:
    define ptsh2 = 0
    """{i}Cela fait une semaine que j'étais allé au parc avec Himeno.{/i}

    {i}Himeno a posté les photos que j'avais prises d'elle et elles ont explosées.{/i}

    {i}Heureusement, Himeno a été gentille et n'a pas publillé celle où l'on voyait clairement Bomi.{/i}"""

    scene classroom day with fade
    pause 1.0
    show screen cexp("hpw", "heb", "hml", "hbn")
    c_himeno "Hey! [playerName]! T'as vraiment bien travaillé avec la caméra."
    show screen cexp("hph", "hes", "hml", "hbn")
    c_himeno """T'as si bien réussi que j'ai reçu des offres d'entreprises !"""
    show screen cexp("hph", "heb", "hml", "hbn")
    c_himeno """Je peux gagner de l'argent maintenant!"""
    show screen cexp("hph", "hea", "hms", "hbn")
    narrateur "Himeno montre les demandes qu'elle a reçu sur instargam."
    show screen cexp("hph", "hes", "hml", "hbn")
    c_himeno "C'est fou ça tu te rend compte? Ta pote devient populaire même en dehors du lycée!"
    show screen cexp("hph", "hea", "hms", "hbn")
    menu:
        "{i}Ouah, c'est vrais qu'il y en a beaucoup... Il y a même certains messages qui sont des propositions de cadeaux provenant de marques de luxe.{/i}"
        "Haha c'est super ! Et t'en as accepté ?":
            playerName "Haha c'est super ! Et t'en as accepté ?"
            show screen cexp("hpw", "hes", "hmt", "hbn")
            c_himeno "Non, je voulais te montrer tout avant d'accepter l'un d'eux!"

        "C'est incroyable Himeno ! ":
            playerName "C'est incroyable Himeno ! "
            show screen cexp("hpw", "heb", "hml", "hbn")
            c_himeno "Ha ha ! Attends que j'accepte les offres et que je devienne le visage de grandes marques !!"
    show screen cexp("hph", "hea", "hms", "hbn")
    """{i}Elle a ouvert un des messages.{/i}

    {i}C'était une demande de guzzi.{/i}

    {i}Une marque très populaire en ce moment, pratiquement connue de tout le monde.{/i}"""

    menu:
        "{i}Tiens? le site de la marque étais vraiment \"guzzi_official.com\", et non pas \"guzzi.com\" ?{/i}"

        "Hey... certaines propositions ont l'air suspectes":
            playerName "Hey... certaines propositions ont l'air suspectes..."
            playerName "Le lien vers le site à l'air bizarre"
            $ ptsh2 += 1
            show screen cexp("hph", "hel", "hmt", "hbn")
            c_himeno "Que veux-tu dire?"

        "T'as vraiment reçu une offre de marque de luxe?":
            playerName "T'as vraiment reçu une offre de marque de luxe?"
            show screen cexp("hph", "hel", "hmf", "hbn")
            c_himeno "Bah ouai..."
            c_himeno "Que veux-tu dire par là?"

    playerName "Je dis ça comme ça..."
    show screen cexp("hph", "hea", "hmn", "hbn")
    """{i}Himeno roule des yeux et ouvre le lien.{/i}

    {i}Le site Web s'ouvre sur une section où on devait entrer nos coordonnées Guglas.{/i}

    {i}Mais pourquoi?{/i}"""
    show screen cexp("hph", "hel", "hmn", "hbn")
    playerName "Attends"
    show screen cexp("hph", "hel", "hmt", "hbn")
    c_himeno "Hein?"
    show screen cexp("hph", "hel", "hml", "hbn")

    menu:
        c_himeno "Qu'est-ce qu'il y a?"
        "Ne mets pas tes coordonnées pendant que je suis à côté de toi !":
            playerName "Ne mets pas tes coordonnées pendant que je suis à côté de toi !"
            show screen cexp("hph", "hea", "hml", "hbn")
            c_himeno "C'est pas comme si ça me dérangeait de toute façon"
            c_himeno "T'es pas du genre à vouloir me hacker non?"
            "{i}Moi non en tout cas..."

        "J'ai l'impression qu'on devrait les vérifier.":
            playerName "J'ai l'impression qu'on devrait les vérifier."
            $ ptsh2 += 1
            show screen cexp("hph", "hea", "hmt", "hbn")
            c_himeno "C'est à dire?"
            playerName "Et bien tu vois, c'est important de...{nw}"
    
    play sound phone_jingle

    c_himeno "Oh, un email."
    show screen cexp("hph", "hea", "hmt", "hbs")
    c_himeno """Eh?! 
    Il dit que mon compte bancaire a été compromis..."""
    show screen cexp("hph", "hel", "hmt", "hbs")
    c_himeno "Pour récupérer mon compte, je dois me reconnecter avec ce lien."
    show screen cexp("hph", "hea", "hmf", "hbs")
    c_himeno "Et apparament, je n'ai que 20 mins pour le faire, sinon je vais tout perdre..."
    show screen cexp("hph", "hea", "hmn", "hbs")
    menu:
        c_himeno "..."
        "Tu devrais vérifier le lien":
            show screen cexp("hph", "hel", "hmn", "hbs")
            $ ptsh2 += 1
            playerName "Himeno, je pense que tu devrais vraiment vérifier le lien avant de faire quoi que ce soit."
            playerName "C'est hyper suspect"
            show screen cexp("hph", "hea", "hmf", "hbs")
            c_himeno "Wahhhh ! Que devrais-je faire..."

            playerName """Je vais chercher une boisson. 

            Juste attends moi."""

        "Je vais chercher du banana milk.":
            show screen cexp("hph", "hel", "hmn", "hbs")
            playerName "Appelle-moi si tu as besoin de quoi que ce soit, je vais chercher du banana milk."
            show screen cexp("hph", "heb", "hml", "hbs")
            c_himeno "Ok ~"

    hide screen cexp
    scene hallway day with fade
    c_himeno "Attends! Peux-tu me chercher un thé glacé ?"
    playerName "Okay"

    if ptsh2 > 2:
        jump HGE
    else: 
        jump HB2
        
label HB2:
    scene park with fade
    """{i}Hmm...{/i}

    {i}C'est est tellement bizarre.{/i}"""
    narrateur "Tu sens ton téléphone vibrer lorsque tu prends le thé glacé et le banana milk."

    call phone_start(usrh, "10:12")
    call message_start(tph, "Reviens! J'ai soif!!")
    call reply_message("Okay okay!")
    call message(tph, "Au fait, c'est bon, je l'ai fait!")
    call message(tph, "Normalement c'est bon")
    call message(tph, "Il falais juste écrire ses codes banquaires.")
    call message(playerName, "Ok cool.")
    call phone_end(False)

    scene black with fade
    narrateur "Quelques semaines plus tard..."
    """{i}...{/i}

    {i}Himeno a juste arrêté de venir en cours.{/i}

    {i}Ce qui est plus inquiétant, c'est que des adultes sont venus dans notre classe pour demander où elle se trouvait.{/i}

    {i}Je devrais aller lui rendre visite.{/i}"""

    narrateur "Tu te rend devant chez elle..."

    """{i}Huh??? {/i}

    {i}Pourquoi les gens sortent-ils ses meubles ?{/i}"""

    narrateur "Tu remarque une foule séparée de personnes criant son nom."

    """{i}Sont-ce des fans ?{/i}

    {i}... {/i}

    {i}Ils ont l'air ass fahés pour des fans...{/i}"""

    narrateur "Tu regardes autour de toi pour voir si tu peux repérer Himeno mais tu ne la vois pas."

    """{i}...{/i}

    {i}Je vais aller chercher quelque chose à manger avant de rentrer à la maison.{/i}"""

    narrateur "Tu vas au super-marché le plus proche et tu t'achètes un onigiri au saumon, des sandwichs japonais au riz."

    """{i}Zut.{/i}

    {i}J'ai oublié mon porte-monnaie.{/i}"""

    narrateur "Tu regardes la caissière."
    scene HB2 with fade
    "{i}...{/i}"

    c_himeno """???
    
    Ah!?? [playerName]?! N-non! Ne me regarde pas !"""

    playerName "Himeno! Que s'est-il passé?"
    
    c_himeno """Ils ont tout pris ! Mon argent, ma maison, et ma vie.
    
    Mon père s'est mis dans une collère si forte qu'il m'a chassé de chez moi.
    
    Je ne pense pas qu'il me pardonnera un jour..."""

    """{i}Des larmes commencent à se former dans ses yeux fatigués.{/i}
    
    {i}Je n'aurais jamais pensé voir Himeno dans cet état.{/i}"""
    window hide
    pause

    jump game_over

label HGE:
    scene park with fade
    """{i}Hmm...{/i}

    {i}C'est est tellement bizarre.{/i}

    {i}J'ai l'impression que j'aurais dû m'assurer qu'elle ne fasse rien.{/i}"""
    
    narrateur "Tu sens ton téléphone vibrer lorsque tu t'aprette à prendre le thé glacé et le banana milk."
    call phone_start(usrh, "10:12")
    call message_start(tph, "Reviens! J'ai soif!!")
    call reply_message("Okay okay!")
    pause
    call phone_end(False)
    scene classroom day

    pause 1
    show screen cexp("hph", "hea", "hmn", "hbn")
    c_himeno "Tu avais raison, ce site est une arnaque."
    show screen cexp("hph", "hea", "hmt", "hbn")
    c_himeno "Même l'e-mail est un faux."
    show screen cexp("hph", "hea", "hmf", "hbn")
    c_himeno "Quand je pense que j'ai failli me faire avoir si failement..."
    show screen cexp("hph", "hea", "hmn", "hbn")
    c_himeno "Bon, vérifions ces propositions maintenant"
    c_himeno "..."
    playerName "Regarde, la plus part sont des fausses mais il y en a qui ont l'air d'être réelles..."
    hide screen cexp

    scene black with fade

    """{i}...{/i}

    {i}Ça fait 2 semaines que j'ai parlé avec Himeno de ses offres.{/i}

    {i}Finalement, certaines demandes se sont avérées être des vraies.{/i}

    {i}Himeno est très rapidement devenue une manequin très renommée.{/i}
    
    {i}Avec le mannequinat et les sponsors qu'elle a réussie à obtenir, Himeno a commencée à faire beaucoup d'argent.{/i}

    {i}Malgré ça, elle a décidée de continuer de venir à l'école, pour m'accompagner surement...{/i}"""

    c_himeno "[playerName]!"
    scene HGE with fade
    c_himeno """Concentre-toi!
    
    Il faut finir la séance pour ce soir."""

    playerName "Ok!"
    """{i}...{/i}

    {i}Elle est vraiment faite pour le public.{/i}"""

    jump happy_ending