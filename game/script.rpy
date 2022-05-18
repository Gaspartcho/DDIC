#region Variables

define hasPlayBefore = True
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

    call phone_start("Akane")

    call message_start("nadia", "hey, this is a phone texting thingy")

# added an alternate way to reply from the player perspective, this time the name doesnt show if you think its extra
call reply_message("oh really? what does it do lol")

# this one is the same as the above one, but instead it has one more place for you to set an image
# you have to make the image be small enough to fit the screen or its gonna stretch weird!
call message_img("nadia", "it works with images too!","images/pic1.png")
call message("nadia", "the text box changes depending on how much content there is. dont put too big images or its gonna look weeeeiiiird")
call message("nadia", "you can also do menus here")

# the next line is the menu system, first and third slot are the menu options, second and fourth one are what happens when you click it

# i made a special reply menu called phone_reply3 which can use 3. if you wish to have more you can make a new reply4 and see how i modified the code between the first reply code
call screen phone_reply("awesome!","choice1","lame","choice2")
# i made a special reply menu called phone_reply3 which can use 3. if you wish to have more you can make a new reply4 and see how i modified the code between the first reply code
##call screen phone_reply3("awesome!","choice1","lame","choice2","im gay","choice3")

label choice1:    
    # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
    call phone_after_menu
    
    # whenever you put the sender name to be "me" it is the player characters own message!
    call message_start("me", "awesome")
    call message("nadia", "i hope you like it")

    jump aftermenu
    
label choice2:
    call phone_after_menu
    call message_start("me", "lame")
    call message("nadia", "well, its a shame but your feelings are valid")
    
    jump aftermenu

label choice3:
    call phone_after_menu
    call message_start("me", "im gay")
    call message("nadia", "nice")
    
    jump aftermenu    
    
label aftermenu:
    call message("nadia", "check the code for comments on how the code works, thanks for your time!")
    call message("nadia", "the base for this code and this stretched phone background comes from cute demon crashers")
    call message("nadia", "the images were drawn by my gf @sloppydraws")
    
    # this one puts away the phone!
    call phone_end

    return