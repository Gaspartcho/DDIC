label route_B1:
    define good_points = 0

    "{i} Je devrais aller voir Bomi et lu demander pourquoi elle fais ça."
    "{i} ..."
    "{i} Elle est déjà partie..."
    narrateur "Après cette longue journée de cours, vous décidez d'aller vous coucher pour vous reposer et vous remettre de toutes vos émotions"
    c_mysteriousMan "Arrette de faire genre... Tu viens de passer la journée à dormir..."

    scene bedroom with fade
    pause 2.0
    "{i} ..."
    "{i} Je vais essayer de lui parler quand même"
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
    call message(tpb, "C'est normal de vouloir être comme elle...")

    label choiceMaking_CHA: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Je pense que chacun a son charme.","choiceMaking_CHA.choice1","T'as pas tort.","choiceMaking_CHA.choice2")
        label .choice1:
            $ good_points += 1
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Je pense que chacun a son charme.") # whenever you put the sender name to be playerName it is the player characters own message!
            call reply_message("Je suis sûr que tu es tout aussi adorable")
            call message(tpb, "Peut-être.")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "T'as pas tort.")
            call reply_message("Elle est impressionnante")
            call message(tpb, "...")
            jump .aftermenu
        label .aftermenu:

    call message(tpb, "De toute façon, je ne suis pas la seule à l'admirer. Tant de gens voudraient être à sa place ou avec elle.")
    call message(tpb, "...")
    call message(tpb, "Est-ce que je devrais me coiffer ?")
    call reply_message("Te coiffer?")
    call message(tpb, "Genre changer mon style...")
    call message(tpb, "Quelque chose qui me correspondrais plus")

    label choiceMaking_HAI: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Tu devrais faire ce que tu veux","choiceMaking_HAI.choice1","J'aime ta coupe.","choiceMaking_HAI.choice2")
        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "À mon avis, tu devrais faire ce que tu veux: C'est juste une coupe de cheveux après tout") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpb, "Ouai, tu a raison.")
            jump .aftermenu
        label .choice2:
            $ good_points += 1
            call phone_after_menu
            call message_start(playerName, "J'aime ta coupe.")
            call reply_message("Je ne pense pas que tu devrais les couper pour l'instant")
            call message(tpb, "Oui mais quand même, je pense que ça m'irais bien...")
            jump .aftermenu
        label .aftermenu:

    call message(tpb, "Bon bah bonne nuit, à demain.")
    call phone_end
    "{i} Un peut bisare... Mais elle à l'air gentille"
    "{i} J'espère juste qu'elle ne fera rien de stupide..."
    c_mysteriousMan "FORESHAOWING!!!"
    scene black with fade
    narrateur "Le lendemain..."
    scene classroom day with fade
    pause 2.0

    c_bomi "Bonjour [playerName]."
    c_bomi "..."
    c_bomi "Qu'en penses-tu?"

    menu:
        c_bomi "..."
        "Je pense que c'est superbe!":
            playerName "Ca te vas super bien en plus!"
            c_bomi "Vraiment? Je suis tellement heureuse!"
        
        "Tu me fais penser à quelqun d'autre...":
            $ good_points += 1
            playerName "Tu m'as l'air familière..."
            c_bomi "Ah!? J-je, n-non..."

    c_himeno "Pfft t'as l'air ridicule"
    with Fade(0.1, 0.0, 0.5, color="#fff")
    c_bomi "E-eh!? A-attends !!"
    c_bomi "Ne prends pas de photos!"
    narrateur "Himeno s'enfuit."
    narrateur "Bomi essaie de la poursuivre et trébuche."

    menu:
        narrateur "Tu l'aides à se relever"
        "Ca a l'air grave":
            playerName "Ca a l'air grave, tu veut que je la poursuive?"
            c_bomi "Non, c'est bon..."

        "Ce n'est pas grave":
            $ good_points += 1
            playerName "Ce n'est pas grave, ne t'inquiète pas"
            playerName "Je ne pense pas que les gens y prêteront beaucoup attention de toute façon"
            c_bomi "Ahahah... Tu as surement raison"
    
    c_bomi "Mais quand même, je ne veut pas que ça circule."
    c_akane "Que se passe t-il ici?"

    menu:
        "Tout va bien.":
            c_akane "..."
            c_akane "Si tu le dis."
            c_akane "Au fait, simpa ta nouvelle coupe Bomi."
            c_akane "J'ai l'impression que tu te fond plus dans la masse maintenant."
            c_bomi "M-Merci!"
        
        "Quelqu'un a pris une photo d'elle!":
            c_akane "Ah. Je pense avoir une idée de qui tu parles."
            c_akane "Encore Himéno. Il vas faloir que je lui parle un jour à celle-là."
            c_akane "D'ailleurs, simpa ta nouvelle coupe Bomi."
            c_akane "Mais je préférais celle d'avant pour être honête."
            c_akane "Tu avais plus de personalité avec l'anciènne."
            c_bomi "D-d'accord."
    
    c_akane "Bon, je dois y aller. A plus!" #elle part.

    c_bomi "[playerName]!"
    c_bomi "C'est la honte!"
    c_bomi "Si cette photo sort, je ne pense pas que je m'en remettrais..."

    menu:
        "Tu es superbe pourtant.":
            playerName "Tu es superbe pourtant."
            playerName "Te teindre les cheveux en bleu était une bonne idée"
        
        "On va récupérer cette image":
            playerName "Les cheveux bleus sont jolis mais ils ne te vont pas trop."
            playerName "Viens. On va récupérer cette image et ça ira mieux."
    
    c_bomi "..."

    if good_points >= 4:
        jump RBB1
    else:
        jump RBF1

label RBB1:
    scene black with fade
    c_bomi """...

    Je ne lui ressemble pas du tout.

    Pourquoi?

    J'ai tout essayé...

    J'ai essayé de me couper les cheveux, d'ajouter des extensions, d'avoir des lentilles teintées...

    Rien ne marche.

    Comment faire pour lui ressembler?

    COMMENT FAIRE POUR LUI RESSEMBLER !?!

    Je n'en peut plus."""

    jump game_over

label RBF1:
    scene black with fade
    narrateur "Le lendemain."
    scene classroom day with fade

    c_bomi "Hey! [playerName]!"
    c_bomi "Elles commençaient à devenir lourdes..."
    c_bomi "Et puis, je prèfère mon style d'avant finalement."

    menu:
        c_bomi "..."
        "Je suis sûr qu'elle ne l'a pas encore postée":
            c_bomi "J'aimerais aller la voir quand même."
        
        "Allons chercher Himeno":
            c_bomi "Ok, c'est partis."
    
    c_bomi "..."
    c_bomi "Je pense qu'elle est sur le toit en train de déjeuner et de prendre des photos pour Instagram."
    "{i} A-t-elle déjà posté?"

    # call phone_start(usrb, "10:18")
    # call message_img() ATTENTION ICI: Mettre une image puis des commentaires méhants (pour + tard)
    # call message()
    # ...

    "{i}Wow..."
    "{i}Ces commentaires sont stupides et méchants..."
    "{i}Himeno n'a aucune pitié."

    # call phone_end

    c_bomi "Ah..."
    c_bomi "J'espérais que tu n'allais pas le voir"
    c_bomi "Je ne pensais pas que c'était si reconnaissable..."

    menu:
        "Tu devrais répliquer":
            c_bomi "..."

        "On devrait le signaler":
            $ good_points += 1
            playerName "N'y fais pas attention."
            playerName "On devrait signaler l'incident sur insta et à l'administration."
    
    playerName "Bon, allons voir Himeno."
    c_bomi "Non!!" # surpirsed ?
    c_bomi "J-je veux dire qu'on ne devrait pas."
    c_bomi "J'ai peur que ça se passe mal..."

    menu:
        c_bomi "..."
        "Tu n'es pas obligée d'y aller":
            playerName "Tu n'es pas obligée d'y aller tu sais?"
            playerName "De toute façon, on a déja la preuve qu'elle t'envoie de la haine"
            playerName "Elle finira par payer de toute façon"
            define final_choice = 0

        "Tu devrais aller lui parler":
            playerName "Tu devrais aller lui parler."
            playerName "Lui dire ce que tu ressent, lui faire comprendre qu'elle te fais du mal."
            define final_choice = 1
        
    c_bomi "Oui mais..."
    c_bomi "Je voudrais pas lui attirer de problèmes..."
    playerName "On dois lui faire comprendre que chaque actions a des conséquences!"
    c_bomi "..."
    playerName "Comment tu te sens?"
    c_bomi "Mal."
    c_bomi "C'est atroce."
    c_bomi "J'ai l'impression que ces commentaires me hantent..."
    c_bomi "Ils m'ont empêché de dormir hier soir."
    c_bomi "Et chaque fois que j'en lis, je me sens encore moins bien."

    menu:
        "On devrait aller voir la psychologue scolaire.":
            $ good_points += 1
            c_bomi "Et risquer qu'ils le disent à ma famille ?"
            c_bomi "Certainement pas!"
            playerName "Oui mais c'est important d'en parler à des personnes qualifiées..."
            playerName "Ils pouront t'aider beaucoup mieu que moi et te donner des vais conseils!"
            c_bomi "..."
            define good_ending = True
        
        "Ils ne veulent rien dire. Ça ira.":
            c_bomi "..." # Triste
            c_bomi "Si tu le dis"
            define good_ending = False

    c_bomi "Bon ok."
    c_bomi "Je ferai ce que tu m'as dit."
    c_bomi "J'espère que tu as raison."

    if good_ending and good_points > 8:
        jump RBG
    else:
        jump RBB2

label RBB2:
    # A changer et a sénariser au fil du temps.

    scene bedroom with fade
    playerName """Ça fait un mois que j'ai parlé à Bomi du post.

    Le post s'est propagé et les gens à l'école ont commencé à le voir.

    Parfois, je trouvais des lettres dans son casier ou des mots méchants écrits sur son bureau.

    Apparemment, Akane a beaucoup d'admirateurs et puisque les gens essayaient d'imiter leur “déesse”, leurs commentaires finissaient par être ciblés.

    J'ai essayé de les cacher du mieux que je pouvais mais ce n'était pas assez.

    Bomi a fini par les découvrir. 

    Au fil des jours, elle semblait se sentir de plus en plus mal.

    À la fin, elle n'est plus venue en cours.

    Personne n'a entendu parler d'elle depuis et je pense que la majorité n'ont rien fait pour essayer de prendre de ses nouvelles.

    Sa chaise est vide, ramassant la poussière au fil du temps."""

    jump game_over

label RBG:
    