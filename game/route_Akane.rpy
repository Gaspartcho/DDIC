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
            call message(tpa, "...")
            call message(tpa, "non...")
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
    narrateur "Le landemain..."
    scene classroom day with fade
    pause 1.0
    c_akane "{cps=50}Bonjour, [playerName].{nw}"

    "{i}Holy Sweet Baby Jesus!!"
    "{i}Elle doit arrêter d'apparaître de nulle part."