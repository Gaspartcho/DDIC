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
            c_akane "Pardon?"

        "Je peux attendre un peu plus longtemps ?":
            playerName "..."
            playerName "Est-ce que tu pourais me laisser un peut plus de temps?"
            playerName "Histoire que je fasse bien connaissance avec tout le monde..."
    show screen cexp("apr", "ael", "amn", "abn", h=h_mid)
    c_akane "Bon, si tu n'as pas envie de le faire, je vais m'en occuper" 
    show screen cexp("apr", "aeb", "ams", "abn", h=h_mid)
    c_akane "Je dois y aller, on se revéras plus tard."
    hide screen cexp
    
    if ptsc1 >= 4:
        jump RAF1
    else:
        jump RAB1

label RAB1:
    "{i}Bon, et puis zut! Qu'est-ce qui pourai mal se passer de toute façon?"
    scene black with fade

    """{i}Ça fait une semaine que je suis arrivé à l'école.{/i}

    {i}J'ai appris les noms de tout le monde, mais je ne me suis pas fait de véritables amis.{/i}

    {i}J'ai décidé d'envoyer le \"cadeau\" d'Akane à Himeno. {/i}

    ...

    ..."""
    scene classroom late with fade 

    """{i}Cela fait trois jours que j'ai envoyé ce lien à Himeno.{/i}

    {i}Je me demande ce que c'était, mais je passe à autre chose et je continue ma journée.{/i}"""
    "Prof" "Les deux solutions à ces fonctions sont-"
    "???" "Excusez-moi. Est-ce que Akane Kousei est là ?"
    show screen cexp("apc", "aea", "amn", "abn", h=h_mid)
    playerName "Akane, qu'est-ce qui se passe?"
    c_akane "..."

    "{i}Elle semble pâle mais calme.{/i}"
    "Prof" "Qui êtes-vous? Ceci est une salle de classe. Vous ne pouvez pas simplement rentrer comme ça!"
    "Mr. Aki" """Je suis le détective Aki. Je suis là pour une enquête sur une affaire impliquant Akane Kousei.

    Mademoiselle Kousei, veuillez sortir et venir avec moi."""
    show screen cexp("apc", "aea", "ams", "abn", h=h_mid)
    pause
    hide screen cexp
    scene black with fade
    """{i}On a appris par Himeno que Akane était responsable de vol et de diverses arnaques en ligne.
    
    {i}Himeno étais l'une des victimes, elle avais perdu beaucoup d'argent à cause de ça.

    {i}Il faudrais qu'elle fasse plus attention à ce qu'elle achète.
    
    {i}Un an plus tard, Akane a été mise en procès.{/i}"""
    scene AB1 with fade
    "Juges" """Kousei Akane.

    Vous êtes accusé de vol contre la famille Yuzu.

    Vous plaidez coupable ?"""
    c_akane "Oui, messieurs."
    "{i}..."
    "{i}Je pense qu'Akane ne pourra jamais finir sa scolarité...{/i}"
    window hide
    pause

    jump game_over

label RAF1:
    define ptsc2 = 0
    scene bedroom with fade
    narrateur "Quelques jours plus tard..."
    call phone_start(usrc, "20:36") from _call_phone_start_5
    call message_start (tpa, "Bonjour, [playerName]. Je sais que ça fait une semaine que je t'ai dit d'envoyer ce lien à Himeno, mais au final t'as plus besoin de le faire.") from _call_message_start_19
    call reply_message ("Ok...") from _call_reply_message_11
    call message (tpa, "Au fait, Je sais pas si tu as remarqué, mais il y a quelqu'un en ligne qui se fait passer pour moi.") from _call_message_58
    call message (tpa, "Il prend des photos de moi, vole mes photos de {b}mon{/b} compte et les publient comme les siennes.") from _call_message_59
    call message (tpa, "C'est légèrement inquiétant...") from _call_message_60

    pause
    window show
    "{i}Elle parle de Bomi?"
    window hide
    
    label choiceMaking_WGD:
        call screen phone_reply("Ca fait peur","choiceMaking_WGD.choice1","Tu devrais le dénoncer","choiceMaking_WGD.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_16
            call message_start(playerName, "Ca fait peur.") from _call_message_start_20
            call reply_message("Qu'est-ce que tu vas faire?") from _call_reply_message_12
            call message(tpa, "Non, pas vraiment. Je ne me sent pas menaçée à ce point.") from _call_message_61
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_17
            call message_start(playerName, "Tu devrais le dénoncer") from _call_message_start_21
            $ ptsc2 += 1
            call message(tpa, "C'est inutile, Ils ne feront sûrement rien") from _call_message_62
            call message(tpa, "Je ne peux même pas si je le voulais de toute façon") from _call_message_63
            call message(tpa, "Je n'ai aucune idée de qui il s'agit.") from _call_message_64

            jump .aftermenu
        label .aftermenu:
    
    pause
    window show
    "{i}..."
    window hide

    label choiceMaking_USP:
        call screen phone_reply("Tu devrais prendre des précautions","choiceMaking_USP.choice1","Tu as raison","choiceMaking_USP.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_18
            call message_start(playerName, "Tu devrais prendre des précautions.") from _call_message_start_22
            $ ptsa2 += 1
            call message(tpa, "Ok mais comment?") from _call_message_65
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_19
            call message_start(playerName, "Tu as raison, il n'y a aucune raison pour que cette personne ne devienne un danger pour toi...") from _call_message_start_23
            call message(tpa, "Bien sûr que j'ai raison.") from _call_message_66
            jump .aftermenu
        label .aftermenu:
    
    call message (tpa, "Je dois manger, salut.") from _call_message_67
    call phone_end from _call_phone_end_5

    "{i}..."
    "{i}Est-ce que je lui dit?"
    "{i}..."

    call phone_start (usrcf, "20:38") from _call_phone_start_6
    call message_start(tpa, " Bonjour, [playerName]!") from _call_message_start_24
    call message(tpa, "Comment vas-tu depuis la semaine dernière?") from _call_message_68
    call message(tpa, "J'espère que ça va.") from _call_message_69
    call reply_message("...") from _call_reply_message_13
    call reply_message("Bomi Park?") from _call_reply_message_14
    call message(tpa, "Quoi?") from _call_message_70
    call message(tpa, "Pourquoi mentionnes-tu son nom ?") from _call_message_71

    label choiceMaking_KUR:
        call screen phone_reply("Je sais qui tu es","choiceMaking_KUR.choice1","Non, rien...","choiceMaking_KUR.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_20
            $ ptsa2 += 1
            call message_start(playerName, "Je sais qui tu es.") from _call_message_start_25
            call message(tpa, "...") from _call_message_72
            call message(tpa, "Ne parle jamais de ça.") from _call_message_73
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_21
            call message_start(playerName, "Ah, rien. J'aimerais en savoir plus sur elle") from _call_message_start_26
            call reply_message("Elle semble être la plus forte de notre classe et j'aimerais savoir comment elle fait") from _call_reply_message_15
            call message(tpa, "Je pourais...") from _call_message_74
            call message(tpa, "Mais non.") from _call_message_75
            jump .aftermenu
        label .aftermenu:
    call phone_end from _call_phone_end_6

    "{i}..."
    "{i}Je devrais avertir Akane."

    call phone_start(usrc, "20:38") from _call_phone_start_7
    label choiceMaking_PBC:
        call screen phone_reply("Sois super prudente","choiceMaking_PBC.choice1","Je vais t'aider à te protéger","choiceMaking_PBC.choice2")
        label .choice1:
            call phone_after_menu from _call_phone_after_menu_22
            call message_start(playerName, "Akane. S'il te plaît, sois super prudente.") from _call_message_start_27
            call message(tpa, "Je le serai.") from _call_message_76
            call message(tpa, "Mais pourquoi tu t'inquiète, ce n'es pas grave tu sais.") from _call_message_77
            call message(tpa, "Juste un peut énervant...") from _call_message_78
            jump .aftermenu
        label .choice2:
            call phone_after_menu from _call_phone_after_menu_23
            $ ptsa2 += 1
            call message_start(playerName, "Akane, je vais t'aider à mettre en place des précautions.") from _call_message_start_28
            call reply_message("On devrait également le signaler pendant qu'on y est comme ça la situation ne deviendra pas incontrôlable.") from _call_reply_message_16
            call message(tpa, "Ok") from _call_message_79
            jump .aftermenu
        label .aftermenu:
    call phone_end from _call_phone_end_7
    "{i}...{/i}"
    if ptsa2 > 2:
        jump RAF
    else:
        jump RAB2

label RAB2:
    "{i}Une semaine plus tard, tu reçois une notification de ton tel et tu vois Himeno est live."

    c_himeno """Oh.

    Mon.

    Dieu.

    Akane a transfert d'ecole!

    Elle est maintenant à l'ecole Z.

    Venons lui dire au revoirs </3"""

    "{i}...

    Je devrais la chercher"
    
    "..."
    scene AB2 with fade
    playerName "Akane!"
    c_akane "Ah. [playerName]."
    playerName "Tu fais quoi?"
    c_akane "Je déménage."
    playerName "???"
    c_akane "Le faux Akane m'a déménage à l'école Z."
    playerName "Mais pourquoi tu ne fais rien?"
    c_akane """Mes parents ont déjà accepté. Je ne peux rien faire.

    au revoir, [playerName]."""

    window hide
    pause
    jump game_over

label RAF:
    scene blacks with fade
    "{i}J'ai rencontré Akane le lendemain à l'école."
    scene AGE with fade
    c_akane "Alors que veux-tu que je fasse ?"
    playerName "Alors..."
    """{i}J'ai expliqué à Akane les choses les plus élémentaires sur la façon de protéger son identité en ligne, mais elle semblait en savoir plus que moi.{/i}
    
    {i}Elle a fini par me guider pendant qu'elle mettait en place les précautions pour elle-même.{/i}"""
    c_akane """Merci de penser à moi.
    
    Aller, on rentre?"""

    window hide
    pause
    jump happy_ending


