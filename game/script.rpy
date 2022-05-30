label splashscreen:
    scene black
    with Pause(1)

    show text "{color=#fff}NSI122 Presents...{/color}" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    stop music

    play music "audio/musics/Ambiant_misterious.mp3" fadein 1.0 loop

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
        
        Tout d'abord, merci d'avoir installé ce programme...
        
        Pour des raisons personnelles, je préfère te cacher mon identité pour l'instant.
        
        Sache juste que nous nous reverons pendant ton aventure.

        Au fait, on m'a demandé de te poser une question avant que je puisse te laisser passer:

        Selon toi, comment faire pour développer ou entretenir des relations sur internet?

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
    scene bedroom_sleep with fade

    call phone_start("Kousei.Akane", "21:30")
    define ta = "Akane"

    call message_start(ta, "Bienvenue à l'école X ! Je suis {b}Akane Kousei{/b}, la déléguée de classe. Si tu as une question, n'hésite pas à venir me voir. Même si tu nous as rejoint très tard dans l'année, je suis sure que toute la classe t'accueillera à bras ouverts :)")
    call message_img(ta, "Au fait, ça c'est moi!", "images/instagram/A1_insta.jpg")
    call message(ta, "Comme tu arrives en millieu d'année, je me doute bien que ça peu être difficile, mais tu peux compter sur moi!")
    pause 1.0

    label choiceMaking_WAY: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Merci! Je vais essayer d'être sage :)","choiceMaking_WAY.choice1","Merci! Je te trouve très belle, ce qui est naturel pour une déléguée!","choiceMaking_WAY.choice2")

        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Merci! Je vais essayer d'être sage :)") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(ta, "Haha ! Si tu veux, je t'enverrai par e-mail ce qu'on a fait depuis le début de l'année dans nos cours en commun^^")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Merci! Je te trouve très belle, ce qui est naturel pour une déléguée!")
            call message(ta, "Ahh… Merci beaucoup ^^")
            jump .aftermenu
            
        label .aftermenu:

    call message(ta, "Quoi qu'il en soit, envoies-moi un SMS dès que t'as besoin de quoi que ce soit et je te répondrai le plus vite possible, je suis dispo presque tout le temps.")
    call message(ta, "Ah euh... Ça donne probablement l'impression que je ne fais pas mon travail de déléguée... Mais il faut que je te prévienne")
    call message(ta, "Il y a cette fille dont je te conseille de pas t'approcher. Elle juge très facilement les gens et tu ne passeras pas un bon moment avec elle.")
    
    label choiceMaking_ST: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Ah… Qu'a-t-elle fait ?","choiceMaking_ST.choice1","À quoi ressemble-t-elle?","choiceMaking_ST.choice2")

        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "Ah… Qu'a-t-elle fait ?")
            call message(ta, "Elle aime se moquer de moi... de tout le monde en fait... je ne sais pas pourquoi.")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "À quoi ressemble-t-elle?")
            jump .aftermenu
            
        label .aftermenu:

    call message_img(ta, "Tiens", "images/instagram/H1_insta.png")
    call message(ta, "Elle s'appelle {b}Himeno Yuzu{/b}. Mais garde ça pour toi s'il te plais: ce serait gênant si les gens savaient que la déléguée se fait harceler. Haha.")
    call message(ta, "Bon, oublies tout ça. Il n'y a aucune raison pour que tu passe un mauvais moment ici.")
    call message(ta, "Oh! Mes parents m'appellent. Je te verrai demain :)")
    call reply_message("A demain.")
    call phone_end # this one puts away the phone!

    narrateur """Il est tard...

    Vous n'arrivez pas à vous endormir...

    Plutôt que d'essayer de lire un livre, vous décidez de faire connaissances avec d'autres membres de la classe:"""

    call phone_start("yuzu.himi", "22:13")
    define th = "Himeno"
    label choiceMaking_LUV: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("heyy~ T'es magnifique!","choiceMaking_LUV.choice1","Yo, la personne la pluuuuus gentille du lycée","choiceMaking_LUV.choice2")
        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "heyy~ T'es magnifique!")
            call message(th, "HAHA! Bien sûr que je le suis!!")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Yo, la personne la pluuuuus gentille du lycée")
            call message(th, "La pire ici est cette petite frimeuse rose.")
            jump .aftermenu
        label .aftermenu:
    call message(th, "Je suis la plus intelligente, la plus belle et la meilleure de toutes !")
    call message(th, "Mais pourtant, je n'ai pas les meilleures notes et c'est super énervant.")
    call message(th, "Cette pourrie-gâtée de cheveux roses est toujours la première.")
    call message(th, "Et il y a aussi la cette déléguée qui fait constament sa cheffe")
    call message(th, "Je te jure c'est parce qu’elles trichent.")
    call message(th, "...")
    call message(th, "Je devrais le faire.")
    label choiceMaking_CH: 
        call screen phone_reply("Tu vas vraiment faire ça ?","choiceMaking_CH.choice1","Je suis sûr que si tu essayes de toutes tes forces, tu seras la meilleure","choiceMaking_CH.choice2")
        label .choice1:    
            call phone_after_menu
            call message_start(playerName, "Tu vas vraiment faire ça ?")
            call message(th, "ui")
            jump .aftermenu
            
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Je suis sûr que si tu essayes de toutes tes forces, tu seras la meilleure")
            call message(th, "C'est ça ouai... Pourquoi je devrais travailler {i}moi{/i} alors que je suis sure que tout le monde triche ici")
            call reply_message("...")
            jump .aftermenu
        label .aftermenu:
    call message(th, "Ah ! Une de mes copines m'appelle.")
    call message(th, "Allé salut. Essaie de ne pas me manquer <3")
    call phone_end

    """{i}...
    
    {i}Je devrais vraiment dormir maintenant."""
    
    jump scene_2

label scene_2:
    scene classroom with Fade(1.0, 2.0, 1.0)

    narrateur "Le lendemain, alors que tu allais à l'école, tu reçois un message d'un compte instargam inconnu:"

    call phone_start("REAL_BUISNESS", "08:02")
    call message_start("REAL_BUISNESS", "Salut [playerName], veux-tu faire un appel vidéo gratuit? Trouves-moi ici http://cunscam.com/xxx xoxo")
    pause 2.0
    window show
    "???" "Je ne cliquerais pas dessus si j'étais toi."
    call phone_end(False)
    menu:
        c_akane "Tu devrais être prudent avec ceux-là. Ils ont tendance à te gâcher la vie."

        "Tu parles d’expérience ?":
            c_akane "Peut-être"

        "J'allais le supprimer de toute façon.":
            c_akane "..."
            c_akane "... Mouai ..."
    
    c_akane "Tu semble nouveau ici."
    c_akane "Bienvenue dans notre classe."
    playerName "On s’est déjà rencontrés non? Tu as mon compte instargam."
    c_akane """Ah bon? Je m’en souviens pas.

    Peut-être que tu m’as confondu avec quelqu'un d'autre."""

    ## akane part du champ
    
    """{i}...{/i}

    {i}C'est étrange{/i}

    {i}Je suis presque sûr que c'est la fille qui m'a envoyé un message hier soir.{/i}"""

    narrateur "Tu tournes la tête en te sentant mal à l'aise et aperçoit une fille étendue sur sa table avec son téléphone allumé."
    narrateur "Tu t'approches du bureau et jette un coup d'œil à son téléphone."

    """{i}...{/i}

    {i}Ça serait pas ma conversation avec Akane d'hier soir?{/i}

    {i}...{/i}"""

    narrateur "Tu tends la main pour essayer de la réveiller... "
    play audio "audio/sound_effects/School Bell.mp3"
    narrateur """... mais la cloche de l'école sonne.
    
    Tu retournes à ta place a coté de Akane."""

    playerName "Qui est-ce ?"
    c_akane "C'est {b}Bomi Park{/b}."
    c_akane "Elle est en tête du classement de notre école."
    c_akane "C'est assez impressionnant pour une première."
    
    pause 1.0
    "{i}...{/i}"
    "{i}Je devrais plus me concentrer en cours.{/i}"
    narrateur "Alors que vous essayez d'écouter le cours, vous sentez que vos paupères sont de plus en plus lourdes..."
    scene black with Fade(3.0, 0, 1.0)
    narrateur "{cps=20}Vous vous endormez.{/cps}"

    pause 3.0
    play music "audio/musics/Ambiant_misterious.mp3" fadein 1.0 loop

    c_mysteriousMan """...
    
    Ah, on y est enfin...
    
    Le moment tant attendu où tu poura choisir entre ces trois filles...
    
    Laquelle tu vas essayer d'aider?"""

    show akane choose at image_choose_path with fade
    c_mysteriousMan "Akane la déléguée de la classe?"

    show bomi choose at image_choose_path with fade
    c_mysteriousMan "Bomi la meilleure élève de l'école?"

    show himeno choose at image_choose_path with fade
    c_mysteriousMan "Ou Himemo, la rebelle du lycée?"
    hide insta himeno 1 with fade

    c_mysteriousMan """En tout cas, choisis bien.
    
    Tes décisions ont une importance ici."""

    menu:
        "{i}Je choisis...{/i}"

        "Akane":
            $ road = "1"
        "Bomi":
            $ road = "2"
        "Himeno":
            $ road = "3"
    
    narrateur "[road]"
    
    c_mysteriousMan """Bien. Bonne chance pour la suite, on se revéra à la fin...

    Allé, réveille-toi, c'est l'heure de la fin des cours.
    
    ;)"""

    stop music fadeout 1.5
    narrateur "Vous vous réveillez."
    scene classroom with fade
    
    narrateur """L'horlogle affcihe \"17:06\".
    
    Il est tard, vous avez dormis toute la journée."""

    if road == "1":
        jump route_A
    if road == "2":
        jump route_B
    if road == "3":
        jump route_H

    return