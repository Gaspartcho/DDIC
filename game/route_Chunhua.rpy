label route_A:
    define ptsc1 = 0
    narrateur "{i}I should go home.{i/}"
    scene bedroom with fade
    pause 2.0
    "{i}I should thank Chunhua for the warm welcome."

    call phone_start(usrc, "18:45") from _call_phone_start_4
    label choiceMaking_UAG: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("thanks for the warm welcome ^^","choiceMaking_UAG.choice1","I'm under the impression you do a lot for our class","choiceMaking_UAG.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_6 # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Hello Chunhua! thanks for the warm welcome ^^") from _call_message_start_9 # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpc, "TIt's no problem. It's my job after all") from _call_message_22
            jump .aftermenu
        label .choice2:
            $ ptsc1 += 1
            call phone_after_menu from _call_phone_after_menu_7
            call message_start(playerName, "I'm under the impression you do a lot for our class") from _call_message_start_10
            call message(playerName, "I'm glad in the care of such a responsible person") from _call_message_23
            call message(tpc, "Thank you.") from _call_message_24
            jump .aftermenu
        label .aftermenu:
    
    call message (tpc, "It's a lot of work") from _call_message_25
    call message (tpc, "People are hard to manage...") from _call_message_26
    call message (tpc, "Some just don't seem to be able to listen to instructions.") from _call_message_27
    call message (tpc, "I hope you're different.") from _call_message_28
    call message (tpc, "Actually, now that i remember, here is a link to my school website. It updates regularly with the upcoming homework, assignments and exams.") from _call_message_29
    call message (tpc, "{u}http://totallynotabadwebsite.com{/u}") from _call_message_30

    label choiceMaking_IPG:
        call screen phone_reply("It looks a bit funny","choiceMaking_IPG.choice1","oh okay, I'll go check it out.","choiceMaking_IPG.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_8
            $ ptsc1 += 1
            call message_start(playerName, "...") from _call_message_start_11
            call reply_message("It looks a bit funny") from _call_reply_message_6
            call message(tpc, "no it doesn't") from _call_message_31
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_9
            call message_start(playerName, "oh okay, I'll go check it out.") from _call_message_start_12
            call message(tpc, "^^") from _call_message_32
            jump .aftermenu
        label .aftermenu:
    
    call message (tpc, "Do you prefer cats or dogs?") from _call_message_34

    label choiceMaking_DOC:
        call screen phone_reply("i like both","choiceMaking_DOC.choice1","i prefer cats","choiceMaking_DOC.choice2")
        label .choice1:
            $ ptsc1 += 1
            call phone_after_menu from _call_phone_after_menu_10
            call message_start(playerName, "i like both") from _call_message_start_13
            call message(tpc, "I see, at least you still like dogs.") from _call_message_35
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_11
            call message_start(playerName, "i prefer cats.") from _call_message_start_14
            call message(tpc, "I see, to each their own i suppose.") from _call_message_36
            jump .aftermenu
        label .aftermenu:
    
    call message (tpc, "I love dogs") from _call_message_37
    call message (tpc, "They are loyal to their owners and do what they're told") from _call_message_38
    call message (tpc, "Most of the time at least...") from _call_message_39
    call message (tpc, "If most people had the same mindset as dogs, we'd probably have world peace.") from _call_message_40
    call message (tpc, "Or something of the sort.") from _call_message_41

    label choiceMaking_DAP:
        call screen phone_reply("But people aren't dogs...","choiceMaking_DAP.choice1","I agree","choiceMaking_DAP.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_12
            call message_start(playerName, "But people aren't dogs...") from _call_message_start_15
            $ ptsc1 += 1
            call reply_message("They need privacy, freedom...") from _call_reply_message_7
            call message(tpc, "Maybe.") from _call_message_42
            call message(tpc, "But it would still be easier to maintain order") from _call_message_43
            call message(playerName, "Do you realize what you're saying?") from _call_message_44
            call message(tpc, "Yes .") from _call_message_45
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_13
            call message_start(playerName, "I agree") from _call_message_start_16
            call reply_message("They're so nice and cute, everyone would be happy.") from _call_reply_message_8
            call message(tpc, "Haha") from _call_message_46
            jump .aftermenu
        label .aftermenu:

    call message (tpc, "I love dog sitting in my spare time.") from _call_message_47
    call message_img(tpc, "", "images/instagram/A2_insta.png") from _call_message_img
    call message (tpc, "It gives me a bit of pocket money") from _call_message_48
    call message (tpc, "My family is pretty well off") from _call_message_49
    call message (tpc, "But a bit of extra cash never hurt anyone.") from _call_message_50
    call message (tpc, "Do you want to join me one day?") from _call_message_51

    label choiceMaking_DSA:
        call screen phone_reply("Of course!","choiceMaking_DSA.choice1","i have a lot to catch up with school...","choiceMaking_DSA.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_14
            call message_start(playerName, "Of course!") from _call_message_start_17
            $ ptsc1 += 1
            call message(tpc, "Perfect.") from _call_message_52
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_15
            call message_start(playerName, "i have a lot to catch up with school...") from _call_message_start_18
            call message(tpc, "That's okay") from _call_message_54
            call message(tpc, "If you ever change your mind...") from _call_message_55
            jump .aftermenu
        label .aftermenu:

    call message(tpc, "could you give me your bank details?") from _call_message_56
    call message(tpc, "that way I could sign you up in advance.") from _call_message_57
    call phone_end(False) from _call_phone_end_4

    narrateur "Uhm"
    narrateur "I'll just wait a little before i do..."
    scene classroom day with fade
    pause 1.0
    c_akane "{cps=50}Hello, [playerName]."
    show screen cexp("apc", "aeb", "ams", "abn", h=h_mid)
    "{i}Holy Sweet Baby Jesus!!"
    "{i}She's got to stop appearing out of nowhere"
    show screen cexp("apc", "ael", "ams", "abn", h=h_mid)
    playerName "Hey Chunhua, you need something?"
    show screen cexp("apc", "ael", "amt", "abn", h=h_mid)
    c_akane "Yes, I need a favor from you."
    c_akane "You know Himeno?"
    c_akane "The blonde girl thats a bit tanned."
    show screen cexp("apc", "aeb", "ams", "abn", h=h_mid)
    c_akane "Could you send her this link?"
    show screen cexp("apc", "ael", "ams", "abn", h=h_mid)
    c_akane "It's a gift card to thanking her and her family."
    c_akane "You see, her family is extremely wealthy and they regularly donate to our school."
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)

    menu:
        c_akane "I thought this would be a nice thank you gift coming from the whole class."
        "Uh... This seems a bit weird":
            $ ptsc1 += 1
            playerName "Uh... This seems a bit weird"
            show screen cexp("apr", "ael", "ams", "abn", h=h_mid)
            c_akane "It's crypted in a way only Himeno can open it"

        "Okay, but why can't you do it yourself?":
            playerName "Okay, but why can't you do it yourself?"
            show screen cexp("apr", "ael", "amt", "abn", h=h_mid)
            c_akane "I'ts symbolic. If I give it to Himeno might think I am looking down on her."
            show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
            c_akane "A new student thanking the donors of our school is a positive message."
    
    "{i}..."
    "{i}This is the second time Chunhua has sent me something suspicious..."
    show screen cexp("apc", "ael", "ams", "abn", h=h_mid)
    playerName "You aren't by any chance trying to scam us?"
    show screen cexp("apr", "aea", "ams", "abn", h=h_mid)
    c_akane "..."
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    c_akane "No."
    show screen cexp("apr", "aeb", "amt", "abn", h=h_mid)
    c_akane "Sometimes i like to do silly tricks..."
    c_akane "Nothing evil though."
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    menu:
        c_akane "So, what will you do?"
        "Chunhua, You shouldn't feel the need to take other people's money.":
            $ ptsc1 += 1
            playerName "Chunhua, You shouldn't feel the need to take other people's money."
            show screen cexp("apr", "ael", "amt", "abn", h=h_mid)
            c_akane "Sorry?"

        "Can i wait a little?":
            playerName "Can i wait a little?"
            playerName "to get to know everyone a bit better..."
    show screen cexp("apr", "ael", "amn", "abn", h=h_mid)
    c_akane "If you don't want to do it, I'll take care of it." 
    "Teacher" "Chunhua! Could you help me with these papers?"
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    c_akane "I need to go, see you soon."
    hide screen cexp
    
    if ptsc1 >= 4:
        jump RAF1
    else:
        jump RAB1

label RAB1:
    """{i}It's been a week.{/i}

    {i}I've learned everyone's names, but i haven't really made any close friends.{/i}

    {i}I decided to send Chunhua's gift to Himeno. {/i}

    ...

    ..."""
    scene classroom late with fade 

    """{i}It's been 3 days since I've sent the gift.{/i}

    {i}I wonder what it was.{/i}"""
    "Teacher" "The two solutions to this function-"
    "???" "Excuse me. Is Zhou Chunhua here?"
    show screen cexp("apc", "aea", "amn", "abn", h=h_mid)
    c_akane "..."
    "Teacher" "Who are you? This is a classroom. You can't just come in like this!"
    "Mr. Aki" """I am detective Aki. I'm here for a case involving Zhou Chunhua.

    Miss Zhou, please step out the classroom and come with me."""
    show screen cexp("apc", "aea", "ams", "abn", h=h_mid)
    pause
    hide screen cexp
    scene black with fade
    "{i}Un an plus tard, Akane a été mise en procès.{/i}"
    scene AB1 with fade
    "Judge" """Zhou Chunhua.
    
    You are accused of theft from the Yuzu family.

    Do you plead guilty ?"""
    c_akane "Yes sir."
    window hide
    pause

    jump game_over

label RAF1:
    define ptsc2 = 0
    scene bedroom with fade
    narrateur "A few days later..."
    call phone_start(usrc, "20:24") from _call_phone_start_5
    call message_start (tpa, "Hello, [playerName]. I know it's been a week since I've asked you to send that gift to Himeno, turns out my gift expired so there's no need for it.") from _call_message_start_19
    call reply_message ("Oh ok.") from _call_reply_message_11
    call message (tpa, "Actually, I don't know if you've noticed, but someone has been catfishing as me.") from _call_message_58
    call message (tpa, "They take pictures of me and steal my pictures from my account.") from _call_message_59
    call message (tpa, "It's slightly worrisome.") from _call_message_60

    pause
    window show
    "{i}Is she talking about Bomi?"
    window hide
    
    label choiceMaking_WGD:
        call screen phone_reply("That's scary","choiceMaking_WGD.choice1","You should call them out","choiceMaking_WGD.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_16
            call message_start(playerName, "That's scary.") from _call_message_start_20
            call reply_message("Are you going to do something about it?") from _call_reply_message_12
            call message(tpa, "No, not really. I don't feel particularily threatened by this .") from _call_message_61
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_17
            call message_start(playerName, "You should call them out") from _call_message_start_21
            $ ptsc2 += 1
            call message(tpa, "There's no point, They surely won't do anything") from _call_message_62
            call message(tpa, "I couldn't even if i wanted to.") from _call_message_63
            call message(tpa, "I haven't got a clue on who it is.") from _call_message_64

            jump .aftermenu
        label .aftermenu:
    
    pause
    window show
    "{i}..."
    window hide

    label choiceMaking_USP:
        call screen phone_reply("You should take precautions","choiceMaking_USP.choice1","You're right, I don't think they will do anything either.","choiceMaking_USP.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_18
            call message_start(playerName, "You should take precautions.") from _call_message_start_22
            $ ptsa2 += 1
            call message(tpa, "I don't really care.") from _call_message_65
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_19
            call message_start(playerName, "You're right, I don't think they will do anything either.") from _call_message_start_23
            call message(tpa, "Of course I'm right.") from _call_message_66
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "Don't worry too much about it.") from _call_message_67
    call message (tpa, "I need to eat, talk to you later.") from _call_message_67
    call phone_end from _call_phone_end_5

    "{i}..."
    "{i}Should I tell her?"
    "{i}..."

    call phone_start (usrcf, "20:38") from _call_phone_start_6
    call message_start(tpa, " Hello, [playerName]!") from _call_message_start_24
    call message(tpa, "How have you been this week?") from _call_message_68
    call message(tpa, "I hope you've settled in well.") from _call_message_69
    call reply_message("...") from _call_reply_message_13
    call reply_message("Bomi Park?") from _call_reply_message_14
    call message(tpa, "What?") from _call_message_70
    call message(tpa, "Why are you mentioning her?") from _call_message_71

    label choiceMaking_KUR:
        call screen phone_reply("I know who you are","choiceMaking_KUR.choice1","No, nothing. I just wanted to know more about her.","choiceMaking_KUR.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_20
            $ ptsa2 += 1
            call message_start(playerName, "I know who you are.") from _call_message_start_25
            call message(tpc, "...") from _call_message_72
            call message(tpc, "Never speak of this.") from _call_message_73
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_21
            call message_start(playerName, "No, nothing. I just wanted to know more about her.") from _call_message_start_26
            call message(tpc, "I could tell you about her...") from _call_message_74
            call message(tpc, "But i won't.") from _call_message_75
            jump .aftermenu
        label .aftermenu:
    call phone_end from _call_phone_end_6

    "{i}..."
    "{i}I should tell Chunhua."

    call phone_start(usrc, "20:46") from _call_phone_start_7
    label choiceMaking_PBC:
        call screen phone_reply("Chunhua, Please be really careful","choiceMaking_PBC.choice1","Chunhua, I'll teach you how to protect yourself","choiceMaking_PBC.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_22
            call message_start(playerName, "Chunhua, Please be really careful") from _call_message_start_27
            call message(tpa, "I will.") from _call_message_76
            call message(tpa, "Why are you worried, It's not that important.") from _call_message_77
            call message(tpa, "its just a bit annoying...") from _call_message_78
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_23
            $ ptsa2 += 1
            call message_start(playerName, "Chunhua, I'll teach you how to protect yourself.") from _call_message_start_28
            call message(tpa, "Fine") from _call_message_79
            jump .aftermenu
        label .aftermenu:
    call phone_end from _call_phone_end_7
    "{i}...{/i}"
    if ptsa2 > 2:
        jump RAF
    else:
        jump RAB2

label RAB2:
    "{i}A week later, i got a notification that Himeno is live on instargam."

    c_himeno """Oh.

    My.

    Days.

    Chunhua is missing!"""

    "{i}...

    I should go find her"
    
    "..."
    scene AB2 with fade
    playerName "Chunhua!"
    playerName "Where is she"
    call phone_start (usrcf, "19:16")
    call message_start(tpc, "Help")

    window hide
    pause
    jump game_over

label RAF:
    scene blacks with fade
    "{i}I met Chunhua the next day at school."
    scene AGE with fade
    c_akane "What do you want me to do?"
    playerName "So..."
    """{i}I explained to Chunhua the basics of online security but she seemed to know more than I did.{/i}
    
    {i}She ended up giving me more tips while she was setting up the safety precautions.{/i}"""
    c_akane """Thanks for thinking of me.
    
    Let's go home?"""

    window hide
    pause
    jump happy_ending


