label route_B:
    define good_points = 0
    scene bedroom_sleep with fade
    call phone_start(usrb, "20:23")
    label choiceMaking_HID: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Hey Bomi, pourquoi tu te caches?","choiceMaking_HID.choice1","Hé bien madame la déléguée, tu n'as pas du tout la même tête en vrai.","choiceMaking_HID.choice2")

        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Hey Bomi, pourquoi tu te caches?") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpb, "Ah, tu m'as trouvé?")
            $ good_points += 1
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Hé bien madame la déléguée, tu n'as pas du tout la même tête en vrai.")
            call message(tpb, "...")
            jump .aftermenu
        label .aftermenu:
    call message(tpb, "Ecoute, je suis désollé de t'avoir menti")
    call message(tpb, "J'admire beaucoup Akane. Elle est intelligente, elle est belle, elle est confiante...")
    call message(tpb, "Mon seul atout est mon niveau scolaire.")
    call message(tpb, "Comparé à elle, ce n'est pas grand chose.")
        
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