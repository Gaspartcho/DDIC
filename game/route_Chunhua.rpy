label route_A:
    default ptsc1 = 0
    narrateur "{i}I should go home.{/i}"
    scene bedroom with fade
    pause 2.0
    "{i}I should thank Chunhua for the warm welcome."

    call phone_start(usrc, "18:45") 
    label choiceMaking_UAG: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Thanks for the warm welcome ^^","choiceMaking_UAG.choice1","I'm under the impression you do a lot for our class","choiceMaking_UAG.choice2")
        label .choice1:
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Hello Chunhua! thanks for the warm welcome ^^")  # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpc, "It's no problem. It's my job after all") 
            jump .aftermenu
        label .choice2:
            $ ptsc1 += 1
            call phone_after_menu 
            call message_start(playerName, "I'm under the impression you do a lot for our class") 
            call message(playerName, "I'm glad in the care of such a responsible person") 
            call message(tpc, "Thank you.") 
            jump .aftermenu
        label .aftermenu:
    
    call message (tpc, "It's a lot of work") 
    call message (tpc, "People are hard to manage...") 
    call message (tpc, "Some just don't seem to be able to listen to instructions.") 
    call message (tpc, "I hope you're different.") 
    call message (tpc, "Actually, now that I remember, here is a link to my school website. It updates regularly with the upcoming homework, assignments and exams.") 
    call message (tpc, "{u}http://totallynotabadwebsite.com{/u}") 

    label choiceMaking_IPG:
        call screen phone_reply("It looks a bit funny","choiceMaking_IPG.choice1","oh okay, I'll go check it out.","choiceMaking_IPG.choice2")
        label .choice1:
            call phone_after_menu 
            $ ptsc1 += 1
            call message_start(playerName, "...") 
            call reply_message("It looks a bit funny") 
            call message(tpc, "no it doesn't")
            jump .aftermenu
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "oh okay, I'll go check it out.") 
            call message(tpc, "^^") 
            jump .aftermenu
        label .aftermenu:
    
    call message (tpc, "Do you prefer cats or dogs?") 

    label choiceMaking_DOC:
        call screen phone_reply("I like dogs","choiceMaking_DOC.choice1","I prefer cats","choiceMaking_DOC.choice2")
        label .choice1:
            $ ptsc1 += 1
            call phone_after_menu 
            call message_start(playerName, "I like dogs") 
            call message(tpc, "I see.") 
            jump .aftermenu
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "I prefer cats.") 
            call message(tpc, "I see, to each their own i suppose.")
            jump .aftermenu
        label .aftermenu:
    
    call message (tpc, "I love dogs") 
    call message (tpc, "They are loyal to their owners and do what they're told") 
    call message (tpc, "Most of the time at least...") 
    call message (tpc, "If most people had the same mindset as dogs, we'd probably have world peace.") 
    call message (tpc, "Or something of the sort.")

    label choiceMaking_DAP:
        call screen phone_reply("But people aren't dogs...","choiceMaking_DAP.choice1","I agree","choiceMaking_DAP.choice2")
        label .choice1:
            call phone_after_menu 
            call message_start(playerName, "But people aren't dogs...") 
            $ ptsc1 += 1
            call reply_message("They need privacy, freedom...") 
            call message(tpc, "Maybe.") 
            call message(tpc, "But it would still be easier to maintain order") 
            call message(playerName, "Do you realize what you're saying?")
            call message(tpc, "Yes .") 
            jump .aftermenu
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "I agree") 
            call reply_message("They're so nice and cute, everyone would be happy.") 
            call message(tpc, "Haha") 
            jump .aftermenu
        label .aftermenu:

    call message (tpc, "I love dog sitting in my spare time.") 
    call message_img(tpc, "", "images/instagram/C2_insta.png") 
    call message (tpc, "It gives me a bit of pocket money") 
    call message (tpc, "My family is pretty well off") 
    call message (tpc, "But a bit of extra cash never hurt anyone.") 
    call message (tpc, "Do you want to join me one day?") 

    label choiceMaking_DSA:
        call screen phone_reply("Of course!","choiceMaking_DSA.choice1","i have a lot to catch up with school...","choiceMaking_DSA.choice2")
        label .choice1:
            call phone_after_menu 
            call message_start(playerName, "Of course!") 
            $ ptsc1 += 1
            call message(tpc, "Perfect.") 
            jump .aftermenu
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "i have a lot to catch up with school...") 
            call message(tpc, "That's okay") 
            call message(tpc, "If you ever change your mind...") 
            jump .aftermenu
        label .aftermenu:

    call message(tpc, "Could you give me your bank details?") 
    call message(tpc, "That way I could sign you up in advance.") 
    call phone_end(False) 

    narrateur "Uhm"
    narrateur "I'll just wait a little before I do..."
    scene classroom day with fade
    pause 1.0
    c_chunhua "{cps=50}Hello, [playerName]."
    show screen cexp("apc", "aeb", "ams", "abn", h=h_mid)
    "{i}Holy Sweet Baby Jesus!!"
    "{i}She has got to stop appearing out of nowhere"
    show screen cexp("apc", "ael", "ams", "abn", h=h_mid)
    playerName "Hey Chunhua, you need something?"
    show screen cexp("apc", "ael", "amt", "abn", h=h_mid)
    c_chunhua "Yes, I need a favor from you."
    c_chunhua "You know Himeno?"
    c_chunhua "The blonde girl thats a bit tanned."
    show screen cexp("apc", "aeb", "ams", "abn", h=h_mid)
    c_chunhua "Could you send her this link?"
    show screen cexp("apc", "ael", "ams", "abn", h=h_mid)
    c_chunhua "It's a gift card to thanking her and her family."
    c_chunhua "You see, her family is extremely wealthy and they regularly donate to our school."
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)

    menu:
        c_chunhua "I thought this would be a nice thank you gift coming from the whole class."
        "Uh... This seems a bit weird":
            $ ptsc1 += 1
            playerName "Uh... This seems a bit weird"
            show screen cexp("apr", "ael", "ams", "abn", h=h_mid)
            c_chunhua "It's crypted in a way only Himeno can open it"

        "Okay, but why can't you do it yourself?":
            playerName "Okay, but why can't you do it yourself?"
            show screen cexp("apr", "ael", "amt", "abn", h=h_mid)
            c_chunhua "It's symbolic. If I give it to Himeno might think I am looking down on her."
            show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
            c_chunhua "A new student thanking the donors of our school is a positive message."
    
    "{i}..."
    "{i}This is the second time Chunhua has sent me something suspicious..."
    show screen cexp("apc", "ael", "ams", "abn", h=h_mid)
    playerName "You aren't by any chance trying to scam us?"
    show screen cexp("apr", "aea", "ams", "abn", h=h_mid)
    c_chunhua "..."
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    c_chunhua "No."
    show screen cexp("apr", "aeb", "amt", "abn", h=h_mid)
    c_chunhua "Sometimes I like to do silly tricks..."
    c_chunhua "Nothing evil though."
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    menu:
        c_chunhua "So, what will you do?"
        "Chunhua, You shouldn't feel the need to take other people's money.":
            $ ptsc1 += 1
            playerName "Chunhua, You shouldn't feel the need to take other people's money."
            show screen cexp("apr", "ael", "amt", "abn", h=h_mid)
            c_chunhua "Sorry?"

        "Can I wait a little?":
            playerName "Can I wait a little?"
            playerName "to get to know everyone a bit better..."
    show screen cexp("apr", "ael", "amn", "abn", h=h_mid)
    c_chunhua "If you don't want to do it, I'll take care of it." 
    "Teacher" "Chunhua! Could you help me with these papers?"
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    c_chunhua "I need to go, see you soon."
    hide screen cexp
    
    if ptsc1 >= 4:
        jump RAF1
    else:
        jump RAB1

label RAB1:
    pause
    """{i}It's been a week.{/i}

    {i}I've learned everyone's names, but I haven't really made any close friends.{/i}

    {i}I decided to send Chunhua's gift to Himeno. {/i}

    ...

    ..."""
    scene classroom late with fade 

    """{i}It's been 3 days since I've sent the gift.{/i}

    {i}I wonder what it was.{/i}"""
    "Teacher" "The two solutions to this function-"
    "???" "Excuse me. Is Zhou Chunhua here?"
    show screen cexp("apc", "aea", "amn", "abn", h=h_mid)
    c_chunhua "..."
    "Teacher" "Who are you? This is a classroom. You can't just come in like this!"
    "Mr. Aki" """I am detective Aki. I'm here for a case involving Zhou Chunhua.

    Miss Zhou, please step out the classroom and come with me."""
    show screen cexp("apc", "aea", "ams", "abn", h=h_mid)
    pause
    hide screen cexp
    scene black with fade
    "{i}A year later, Chunhua was put on trial.{/i}"
    scene AB1 with fade
    "Judge" """Zhou Chunhua.
    
    You are accused of theft by the Yuzu family.

    Do you plead guilty ?"""
    c_chunhua "Yes sir."
    "Judge" "Zhou Chunhua. You are sentenced to 5 years in prison."
    window hide
    pause

    jump game_over

label RAF1:
    define ptsc2 = 0
    scene bedroom with fade
    narrateur "A few days later..."
    call phone_start(usrc, "20:24") 
    call message_start (tpc, "Hello, [playerName]. I know it's been a week since I've asked you to send that gift to Himeno, turns out my gift expired so there's no need for it.") 
    call message (tpc, "Actually, I don't know if you've noticed, but someone has been catfishing as me.") 
    call message (tpc, "They take pictures of me and steal my pictures from my account.") 
    call message (tpc, "It's slightly worrisome.") 

    pause
    window show
    "{i}Is she talking about Bomi?"
    window hide
    
    label choiceMaking_WGD:
        call screen phone_reply("That's scary","choiceMaking_WGD.choice1","You should call them out","choiceMaking_WGD.choice2")
        label .choice1:
            call phone_after_menu 
            call message_start(playerName, "That's scary.") 
            call reply_message("Are you going to do something about it?") 
            call message(tpc, "No, not really. I don't feel particularily threatened by this .") 
            jump .aftermenu
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "You should call them out.") 
            $ ptsc2 += 1
            call message(tpc, "There's no point, They surely won't do anything")
            call message(tpc, "I couldn't even if I wanted to.") 
            call message(tpc, "I haven't got a clue on who it is.") 

            jump .aftermenu
        label .aftermenu:
    
    pause
    window show
    "{i}..."
    window hide

    label choiceMaking_USP:
        call screen phone_reply("You should take precautions","choiceMaking_USP.choice1","You're right, I don't think they will do anything either.","choiceMaking_USP.choice2")
        label .choice1:
            call phone_after_menu 
            call message_start(playerName, "You should take precautions.") 
            $ ptsc2 += 1
            call message(tpc, "I don't really care.") 
            jump .aftermenu
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "You're right, I don't think they will do anything either.") 
            call message(tpc, "Of course I'm right.") 
            jump .aftermenu
        label .aftermenu:
    
    call message (tpc, "Don't worry too much about it.") 
    call message (tpc, "I need to eat, talk to you later.") 
    call phone_end

    "{i}..."
    "{i}Should I tell her?"
    "{i}..."

    call phone_start (usrcf, "20:38") 
    call message_start(tpc, " Hello, [playerName]!") 
    call message(tpc, "How have you been this week?") 
    call message(tpc, "I hope you've settled in well.") 
    call reply_message("...") 
    call reply_message("Bomi Park?")
    call message(tpc, "What?") 
    call message(tpc, "Why are you mentioning her?")

    label choiceMaking_KUR:
        call screen phone_reply("I know who you are","choiceMaking_KUR.choice1","No, nothing. I just wanted to know more about her.","choiceMaking_KUR.choice2")
        label .choice1:
            call phone_after_menu 
            $ ptsc2 += 1
            call message_start(playerName, "I know who you are.") 
            call message(tpc, "...") 
            call message(tpc, "Never speak of this.") 
            jump .aftermenu
        label .choice2:
            call phone_after_menu 
            call message_start(playerName, "No, nothing. I just wanted to know more about her.") 
            call message(tpc, "I could tell you about her...") 
            call message(tpc, "But I won't.") 
            jump .aftermenu
        label .aftermenu:
    call phone_end 

    "{i}..."
    "{i}I should tell Chunhua."

    call phone_start(usrc, "20:46") 
    label choiceMaking_PBC:
        call screen phone_reply("Chunhua, Please be really careful","choiceMaking_PBC.choice1","Chunhua, I'll teach you how to protect yourself","choiceMaking_PBC.choice2")
        label .choice1:
            call phone_after_menu 
            call message_start(playerName, "Chunhua, Please be really careful") 
            call message(tpc, "I will.") 
            call message(tpc, "Why are you worried, it's not that important.") 
            call message(tpc, "It's just a bit annoying...") 
            jump .aftermenu
        label .choice2:
            call phone_after_menu 
            $ ptsc2 += 1
            call message_start(playerName, "Chunhua, I'll teach you how to protect yourself.") 
            call message(tpc, "Fine") 
            jump .aftermenu
        label .aftermenu:
    call phone_end
    "{i}...{/i}"
    if ptsc2 > 2:
        jump RCF
    else:
        jump RCB2

label RCB2:
    "{i}A week later, I got a notification that Himeno is live on instargam."

    c_himeno """Oh.

    My.

    Days.

    Chunhua is missing!"""

    "{i}...

    I should go find her"
    
    "..."
    scene AB2 with fade
    playerName "Chunhua!"
    playerName "Where is she?"
    call phone_start (usrc, "19:16")
    call message_start(tpc, "Help")
    call phone_end
    jump game_over

label RCF:
    scene blacks with fade
    "{i}I met Chunhua the next day at school."
    scene AGE with fade
    c_chunhua "What do you want me to do?"
    playerName "So..."
    """{i}I explained to Chunhua the basics of online security but she seemed to know more than I did.{/i}
    
    {i}She ended up giving me more tips while she was setting up the safety precautions.{/i}"""
    c_chunhua """Thanks for thinking of me.
    
    Let's go home."""

    window hide
    pause
    jump happy_ending


