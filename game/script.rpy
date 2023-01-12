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
        narrateur "welcome back, \"%(playerName)s\""

        stop music 

    else:
        narrateur """Hello!
        
        Welcome!"""

        stop music

        call name_choose
    
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
    call phone_start(usrcf, "21:30") 

    call message_start(tpc, "Welcome to Nōburu highschool. I'm {b}Zhou ChunHua{/b}, the class president! If you have any questions, don't hesitate to ask your classmates, teachers or even me. Even if you joined us in the middle of the school year, we welcome you with open arms :)")
    call message_img(tpc, "This is me!", "images/instagram/A1_insta.png") 
    call message(tpc, "i believe that starting school in the middle of a semester can be very difficult, so you can count on me!") 
    pause 1.0

    label choiceMaking_WAY: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Thanks! I'll try to behave :)","choiceMaking_WAY.choice1","Thanks! you're really pretty ~","choiceMaking_WAY.choice2")

        label .choice1:    
            call phone_after_menu  # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Thanks! I'll try to behave :)")  # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpc, "Haha ! If you want, I'll send you everything we've done since the beginning of the school year^^") 
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "Thanks! you're really pretty ~") 
            call message(tpc, "Ahh... Thanks ^^") 
            jump .aftermenu
            
        label .aftermenu:

    call message(tpc, "Either way, shoot me a message and i'll reply to you as fast as I can, i'm usually available.") 
    call message(tpc, "Oh uh... that probably gives the impression that I'm not doing my work as class representative, but I swear I'm doing the most i can!") 
    call message(tpc, "Oh, theres a girl that i would suggest you avoid... She's a bit judgemental and loves to gossip.") 
    
    label choiceMaking_ST: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Oh. What has she done?","choiceMaking_ST.choice1","What does she look like?","choiceMaking_ST.choice2")

        label .choice1:    
            call phone_after_menu 
            call message_start(playerName, "What has she done?") 
            call message(tpc, "She bullies me sometimes... everyone actually... I don't know why.") 
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "What does she look like?") 
            jump .aftermenu
            
        label .aftermenu:

    call message_img(tpc, "Here", "images/instagram/H1_insta.png") 
    call message(tpc, "Her name's {b}Himeno Yuzu{/b}. I don't want you to talk about it though, it'd be embarassing if everyone knew the class president gets bullied, Haha...") 
    call message(tpc, "Oh! My parents are calling me. I'll see you tomorrow :)") 
    call phone_end # this one puts away the phone!

    narrateur """...

    ...
    
    She can't be that bad."""

    call phone_start(usrh, "22:13") 
    label choiceMaking_LUV: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("heyy~ you're hot!","choiceMaking_LUV.choice1","hey you can't possibly be that mean","choiceMaking_LUV.choice2")
        label .choice1:    
            call phone_after_menu 
            call message_start(playerName, "heyy~ you're hot!") 
            call message(tph, "HAHA! OFC I AM!!") 
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "hey you can't possibly be that mean") 
            call message(tph, "the only annoying woman here is that pig looking nerd") 
            jump .aftermenu
        label .aftermenu:
    call message(tph, "i'm obviously the best") 
    call message(tph, "Yet SOMEHOW, SHE is always first") 
    call message(tph, "I swear to you she's cheating") 
    call message(tph, "...") 
    call message(tph, "I should do the same") 
    label choiceMaking_CH: 
        call screen phone_reply("Are you actually gonna do it?","choiceMaking_CH.choice1","You could probably do well without cheating if you tried","choiceMaking_CH.choice2")
        label .choice1:    
            call phone_after_menu 
            call message_start(playerName, "Are you actually gonna do it?") 
            call message(tph, "no") 
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "You could probably do well without cheating if you tried") 
            call message(tph, "yeah right.") 
            call reply_message("...") 
            jump .aftermenu
        label .aftermenu:
    call message(tph, "Oh ! One of my friends are calling me.") 
    call message(tph, "don't miss me too much <3") 
    call phone_end 

    """{i}...
    
    {i}I should sleep now."""
    
    jump scene_2

label scene_2:
    scene classroom day with Fade(1.0, 2.0, 1.0)

    narrateur "the next day at school, i recieve a text message from an unknown number"

    call phone_start("Melissa", "08:02")
    call message_start("Melissa", "Hey [playerName], wanna video chat me for free? find me here http://itsascam.com/xxx xoxo") 
    pause 2.0
    window show
    "???" "I wouldn't click on that if i were you."
    call phone_end(False) 

    show screen cexp("apc", "ael", "amn", "abn", p=p_center, h=h_down)

    menu:
        c_chunhua "You should be careful with that stuff, it could ruin your life."

        "Are you talking from experience?":
            playerName "Are you talking from experience?"
            show screen cexp("apc", "aeb", "ams", "abn", p=p_center, h=h_down)
            c_chunhua """...
            
            Maybe"""

        "I was going to delete it anyways":
            playerName "I was going to delete it anyways"
            c_chunhua "..."
            show screen cexp("apc", "ael", "ams", "abn", p=p_center, h=h_down)
            c_chunhua "Right."
    
    show screen cexp("apr", "ael", "ams", "abn", p=p_center, h=h_down)
    c_chunhua "You seem new here."
    show screen cexp("apc", "aeb", "ams", "abn", p=p_center, h=h_down)
    c_chunhua "Welcome to Nōburu high."
    playerName "Didn't we talk on instargam last night?"
    show screen cexp("apc", "ael", "amt", "abn", p=p_center, h=h_down)
    c_chunhua """Really? I don't recall.

    Maybe you confused me for someone else."""

    show screen cexp("apr", "aeb", "ams", "abn", p=p_center, h=h_down)
    
    """{i}...{/i}

    {i}That's weird{/i}

    {i}I'm pretty sure i talked to her last night{/i}"""
    show screen cexp("bpb", "beb", "bms", "bbn", p=p_center, h=h_down) 
    narrateur "You look to the side, feeling a bit awkward that Chunhua didn't recognize you."
    narrateur "You spot a girl with pink hair dozing off on her desk."
    narrateur "You approach her and take a peek at her phone."

    """{i}...{/i}

    {i}Isn't that my convo with Chunhua last night?{/i}

    {i}...{/i}"""

    narrateur "You reach out to try and wake her up... "
    play audio class_bell
    narrateur """... but the bell rings.
    
    You go back to see Chunhua."""
    show screen cexp("apr", "aeb", "ams", "abn", p=p_center, h=h_down)
    playerName "Who's that?"
    show screen cexp("apr", "ael", "amt", "abn", p=p_center, h=h_down)
    c_chunhua "That's {b}Bomi Park{/b}."
    show screen cexp("apr", "ael", "ams", "abn", p=p_center, h=h_down)
    c_chunhua "She's ranked first on the school leaderboard in terms of average."
    show screen cexp("apr", "aeb", "ams", "abn", p=p_center, h=h_down)
    c_chunhua "It's pretty impressive"
    
    pause 1.0
    "{i}...{/i}"
    "{i}I should focus on class.{/i}"
    hide screen cexp
    window hide
    scene black with fade
    show screen cexp("apr", "ael", "ams", "abn", p=p_center, h=h_down) with fade
    hide screen cexp with fade 
    scene classroom day with fade
    scene black with fade
    show screen cexp("bpf", "bel", "bms", "bbn", p=p_center, h=h_down) with fade
    hide screen cexp with fade
    scene classroom day with fade
    scene black with fade
    show screen cexp("hph", "hel", "hms", "hbn", p=p_center, h=h_down) with fade
    hide screen cexp with fade
    scene classroom day with fade
    scene black with fade
    pause 2.0

    show screen mlt with fade

    jump road_menu

label road_menu:
    menu:
        "Chunhua":
            $ road = "1"
            playerName "Chunhua!"
        "Bomi":
            $ road = "2"
            playerName "Bomi!"
        "Himeno":
            $ road = "3"
            playerName "Himeno!"
    hide screen mlt with fade
    c_mysteriousMan """good choice!
    
    wake up :)"""
    scene classroom late with fade 
    
    narrateur """The clock displays \"17:06\".
    
    It's late."""

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
    
    You lost.
    
    What do you want to do now?"""

    menu:
        "Go back to selection":
            playerName "Go back to route menu."
            c_mysteriousMan """Going back to the route menu.
            
            Who will you pick now?"""
            jump road_menu

        "Quit Game":
            playerName "Quit Game."
            narrateur """Okay! 

            I might forget you the next time I see you, but you'll listen to my cringe little monologue again won't you?
            
            See you next time :)"""

            stop music fadeout 1.5

            return
    
label happy_ending:
    scene black with fade

    narrateur """You finished the game \"Doki-Doki information Club\"!
    
    created by \"NSI122\", Laura and Gas
    
    Thank you for playing."""

    menu:
        narrateur "Would you like to play again?"

        "yes":
            jump start
        "no":
            return