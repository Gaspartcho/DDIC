label route_B:
    define good_points = 0
    scene bedroom_sleep with fade
    call phone_start(usrb, "20:23")
    label choiceMaking_HID: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Hey Bomi, pourquoi tu te caches?","choiceMaking_HID.choice1","Hé bien madame la déléguée, tu n'as pas du tout la même tête en vrai.","choiceMaking_HID.choice2")

        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Hey Bomi, pourquoi tu te caches?") # whenever you put the sender name to be playerName it is the player characters own message!
            $ good_points += 1
            call message(tpb, "Ah, tu m'as trouvé?")
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
    label choiceMaking_CHA: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Je pense que chacun a son charme.","choiceMaking_CHA.choice1","T’as pas tort.","choiceMaking_CHA.choice2")
        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Je pense que chacun a son charme.") # whenever you put the sender name to be playerName it is the player characters own message!
            call message_start(playerName, "Je suis sûr que tu es tout aussi adorable")
            call message(tpb, "Peut-être.")
            $ good_points += 1
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "T’as pas tort.")
            call message_start(playerName, "Elle est impressionnante")
            call message(tpb, "...")
            jump .aftermenu
        label .aftermenu:
    call message(tpb, "De toute façon, je ne suis pas la seule à l’admirer. Tant de gens voudraient être à sa place ou avec elle.")
    call message(tpb, "...")
    call message(tpb, "Est-ce que je devrais me coiffer ?")
    call message_start(playerName, "coiffer?")
    call message(tpb, "Genre... changer mon style.")
    label choiceMaking_HAI: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("À mon avis, tu devrais faire ce que tu veux, à partir du moment où tu ne le regrettes pas.","choiceMaking_HAI.choice1","J'aime ta coupe.","choiceMaking_HAI.choice2")
        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "À mon avis, tu devrais faire ce que tu veux, à partir du moment où tu ne le regrettes pas.") # whenever you put the sender name to be playerName it is the player characters own message!
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "J'aime ta coupe.")
            call message_start(playerName, "Je ne pense pas que tu devrais les couper pour l’instant")
            $ good_points += 1
            jump .aftermenu
        label .aftermenu:
    call message(tpb, "...")
    call message(tpb, "Bonne nuit, à demain.")
    call phone_end
    playerName "..."
    scene black with fade
    narrateur "Tu vas dormir et tu vas à l'école le lendemain."
    pause 3
    scene classroom with fade

    jump route_B