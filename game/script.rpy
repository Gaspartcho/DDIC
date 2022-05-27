label splashscreen:
    scene black
    with Pause(1)

    show text "{color=#fff}NSI122 Presents...{/color}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    stop music

    play music "audio/musics/Ambiant_misterious.mp3" fadein 1.0 loop

    if hasPlayBefore:
        c_mysteriousMan """...

        Tu es revenu...

        Je vois...

        J'imagine que tu voulais vérifier que tu avais bien tout exploré...

        Que tu avais bien tout découvert...

        Tu dois te poser beaucoup de questions... 
        
        Sur le fonctionnement de cet univers...

        Sur la psychologie des personnages que tu a rencontré...

        Quelle curiosité, tu ne me déçois pas.

        Moi aussi je me pose beaucoup de questions tu sais...

        Combien de parties as-tu relancé?

        Combien de fois avons-nous eu cette discution?

        Combien de fois t'ai-je répété ce monologue?

        Pour être honnête avec toi...

        ...
        
        Quoi? Tu pensais vraiment que j'allais faire un discours méta sur la nature du jeu vidéo?
        
        Franchement tu as pris confiance depuis la dernière fois.
        
        Bon, je te laisse... Je t'ai déjà gardé assé longtemps.
        
        ;)"""

        stop music fadeout 1.0

        menu:
            narrateur "Voulez-vous continuer en tant que \"%(playerName)s\" ?"

            "Oui (Continuer à jouer)":
                jump .after_menu

            "Non (Changer de nom avant de continuer à jouer)":
                call name_choose

        label .after_menu:
            narrateur """Rénitialisation du jeu pour \"%(playerName)s\"...

            Terminé!"""

    else:
        c_mysteriousMan """...
        
        Oh !
        
        Tu es là !
        
        Tout d'abors, merci d'avoir installé ce programme...
        
        Pour des raisons personnelles, je préfère te cacher mon identitée pour l'instant.
        
        Sache juste que nous nous revérons pendant ton aventure.

        Au fait, on m'a demandé de te poser une question avant que je puisse te laisser passer:

        Selon toi, comment faire pour développer ou entretenir des relations sur internet?

        Réfléchis bien.
        
        C'est tout pour moi. A bientôt.
        
        ;)"""

        stop music fadeout 1.0

        narrateur """Preparation pour la première uttilisation du programme...

        Erreur: Aucun nom d'uttilisateur enrengistré."""

        call name_choose
    
        narrateur "Initialisation pour le joueur \"%(playerName)s\": Terminé!"

    jump game_Launching

label name_choose:
    $ playerName = renpy.input("Veuillez entrer votre nom:", length=32)
    $ playerName = playerName.strip()

    if not playerName:
        $ playerName = defaultPlayerName

        narrateur "Erreur: Nom de personnage invalide! Votre nom sera par défaut \"%(defaultPlayerName)s\""
    return

label game_Launching:
    $ hasPlayBefore = True
    narrateur "Lancement du jeu..."
    show text "{color=#fff}Terminé!{/color}"
    image white = "#fff"
    scene white with Dissolve (1.5)
    pause (1.5)
    jump scene_1

label scene_1:
    scene black
    define talkingCharacter = "Akane"
    call phone_start(talkingCharacter, "21:30")
    call message_start(talkingCharacter, "Bienvenue à l'école X ! Je suis Akane Kousei, votre délégué de classe. Si vous avez des questions à poser, n'hésitez pas à les poser soit à moi, à vos camarades de classe ou aux enseignants :)","images\instagram\A1_insta.png")
    call message(talkingCharacter, "Comme tu arrive en millieu d'année, je me doute bien que ça peu être difficile, mais tu peux compter sur moi!")
    pause 1.0

    label choiceMaking_WAY: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Merci! Je serai à ta charge :)","choiceMaking_WAY.choice1","Merci! Tu es très belle, comme il se doit pour être déléguée de classe !","choiceMaking_WAY.choice2")

        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Merci! Je serai à ta charge :)") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(talkingCharacter, "Haha ! Si tu le souhaites, je t'enverrai par e-mail le travail que nous avons fait jusqu'à présent dans les cours que nous partageons ^^")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Merci! Tu es très belle, comme il se doit pour être déléguée de classe !")
            call message(talkingCharacter, "Ahh… Merci beaucoup ^^J'aimerais avoir l'air aussi bien en personne.")
            jump .aftermenu
            
        label .aftermenu:

    call message(talkingCharacter, "Quoi qu'il en soit, envoies-moi un SMS quand tu le souhaites et je te répondrai le plus vite possible, je ne suis pas une personne très occupée.")
    call message(talkingCharacter, "Ah ! Cela donne probablement l'impression que je ne fais pas mon travail de délégué de classe… Je jure que les choses se font ici !")
    
    label choiceMaking_ST: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("\"Deux-trois choses?\"","choiceMaking_ST.choice1","Ok bonne nuit","choiceMaking_ST.choice2")

        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "\"Deux-trois choses?\"")
            call message(talkingCharacter, "Oui, il faut que je te préviènne: il y a cette fille, {b}Bomi{/b}. Elle terrorsie un peut qui elle veut...")
            call message_img(talkingCharacter, "Attend, je t'envoie une photo", "images/instagram/H1_insta.png")
            call message(talkingCharacter, "On ne dirais pas comme ça, mais c'est une vraie peste! Toujours à embêter des gens comme Bomi")
            call message(talkingCharacter, "Bref, tout ça pour te dire de ne pas trop te rapprocher d'elle...")
            call message(playerName, "D'accord, je ferais attention, merci.")
            call message(talkingCharacter, "Oh, mais ne t'inquiète pas, il y a pleint d'autres bon trucs ici!")
            call message(talkingCharacter, "Bon, je vais aller me coucher, il commence à faire tard. Bonne nuit")
            call message(playerName, "Bonne nuit.")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Ok bonne nuit")
            call message(talkingCharacter, "Bonne nuit")
            
            jump .aftermenu
            
        label .aftermenu:
            
    call phone_end # this one puts away the phone!

    jump scene_2

label scene_2:
    


    c_bomi "Oh!"
    
    c_bomi "Bon... - Bonjour!"
    
    c_bomi "Tu es le nouvel élève c'est ça?"
    
    c_bomi "Bienvenue!"
    
    c_bomi """Je m'appelle Bomi!
    
    ...
    
    ..."""

    menu:
        c_bomi "..."

        "Est-ce que ça vas?":
            c_bomi "oui oui, je vais bien..."

        "{i}Se retouner et commencer à partir...{/i}":
            c_bomi "Non attend!"
    
    c_bomi """Désollé... Je suis un peut timide
    
    """

    return



# added an alternate way to reply from the player perspective, this time the name doesnt show if you think its extra
call reply_message("oh really? what does it do lol")
call message_img("nadia", "it works with images too!","images/pic1.png")