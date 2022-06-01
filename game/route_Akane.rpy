label route_A:
    define good_points = 0
    narrateur "Vous décidez de rentrer chez vous dirrectement."
    scene bedroom with fade

    call phone_start(usra, "18:45")
    call message_start(tpa, "Salut [playerName], Comment s'es passé ta première journée?")
    call message(playerName, "Très bien, merci.")
    pause 2.0
    
    label choiceMaking_UAG: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Merci pour l'accueil aujourd'hui","choiceMaking_UAG.choice1","Tu fais beaucoup pour la classe","choiceMaking_UAG.choice2")
        label .choice1:
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Encore merci pour l'accueil à l'école aujourd'hui") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpa, "Tkt. Je ne fais que mon devoir après tout")
            jump .aftermenu
        label .choice2:
            $ good_points += 1
            call phone_after_menu
            call message_start(playerName, "J'ai l'impression que tu fais beaucoup pour la classe")
            call reply_message("Je suis content qu'on ait quelqu'un d'aussi responsable.")
            call message(tpa, "Merci beaucoup.")
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "N'empèche, avec ton arrivée, on commence à être beaucoup.")
    call message (tpa, "Les gens sont très difficiles à gérer...")
    call message (tpa, "Certaines ne semblent tout simplement pas capables d'écouter des consignes.")
    call message (tpa, "J'espère que au moins tu es différent")
    call message (tpa, "Au fait, voici un lien de mon site web. Il contient tous les cours, leçons, devoirs et examens à venir mis à jour régulièrement.")
    call message (tpa, "{u}http://ipgraber.shadowsite.com{/u}")

    label choiceMaking_IPG:
        call screen phone_reply("Ce n'est pas un ip grabber?","choiceMaking_IPG.choice1","Haha merci!","choiceMaking_IPG.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "...")
            call message(playerName, "C'est un ip grabber ça non?")
            call message(tpa, "non.")
            jump .aftermenu
        label .choice2:
            $ good_points += 1
            call phone_after_menu
            call message_start(playerName, "Haha merci! C'est super utile")
            call message(tpa, "^^")
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "Au fait:")
    call message (tpa, "Tu préfère les chats ou les chiens?")

    label choiceMaking_DOC:
        call screen phone_reply("J'aime les deux","choiceMaking_DOC.choice1","Je préfère les chats","choiceMaking_DOC.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "J'aime les deux.")
            call message(tpa, "oh... tu penses aussi que les chiens sont mignons.")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je préfère les chats.")
            call message(tpa, "Je vois, chacun le sien.")
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "J'adore les chiens")
    call message (tpa, "Ils sont fidèles à leurs maîtres et font ce qu'on leur dit")
    call message (tpa, "Au moins la plupart du temps...")
    call message (tpa, "Si la plupart des gens avaient le même état d'esprit que les chiens, on aurait la paix dans le monde.")
    call message (tpa, "Ou quelque chose comme ça")

    label choiceMaking_DAP:
        call screen phone_reply("Les gens ne sont pas des chiens","choiceMaking_DAP.choice1","Je suis d'accord","choiceMaking_DAP.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Mais, les gens ne sont pas des chiens...")
            call message(playerName, "Ils ont besoin de leur vie privée, de leur libre arbitre...")
            call message(tpa, "Peut-être.")
            call message(tpa, "Mais au moins ce serait plus facile de maintenir l'ordre")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je suis d'accord.")
            call message(playerName, "Ils sont tellement sympa et mignons, tout le monde serait content")
            call message(tpa, "Haha")
            jump .aftermenu
        label .aftermenu:

    call message (tpa, "D'ailleurs, j'adore faire du dog-sitting pendant mon temps libre.")
    call message_img(tpa, "", "images/instagram/A2_insta.png")
    call message (tpa, "Cela rapporte un peut d'argent.")
    call message (tpa, "Un peut d'argent de poche de temps en temps, ça ne fais ed mal à personne")
    call message (tpa, "Tu veux m'accompagner un jour ?")

    label choiceMaking_DSA:
        call screen phone_reply("Bien sûr!","choiceMaking_DSA.choice1","J'ai beaucoup à rattraper avec l'école","choiceMaking_DSA.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Bien sûr!")
            call message(playerName, "Je viendrai avec toi après avoir fini tous mes devoirs!")
            call message(tpa, "Parfait")
            call message(tpa, "Au fait, c'est juste une formalité, mais...")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je suis désolé")
            call message(playerName, "J'ai beaucoup à rattraper avec l'école :((")
            call message(tpa, "Ok pas de problème")
            call message(tpa, "Juste, au cas où tu changes d'avis...")
            jump .aftermenu
        label .aftermenu:

    call message(tpa, "Tu peut me donner tes coordonnées banquaires?")
    call message(tpa, "Comme ça on poura te payer en avance...")
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
    c_akane "Tu vois Himeno, la fille dont je t'ai parlé l'autre jour."
    playerName "Oui et?"
    c_akane "J'aurais besoin que tu lui envoies ce lien."
    c_akane "C'est un chèque caudeau pour la remercier."
    c_akane "Tu vois, sa famille est très riche: elle donne beaucoup pour financer l'école."
    c_akane "Donc j'aimerais lui faire un petit cdeau de la part de toute la classe pour la remercier."

    menu:
        "Euhh. Ton chèque à l'air bizarre":
            c_akane "Il est crypté pour que personne d'autre que Himeno peut l'ouvrir..."

        "Tu ne peut pas le faire toi-même?":
            c_akane "C'est pour le simbolisme tu vois..."
            c_akane "Un vouvel élève qui remercie déja les bienfaiteurs de l'école, ça donnera un message positif."
    
    "{i}..."
    "{i}C'est la deuxième fois qu'Akane m'envoie quelque chose à ouvrir..."
    playerName "Tu essayerais pas de nous arnaquer Himeno et moi par hasard?"
    c_akane "..."
    c_akane "Non." #sourit

    menu:
        "Tu ne devrais pas prendre l'argent des autres":
            playerName "Akane, tu ne devrais pas avoir envie de prendre l'argent des autres. Tu n'e pense qu'à l'autre plus misérable et causer plus de chaos en prenant le peu qu'il a."
            c_akane "Pardon?"

        "Je peux attendre un peu plus longtemps ?":
            playerName "Est-ce que tu pourais me laisser un peut plus de temps?"
            playerName "Histoire que je fasse bien connaissance avec tout le monde..."
    
    c_akane "Bon, si tu n'as pas envie de le faire, je vais m'en occuper" # fachée
    c_akane "Je dois y aller, on se revéras plus tard."

    if good_points > 4:
        jump RAB1
    else:
        jump RAF1

label RAB1:
    #a changer parce que j'aime pas (ou au moins on refait un ou 2 trucs)
    jump game_over

label RAF1:
    scene bedroom with fade
    narrateur "Quelques jours plus tard..."
    call phone_start(usra, "20:36")
    call message_start (tpa "Bonjour, [playerName]. Je sais que ca fait une semaine que je t'ai dit d'envoyer ce lien à Himeno, mais au final t'as plus besoin de le faire.")
    call messsage (playerName, "Ok...")
    call message (tpa, "Au fait, Je sais pas si tu as remarqué, mais il y a quelqu'un en ligne qui se fait passer pour moi.")
    call message (tpa, "Il prend des photos de moi, vole mes photos de mon compte et les publient comme les siennes.")
    call message (tpa "C'est légèrement inquiétant...")

    window show
    "{i}Elle parle de Bomi?"
    window hide
    
    label choiceMaking_WGD:
        call screen phone_reply("Ca fait peur","choiceMaking_WGD.choice1","Tu devrais le dénoncer","choiceMaking_WGD.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Ca fait peur.")
            call message(playerName, "Qu'est-ce que tu vas faire?")
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
            call message(playerName, "Ok mais comment?")
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

    call phone_start (usra, "20:38")
    call message_start(tpa, " Bonjour, [playerName]!")
    call message(tpa, "Comment se passe les cours depuis la semaine dernière?")
    call message(tpa, "Tout vas bien j'espère?")
    call message(playerName, "...")
    call message(playerName, "Bomi Park?")
    call message(tpa, "Quoi?")
    call message(tpa, "Pourquoi est-ce que tu mentionnes son nom ?")

    label choiceMaking_KUR:
        call screen phone_reply("Je sais qui tu es","choiceMaking_KUR.choice1","Non, rien...","choiceMaking_KUR.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Je sais qui tu es.")
            call message(tpa, "...")
            call message(tpa, "Ne parle jamais de ça!")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Ah, rien. J'aimerais en savoir plus sur elle")
            call message(playerName, "Elle semble être la plus forte de notre classe et j'aimerais savoir comment elle fait")
            call message(tpa, "Je pourais...")
            call message(tpa, "Mais non.")
            jump .aftermenu
        label .aftermenu:
    call phone_end

    "{i}..."
    "{i}Je devrais avertir Akane..."

    call phone_start("kousei.akane (Real)")
    label choiceMaking_PBC:
        call screen phone_reply("Sois super prudente","choiceMaking_PBC.choice1","Je vais t'aider à te protéger","choiceMaking_PBC.choice2")
        label .choice1:
            call phone_after_menu
            call message_start(playerName, "Je sais qui tu es.")
            call message(tpa, "...")
            call message(tpa, "Ne parle jamais de ça!")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Ah, rien. J'aimerais en savoir plus sur elle")
            call message(playerName, "Elle semble être la plus forte de notre classe et j'aimerais savoir comment elle fait")
            call message(tpa, "Je pourais...")
            call message(tpa, "Mais non.")
            jump .aftermenu
        label .aftermenu:
    call phone_end