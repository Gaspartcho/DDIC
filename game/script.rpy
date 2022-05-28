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
    define ta = "Akane"
    define tb = "Bomi"
    define th = "Himeno"
    call phone_start("Kousei.Akane", "21:30")
    call message_start(ta, "Bienvenue à l'école X ! Je suis Akane Kousei, votre déléguée de classe. Si vous avez une question, n'hésitez pas à les poser soit à vos camarades, soit aux enseignants, ou vous pouvez venir me voir. Même si vous nous avez rejoint très tard dans l'année, nous vous accueillons toujours à bras ouverts :)")
    call message(ta, "Comme tu arrive en millieu d'année, je me doute bien que ça peu être difficile, mais tu peux compter sur moi!")
    call message_img(ta, "Ça c'est moi.", "images/instagram/A1_insta.png")
    pause 1.0

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
            call message(ta, "J'aimerais bien être aussi belle en vrai.")
            jump .aftermenu
            
        label .aftermenu:

    call message(ta, "Quoi qu'il en soit, envoies-moi un SMS dès que t’as besoin de quoi que ce soit et je te répondrai le plus vite possible, je suis presque tout le temps dispo.")
    call message(ta, "Ah euh… Ça donne probablement l'impression que je ne fais pas mon travail de déléguée… Je te jure que c’est qu’une impression !")
    call message(ta, "Il y a cette fille dont je te conseille de pas t’approcher. Elle juge très facilement et tu ne passeras pas un bon moment avec elle.")
    
    label choiceMaking_ST: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("\"Ah… Qu'a-t-elle fait ?\"","choiceMaking_ST.choice1","À quoi ressemble-t-elle?","choiceMaking_ST.choice2")

        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "\"Ah… Qu'a-t-elle fait ?\"")
            call message(ta, "Elle aime se moquer de moi... je ne sais pas pourquoi.")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "À quoi ressemble-t-elle?")
            jump .aftermenu
            
        label .aftermenu:

    call message_img(ta, "Attend, je t'envoie une photo", "images/instagram/H1_insta.png")
    call message(ta, "C'est {b}Himeno Yuzu{/b}. Je ne veux pas que vous fassiez quoi que ce soit, ce serait gênant si les gens savaient que la déléguée se fait harceler. Haha.")
    call message(ta, "Oh! Mes parents m'appellent. Je te verrai demain :))")
    call phone_end # this one puts away the phone!
    scene black
    define talkingCharacter = ""
    call phone_start("yuzu.himi", "22:13")
    label choiceMaking_LUV: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("heyy~ T'es magnifique!","choiceMaking_LUV.choice1","Yo, la personne la pluuuuus gentille du lycée","choiceMaking_LUV.choice2")
        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "\"heyy~ T'es magnifique!\"")
            call message(tb, "HAHA! Bien sûr que je le suis!!")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Yo, la personne la pluuuuus gentille du lycée")
            call message(tb, "La pire ici est cette petite frimeuse rose.")
            jump .aftermenu
        label .aftermenu:
    call message(tb, "Je suis la plus intelligente, la plus belle et la meilleure de toutes !")
    call message(tb, "Mais pourtant, je n'ai pas les meilleures notes et c'est super énervant.")
    call message(tb, "Cette pourrie-gâtée rose est toujours la première.")
    call message(tb, "Je jure que c'est parce qu’elle triche.")
    call message(tb, "...")
    call message(tb, "Je devrais le faire.")
    label choiceMaking_CH: 
        call screen phone_reply("Tu vas vraiment faire ça ?","choiceMaking_CH.choice1","Je suis sûr que si tu essayes de toutes tes forces, tu seras la meilleure","choiceMaking_CH.choice2")
        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "\"Tu vas vraiment faire ça ?\"")
            call message(tab, "ui")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je suis sûr que si tu essayes de toutes tes forces, tu seras la meilleure")
            call message(tb, "J’en suis encore loin.")
            jump .aftermenu
        label .aftermenu:
    call message(tb, "Ah ! Une de mes copines m'appelle.")
    call message(tb, "Ne me manque pas trop <3")

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