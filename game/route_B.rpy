label route_B:
    label RB1:
        define good_points = 0
        call phone_start("bombomii", "21:30")
        label choiceMaking_WAY: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Merci! Je vais essayer d’être sage :)","choiceMaking_WAY.choice1","Merci! Je te trouve très belle, ce qui est naturel pour une déléguée!","choiceMaking_WAY.choice2")

        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Merci! Je vais essayer d’être sage :)") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(ta, "Haha ! Si tu veux, je t'enverrai par e-mail ce qu’on a fait depuis le début de l’année dans nos cours en commun^^")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Merci! Je te trouve très belle, ce qui est naturel pour une déléguée!")
            call message(ta, "Ahh… Merci beaucoup ^^")
            jump .aftermenu
        menu:
            c_bomi "..."

            "Hey Bomi, pourquoi tu te caches?":
                $ good_points += 1
                c_bomi "Ah, tu l'as remarqué?"
                # Blushes (kind of)
            
            "Hé bien madame la déléguée, tu n'as pas du tout la même tête en vrai.":
                #looks down
                c_bomi "..."
            
        c_bomi "Ecoute, je suis désollé de t'avoir menti"
        c_bomi "J'admire beaucoup Akane. Elle est intelligente, elle est belle, elle est confiante..."
        c_bomi "Mon seul atout est mon niveau scolaire."
        c_bomi "Comparé à elle, ce n'est pas grand chose."

        menu:
            c_bomi "..."

            "Je pense que chacun a son charme.":
                $ good_points += 1
                playerName "Je pense que chacun a son charme."
                playerName "Je suis sûr que tu es tout aussi adorable"
                c_bomi "Peut-être que tu a raison..."

            "C'est vrais qu'elle est impressionnante":
                jump .after_menu

        c_bomi "De toute façon, je ne suis pas la seule à l'admirer. Beaucoup de gens voudraient être à sa place ou avec elle."
        c_bomi "..."
        c_bomi "Est-ce que je devrais me coifer?"

        menu:
            "Oui":
                playerName "À mon avis, tu devrais faire ce que tu veux, c'est juste une coupe de cheveux après tout."
                c_bomi "Oui..."
                c_bomi "C'est ça..."
            
            "Non":
                $ good_points += 1
                playerName "J'aime ta coupe. Je ne pense pas que tu devrais les couper pour l'instant"
                c_bomi "Je sais mais..."
                c_bomi "Elle à l'air si sure d'elle comme ça..."
        
        c_bomi "..."
        c_bomi "Bon, je dois y aller..."
        c_bomi "A demain."


        jump route_B