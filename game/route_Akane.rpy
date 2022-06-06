label route_A:
    define good_points = 0
    narrateur "Vous décidez de rentrer chez vous dirrectement."
    scene bedroom with fade

    call phone_start(usra, "18:45")
    label choiceMaking_UAG: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Merci pour l'accueil à l'école aujourd'hui","choiceMaking_UAG.choice1","Tu fais beaucoup pour la classe","choiceMaking_UAG.choice2")
        label .choice1:
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Salut Akane! Merci pour l'accueil à l'école aujourd'hui") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpa, "Tkt. Je ne fais que mon devoir après tout")
            jump .aftermenu
        label .choice2:
            $ good_points += 1
            call phone_after_menu
            call message_start(playerName, "J'ai l'impression que tu fais beaucoup pour la classe")
            call message(tpa, "Je suis content qu'on ait quelqu'un d'aussi responsable comme déléguée.")
            call message(tpa, "Merci beaucoup.")
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "C'est beaucoup de travail quand même.")
    call message (tpa, "Les gens sont très difficiles à gérer...")
    call message (tpa, "Certaines ne semblent tout simplement pas capables d'écouter des consignes.")
    call message (tpa, "J'espère que au moins tu es différent")
    call message (tpa, "Au fait, voici un lien de mon site web. Il contient tous les cours, leçons, devoirs et examens à venir mis à jour régulièrement.")
    call message (tpa, "{u}http://totallynotabadwebsite.com{/u}")

    label choiceMaking_IPG:
        call screen phone_reply("Le site est un peu bizarre, est-ce qu'il est sûr ?","choiceMaking_IPG.choice1","ah ok, j'irai peut-être voir.","choiceMaking_IPG.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "...")
            call reply_message("Le site est un peu bizarre, est-ce qu'il est sûr ?")
            call message(tpa, "non.")
            jump .aftermenu
        label .choice2:
            $ good_points += 1
            call phone_after_menu
            call message_start(playerName, "ah ok, j'irai peut-être voir")
            call message(tpa, "^^")
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "Au fait:")
    call message (tpa, "Tu préfère les chats ou les chiens?")

    label choiceMaking_DOC:
        call screen phone_reply("J'aime les deux","choiceMaking_DOC.choice1","Je préfère les chats","choiceMaking_DOC.choice2")
        label .choice1:
            $ good_points += 1
            call phone_after_menu
            call message_start(playerName, "J'aime les deux.")
            call message(tpa, "Je vois, eh bien au moins tu penses aussi que les chiens sont mignons.")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je préfère les chats.")
            call message(tpa, "Je vois, chacun ses goûts.")
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "J'adore les chiens")
    call message (tpa, "Ils sont fidèles à leurs maîtres et font ce qu'on leur dit")
    call message (tpa, "Au moins la plupart du temps...")
    call message (tpa, "Si la plupart des gens avaient le même état d'esprit que les chiens, on aurait la paix dans le monde.")
    call message (tpa, "Ou quelque chose de mieux que ce qu'on a")

    label choiceMaking_DAP:
        call screen phone_reply("Les gens ne sont pas des chiens","choiceMaking_DAP.choice1","Je suis d'accord","choiceMaking_DAP.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Mais, les gens ne sont pas des chiens...")
            $ good_points += 1
            call reply_message("Ils ont besoin de leur vie privée, de leur libre arbitre...")
            call message(tpa, "Peut-être.")
            call message(tpa, "Mais au moins ce serait plus facile de maintenir l'ordre")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je suis d'accord.")
            call reply_message("Ils sont tellement sympa et mignons, tout le monde serait content")
            call message(tpa, "Haha")
            jump .aftermenu
        label .aftermenu:

    call message (tpa, "D'ailleurs, j'adore faire du dog-sitting pendant mon temps libre.")
    call message_img(tpa, "", "images/instagram/A2_insta.png")
    call message (tpa, "Cela rapporte un peut d'argent.")
    call message (tpa, "Ma famille est plutôt aisée")
    call message (tpa, "Mais un peut d'argent de poche de temps en temps, ça ne fais de mal à personne")
    call message (tpa, "Tu veux m'accompagner un jour ?")

    label choiceMaking_DSA:
        call screen phone_reply("Bien sûr!","choiceMaking_DSA.choice1","J'ai beaucoup à rattraper avec l'école","choiceMaking_DSA.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Bien sûr!")
            $ good_points += 1
            call reply_message("Je viendrai avec toi après avoir fini tous mes devoirs!")
            call message(tpa, "Parfait")
            call message(tpa, "Au fait, c'est juste une formalité, mais...")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je suis désolé")
            call reply_message("J'ai beaucoup à rattraper avec l'école :((")
            call message(tpa, "Ok pas de problème")
            call message(tpa, "Juste, au cas où tu changes d'avis...")
            jump .aftermenu
        label .aftermenu:

    call message(tpa, "Tu peut me donner tes coordonnées banquaires?")
    call message(tpa, "Comme ça on poura te faire un compte en avance...")
    call phone_end

    narrateur "Tu as décidé d'attendre de pouvoir faire le travail avant lui transmettre tes coordonnées."
    narrateur "Tu poses ton téléphone et tu t'endors..."
    scene black with fade
    narrateur "Le lendemain..."
    scene classroom day with fade
    pause 1.0
    c_akane "{cps=50}Bonjour, [playerName].{nw}"

    "{i}Holy Sweet Baby Jesus!!"
    "{i}Elle doit arrêter d'apparaître de nulle part."
    playerName "Salut Akane, t'as besoin de quelque chose?"
    c_akane "Oui, j'aurais besoin de ton aide."
    c_akane "Tu vois Himeno?"
    c_akane "La blonde un peu bronzée."
    c_akane "Tu peux lui envoyer ce lien?"
    c_akane "C'est un chèque cadeau pour la remercier."
    c_akane "Tu vois, sa famille est très riche: elle donne beaucoup pour financer l'école."
    c_akane "Donc j'aimerais lui faire un petit cadeau de la part de toute la classe pour la remercier."

    menu:
        "Euhh. Ca m’a l’air bizarre":
            $ good_points += 1
            playerName "Euhh. Ca m’a l’air bizarre"
            c_akane "Il est crypté pour que personne d'autre que Himeno peut l'ouvrir..."

        "D’accord, mais pourquoi ne le fais-tu pas toi-même?":
            playerName "D’accord, mais pourquoi ne le fais-tu pas toi-même?"
            c_akane "C'est pour le symbolisme tu vois..."
            c_akane "Un nouvel élève qui remercie déja les bienfaiteurs de l'école, ça donnera un message positif."
    
    "{i}..."
    "{i}C'est la deuxième fois qu'Akane m'envoie quelque chose à ouvrir..."
    playerName "Tu essayerais pas de nous arnaquer Himeno et moi par hasard?"
    c_akane "..."
    c_akane "Non." #sourit

    menu:
        "Tu ne devrais pas prendre l'argent des autres":
            $ good_points += 1
            playerName "Akane, tu ne devrais pas avoir envie de prendre l'argent des autres. Tu n'e pense qu'à l'autre plus misérable et causer plus de chaos en prenant le peu qu'il a."
            c_akane "Pardon?"

        "Je peux attendre un peu plus longtemps ?":
            playerName "Est-ce que tu pourais me laisser un peut plus de temps?"
            playerName "Histoire que je fasse bien connaissance avec tout le monde..."
    
    c_akane "Bon, si tu n'as pas envie de le faire, je vais m'en occuper" 
    c_akane "Je dois y aller, on se revéras plus tard."
    scene black with fade

    if good_points >= 4:
        jump RAF1
    else:
        jump RAB1

label RAB1:
    """{i}Qu’est-ce qui pourrait se passer?{/i}

    {i}Ça fait une semaine que je suis arrivé à l'école.{/i}

    {i}J'ai appris les noms de tout le monde, mais je ne me suis pas fait de véritables amis.{/i}

    {i}J'ai décidé d'envoyer le cadeau d'Akane à Himeno. {/i}

    {i}Je suis sûr que ce n'est rien de grave.{/i}

    …

    …"""
    scene classroom late with fade 

    """{i}Cela fait trois jours que j'ai envoyé ce lien à Himeno.{/i}

    {i}Je me demande ce que c'était, mais je passe à autre chose et je continue ma journée.{/i}"""
    "Professeur" "Les deux solutions à ces fonctions sont-"
    "???" "Excusez-moi. Est-ce que Akane Kousei est là ?"
    """{i}Je jette un coup d'œil à Akane.{/i}

    {i}Elle semble pâle mais calme.{/i}"""
    "Teacher" "Qui êtes-vous? Ceci est une salle de classe. Vous ne pouvez pas simplement rentrer comme ça."
    "Detective Aki" """Je suis le détective Aki. Je suis là pour une enquête sur une affaire impliquant Akane Kousei.

    Veuillez sortir et venir avec moi."""
    """{i}Je m'attendais à ce que Akane commence enfin à montrer de l'émotion et à se battre, mais elle les a simplement suivis calmement avec un sourire.{/i}

    {i}On a appris par Himeno que Akane était responsable de vol parce que Himeno ne faisait pas attention à ce qu’elle achète.{/i}"""

    "{i}Un an plus tard, Akane a été mise en procès.{/i}"
    scene AB1 with fade
    "Juges" """Kousei Akane.

    Vous êtes accusé de vol contre la famille Yuzu.

    Vous plaidez coupable ?"""
    c_akane "Oui, messieurs."
    "{i}Je pense qu'Akane ne pourra jamais finir sa scolarité...{/i}"

    jump game_over

label RAF1:
    define good_points = 0
    scene bedroom with fade
    narrateur "Quelques jours plus tard..."
    call phone_start(usra, "20:36")
    call message_start (tpa, "Bonjour, [playerName]. Je sais que ça fait une semaine que je t'ai dit d'envoyer ce lien à Himeno, mais au final t'as plus besoin de le faire.")
    call reply_message ("Ok...")
    call message (tpa, "Au fait, Je sais pas si tu as remarqué, mais il y a quelqu'un en ligne qui se fait passer pour moi.")
    call message (tpa, "Il prend des photos de moi, vole mes photos de mon compte et les publient comme les siennes.")
    call message (tpa, "C'est légèrement inquiétant...")

    window show
    "{i}Elle parle de Bomi?"
    window hide
    
    label choiceMaking_WGD:
        call screen phone_reply("Ca fait peur","choiceMaking_WGD.choice1","Tu devrais le dénoncer","choiceMaking_WGD.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Ca fait peur.")
            call reply_message("Qu'est-ce que tu vas faire?")
            call message(tpa, "Non, pas vraiment. Je ne me sent pas menaçée à ce point.")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Tu devrais le dénoncer")
            call message(tpa, "C'est inutile, Ils ne feront sûrement rien")
            call message(tpa, "Je ne peux même pas si je le voulais de toute façon")
            call message(tpa, "Je n'ai aucune idée de qui il s'agit.")

            jump .aftermenu
        label .aftermenu:
    
    window show
    "{i}..."
    window hide

    label choiceMaking_USP:
        call screen phone_reply("Tu devrais prendre des précautions","choiceMaking_USP.choice1","Je ne veut pas que tu ais des problèmes","choiceMaking_USP.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Tu devrais prendre des précautions.")
            call message(tpa, "Ok mais comment?")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je ne veut pas que tu ais des problèmes")
            call message(tpa, "Je peux prendre soin de moi, ne t'inquiète pas")
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "Je dois manger, salut.")
    call phone_end

    "{i}..."
    "{i}Est-ce que je lui dit?"
    "{i}..."

    call phone_start (usraf, "20:38")
    call message_start(tpa, " Bonjour, [playerName]!")
    call message(tpa, "Comment vas-tu depuis la semaine dernière?")
    call message(tpa, "J'espère que ça va.")
    call reply_message("...")
    call reply_message("Bomi Park?")
    call message(tpa, "Quoi?")
    call message(tpa, "Pourquoi mentionnes-tu son nom ?")

    label choiceMaking_KUR:
        call screen phone_reply("Je sais qui tu es","choiceMaking_KUR.choice1","Non, rien...","choiceMaking_KUR.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Je sais qui tu es.")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Ah, rien. J'aimerais en savoir plus sur elle")
            call reply_message("Elle semble être la plus forte de notre classe et j'aimerais savoir comment elle fait")
            call message(tpa, "Je pourais...")
            call message(tpa, "Mais non.")
            jump .aftermenu
        label .aftermenu:
            call message(tpa, "...")
            call message(tpa, "Ne parle jamais de ça.")
    call phone_end

    "{i}..."
    "{i}Je devrais avertir Akane."

    call phone_start(usra, "20:38")
    label choiceMaking_PBC:
        call screen phone_reply("Sois super prudente","choiceMaking_PBC.choice1","Je vais t'aider à te protéger","choiceMaking_PBC.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Akane. S'il te plaît, sois super prudente.")
            call message(tpa, "Je le serai.")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Akane, je vais t'aider à mettre en place des précautions.")
            call reply_message("On devrait également le signaler pendant qu'on y est comme ça la situation ne deviendra pas incontrôlable.")
            call message(tpa, "Ok")
            jump .aftermenu
        label .aftermenu:
    call phone_end
    "..."
    if good_points > 2:
        jump RAF
    else:
        jump RAB2

label RAB2:
    "{i}Une semaine plus tard, tu reçois une notification de ton tel et tu vois Himeno est live."

    c_himeno """Oh.

    Mon.

    Dieu.

    Akane a transfert d’ecole!

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

label RAF:
    "{i}J'ai rencontré Akane le lendemain à l'école."
    c_akane "Alors que veux-tu que je fasse ?"
    playerName "Alors…"
    """{i}J'ai expliqué à Akane les choses les plus élémentaires sur la façon de protéger son identité en ligne, mais elle semblait en savoir plus que moi.{/i}
    
    {i}Elle a fini par me guider pendant qu'elle mettait en place les précautions pour elle-même.{/i}"""
    c_akane """Merci de penser à moi.
    
    Aller, on rentre?"""
    
    scene AGE with fade
    pause
    jump happy_ending


