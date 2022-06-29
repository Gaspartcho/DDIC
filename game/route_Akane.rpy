label route_A:
    define ptsa1 = 0
    narrateur "Vous décidez de rentrer chez vous dirrectement."
    scene bedroom with fade
    pause 2.0
    "{i}Je devrais quand même remercier Akane pour son acceuil..."

    call phone_start(usrc, "18:45") from _call_phone_start_4
    label choiceMaking_UAG: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Merci pour l'accueil à l'école aujourd'hui","choiceMaking_UAG.choice1","Tu fais beaucoup pour la classe","choiceMaking_UAG.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_6 # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Salut Akane! Merci pour l'accueil à l'école aujourd'hui") from _call_message_start_9 # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpa, "Tkt. Je ne fais que mon devoir après tout") from _call_message_22
            jump .aftermenu
        label .choice2:
            $ ptsa1 += 1
            call phone_after_menu from _call_phone_after_menu_7
            call message_start(playerName, "J'ai l'impression que tu fais beaucoup pour la classe") from _call_message_start_10
            call message(playerName, "Je suis content qu'on ait quelqu'un d'aussi responsable comme déléguée.") from _call_message_23
            call message(tpa, "Merci beaucoup.") from _call_message_24
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "C'est beaucoup de travail quand même.") from _call_message_25
    call message (tpa, "Les gens sont très difficiles à gérer...") from _call_message_26
    call message (tpa, "Certaines ne semblent tout simplement pas capables d'écouter des consignes.") from _call_message_27
    call message (tpa, "J'espère que au moins tu es différent") from _call_message_28
    call message (tpa, "Au fait, voici un lien de mon site web. Il contient tous les cours, leçons, devoirs et examens à venir mis à jour régulièrement.") from _call_message_29
    call message (tpa, "{u}http://totallynotabadwebsite.com{/u}") from _call_message_30

    label choiceMaking_IPG:
        call screen phone_reply("Le site est un peu bizarre","choiceMaking_IPG.choice1","ah ok, j'irai peut-être voir.","choiceMaking_IPG.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_8
            $ ptsa1 += 1
            call message_start(playerName, "...") from _call_message_start_11
            call reply_message("Le site est un peu bizarre, est-ce qu'il est sûr ?") from _call_reply_message_6
            call message(tpa, "non.") from _call_message_31
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_9
            call message_start(playerName, "ah ok, j'irai peut-être voir") from _call_message_start_12
            call message(tpa, "^^") from _call_message_32
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "Au fait:") from _call_message_33
    call message (tpa, "Tu préfère les chats ou les chiens?") from _call_message_34

    label choiceMaking_DOC:
        call screen phone_reply("J'aime les deux","choiceMaking_DOC.choice1","Je préfère les chats","choiceMaking_DOC.choice2")
        label .choice1:
            $ ptsa1 += 1
            call phone_after_menu from _call_phone_after_menu_10
            call message_start(playerName, "J'aime les deux.") from _call_message_start_13
            call message(tpa, "Je vois, eh bien au moins tu penses aussi que les chiens sont mignons.") from _call_message_35
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_11
            call message_start(playerName, "Je préfère les chats.") from _call_message_start_14
            call message(tpa, "Je vois, chacun ses goûts.") from _call_message_36
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "J'adore les chiens") from _call_message_37
    call message (tpa, "Ils sont fidèles à leurs maîtres et font ce qu'on leur dit") from _call_message_38
    call message (tpa, "Du moins la plupart du temps...") from _call_message_39
    call message (tpa, "Si la plupart des gens avaient le même état d'esprit que les chiens, on aurait la paix dans le monde.") from _call_message_40
    call message (tpa, "Ou en tout cas quelque chose de mieux que ce qu'on a") from _call_message_41

    label choiceMaking_DAP:
        call screen phone_reply("Les gens ne sont pas des chiens","choiceMaking_DAP.choice1","Je suis d'accord","choiceMaking_DAP.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_12
            call message_start(playerName, "Mais, les gens ne sont pas des chiens...") from _call_message_start_15
            $ ptsa1 += 1
            call reply_message("Ils ont besoin de leur vie privée, de leur libre arbitre...") from _call_reply_message_7
            call message(tpa, "Peut-être.") from _call_message_42
            call message(tpa, "Mais au moins ce serait plus facile de maintenir l'ordre") from _call_message_43
            call message(playerName, "Tu te rend compte au moins de ce que tu dis?") from _call_message_44
            call message(tpa, "Oui.") from _call_message_45
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_13
            call message_start(playerName, "Je suis d'accord.") from _call_message_start_16
            call reply_message("Ils sont tellement sympa et mignons, tout le monde serait content") from _call_reply_message_8
            call message(tpa, "Haha") from _call_message_46
            jump .aftermenu
        label .aftermenu:

    call message (tpa, "D'ailleurs, j'adore faire du dog-sitting pendant mon temps libre.") from _call_message_47
    call message_img(tpa, "", "images/instagram/A2_insta.png") from _call_message_img
    call message (tpa, "Cela rapporte un peut d'argent.") from _call_message_48
    call message (tpa, "Ma famille est plutôt aisée") from _call_message_49
    call message (tpa, "Mais un peut d'argent de poche de temps en temps, ça ne fais de mal à personne") from _call_message_50
    call message (tpa, "Ca te dirais de m'accompagner un jour ?") from _call_message_51

    label choiceMaking_DSA:
        call screen phone_reply("Bien sûr!","choiceMaking_DSA.choice1","J'ai beaucoup à rattraper avec l'école","choiceMaking_DSA.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_14
            call message_start(playerName, "Bien sûr!") from _call_message_start_17
            $ ptsa1 += 1
            call reply_message("Je viendrai avec toi après avoir fini tous mes devoirs!") from _call_reply_message_9
            call message(tpa, "Parfait") from _call_message_52
            call message(tpa, "Au fait, c'est juste une formalité, mais...") from _call_message_53
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_15
            call message_start(playerName, "Je suis désolé") from _call_message_start_18
            call reply_message("J'ai beaucoup à rattraper avec l'école :((") from _call_reply_message_10
            call message(tpa, "Ok pas de problème") from _call_message_54
            call message(tpa, "Juste, au cas où tu changes d'avis...") from _call_message_55
            jump .aftermenu
        label .aftermenu:

    call message(tpa, "Tu peut me donner tes coordonnées banquaires?") from _call_message_56
    call message(tpa, "Comme ça on poura te faire un virement en avance...") from _call_message_57
    call phone_end(False) from _call_phone_end_4

    narrateur "Tu as décidé d'attendre de pouvoir faire le travail avant lui transmettre tes coordonnées."
    narrateur "Tu poses ton téléphone et tu t'endors..."
    scene black with fade
    narrateur "Le lendemain..."
    scene classroom day with fade
    pause 1.0
    c_akane "{cps=50}Bonjour, [playerName].{nw}"
    show screen cexp("apc", "aeb", "ams", "abn", h=h_mid)
    "{i}Holy Sweet Baby Jesus!!"
    "{i}Elle doit arrêter d'apparaître de nulle part."
    show screen cexp("apc", "ael", "ams", "abn", h=h_mid)
    playerName "Salut Akane, t'as besoin de quelque chose?"
    show screen cexp("apc", "ael", "amt", "abn", h=h_mid)
    c_akane "Oui, j'aurais besoin de ton aide."
    c_akane "Tu vois Himeno?"
    c_akane "La blonde un peu bronzée."
    show screen cexp("apc", "aeb", "ams", "abn", h=h_mid)
    c_akane "Tu peux lui envoyer ce lien?"
    show screen cexp("apc", "ael", "ams", "abn", h=h_mid)
    c_akane "C'est un chèque cadeau pour la remercier."
    c_akane "Tu vois, sa famille est très riche: elle donne beaucoup pour financer l'école."
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)

    menu:
        c_akane "Donc j'aimerais lui faire un petit cadeau de la part de toute la classe pour la remercier."
        "Euhh. Ca m'a l'air bizarre":
            $ ptsa1 += 1
            playerName "Euhh. Ca m'a l'air bizarre"
            show screen cexp("apr", "ael", "ams", "abn", h=h_mid)
            c_akane "Il est crypté pour que personne d'autre que Himeno peut l'ouvrir..."

        "D'accord, mais pourquoi ne le fais-tu pas toi-même?":
            playerName "D'accord, mais pourquoi ne le fais-tu pas toi-même?"
            show screen cexp("apr", "ael", "amt", "abn", h=h_mid)
            c_akane "C'est pour le symbolisme tu vois..."
            show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
            c_akane "Un nouvel élève qui remercie déja les bienfaiteurs de l'école, ça donnera un message positif."
    
    "{i}..."
    "{i}C'est la deuxième fois qu'Akane m'envoie quelque chose de suspect..."
    show screen cexp("apc", "ael", "ams", "abn", h=h_mid)
    playerName "Tu essayerais pas de nous arnaquer Himeno et moi par hasard?"
    show screen cexp("apr", "aea", "ams", "abn", h=h_mid)
    c_akane "..."
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    c_akane "Non."
    show screen cexp("apr", "aeb", "amt", "abn", h=h_mid)
    c_akane "C'a m'arrive de faire des blagues aux gens parfois..."
    c_akane "Mais rien de méchant."
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    menu:
        c_akane "Et donc sinon, pour le lien?"
        "Tu ne devrais pas prendre l'argent des autres":
            $ ptsa1 += 1
            playerName "Akane, tu ne devrais pas avoir envie de prendre l'argent des autres."
            playerName "Penses à l'autre qui est plus misérable et en prenant le peu qu'il a, tu lui ruine sa vie!"
            show screen cexp("apr", "ael", "amt", "abn", h=h_mid)
            c_akane "Pardon?"

        "Je peux attendre un peu plus longtemps ?":
            playerName "..."
            playerName "Est-ce que tu pourais me laisser un peut plus de temps?"
            playerName "Histoire que je fasse bien connaissance avec tout le monde..."
    show screen cexp("apr", "ael", "amn", "abn", h=h_mid)
    c_akane "Bon, si tu n'as pas envie de le faire, je vais m'en occuper" 
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    c_akane "Je dois y aller, on se revéras plus tard."
    hide screen cexp
    
    if ptsa1 >= 4:
        jump RAF1
    else:
        jump RAB1

label RAB1:
    "{i}Bon, et puis zut! Qu'est-ce qui pourai mal se passer de toute façon?"
    scene black with fade

    """{i}Ça fait une semaine que je suis arrivé à l'école.{/i}

    {i}J'ai appris les noms de tout le monde, mais je ne me suis pas fait de véritables amis.{/i}

    {i}J'ai décidé d'envoyer le \"cadeau\" d'Akane à Himeno. {/i}

    ...

    ..."""
    scene classroom late with fade 

    """{i}Cela fait trois jours que j'ai envoyé ce lien à Himeno.{/i}

    {i}Je me demande ce que c'était, mais je passe à autre chose et je continue ma journée.{/i}"""
    "Prof" "Les deux solutions à ces fonctions sont-"
    "???" "Excusez-moi. Est-ce que Akane Kousei est là ?"
    show screen cexp("apc", "aea", "amn", "abn", h=h_mid)
    playerName "Akane, qu'est-ce qui se passe?"
    c_akane "..."

    "{i}Elle semble pâle mais calme.{/i}"
    "Prof" "Qui êtes-vous? Ceci est une salle de classe. Vous ne pouvez pas simplement rentrer comme ça!"
    "Mr. Aki" """Je suis le détective Aki. Je suis là pour une enquête sur une affaire impliquant Akane Kousei.

    Mademoiselle Kousei, veuillez sortir et venir avec moi."""
    show screen cexp("apc", "aea", "ams", "abn", h=h_mid)
    pause
    hide screen cexp
    scene black with fade
    """{i}On a appris par Himeno que Akane était responsable de vol et de diverses arnaques en ligne.
    
    {i}Himeno étais l'une des victimes, elle avais perdu beaucoup d'argent à cause de ça.

    {i}Il faudrais qu'elle fasse plus attention à ce qu'elle achète.
    
    {i}Un an plus tard, Akane a été mise en procès.{/i}"""
    scene AB1 with fade
    "Juges" """Kousei Akane.

    Vous êtes accusé de vol contre la famille Yuzu.

    Vous plaidez coupable ?"""
    c_akane "Oui, messieurs."
    "{i}..."
    "{i}Je pense qu'Akane ne pourra jamais finir sa scolarité...{/i}"
    window hide
    pause

    jump game_over

label RAF1:
    define ptsa2 = 0
    scene bedroom with fade
    narrateur "Quelques jours plus tard..."
    call phone_start(usrc, "20:36") from _call_phone_start_5
    call message_start (tpa, "Bonjour, [playerName]. Je sais que ça fait une semaine que je t'ai dit d'envoyer ce lien à Himeno, mais au final t'as plus besoin de le faire.") from _call_message_start_19
    call reply_message ("Ok...") from _call_reply_message_11
    call message (tpa, "Au fait, Je sais pas si tu as remarqué, mais il y a quelqu'un en ligne qui se fait passer pour moi.") from _call_message_58
    call message (tpa, "Il prend des photos de moi, vole mes photos de {b}mon{/b} compte et les publient comme les siennes.") from _call_message_59
    call message (tpa, "C'est légèrement inquiétant...") from _call_message_60

    pause
    window show
    "{i}Elle parle de Bomi?"
    window hide
    
    label choiceMaking_WGD:
        call screen phone_reply("Ca fait peur","choiceMaking_WGD.choice1","Tu devrais le dénoncer","choiceMaking_WGD.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_16
            call message_start(playerName, "Ca fait peur.") from _call_message_start_20
            call reply_message("Qu'est-ce que tu vas faire?") from _call_reply_message_12
            call message(tpa, "Non, pas vraiment. Je ne me sent pas menaçée à ce point.") from _call_message_61
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_17
            call message_start(playerName, "Tu devrais le dénoncer") from _call_message_start_21
            $ ptsa2 += 1
            call message(tpa, "C'est inutile, Ils ne feront sûrement rien") from _call_message_62
            call message(tpa, "Je ne peux même pas si je le voulais de toute façon") from _call_message_63
            call message(tpa, "Je n'ai aucune idée de qui il s'agit.") from _call_message_64

            jump .aftermenu
        label .aftermenu:
    
    pause
    window show
    "{i}..."
    window hide

    label choiceMaking_USP:
        call screen phone_reply("Tu devrais prendre des précautions","choiceMaking_USP.choice1","Tu as raison","choiceMaking_USP.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_18
            call message_start(playerName, "Tu devrais prendre des précautions.") from _call_message_start_22
            $ ptsa2 += 1
            call message(tpa, "Ok mais comment?") from _call_message_65
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_19
            call message_start(playerName, "Tu as raison, il n'y a aucune raison pour que cette personne ne devienne un danger pour toi...") from _call_message_start_23
            call message(tpa, "Bien sûr que j'ai raison.") from _call_message_66
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "Je dois manger, salut.") from _call_message_67
    call phone_end from _call_phone_end_5

    "{i}..."
    "{i}Est-ce que je lui dit?"
    "{i}..."

    call phone_start (usrcf, "20:38") from _call_phone_start_6
    call message_start(tpa, " Bonjour, [playerName]!") from _call_message_start_24
    call message(tpa, "Comment vas-tu depuis la semaine dernière?") from _call_message_68
    call message(tpa, "J'espère que ça va.") from _call_message_69
    call reply_message("...") from _call_reply_message_13
    call reply_message("Bomi Park?") from _call_reply_message_14
    call message(tpa, "Quoi?") from _call_message_70
    call message(tpa, "Pourquoi mentionnes-tu son nom ?") from _call_message_71

    label choiceMaking_KUR:
        call screen phone_reply("Je sais qui tu es","choiceMaking_KUR.choice1","Non, rien...","choiceMaking_KUR.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_20
            $ ptsa2 += 1
            call message_start(playerName, "Je sais qui tu es.") from _call_message_start_25
            call message(tpa, "...") from _call_message_72
            call message(tpa, "Ne parle jamais de ça.") from _call_message_73
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_21
            call message_start(playerName, "Ah, rien. J'aimerais en savoir plus sur elle") from _call_message_start_26
            call reply_message("Elle semble être la plus forte de notre classe et j'aimerais savoir comment elle fait") from _call_reply_message_15
            call message(tpa, "Je pourais...") from _call_message_74
            call message(tpa, "Mais non.") from _call_message_75
            jump .aftermenu
        label .aftermenu:
    call phone_end from _call_phone_end_6

    "{i}..."
    "{i}Je devrais avertir Akane."

    call phone_start(usrc, "20:38") from _call_phone_start_7
    label choiceMaking_PBC:
        call screen phone_reply("Sois super prudente","choiceMaking_PBC.choice1","Je vais t'aider à te protéger","choiceMaking_PBC.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_22
            call message_start(playerName, "Akane. S'il te plaît, sois super prudente.") from _call_message_start_27
            call message(tpa, "Je le serai.") from _call_message_76
            call message(tpa, "Mais pourquoi tu t'inquiète, ce n'es pas grave tu sais.") from _call_message_77
            call message(tpa, "Juste un peut énervant...") from _call_message_78
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_23
            $ ptsa2 += 1
            call message_start(playerName, "Akane, je vais t'aider à mettre en place des précautions.") from _call_message_start_28
            call reply_message("On devrait également le signaler pendant qu'on y est comme ça la situation ne deviendra pas incontrôlable.") from _call_reply_message_16
            call message(tpa, "Ok") from _call_message_79
            jump .aftermenu
        label .aftermenu:
    call phone_end from _call_phone_end_7
    "{i}...{/i}"
    if ptsa2 > 2:
        jump RAF
    else:
        jump RAB2

label RAB2:
    "{i}Une semaine plus tard, tu reçois une notification de ton tel et tu vois Himeno est live."

    c_himeno """Oh.

    Mon.

    Dieu.

    Akane a transfert d'ecole!

    Elle est maintenant à l'ecole Z.

    Venons lui dire au revoirs </3"""

    "{i}...

    Je devrais la chercher"
    
    "..."
    scene AB2 with fade
    playerName "Akane!"
    c_akane "Ah. [playerName]."
    playerName "Tu fais quoi?"
    c_akane "Je déménage."
    playerName "???"
    c_akane "Le faux Akane m'a déménage à l'école Z."
    playerName "Mais pourquoi tu ne fais rien?"
    c_akane """Mes parents ont déjà accepté. Je ne peux rien faire.

    au revoir, [playerName]."""

    window hide
    pause
    jump game_over

label RAF:
    scene blacks with fade
    "{i}J'ai rencontré Akane le lendemain à l'école."
    scene AGE with fade
    c_akane "Alors que veux-tu que je fasse ?"
    playerName "Alors..."
    """{i}J'ai expliqué à Akane les choses les plus élémentaires sur la façon de protéger son identité en ligne, mais elle semblait en savoir plus que moi.{/i}
    
    {i}Elle a fini par me guider pendant qu'elle mettait en place les précautions pour elle-même.{/i}"""
    c_akane """Merci de penser à moi.
    
    Aller, on rentre?"""

    window hide
    pause
    jump happy_ending


