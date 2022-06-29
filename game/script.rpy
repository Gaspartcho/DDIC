label splashscreen:
    scene black
    with Pause(1)

    show text "{color=#fff}NSI122 Presents...{/color}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    pause 1.5
    stop music

    if hasPlayBefore:
        narrateur """

        welcome back, \"%(playerName)s\""""

        stop music 

    else:
        narrateur """Hello!
        
        Welcome!"""

        stop music

        call name_choose from _call_name_choose_1
    
        narrateur """I hope you enjoy your stay, \"%(playerName)s\" <3"""

    jump game_Launching

label name_choose:
    $ playerName = renpy.input("What's your name?", length=32)
    $ playerName = playerName.strip()

    if not playerName:
        $ playerName = defaultPlayerName

        narrateur """...
        
        that's not valid...

        we'll just call you \"%(defaultPlayerName)s\"
        
        okay?
        
        okay <3"""
    return

label game_Launching:
    $ hasPlayBefore = True
    narrateur "Loading..."
    show text "{color=#fff}Done!{/color}"
    image white = "#fff"
    scene white with Dissolve (1.5)
    pause (1.5)
    jump scene_1

label scene_1:
    scene bedroom with fade
    call phone_start(usracf, "21:30") from _call_phone_start_8

    call message_start(tpc, "Welcome to Nōburu highschool! I'm {b}Zhou ChunHua{/b}, the class president. If you have any questions, don't hesitate to ask your classmates, teachers or even me. Even if you joined us in the middle of the school year, we welcome you with open arms :)") from _call_message_start_29
    call message_img(tpc, "This is me!", "images/instagram/A1_insta.png") from _call_message_img_1
    call message(tpc, "i believe that starting school in the middle of a semester can be very difficult, so you can count on me!") from _call_message_80
    pause 1.0

    label choiceMaking_WAY: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Thanks! I'll try to behave :)","choiceMaking_WAY.choice1","Thanks! you're really pretty ~","choiceMaking_WAY.choice2")

        label .choice1:    
            call phone_after_menu from _call_phone_after_menu_24 # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Thanks! I'll try to behave :)") from _call_message_start_30 # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpc, "Haha ! If you want, I'll send you everything we've done since the beginning of the school year^^") from _call_message_81
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_25
            call message_start(playerName, "Thanks! you're really pretty ~") from _call_message_start_31
            call message(tpc, "Ahh... Thanks ^^") from _call_message_82
            jump .aftermenu
            
        label .aftermenu:

    call message(tpc, "Either way, shoot me a message and i'll reply to you as fast as I can, i'm usually available.") from _call_message_83
    call message(tpc, "Oh uh... that probably gives the impression that I'm not doing my work as class representative, but I swear I'm doing the most i can!") from _call_message_84
    call message(tpc, "Oh, theres a girl that i would suggest you avoid... She's a bit judgemental and loves to gossip.") from _call_message_85
    
    label choiceMaking_ST: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Oh. What has she done?","choiceMaking_ST.choice1","What does she look like?","choiceMaking_ST.choice2")

        label .choice1:    
            call phone_after_menu from _call_phone_after_menu_26
            call message_start(playerName, "Oh. What has she done?") from _call_message_start_32
            call message(tpc, "Elle aime se moquer de moi... de tout le monde en fait... je ne sais pas pourquoi.") from _call_message_86
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_27
            call message_start(playerName, "What does she look like?") from _call_message_start_33
            jump .aftermenu
            
        label .aftermenu:

    call message_img(tpc, "Here", "images/instagram/H1_insta.png") from _call_message_img_2
    call message(tpc, "Her name's {b}Himeno Yuzu{/b}. I don't want you to talk about it though, it'd be embarassing if everyone knew the classpresident gets bullied, Haha...") from _call_message_87
    call message(tpc, "Oh! My parents are calling me. I'll see you tomorrow :)") from _call_message_89
    call phone_end from _call_phone_end_8 # this one puts away the phone!

    narrateur """...
    
    She can't be that bad."""

    call phone_start(usrh, "22:13") from _call_phone_start_9
    label choiceMaking_LUV: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("heyy~ you're hot!","choiceMaking_LUV.choice1","hey you can't possibly be that much of a bitch","choiceMaking_LUV.choice2")
        label .choice1:    
            call phone_after_menu from _call_phone_after_menu_28
            call message_start(playerName, "heyy~ you're hot!") from _call_message_start_34
            call message(tph, "HAHA! OFC I AM!!") from _call_message_90
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_29
            call message_start(playerName, "hey you can't possibly be that much of a bitch") from _call_message_start_35
            call message(tph, "the only bitch here is that pig looking nerd") from _call_message_91
            jump .aftermenu
        label .aftermenu:
    call message(tph, "i'm obviously the best") from _call_message_92
    call message(tph, "Yet SOMEHOW, that SLAG is always first") from _call_message_94
    call message(tph, "I swear to you she's cheating") from _call_message_95
    call message(tph, "...") from _call_message_96
    call message(tph, "I should do the same") from _call_message_97
    label choiceMaking_CH: 
        call screen phone_reply("Are you actually gonna do it?","choiceMaking_CH.choice1","You could probably do well without cheating if you tried","choiceMaking_CH.choice2")
        label .choice1:    
            call phone_after_menu from _call_phone_after_menu_30
            call message_start(playerName, "Are you actually gonna do it?") from _call_message_start_36
            call message(tph, "no") from _call_message_98
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_31
            call message_start(playerName, "You could probably do well without cheating if you tried") from _call_message_start_37
            call message(tph, "yeah right.") from _call_message_99
            call reply_message("...") from _call_reply_message_18
            jump .aftermenu
        label .aftermenu:
    call message(tph, "Oh ! One of my friends are calling me.") from _call_message_100
    call message(tph, "don't miss me too much <3") from _call_message_101
    call phone_end from _call_phone_end_9

    """{i}...
    
    {i}I should sleep now."""
    
    jump scene_2

label scene_2:
    scene classroom day with Fade(1.0, 2.0, 1.0)

    narrateur "the next day at school, i recieve a text message from an unknown number"

    call phone_start("REAL_BUISNESS", "08:02") from _call_phone_start_10
    call message_start("REAL_BUISNESS", "Hey [playerName], wanna video chat me for free? fine me here http://cunscam.com/xxx xoxo") from _call_message_start_38
    pause 2.0
    window show
    "???" "I wouldn't click on that if i were you."
    call phone_end(False) from _call_phone_end_10

    show screen cexp("apc", "ael", "amn", "abn", p=p_center, h=h_down)

    menu:
        c_akane "You should be careful with that stuff, it could ruin your life."

        "Are you talking from experience?":
            playerName "Are you talking from experience?"
            show screen cexp("apc", "aeb", "ams", "abn", p=p_center, h=h_down)
            c_akane "Maybe"

        "I was going to delete it anyways":
            playerName "I was going to delete it anyways"
            c_akane "..."
            show screen cexp("apc", "ael", "ams", "abn", p=p_center, h=h_down)
            c_akane "Right."
    
    show screen cexp("apr", "ael", "ams", "abn", p=p_center, h=h_down)
    c_akane "You seem new here."
    show screen cexp("apc", "aeb", "ams", "abn", p=p_center, h=h_down)
    c_akane "Welcome to Nōburu high."
    playerName "Didn't we talk on instargam last night?"
    show screen cexp("apc", "ael", "amt", "abn", p=p_center, h=h_down)
    c_akane """Really? I don't recall.

    Maybe you confused me for someone else."""

    show screen cexp("apr", "aeb", "ams", "abn", p=p_center, h=h_down)
    
    """{i}...{/i}

    {i}That's weird{/i}

    {i}I'm pretty sure i talked to her last night{/i}"""
    show screen cexp("bpb", "beb", "bms", "bbn", p=p_center, h=h_down) 
    narrateur "You look to the side, feeling a bit awkward that Akane didn't recognize you."
    narrateur "You spot a girl with pink hair dozing off on her desk."
    narrateur "You approach her and take a peek at her phone."

    """{i}...{/i}

    {i}Isn't that my convo with Akane last night?{/i}

    {i}...{/i}"""

    narrateur "You reach out to try and wake her up... "
    play audio class_bell
    narrateur """... but the bell rings.
    
    You go back to see Akane."""
    show screen cexp("apr", "aeb", "ams", "abn", p=p_center, h=h_down)
    playerName "Who's that?"
    show screen cexp("apr", "ael", "amt", "abn", p=p_center, h=h_down)
    c_akane "That's {b}Bomi Park{/b}."
    show screen cexp("apr", "ael", "ams", "abn", p=p_center, h=h_down)
    c_akane "She's ranked first on the school leaderboard in terms of average."
    show screen cexp("apr", "aeb", "ams", "abn", p=p_center, h=h_down)
    c_akane "It's pretty impressive"
    
    pause 1.0
    "{i}...{/i}"
    "{i}I should focus on class.{/i}"
    hide screen cexp with fade
    scene black with Fade(3.0, 0, 1.0)
    scene classroom with Fade(3.0, 0, 1.0)
    scene black with Fade(3.0, 0, 1.0)
    pause 2.0

    narrator """En tout cas, choisis bien.
    
    Tes décisions ont une importance ici."""

    show screen mlt with fade

    jump road_menu

label road_menu:
    menu:
        "{i}Je choisis...{/i}"

        "Akane":
            $ road = "1"
            playerName "Akane!"
        "Bomi":
            $ road = "2"
            playerName "Bomi!"
        "Himeno":
            $ road = "3"
            playerName "Himeno!"
    hide screen mlt with fade
    c_mysteriousMan """Bien. Bonne chance pour la suite, on se reverra à la fin...

    Allez, réveille-toi, c'est l'heure de la fin des cours.
    
    ;)"""

    stop music fadeout 1.5
    narrateur "Vous vous réveillez."
    scene classroom late with fade 
    
    narrateur """L'horloge affiche \"17:06\".
    
    Il est tard, vous avez dormi toute la journée."""

    if road == "1":
        jump route_A
    if road == "2":
        jump route_B1
    if road == "3":
        jump RH1

label game_over:
    scene black with fade
    play music MisteriousMan_theme fadein 1.0 loop
    c_mysteriousMan """...
    
    Tu as perdu.
    
    Tu as fais les mauvais choix et tu a perdu.
    
    Que veut-tu faire maintenant?"""

    menu:
        "Recommencer au choix des routes":
            playerName """Recommencer au choix des routes.
            
            Recommencer, encore et encore.
            
            Jusqu'à que j'y arrive enfin."""

            c_mysteriousMan "Bien. J'aime cet état d'espris!"
            c_mysteriousMan "Qui vas-tu choisir à présent?"
            jump road_menu

        "Quiter le jeu":
            playerName "Quiter le jeu."
            c_mysteriousMan """Bien. A la prochaine alors.

            Je t'aurais surement oulillé d'ici là, mais tu me ré-écoutera débiter mon discours ennuillant comme la pluie non?
            
            Dépèche toi quand même de revenir, je me sent si seul ici...
            
            ;)"""

            stop music fadeout 1.5

            return
    
label happy_ending:
    scene black with fade
    play music MisteriousMan_theme fadein 1.0 loop
    c_mysteriousMan """Bravo!
    
    Tu as gagné!
    
    Tu as réussi!
    
    Tu as triomphé!
    
    Tu as fait quelque chose de bien.
    
    Tu as aidé des gens.
    
    Tu as rendu le monde meilleur...
    
    ...
    
    ...
    
    Qu'est-ce que tu fais encore là?
    
    Tu peux partir tu sais?
    
    Rien ne t'oblige à rester ici..."""

    menu:
        "Non non rien, je m'en vais":
            c_mysteriousMan """Tu es bizare tu sais...
            
            J'ai eu peur que tu te sois endormis devant ton écran.
            
            Bon, et bien c'est un au revoirs alors...
            
            N'hésite pas à revenir me voir de temps en temps...
            
            Je t'aurais oublillé mais...
            
            Ce sera toujours amusant.
            
            ;)"""

        "Tu m'avais promis quelque chose...":
            c_mysteriousMan """...
            
            Moi?
            
            Et qu'es-ce que je pourais bien t'avoir promis?"""

            playerName "Ton identitée?"

            c_mysteriousMan """Ah!
            
            Oui c'est vrais...
            
            Et bien c'est simple...
            
            Je suis juste un bout de code écris par un dévelopeur de ce jeu.
            
            Il avais juste envie que je sois là...
            
            Donc je suis là.
            
            Rien de plus compliqué.
            
            Déçu?
            
            Oui, je sais...
            
            Mais bon, tous les histoires ne sont pas forcément palpitantes, non?
            
            ;)"""
    
    stop music fadeout 1.5

    narrateur """Fin du programme.
    
    Vous avez terminé le jeu \"Doki-Doki Litterature Club\"!
    
    Une création de \"NSI122\"
    
    Merci d'avoir jouer."""

    menu:
        narrateur "Voulez-vous recommencer une partie?"

        "oui":
            jump start
        "non":
            return