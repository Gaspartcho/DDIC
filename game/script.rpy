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
    play music MisteriousMan_theme fadein 1.0 loop

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
        
        Tout d'abord, merci d'avoir installé ce petit jeu...
        
        Pour des raisons personnelles, je préfère te cacher mon identité pour l'instant.
        
        Sache juste que nous nous reverons pendant ton aventure.

        Juste de temps en temps... Quand je me sentirais seul...

        Au fait, on m'a demandé de te poser une question avant que je puisse te laisser passer:

        Selon toi, comment faire pour développer ou entretenir des relations saines sur internet?

        Réfléchis bien.
        
        C'est tout pour moi. A bientôt.
        
        ;)"""

        stop music fadeout 1.0

        narrateur """Préparation pour la première utilisation du programme...

        Erreur: Aucun nom d'utilisateur enregistré."""

        call name_choose
    
        narrateur """Initialisation du programme pour le joueur \"%(playerName)s\":
            
        Terminé!"""

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
    scene bedroom with fade
    call phone_start(usraf, "21:30")

    call message_start(tpa, "Bienvenue à l'école X ! Je suis {b}Akane Kousei{/b}, la déléguée de classe. Si tu as des questions, n'hésite pas à les poser soit à tes camarades, soit aux enseignants, ou tu peux venir me voir. Même si tu nous as rejoints très tard dans l'année, nous t’accueillons toujours à bras ouverts :)")
    call message_img(tpa, "Au fait, ça c'est moi!", "images/instagram/A1_insta.png")
    call message(tpa, "Comme tu arrives en millieu d'année, je me doute bien que ça peu être difficile, mais tu peux compter sur moi!")
    pause 1.0

    label choiceMaking_WAY: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Merci! Je vais essayer d'être sage :)","choiceMaking_WAY.choice1","Merci! Je te trouve très belle, ce qui est naturel pour une déléguée!","choiceMaking_WAY.choice2")

        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Merci! Je vais essayer d'être sage :)") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpa, "Haha ! Si tu veux, je t'enverrai par e-mail ce qu'on a fait depuis le début de l'année dans nos cours en commun^^")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Merci! Je te trouve très belle, ce qui est naturel pour une déléguée!")
            call message(tpa, "Ahh... Merci beaucoup ^^")
            jump .aftermenu
            
        label .aftermenu:

    call message(tpa, "Quoi qu'il en soit, envoie-moi un SMS dès que t'as besoin de quoi que ce soit et je te répondrai le plus vite possible, je suis dispo presque tout le temps.")
    call message(tpa, "Ah euh... Ça donne probablement l'impression que je ne fais pas mon travail de déléguée... Mais il faut que je te prévienne")
    call message(tpa, "Il y a cette fille dont je te conseille de pas t'approcher. Elle juge très facilement les gens et tu ne passeras pas un bon moment avec elle.")
    
    label choiceMaking_ST: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Ah... Qu'a-t-elle fait ?","choiceMaking_ST.choice1","À quoi ressemble-t-elle?","choiceMaking_ST.choice2")

        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "Ah... Qu'a-t-elle fait ?")
            call message(tpa, "Elle aime se moquer de moi... de tout le monde en fait... je ne sais pas pourquoi.")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "À quoi ressemble-t-elle?")
            jump .aftermenu
            
        label .aftermenu:

    call message_img(tpa, "Tiens", "images/instagram/H1_insta.png")
    call message(tpa, "Elle s'appelle {b}Himeno Yuzu{/b}. Je ne veux pas que tu en parles, ce serait gênant si les gens savaient que la déléguée se fait harceler. Haha.")
    call message(tpa, "Bon, oublies tout ça. Il n'y a aucune raison pour que tu passe un mauvais moment ici.")
    call message(tpa, "Oh! Mes parents m'appellent. Je te verrai demain :)")
    call reply_message("A demain.")
    call phone_end # this one puts away the phone!

    narrateur """Il est tard...

    Vous n'arrivez pas à vous endormir...

    Plutôt que d'essayer de lire un livre, vous décidez de faire connaissances avec d'autres membres de la classe:"""

    call phone_start(usrh, "22:13")
    label choiceMaking_LUV: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("heyy~ T'es magnifique!","choiceMaking_LUV.choice1","Yo, la personne la pluuuuus gentille du lycée","choiceMaking_LUV.choice2")
        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "heyy~ T'es magnifique!")
            call message(tph, "HAHA! Bien sûr que je le suis!!")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Yo, la personne la pluuuuus gentille du lycée")
            call message(tph, "La pire ici est cette petite frimeuse rose.")
            jump .aftermenu
        label .aftermenu:
    call message(tph, "Je suis la plus intelligente, la plus belle et la meilleure de toutes !")
    call message(tph, "Mais pourtant, je n'ai pas les meilleures notes et c'est super énervant.")
    call message(tph, "Cette pourrie-gâtée de cheveux roses est toujours la première.")
    call message(tph, "Et il y a aussi la cette déléguée qui fait constament sa cheffe")
    call message(tph, "Je te jure c'est parce qu'elles trichent.")
    call message(tph, "...")
    call message(tph, "Je devrais faire pareil.")
    label choiceMaking_CH: 
        call screen phone_reply("Tu vas vraiment faire ça ?","choiceMaking_CH.choice1","Je suis sûr que si tu essayes de toutes tes forces, tu seras la meilleure","choiceMaking_CH.choice2")
        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "Tu vas vraiment faire ça ?")
            call message(tph, "ui")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je suis sûr que si tu essayes de toutes tes forces, tu seras la meilleure")
            call message(tph, "C'est ça ouai... Pourquoi je devrais travailler {i}moi{/i} alors que je suis sure que tout le monde triche ici")
            call reply_message("...")
            jump .aftermenu
        label .aftermenu:
    call message(tph, "Ah ! Une de mes copines m'appelle.")
    call message(tph, "J’espère que je ne te manquerai pas trop <3")
    call phone_end

    """{i}...
    
    {i}Je devrais vraiment dormir maintenant."""
    
    jump scene_2

label scene_2:
    scene classroom day with Fade(1.0, 2.0, 1.0)

    narrateur "Le lendemain, alors que tu allais à l'école, tu reçois un message d'un compte instargam inconnu:"

    call phone_start("REAL_BUISNESS", "08:02")
    call message_start("REAL_BUISNESS", "Salut [playerName], veux-tu faire un appel vidéo gratuit? Trouves-moi ici http://cunscam.com/xxx xoxo")
    pause 2.0
    window show
    "???" "Je ne cliquerais pas dessus si j'étais toi."
    call phone_end(False)

    show screen cexp("apc", "ael", "amn", "abn")

    menu:
        c_akane "Tu devrais être prudent avec ceux-là. Ils ont tendance à te gâcher la vie."

        "Tu parles d'expérience ?":
            playerName "Tu parles d'expérience ?"
            show screen cexp("apc", "aeb", "ams", "abn")
            c_akane "Peut-être"

        "J'allais le supprimer de toute façon.":
            playerName "J'allais le supprimer de toute façon."
            c_akane "..."
            show screen cexp("apc", "ael", "ams", "abn")
            c_akane "... Mouai ..."
    
    show screen cexp("apr", "ael", "ams", "abn")
    c_akane "Tu semble nouveau ici."
    show screen cexp("apc", "aeb", "ams", "abn")
    c_akane "Bienvenue dans notre classe."
    playerName "On s'est déjà rencontrés non? Tu as mon compte instargam."
    show screen cexp("apc", "ael", "amt", "abn")
    c_akane """Ah bon? Je m'en souviens pas.

    Peut-être que tu m'as confondu avec quelqu'un d'autre."""

    show screen cexp("apr", "aeb", "ams", "abn")
    
    """{i}...{/i}

    {i}C'est étrange{/i}

    {i}Je suis presque sûr que c'est la fille qui m'a envoyé un message hier soir.{/i}"""
    show screen cexp("bpb", "beb", "bms", "bbn") 
    narrateur "Tu tournes la tête en te sentant mal à l'aise et aperçoit une fille endormie sur sa table avec son téléphone allumé."
    narrateur "Tu t'approches du bureau et jette un coup d'œil à son téléphone."

    """{i}...{/i}

    {i}Ça ne serait pas ma conversation avec Akane d'hier soir?{/i}

    {i}...{/i}"""

    narrateur "Tu tends la main pour essayer de la réveiller... "
    play audio class_bell
    narrateur """... mais la cloche de l'école sonne.
    
    Tu retournes à ta place a coté de Akane."""
    show screen cexp("apr", "aeb", "ams", "abn")
    playerName "Qui est-ce ?"
    show screen cexp("apr", "ael", "amt", "abn")
    c_akane "C'est {b}Bomi Park{/b}."
    show screen cexp("apr", "ael", "ams", "abn")
    c_akane "Elle est en tête du classement de notre école."
    show screen cexp("apr", "aeb", "ams", "abn")
    c_akane "C'est assez impressionnant pour une première."
    
    pause 1.0
    "{i}...{/i}"
    "{i}Je devrais plus me concentrer en cours.{/i}"
    hide screen cexp with fade
    narrateur "Alors que vous essayez d'écouter le cours, vous sentez que vos paupères sont de plus en plus lourdes..."
    scene black with Fade(3.0, 0, 1.0)
    narrateur "{cps=20}Vous vous endormez.{/cps}"

    pause 2.0
    play music MisteriousMan_theme fadein 1.0 loop

    c_mysteriousMan """...
    
    Ah, on y est enfin...
    
    Le moment tant attendu où tu poura choisir l'une de ces trois filles...

    Je pense que tu as du comprendre quels sont leur problèmes...
    
    Laquelle tu vas essayer d'aider?"""

    show screen cexp("apr", "ael", "ams", "abn") with fade
    c_mysteriousMan "Akane la déléguée de la classe?"
    hide akane choose

    show screen cexp("bpf", "bel", "bmh", "bbn") with fade
    c_mysteriousMan "Bomi la meilleure élève de l'école?"
    hide bomi choose

    show screen cexp("hph", "hel", "hms", "hbn") with fade
    c_mysteriousMan "Ou Himemo, la rebelle du lycée?"
    hide screen cexp with fade
    c_mysteriousMan """En tout cas, choisis bien.
    
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
    c_mysteriousMan """Bien. Bonne chance pour la suite, on se revéra à la fin...

    Allé, réveille-toi, c'est l'heure de la fin des cours.
    
    ;)"""

    stop music fadeout 1.5
    narrateur "Vous vous réveillez."
    scene classroom late with fade 
    
    narrateur """L'horlogle affcihe \"17:06\".
    
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
    
    Tu peut partir tu sais?
    
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