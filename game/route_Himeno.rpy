label RH1:
    define ptsh1 = 0
    narrateur """{i}The clock rings 3 times. Classes are over{/i}"""

    "{i}This first day of school wasn't too bad."
    playerName "Hmm?"

    call phone_start(usrh, "17:05")
    call message_start(tph, "Meet me at the park, I know you're done with classes <3") 
    call phone_end
    "{i}..."
    
    "{i}I wonder what is it that she want.{/i}"

    scene park with fade

    narrateur "You find Himeno sat on a bench at the back of the park."
    show screen cexp("hpw", "heb", "hml", "hbn")

    c_himeno "Hey [playerName]"
    show screen cexp("hph", "hel", "hms", "hbn")
    menu:
        c_himeno "Ready to ruin some lives?"
        "What are we doing? I hope nothing bad":
            playerName "What are we doing? I hope nothing bad"
            show screen cexp("hph", "heb", "hmt", "hbn")
            c_himeno """But of course we are! 

            We're going to execute the most evil plan of humanity"""

        "We are definitely up to no good":
            playerName "We are definitely up to no good."
            $ ptsh1 += 1
            show screen cexp("hph", "heb", "hmt", "hbn")
            c_himeno "Don't be dumb, it's for the greater good"
    
    playerName "..."
    show screen cexp("hph", "hel", "hms", "hbn")
    c_himeno """My makeup is slaying today.

    I'm asking you to take my pics."""
    show screen cexp("hph", "hes", "hmm", "hbn")
    c_himeno """It'll be fun, you'll see
        
    We're going to ruin people's lives by showing them that I'm missing in their life."""

    menu:
        c_himeno "You'll do that won't you ?"
        "I'm the best camera man you'll find.":
            playerName "I'm the best camera man you'll find."
            $ ptsh1 += 1
            define himeno_help = False
            show screen cexp("hph", "heb", "hms", "hbn")
            c_himeno """Perfect!

            See? We're the perfect duo"""

        "I'm not really good with a camera":
            define himeno_help = True
            playerName "I'm not really good with a camera"
            show screen cexp("hpw", "hes", "hmt", "hbn")
            c_himeno "It's fine, I'll guide you"
    
    show screen cexp("hph", "heb", "hms", "hbn")

    play sound camera_effect
    show screen cexp("hpw", "hel", "hms", "hbn")
    with Fade(0.1, 0.0, 0.5, color="#fff")
    play sound camera_effect
    show screen cexp("hph", "hel", "hms", "hbn")
    with Fade(0.1, 0.0, 0.5, color="#fff")
    play sound camera_effect
    show screen cexp("hpw", "heb", "hml", "hbn")
    with Fade(0.1, 0.0, 0.5, color="#fff")
    play sound camera_effect
    show screen cexp("hph", "hel", "hml", "hbn")
    with Fade(0.1, 0.0, 0.5, color="#fff")

    show screen cexp("hpw", "hel", "hms", "hbn")
    c_himeno "Let me see! I wanna know how they turned out!"
    show screen cexp("hph", "hea", "hmf", "hba")
    c_himeno "Hey! Isn't that..."
    show screen cexp("hph", "hea", "hmn", "hba")

    """{i}What{/i}

    {i}Did I take bad angles?{/i}"""

    if himeno_help:
        "{i}I did everything she asked me to do though...{/i}"
    else:
        "{i}I followed the few photography rules i saw online though...{/i}"

    "{i}Surely, she's exagerating-{/i}"
    show screen cexp("hph", "hel", "hmf", "hba")
    c_himeno "Bomi is in my pics."

    narrateur "You get closer and peek at her phone."

    playerName "Huh?"
    show screen cexp("hph", "hea", "hml", "hba")
    c_himeno "Pfft!"
    show screen cexp("hph", "hel", "hml", "hba")
    c_himeno "She looks like a stalker."
    show screen cexp("hph", "hea", "hml", "hba")
    c_himeno "What is she doing?"
    show screen cexp("hpw", "hel", "hml", "hba")

    c_himeno """ Hey! 

    Go away! I'll file a restraining order!"""

    menu:
        c_himeno "leave me alone!"
        "Don't be like that... Maybe she's just here by chance.":
            playerName "Don't be like that... Maybe she's just here by chance."
            show screen cexp("hph", "hel", "hmn", "hba")
            $ ptsh1 += 1
            c_himeno "She's following me, that's enough to punish her."

        "She'll leave, just ignore her.":
            playerName "She'll leave, just ignore her."
            show screen cexp("hph", "hel", "hmf", "hba")
            c_himeno """What? And let her keep following me?

            No."""
    c_himeno "I would rather kill myself than let myself get stepped on."
    show screen cexp("hpw", "hel", "hmn", "hba")
    menu:
        c_himeno "Especially by her."
        "She'll get what's coming to her":
            playerName "She'll get what's coming to her"
            show screen cexp("hph", "hea", "hmn", "hba")
            c_himeno "Duh, obviously."
            c_himeno "Everything about her pisses me off!"

        "We could just ask her why she's following you":
            playerName "We could just ask her why she's following you..."
            playerName "Has she ever done anything to bother you?"
            $ ptsh1 += 1
            show screen cexp("hph", "hea", "hmn", "hba")
            c_himeno """...

            Yeah"""

    show screen cexp("hph", "hea", "hmf", "hba")
    c_himeno """She took {b}my{/b} spot at the top of the leaderboard.

    Like I said,"""
    show screen cexp("hph", "hel", "hmf", "hba")
    menu:
        c_himeno "She's def cheating."
        "I'm sure she's worked hard to get to where she is":
            playerName """I'm sure she's worked hard to get to where she is. 
            
            I think you can do better than her too."""
            show screen cexp("hph", "hea", "hmn", "hba")
            $ ptsh1 += 1
            c_himeno "..."

        "Maybe she's just a genius. ":
            playerName "Maybe she's just a genius. "
            show screen cexp("hph", "hea", "hmn", "hba")
            c_himeno "..."

    """{i}Himeno seems pissed.{/i}

    {i}Maybe I shouldn't have said that.{/i}"""
    show screen cexp("hph", "hel", "hmf", "hba", "hlc")
    c_himeno "... Shut up..."
    show screen cexp("hph", "hel", "hmn", "hba", "hlc")
    playerName "Huh?"
    show screen cexp("hph", "hea", "hmf", "hba", "hlc")
    c_himeno "What right do you have to say that?"
    show screen cexp("hph", "hel", "hmf", "hba", "hlc")
    c_himeno "You think I don't try?"
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno """All I ever wanted...

    ... was for my father to notice me"""
    show screen cexp("hph", "hea", "hmf", "hbs", "hlc")
    c_himeno """He's never home.

    Whether I do things well or not..."""
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno "... He never looks at me."
    show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
    c_himeno "..."
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno """Ah

    Why..."""
    show screen cexp("hph", "heb", "hmf", "hbs", "hlc")
    c_himeno "You ruined my makeup"
    show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
    "..."

    menu:
        "{i}I should say something{/i}"
        "He'll acknowledge you one day.":
            show screen cexp("hph", "hel", "hmn", "hbs", "hlc")
            playerName "He'll acknowledge you one day, don't worry."
            playerName "Which is why you should be nice,"
            playerName "... for the day he sees you,"
            playerName "... He'll see you in the best light possible."
            $ ptsh1 += 1
            show screen cexp("hph", "hea", "hmn", "hbs", "hlc")

        "... ":
            playerName "... "
            show screen cexp("hph", "hea", "hmn", "hbs", "hlc")
    
    c_himeno "..."
    show screen cexp("hph", "hel", "hmf", "hbs", "hlc")
    c_himeno "I'm gonna go home..."
    hide screen cexp with fade
    pause 2.0
    narrateur "You glance at where Bomi was standing in the picture but she wasn't there anymore"

    "{i}She must have left when Himeno called her out.{/i}"
    narrateur "You also decide to go back home."
    scene black with fade

    "{i}I wonder what Himeno will do .{/i}"
    pause 5

    if ptsh1 >= 4: 
        jump RH2
    else:
        jump HB1

label HB1:
    pause 5
    scene classroom late with fade
    """{i}It's been a week since I was at the park with Himeno.{/i}

    {i}Himeno ended up posting that picture and spread a lot of hate.{/i}

    {i}Bomi ended up enduring a lot of bullying since the cyberbullying became physical.{/i}"""
    show screen cexp("hpw", "hel", "hmf", "hbn")
    c_himeno "Hey [playerName]."
    
    "{i}Himeno's gaze seems to turn cold whenever she looks at me.{/i}"
    show screen cexp("hph", "hel", "hmf", "hbn")
    c_himeno "Come with me."
    show screen cexp("hph", "hea", "hmn", "hbn")
    playerName "Ok."

    """{i}To be fair, it’s not like I can go against her...{/i}

    {i}She ended up finding dirt on me.{/i}"""
    hide screen cexp
    scene hallway late with fade
    show screen cexp("hph", "hel", "hmf", "hbs", p=p_right)
    narrateur "You follow her into the hallway when a pink figure out of nowhere tackles Himeno"
    hide screen cexp
    show screen h_and_bomi
    c_bomi """You!

    Did!

    This!

    You ruined my life!"""

    hide screen h_and_bomi

    """{i}Himeno and Bomi struggled against each other. {/i}

    {i}There didn’t seem to be any boundaries, they clawed at each other.{/i}"""

    c_himeno "Get off of me- !"

    narrateur "You notice Himeno step back onto the edge of the stairs"

    playerName "Wait--"
    scene black with fade

    """{i}It was too late.{/i}

    {i}Before I could do anything, Himeno fell backwards down two flights of stairs.{/i}"""

    c_bomi "..."

    """{i}Before I could grab Bomi and ask her to help she ran away.{/i}

    {i}What a mess.{/i}

    {i}A few hours later, we were at the hospital.{/i}
    
    {i}Himeno was rushed to the hospital since she wouldn’t wake up after she fell.{/i}"""

    """{i}According to doctors, the stairs really roughed her up.{/i}

    {i}She landed awkwardly and disfigured her face permanently.{/i}"""

    window hide
    pause
    jump game_over

label RH2:
    define ptsh2 = 0
    """{i}It’s been a week since I was at the park with Himeno. {/i}

    {i}Himeno posted the pictures we took of her and they blew up.{/i}

    {i}Thankfully, Himeno was merciful and edited her out.{/i}"""

    scene classroom day with fade
    pause 1.0
    show screen cexp("hpw", "heb", "hml", "hbn")
    c_himeno "Hey! [playerName]! You did really well with the camera work."
    show screen cexp("hph", "hes", "hml", "hbn")
    c_himeno """You did so well that I've been receiving offers from businesses!"""
    show screen cexp("hph", "heb", "hml", "hbn")
    c_himeno """I can actually make money!"""
    show screen cexp("hph", "hea", "hms", "hbn")
    narrateur "Himeno pulls out her phone and shows her requests on instargam."
    show screen cexp("hph", "hes", "hml", "hbn")
    c_himeno "It's crazy out here. You're girl is getting popular ~~"
    show screen cexp("hph", "hea", "hms", "hbn")
    menu:
        "{i}It was a mixture of jewelry, clothing and makeup. Some of them were free claim gifts and a lot of them were compliments from fans.{/i}"
        "Haha that's great! Have you accepted any?":
            playerName "Haha that's great! Have you accepted any?"
            show screen cexp("hpw", "hes", "hmt", "hbn")
            c_himeno "Nope! I wanted to show you all before I accepted any of them!"

        "That's amazing Himeno! You're gonna become an actual influencer!":
            playerName "That's amazing Himeno! You're gonna become an actual influencer!"
            show screen cexp("hpw", "heb", "hml", "hbn")
            c_himeno "Haha! Wait till I accept the offers and become the face of high brands!!"
    show screen cexp("hph", "hea", "hms", "hbn")
    """{i}She opened one of the offers.{/i}

    {i}It was a request from guzzi.{/i}

    {i}A really well known brand by basically everyone.{/i}"""

    menu:
        "{i}But wasn't the official website guzzi.com and not guzzi_official.com?{/i}"

        "Hey… some of these don't look right.":
            playerName "Hey… some of these don't look right."
            $ ptsh2 += 1
            show screen cexp("hph", "hel", "hmt", "hbn")
            c_himeno "What do you mean?"

        "You got a request from a luxury brand? I find that a bit suspicious…":
            playerName "You got a request from a luxury brand? I find that a bit suspicious…"
            show screen cexp("hph", "hel", "hmf", "hbn")
            c_himeno "Of course!"
            c_himeno "What do you mean?!"

    playerName "I'm just saying…"
    show screen cexp("hph", "hea", "hmn", "hbn")
    """{i}Himeno pouts at me and opens the link anyways.{/i}

    {i}The website opens up to a section where you enter your bank details.{/i}"""

    c_himeno "What? I thought they were going to send a free item for me to advertise."
    c_himeno "Well, whatever. I guess it'll guarantee that we'll come back later."
    show screen cexp("hph", "hel", "hmn", "hbn")
    playerName "Wait"
    show screen cexp("hph", "hel", "hmt", "hbn")
    c_himeno "Huh?"
    show screen cexp("hph", "hel", "hml", "hbn")

    menu:
        c_himeno "What's wrong?"
        "Don't type in your details while I'm next to you!":
            playerName "Don't type in your details while I'm next to you!"
            show screen cexp("hph", "hea", "hml", "hbn")
            c_himeno "Oh! Right! Well. It's not like I mind anyways"

        "I feel like we should check these.":
            playerName "I feel like we should check these."
            $ ptsh2 += 1
            show screen cexp("hph", "hea", "hmt", "hbn")
            c_himeno "How?"
    
    play sound phone_jingle

    c_himeno "Oh, an email."
    show screen cexp("hph", "hea", "hmt", "hbs")
    c_himeno """Eh?! 
    It says my bank account got compromised…"""
    show screen cexp("hph", "hel", "hmt", "hbs")
    c_himeno "To claim my account back I have to log back in."
    show screen cexp("hph", "hea", "hmf", "hbs")
    menu:
        c_himeno "..."
        "you should check the link":
            show screen cexp("hph", "hel", "hmn", "hbs")
            $ ptsh2 += 1
            playerName "Himeno, I think you should check them before you do anything."
            playerName "This is super sus."
            show screen cexp("hph", "hea", "hmf", "hbs")
            c_himeno "Wahhhh ! What should I do…"

            playerName """I’ll go grab us a drink. Just wait for me.

            Just wait for me."""

        "I’ll go grab us some banana milk.":
            show screen cexp("hph", "hel", "hmn", "hbs")
            playerName "Call me back if you need anything, I’ll go grab us some banana milk."
            show screen cexp("hph", "heb", "hml", "hbs")
            c_himeno "Okay ~ It’ll be done in a jiffy."
    show screen cexp("hpw", "hel", "hml", "hbn")
    c_himeno "Wait! Could you get me an ice tea?"
    playerName "Okay"
    hide screen cexp
    scene hallway day with fade

    if ptsh2 > 2:
        jump HGE
    else: 
        jump HB2
        
label HB2:
    """{i}Hmm...{/i}

    {i}This is so weird.{/i}"""
    narrateur "You feel your phone vibrate while you pick up the ice tea and banana milk."

    call phone_start(usrh, "10:12") 
    call message_start(tph, "Come back! I'm thirsty!!") 
    call reply_message("Okay okay!") 
    call message(tph, "I sent the email!") 
    call message(tph, "It should be okay now") 
    call message(tph, "I just had to send my bank account details.")
    call phone_end(False)

    scene black with fade
    narrateur "A few weeks later..."
    """{i}...{/i}

    {i}Himeno just stopped coming to school.{/i}

    {i}What's more concerning is that a bunch of adults came in our class to ask about her whereabouts.{/i}

    {i}I should pay her a visit.{/i}"""

    narrateur "You drop by her place..."

    """{i}Huh??? {/i}

    {i}Why are there people taking out the furniture??{/i}"""

    narrateur "You notice a crowd nearby screaming her name."

    """{i}Are they fans?{/i}

    {i}... {/i}

    {i}They seem a bit angry for fans...{/i}"""

    narrateur "You look around you to see if you can see Himeno but she is nowhere to be found."

    """{i}...{/i}

    {i}I'm going to get something to eat before going home.{/i}"""

    narrateur "You go to the nearest convenient store and buy a salmon onigiri, a japanese riceball sandwiches."

    """{i}Crap.{/i}

    {i}I forgot my wallet.{/i}"""

    narrateur "You look at the cashier."
    scene HB2 with fade
    "{i}...{/i}"

    c_himeno """???
    
    Ah!?? [playerName]?! N-no! Don't look at me!"""

    playerName "Himeno! What happened?"
    
    c_himeno """They took everything! My money, my home and my life.
    
    Daddy got mad at me and kicked me out.
    
    I don't know if he will ever forgive me..."""

    """{i}Tears start forming in her tired eyes.{/i}
    
    {i}I never thought that I would see Himeno in this state.{/i}"""

    window hide
    pause
    jump game_over

label HGE:
    """{i}Hmm...{/i}

    {i}This is so weird.{/i}

    {i}I'm getting the feeling that I should make sure that she doesn't do anything.{/i}"""
    
    narrateur "You feel your phone vibrate while you pick up the ice tea and banana milk."
    call phone_start(usrh, "10:12") 
    call message_start(tph, "Come back! I'm thirsty!!") 
    call reply_message("Okay okay!") 
    pause
    call phone_end(False)
    scene classroom day

    pause 1
    show screen cexp("hph", "hea", "hmn", "hbn")
    c_himeno "You were right, this website's a scam."
    show screen cexp("hph", "hea", "hmt", "hbn")
    c_himeno "Even the email is fake."
    show screen cexp("hph", "hea", "hmf", "hbn")
    c_himeno "Imagine if I did send an email..."
    show screen cexp("hph", "hea", "hmn", "hbn")
    c_himeno "Well, let's verify these requests."
    c_himeno "..."
    show screen cexp("hph", "hea", "hms", "hbn")
    playerName "Look, most of these are fake but there are some that seem legit!"
    hide screen cexp

    scene black with fade

    """{i}...{/i}

    {i}It's been 2 weeks since I spoke to Himeno about her offers.{/i}

    {i}In the end, some requests were verified and real.{/i}

    {i}Himeno quickly picked up modeling and got famous super fast.{/i}
    
    {i}With the modeling and sponsors that she managed to get, Himeno started making a lot of money.{/i}

    {i}Despite that, she still came to school, surely to keep me company...{/i}"""

    c_himeno "[playerName]!"
    scene HGE with fade
    c_himeno """Focus!
    
    We need to finish this photoshoot tonight."""

    playerName "Okay!"
    """{i}...{/i}

    {i}She's really made for the public eye.{/i}"""

    window hide
    pause
    jump happy_ending