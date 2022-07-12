label route_B1:
    define ptsb1 = 0

    "{i} I should see how Bomi is doing."
    "{i} ..."
    "{i} Her chair is empty."
    "{i} I should go home."

    scene bedroom with fade
    pause 2
    "{i} ..."
    "{i}I wonder if she has an instargam account."
    "{i}That's not catfishing..."
    "{i}Ah! I found it...{/i}"

    call phone_start(usrb, "20:23") from _call_phone_start
    label choiceMaking_HID: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Hey Bomi, why do you hide yourself?","choiceMaking_HID.choice1","You were right, you clearly don't have look the same in person","choiceMaking_HID.choice2")
        
        label .choice1:    
            call phone_after_menu from _call_phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Hey Bomi, why do you hide yourself?") from _call_message_start # whenever you put the sender name to be playerName it is the player characters own message!
            $ ptsb1 += 1
            call message(tpb, "Oh, you found me?") from _call_message
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_1
            call message_start(playerName, "You were right, you clearly don't have look the same in person.") from _call_message_start_1
            call message(tpb, "...") from _call_message_1
            jump .aftermenu
        label .aftermenu:
    
    call message(tpb, "I'm sorry for lying to you") from _call_message_2
    call message(tpb, "I think Chunhua is really cool. She's smart, beautiful, confident...") from _call_message_3
    call message(tpb, "My only good trait is having straight As.") from _call_message_4
    call message(tpb, "It's not much compared to what she's has...") from _call_message_5

    label choiceMaking_CHA: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("I think everyone has their own charm.","choiceMaking_CHA.choice1","You're not wrong.","choiceMaking_CHA.choice2")
        label .choice1:
            $ ptsb1 += 1
            call phone_after_menu from _call_phone_after_menu_2 # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "I think everyone has their own charm.") from _call_message_start_2 # whenever you put the sender name to be playerName it is the player characters own message!
            call reply_message("I'm sure you're just as lovely.") from _call_reply_message
            call message(tpb, "Maybe.") from _call_message_7
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_3
            call message_start(playerName, "You're not wrong.") from _call_message_start_3
            call reply_message("She's is one hell of a woman") from _call_reply_message_1
            call message(tpb, "...") from _call_message_8
            jump .aftermenu
        label .aftermenu:

    call message(tpb, "Anyways, I'm not the only one that admires her. So many people want to either be or be with her.") from _call_message_9
    call message(tpb, "...") from _call_message_10
    call message(tpb, "Should i get a new haircut ?") from _call_message_11
    call message(tpb, "To something that would look better") from _call_message_13

    label choiceMaking_HAI: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("idk, you tell me","choiceMaking_HAI.choice1","I like ya cut G.","choiceMaking_HAI.choice2")
        label .choice1:    
            call phone_after_menu from _call_phone_after_menu_4 # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "idk, you tell me") from _call_message_start_4 # whenever you put the sender name to be playerName it is the player characters own message!
            jump .aftermenu
        label .choice2:
            $ ptsb1 += 1
            call phone_after_menu from _call_phone_after_menu_5
            call message_start(playerName, "I like ya cut G.") from _call_message_start_5
            call message(tpb, "Really?") from _call_message_16
            jump .aftermenu
        label .aftermenu:
    
    call message(tpb, "...") from _call_message_16
    call message(tpb, "à demain.") from _call_message_17
    call phone_end from _call_phone_end
    "{i} What a weird girl"
    "{i} I hope she doesn't do anything dumb..."
    scene classroom day with fade
    pause 1.0
    show screen cexp("bpbb", "beb", "bmh", "bbn", h=h_down)
    c_bomi "Hey [playerName]."
    show screen cexp("bpfb", "bel", "bmn", "bbn", h=h_down)
    c_bomi "..."
    show screen cexp("bpbb", "bel", "bmt", "bbn", h=h_down)

    menu:
        c_bomi "What do you think?"
        "I think it's great!":
            playerName "I think it's great!"
            show screen cexp("bpbb", "beb", "bmh", "bbn", h=h_down)
            c_bomi "Really? I'm so glad!"
        
        "You seem familiar...":
            $ ptsb1 += 1
            playerName "You seem familiar..."
            show screen cexp("bpfb", "bea", "bms", "bbs", h=h_down)
            c_bomi "Ah!? I-I no..."

    show screen cexp("bpbb", "bbs", "bea", "bms", p=p_right, h=h_down)
    show screen h_photo_bomi
    c_himeno "Pfft you look ridiculous"
    play sound camera_effect
    with Fade(0.1, 0.0, 0.5, color="#fff")
    show screen cexp("bpfb", "bel", "bmf", "bbs", p=p_right, h=h_down)
    c_bomi "E-eh!? W-wait !!"
    show screen cexp("bpfb", "beb", "bms", "bbs", p=p_right, h=h_down)
    c_bomi "Dont take pictures!"
    moveoutleft screen h_photo_bomi
    show screen cexp("bpbb", "beb", "bms", "bbs", h=h_down)
    narrateur "Bomi tries to follow her but trips."
    show screen cexp("bpbb", "bea", "bms", "bbs", h=h_down)
    menu:
        narrateur "You help her get up"
        "Should I follow her?":
            playerName "Should I follow her ?"
            $ ptsb1 += 1
            show screen cexp("bpbb", "bel", "bms", "bbs", h=h_down)
            c_bomi "..."

        "I don't think people will pay attention to it anyways":
            playerName "I don't think people will pay attention to it anyways"
            show screen cexp("bpbb", "beb", "bmh", "bbs", h=h_down)
            c_bomi "Ahahah... I hope you're right"
    show screen cexp("bpbb", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    c_bomi "I don't want the picture to go around."
    show screen cexp("bpbb", "bel", "bms", "bbs", p=p_left, h=h_down)
    show screen a_and_b
    menu:
        c_akane "What's happening?"
        "Everything is fine.":
            playerName "Everything is fine."
            c_akane "If you say so."
        
        "Someone took a picture of her!":
            $ ptsb1 += 1
            playerName "Someone took a picture of her!"
            c_akane "Ah. I think i know who you're talking about."
            c_akane "I can't really do much since she has a lot of influence over this school."
    show screen cexp("bpbb", "bel", "bmt", "bbs", p=p_left, h=h_down)
    c_bomi "[playerName]!"
    hide screen a_and_b
    scene hallway day with fade
    show screen cexp("bpbb", "bea", "bmt", "bbs", h=h_down)
    c_bomi "It's so embarassing!"
    show screen cexp("bpbb", "bel", "bms", "bbs", h=h_down)
    c_bomi "If this picture spreads, I don't think I could recover..."

    menu:
        "But you look really good.":
            show screen cexp("bpfb", "bel", "bmh", "bbs", h=h_down)
            playerName "But you look really good."
            playerName "The hair extensions were definitely the move."
        
        "The purple hair looks good but it doesn't suit you.":
            show screen cexp("bpfb", "bel", "bmn", "bbs", h=h_down)
            playerName "The purple hair looks good but it doesn't suit you."
            playerName "Come. Let's get the picture back, it'll get better."
    show screen cexp("bpbb", "bea", "bmn", "bbs", h=h_down)
    c_bomi "..."
    show screen cexp("bpbb", "bel", "bmt", "bbs", h=h_down)
    c_bomi "It's fine."
    show screen cexp("bpbb", "beb", "bmh", "bbs", h=h_down)
    c_bomi "Let's go back to class."
    hide screen cexp
    scene black with fade
    jump RBF1

    if ptsb1 >= 4:
        jump RBF1
    else:
        jump RBB1

label RBB1:
    c_bomi """...

    I don't look like her at all 

    Why?

    I've tried everything...

    I've cut, dyed my hair, bought colored lenses...

    it's not working."""

    window hide
    pause
    jump game_over

label RBF1:
    scene classroom day with fade

    "???" "Hey! [playerName]!"
    show screen cexp("bpb", "bel", "bmh", "bbn", h=h_down)
    c_bomi "I got rid of my extensions."
    show screen cexp("bpf", "beb", "bmh", "bbs", h=h_down)
    c_bomi "They were starting to get heavy, haha"
    show screen cexp("bpf", "bea", "bms", "bbs", h=h_down)
    menu:
        c_bomi "..."
        "I'm sure she hasn't posted it yet":
            show screen cexp("bpf", "bel", "bms", "bbs", h=h_down)
            playerName "I'm sure she hasn't posted it yet."
            
        "Let's go find Himeno":
            show screen cexp("bpf", "bel", "bms", "bbs", h=h_down)
            playerName "Let's go find Himeno"
    show screen cexp("bpf", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    show screen cexp("bpf", "bel", "bmt", "bbs", h=h_down)
    c_bomi "I think she's on the rooftop taking pictures for her followers."
    show screen cexp("bpf", "bel", "bms", "bbs", h=h_down)
    "{i} Has she already posted?"
    narrateur """You pull out your phone to check.
    You look at Bomi, account first."""
    show screen cexp("bpf", "bea", "bms", "bbs", h=h_down)
    "{i}Wow..."
    "{i}These comments are harsh..."
    "{i}Himeno has no mercy."
    "..."
    show screen cexp("bpb", "beb", "bms", "bbs", h=h_down)
    narrateur "You find the picture of Bomi posted on her spam account, viral."
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)
    c_bomi "Oh..."
    show screen cexp("bpb", "bea", "bmf", "bbs", h=h_down)
    c_bomi "I was hoping she wouldn't have done that..."
    show screen cexp("bpb", "beb", "bmf", "bbs", h=h_down)
    c_bomi "I didn't think it was that noticeable..."
    show screen cexp("bpb", "bel", "bms", "bbs", h=h_down)
    menu:
        c_bomi "..."
        "You should respond":
            playerName "You should respond"

        "Don't pay attention to it.":
            playerName "Don't pay attention to it."
            playerName "we should report her account and to the school administration."

    show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    playerName "Let's just go see her."
    show screen cexp("bpb", "bel", "bmt", "bbs", h=h_down)
    c_bomi "No!!" 
    show screen cexp("bpf", "bea", "bmt", "bbs", h=h_down)
    c_bomi "I-I mean we shouldn't."
    show screen cexp("bpf", "bel", "bmt", "bbs", h=h_down)
    c_bomi "It'll get more complicated than it should be."
    show screen cexp("bpb", "bea", "bmt", "bbs", h=h_down)
    c_bomi "It'll go by... right ?"
    show screen cexp("bpb", "bel", "bms", "bbs", h=h_down)

    menu:
        c_bomi "..."
        "Yeah. Just keep proof somewhere and ignore the haters.":
            playerName "Yeah. Just keep proof somewhere and ignore the haters."
            playerName "She'll end up facing the consequences anyways"

        "Defend yourself.":
            playerName "Defend yourself."
            playerName "They'll end up believing you"
            playerName "Himeno's got whats coming to her!"

    show screen cexp("bpb", "bea", "bmf", "bbs", h=h_down)
    c_bomi "But..."
    show screen cexp("bpb", "beb", "bmf", "bbs", h=h_down)
    c_bomi "I don't want to cause her trouble..."
    show screen cexp("bpb", "bel", "bms", "bbs", h=h_down)
    c_bomi "..."
    playerName "How do you feel?"
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)
    c_bomi "Bad."
    show screen cexp("bpb", "bea", "bmf", "bbs", h=h_down)
    c_bomi "It's horrible."
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)
    c_bomi "The comments fill my head making me believe them..."
    show screen cexp("bpb", "beb", "bmf", "bbs", h=h_down)
    c_bomi "They kept me up last night."
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)

    menu:
        c_bomi "The more i read, the more i believe it."
        "We should get you a therapist":
            playerName "We should get you a therapist"
            show screen cexp("bpb", "bel", "bmt", "bbn", h=h_down)
            c_bomi "And risk the school telling my family?"
            show screen cexp("bpb", "bea", "bmt", "bbs", h=h_down)
            c_bomi "No way!"
            show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
            c_bomi "..."
        
        "They don't mean anything, it'll work out.":
            playerName "They don't mean anything, it'll work out."
            show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
            c_bomi "..." 
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)
    c_bomi "Fine."
    show screen cexp("bpf", "bel", "bmt", "bbs", h=h_down)
    c_bomi "I hope you're right about this."
    hide screen cexp 
    scene black with fade
    jump RBB2

label RBB2:
    # A changer et a sénariser au fil du temps.
    """{i}It's been a month since I've talked to Bomi about the post.{/i}

    {i}The post spread so much that even the kids at school got whiff of it.{/i}

    {i}Sometimes I'd find hate messages on her locker.{/i}

    {i}Apparently Chunhua had a lot of admirers and if someone tried to imitate their “godesse”, they'd get targeted.{/i}

    {i}I tried to clean and keep the hate away from Bomi but it wasn't enough.{/i}"""
    scene classroom late with fade
    "{i}Bomi ended up finding out about it."
    show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    show screen cexp("bpb", "bel", "bms", "bbs", h=h_down)
    c_bomi "..."
    show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    hide screen cexp
    scene BB2 with fade
    """{i}Eventually she just stopped coming to school.{/i}

    {i}No one had heard from her and te be fair, no one cared.{/i}"""

    window hide
    pause
    jump game_over
