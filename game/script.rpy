#region Variables

define hasPlayBefore = False
define defaultPlayerName = "Shujin"
define playerName = defaultPlayerName
define LovePoints = {"Akane":0, "Bomi":0, "Himeno":0}

#endregion

#region Randoms Functions

init python:
    def beepy_voice(event, interact=True, sound="audio/Narator_U_Voice.mp3", **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play(sound, loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

#endregion

#region Characters

define c_mysteriousMan = Character("???", who_color="#000")
define narrateur = Character(" ", callback=beepy_voice)

#endregion


label splashscreen:
    scene black
    with Pause(1)

    show text "{color=#fff}NSI122 Presents...{/color}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return


label start:

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
        
        C'est tout pour moi. A bientot.
        
        ;)"""

        narrateur "Preparation pour la première uttilisation du programme..."

        narrateur "Erreur: Aucun nom d'uttilisateur enrengistré."

        call name_choose
    
        narrateur "Initialisation Terminé!"

    jump game_Launching

label name_choose():
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
    call phone_start(talkingCharacter)
    call message_start(talkingCharacter, "Salut! Je t'ai ajouté en amis comme ça tu pouras me joindre si tu a des questions.")
    pause 1.0

    label choiceMaking_WAY: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Cool merci","choiceMaking_WAY.choice1","Qui es-tu ?","choiceMaking_WAY.choice2")

        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Cool merci") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(talkingCharacter, "Pas de problème, ça me fais plaisir ;)")
            call message(talkingCharacter, "Je ne suis pas déléguée pour rien")
            call message(talkingCharacter, "(enfin celle de l'année dernière mais ce n'est pas important...)")

            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Qui es-tu ?")
            call message(talkingCharacter, "Ah oui, j'ai complètement oublillé les présentations...")
            call message(talkingCharacter, "Je m'appelle Akane! Je suis la déléguée de nottre classe. Enfin celle de l'année dernière mais on n'a pas encore fais les éléctions donc je prend le rôle pour l'instant")
            call message(talkingCharacter, "Mais de toute façon je vais surement être ré-élue: je suis copine avec tout le monde ici.")
            
            jump .aftermenu
            
        label .aftermenu:

    call message(talkingCharacter, "Bref, tu commence bien demain c'est ça?")
    call message(playerName, "Ouai")
    call message(talkingCharacter, "Ok cool. Pense bien à aller me voir dans la cour demain matin pour que je t'explique le fonctionnement et que je te présente au reste de la classe")
    
    label choiceMaking_ST: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Le fonctionnement?","choiceMaking_ST.choice1","Ok bonne nuit","choiceMaking_ST.choice2")

        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "Le fonctionnement?")
            call message(talkingCharacter, "Ne t'inquiète pas, ce n'est pas grand chose: just un ou deux {i}petits{/i} détails")
            call message(talkingCharacter, "Bon je vais aller me coucher. Bonne nuit.")
            call message(playerName, "A demain")

            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Ok bonne nuit")
            call message(talkingCharacter, "Bonne nuit")
            
            jump .aftermenu
            
        label .aftermenu:
            
        call phone_end # this one puts away the phone!

        return




                # added an alternate way to reply from the player perspective, this time the name doesnt show if you think its extra
        call reply_message("oh really? what does it do lol")

        # this one is the same as the above one, but instead it has one more place for you to set an image
        # you have to make the image be small enough to fit the screen or its gonna stretch weird!
        call message_img("nadia", "it works with images too!","images/pic1.png")
        call message("nadia", "the text box changes depending on how much content there is. dont put too big images or its gonna look weeeeiiiird")
        call message("nadia", "you can also do menus here")