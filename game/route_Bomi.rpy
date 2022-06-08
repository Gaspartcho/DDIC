label route_B1:
    define ptsb1 = 0

    "{i} Je devrais aller voir Bomi et lui demander pourquoi elle fais ça."
    "{i} ..."
    "{i} Sa chaise est déjà vide."
    narrateur "Après cette longue journée de cours, tu décides de rentrer chez toi et te coucher..."

    scene bedroom with fade
    pause 2
    "{i} ..."
    "{i} Je vais essayer de lui parler quand même"
    "{i}Je me demande si elle a un compte instargam..."
    "{i}A elle, je veut dire..."
    "{i}Ah! je l'ai trouvé...{/i}"

    #Il ya a un bug ici, jredais pas pourquoi...
    call phone_start(usrb, "20:23")
    label choiceMaking_HID: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Hey Bomi, pourquoi tu te caches?","choiceMaking_HID.choice1","Hé bien madame la déléguée, tu n'as pas du tout la même tête en vrai.","choiceMaking_HID.choice2")
        
        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Hey Bomi, pourquoi tu te caches?") # whenever you put the sender name to be playerName it is the player characters own message!
            $ ptsb1 += 1
            call message(tpb, "Ah, tu m'as trouvé?")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "Hé bien madame la déléguée, tu n'as pas du tout la même tête en vrai.")
            call message(tpb, "...")
            jump .aftermenu
        label .aftermenu:
    
    call message(tpb, "Je suis désollé de t'avoir menti")
    call message(tpb, "J'admire beaucoup Akane. Elle est intelligente, elle est belle, elle est confiante...")
    call message(tpb, "Mon seul atout est mon niveau scolaire.")
    call message(tpb, "Comparé à elle, ce n'est pas grand chose.")
    call message(tpb, "C'est normal de vouloir être comme elle...")

    label choiceMaking_CHA: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("Je pense que chacun a son charme.","choiceMaking_CHA.choice1","T'as pas tort.","choiceMaking_CHA.choice2")
        label .choice1:
            $ ptsb1 += 1
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "Je pense que chacun a son charme.") # whenever you put the sender name to be playerName it is the player characters own message!
            call reply_message("Je suis sûr que tu es tout aussi adorable")
            call message(tpb, "Peut-être.")
            jump .aftermenu
        label .choice2:
            call phone_after_menu
            call message_start(playerName, "T'as pas tort.")
            call reply_message("Elle est impressionnante")
            call message(tpb, "...")
            jump .aftermenu
        label .aftermenu:

    call message(tpb, "De toute façon, je ne suis pas la seule à l'admirer. Tant de gens voudraient être à sa place ou avec elle.")
    call message(tpb, "...")
    call message(tpb, "Est-ce que je devrais me coiffer ?")
    call reply_message("Te coiffer?")
    call message(tpb, "Genre changer mon style...")
    call message(tpb, "Quelque chose qui me correspondrais plus")

    label choiceMaking_HAI: # Use this template eatch time u want to make a phone menu
        call screen phone_reply("je ne sais pas","choiceMaking_HAI.choice1","J'aime ta coupe.","choiceMaking_HAI.choice2")
        label .choice1:    
            call phone_after_menu # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
            call message_start(playerName, "je ne sais pas, je ne me souviens plus de ta coiffure actuelle.") # whenever you put the sender name to be playerName it is the player characters own message!
            call message(tpb, "...")
            jump .aftermenu
        label .choice2:
            $ ptsb1 += 1
            call phone_after_menu
            call message_start(playerName, "J'aime ta coupe.")
            call reply_message("Je ne pense pas que tu devrais les couper pour l'instant")
            call message(tpb, "Oui mais quand même...")
            call message(tpb, "...")
            jump .aftermenu
        label .aftermenu:

    call message(tpb, "à demain.")
    call phone_end
    "{i} Un peut bizarre... Mais elle à l'air gentille"
    "{i} J'espère juste qu'elle ne fera rien de stupide..."
    c_mysteriousMan "FORESHAOWING!!!"
    scene black with fade
    narrateur "Le lendemain..."
    scene classroom day with fade
    pause 2.0
    show screen cexp("bpbb", "beb", "bmh", "bbn", p=p_center, h=h_down)
    c_bomi "Bonjour [playerName]."
    show screen cexp("bpfb", "bel", "bmn", "bbn", p=p_center, h=h_down)
    c_bomi "..."
    show screen cexp("bpbb", "bel", "bmt", "bbn", p=p_center, h=h_down)

    menu:
        c_bomi "Qu'en penses-tu?"
        "Je pense que c'est superbe!":
            playerName "Je pense que c'est superbe!"
            show screen cexp("bpbb", "beb", "bmh", "bbn", p=p_center, h=h_down)
            c_bomi "Vraiment? Je suis tellement heureuse!"
        
        "Tu m'as l'air familière...":
            $ ptsb1 += 1
            playerName "Tu m'as l'air familière..."
            show screen cexp("bpfb", "bea", "bms", "bbs", p=p_center, h=h_down)
            c_bomi "Ah!? J-je, n-non..."

    c_himeno "Pfft t'as l'air ridicule"
    play sound camera_effect
    with Fade(0.1, 0.0, 0.5, color="#fff")
    show screen cexp("bpfb", "bel", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "E-eh!? A-attends !!"
    show screen cexp("bpfb", "beb", "bms", "bbs", p=p_center, h=h_down)
    c_bomi "Ne prends pas de photos!"
    narrateur "Himeno s'enfuit."
    show screen cexp("bpbb", "beb", "bms", "bbs", p=p_center, h=h_down)
    narrateur "Bomi essaie de la poursuivre et trébuche."
    show screen cexp("bpbb", "bea", "bms", "bbs", p=p_center, h=h_down)
    menu:
        narrateur "Tu l'aides à se relever"
        "Tu veux que je la poursuive ?":
            playerName "Tu veux que je la poursuive ?"
            $ ptsb1 += 1
            show screen cexp("bpbb", "bel", "bms", "bbs", p=p_center, h=h_down)
            c_bomi "..."

        "Je ne pense pas que les gens y prêteront attention de toute façon":
            playerName "Je ne pense pas que les gens y prêteront attention de toute façon"
            show screen cexp("bpbb", "beb", "bmh", "bbs", p=p_center, h=h_down)
            c_bomi "Ahahah... Tu as surement raison"
    show screen cexp("bpbb", "bea", "bms", "bbs", p=p_center, h=h_down)
    c_bomi "..."
    c_bomi "Je ne veut pas que ça circule."
    show screen cexp("bpbb", "bea", "bms", "bbs", p=p_left, h=h_down)
    menu:
        c_akane "Que se passe t-il ici?"
        "Tout va bien.":
            playerName "Tout va bien."
            c_akane "Si tu le dis."
        
        "Quelqu'un a pris une photo d'elle!":
            $ ptsb1 += 1
            playerName "Quelqu'un a pris une photo d'elle!"
            c_akane "Ah. Je pense avoir une idée de qui tu parles."
            c_akane "Je ne peux pas vraiment faire quoi que ce soit puisque sa famille a beaucoup d'influence sur l'école."
    show screen cexp("bpbb", "bel", "bmt", "bbs", p=p_left, h=h_down)
    c_bomi "[playerName]!"
    scene hallway day with fade
    show screen cexp("bpbb", "bea", "bmt", "bbs", p=p_center, h=h_down)
    c_bomi "C'est la honte!"
    show screen cexp("bpbb", "bel", "bms", "bbs", p=p_center, h=h_down)
    c_bomi "Si cette photo sort, je ne pense pas que je m'en remettrais..."

    menu:
        "Tu es superbe pourtant.":
            show screen cexp("bpfb", "bel", "bmh", "bbs", p=p_center, h=h_down)
            playerName "Tu es superbe pourtant."
            playerName "Je pense que les extensions etaient une bonne idee"
        
        "Les cheveux bleus sont jolis mais ils ne te vont pas trop.":
            show screen cexp("bpfb", "bel", "bmn", "bbs", p=p_center, h=h_down)
            playerName "Les cheveux bleus sont jolis mais ils ne te vont pas trop."
            playerName "Viens. On va récupérer cette image et ça ira mieux."
    show screen cexp("bpbb", "bea", "bmn", "bbs", p=p_center, h=h_down)
    c_bomi "..."
    show screen cexp("bpbb", "bel", "bmt", "bbs", p=p_center, h=h_down)
    c_bomi "C'est pas grave."
    show screen cexp("bpbb", "beb", "bmh", "bbs", p=p_center, h=h_down)
    c_bomi "Retournons en classe."
    hide screen cexp
    scene black with fade 

    if ptsb1 >= 4:
        jump RBF1
    else:
        jump RBB1

label RBB1:
    scene BB1 with fade
    c_bomi """...

    Je ne lui ressemble pas du tout.

    Pourquoi?

    J'ai tout essayé...

    J'ai essayé de me couper les cheveux, d'ajouter des extensions, d'avoir des lentilles teintées...

    Rien ne marche.

    Comment faire pour lui ressembler?

    COMMENT FAIRE POUR LUI RESSEMBLER !?!

    Je n'en peut plus."""

    jump game_over

label RBF1:
    define ptsb2 = 0
    scene black with fade
    narrateur "Le lendemain."
    scene classroom day with fade

    "???" "Hey! [playerName]!"
    show screen cexp("bpb", "bel", "bmh", "bbn", p=p_center, h=h_down)
    c_bomi "J'ai retiré mes extensions."
    show screen cexp("bpf", "beb", "bmh", "bbs", p=p_center, h=h_down)
    c_bomi "Elles commençaient à devenir lourdes haha"
    show screen cexp("bpf", "bea", "bms", "bbs", p=p_center, h=h_down)
    menu:
        c_bomi "..."
        "Je suis sûr qu'elle ne l'a pas encore postée":
            show screen cexp("bpf", "bel", "bms", "bbs", p=p_center, h=h_down)
            playerName "Je suis sûr qu'elle ne l'a pas encore postée"
            
        "Allons chercher Himeno":
            show screen cexp("bpf", "bel", "bms", "bbs", p=p_center, h=h_down)
            playerName "Allons chercher Himeno"
            $ ptsb2 += 1
    show screen cexp("bpf", "bea", "bms", "bbs", p=p_center, h=h_down)
    c_bomi "..."
    show screen cexp("bpf", "bel", "bmt", "bbs", p=p_center, h=h_down)
    c_bomi "Je pense qu'elle est sur le toit en train de déjeuner et de prendre des photos pour Instagram."
    show screen cexp("bpf", "bel", "bms", "bbs", p=p_center, h=h_down)
    "{i} A-t-elle déjà posté?"
    narrateur """Tu sors ton tel pour vérifier.
    D'abord, tu regardes le compte de Bomi"""
    show screen cexp("bpf", "bea", "bms", "bbs")
    "{i}Wow..."
    "{i}Ces commentaires sont stupides et méchants..."
    "{i}Himeno n'a aucune pitié."
    "..."
    show screen cexp("bpb", "beb", "bms", "bbs", p=p_center, h=h_down)
    narrateur "Tu trouves la photo de Bomi avec ses extensions de cheveux, postée et virale."
    show screen cexp("bpb", "bel", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "Ah..."
    show screen cexp("bpb", "bea", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "J'espérais que tu n'allais pas le voir"
    show screen cexp("bpb", "beb", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "Je ne pensais pas que c'était si reconnaissable..."
    show screen cexp("bpb", "bel", "bms", "bbs", p=p_center, h=h_down)
    menu:
        "Tu devrais y repondre":
            playerName "Tu devrais y repondre"

        "N'y fais pas attention.":
            $ ptsb2 += 1
            playerName "N'y fais pas attention."
            playerName "On devrait signaler l'incident sur instar et à l'administration."
    show screen cexp("bpb", "bea", "bms", "bbs", p=p_center, h=h_down)
    c_bomi "..."
    playerName "Bon, allons voir Himeno."
    show screen cexp("bpb", "bel", "bmt", "bbs", p=p_center, h=h_down)
    c_bomi "Non!!" 
    show screen cexp("bpf", "bea", "bmt", "bbs", p=p_center, h=h_down)
    c_bomi "J-je veux dire qu'on ne devrait pas."
    show screen cexp("bpf", "bel", "bmt", "bbs", p=p_center, h=h_down)
    c_bomi "Ça deviendrait plus compliqué que voulu."
    show screen cexp("bpb", "bea", "bmt", "bbs", p=p_center, h=h_down)
    c_bomi "Ça passera... n'est-ce pas ?"
    show screen cexp("bpb", "bel", "bms", "bbs", p=p_center, h=h_down)

    menu:
        c_bomi "..."
        "Ouais. T'as juste à les ignorer et garder une preuve qu'on t'a envoyé de la haine.":
            $ ptsb2 += 1
            playerName "Ouais. T'as juste à les ignorer et garder une preuve qu'on t'a envoyé de la haine."
            playerName "Elle finira par payer de toute façon."

        "Defends-toi. ":
            playerName "Defends-toi. "
            playerName "Ils finiront par te croire."
            playerName "Himeno a ce qui lui arrive."
    show screen cexp("bpb", "bea", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "Oui mais..."
    show screen cexp("bpb", "beb", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "Je voudrais pas lui attirer de problèmes..."
    show screen cexp("bpb", "bel", "bms", "bbs", p=p_center, h=h_down)
    playerName "On dois lui faire comprendre que chaque actions a des conséquences!"
    show screen cexp("bpb", "bea", "bms", "bbs", p=p_center, h=h_down)
    c_bomi "..."
    playerName "Comment tu te sens?"
    show screen cexp("bpb", "bel", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "Mal."
    show screen cexp("bpb", "bea", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "C'est atroce."
    show screen cexp("bpb", "bel", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "J'ai l'impression que ces commentaires me hantent..."
    show screen cexp("bpb", "beb", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "Ils m'ont empêché de dormir hier soir."
    show screen cexp("bpb", "bel", "bmf", "bbs", p=p_center, h=h_down)

    menu:
        c_bomi "Et chaque fois que j'en lis, je me sens encore moins bien."
        "On devrait aller voir la psychologue scolaire.":
            playerName "On devrait aller voir la psychologue scolaire."
            $ ptsb2 += 1
            show screen cexp("bpb", "bel", "bmt", "bbn", p=p_center, h=h_down)
            c_bomi "Et risquer qu'ils le disent à ma famille ?"
            show screen cexp("bpb", "bea", "bmt", "bbs", p=p_center, h=h_down)
            c_bomi "Certainement pas!"
            show screen cexp("bpb", "bel", "bms", "bbs", p=p_center, h=h_down)
            playerName "Oui mais c'est important d'en parler à des personnes qualifiées..."
            playerName "Ils pouront t'aider beaucoup mieux que moi et te donner des vrais conseils!"
            show screen cexp("bpb", "bea", "bms", "bbs", p=p_center, h=h_down)
            c_bomi "..."
        
        "Ils ne veulent rien dire. Ça ira.":
            playerName "Ils ne veulent rien dire. Ça ira."
            show screen cexp("bpb", "bea", "bms", "bbs", p=p_center, h=h_down)
            c_bomi "..." 
    show screen cexp("bpb", "bel", "bmf", "bbs", p=p_center, h=h_down)
    c_bomi "Bon ok."
    c_bomi "Je ferai ce que tu m'as dit."
    show screen cexp("bpf", "bel", "bmt", "bbs", p=p_center, h=h_down)
    c_bomi "J'espère que tu as raison."
    scene black with fade

    if ptsb2 > 2:
        jump RBG
    else:
        jump RBB2

label RBB2:
    # A changer et a sénariser au fil du temps.
    """{i}Ça fait un mois que j'ai parlé à Bomi du post.{/i}

    {i}Le post s'est propagé et les gens à l'école ont commencé à le voir.{/i}

    {i}Parfois, je trouvais des lettres dans son casier ou des mots méchants écrits sur son bureau.{/i}

    {i}Apparemment, Akane a beaucoup d'admirateurs et puisque les gens essayaient d'imiter leur “déesse”, leurs commentaires finissaient par être ciblés.{/i}

    {i}J'ai essayé de les cacher du mieux que je pouvais mais ce n'était pas assez.{/i}"""
    scene classroom late with fade
    "{i}Bomi a fini par les découvrir."

    c_bomi "..."
    c_bomi "..."
    c_bomi "..."

    "{i}Au fil des jours, elle semblait se sentir de plus en plus mal."

    """{i}À la fin, elle n'est plus venue en cours.{/i}

    {i}Personne n'a entendu parler d'elle depuis et je pense que la majorité n'ont rien fait pour essayer de prendre de ses nouvelles.{/i}

    {i}Sa chaise est vide, ramassant la poussière au fil du temps.{/i}"""

    jump game_over

label RBG:
    """{i}Ça fait un mois que j'ai parlé à Bomi du post.{/i}

    {i}Bomi avait réussi à le supprimer pour “diffamation” et le compte de Himeno a été suspendu pendant un certain temps.{/i}

    {i}J'ai accompagné Bomi à ses séances de thérapie et lentement mais sûrement, elle se reprenait en main.{/i}

    {i}Même si la publication est devenue virale et que certains fans d'Akane l'ont encore insultée, Bomi a reçu beaucoup de soutien.{/i}"""
    scene BGE with fade

    "Serveur" "Voici votre plat."
    playerName "Tiens, c'est chaud."
    playerName "Tu peux le prendre d'abord."
    c_bomi "Non, non, c'est pas grave je peux attendre."
    narrateur """Elle détourne le regard en pensant du ramen.
    
    Tu sors ton portable et prends une photo d'elle et le plat.
    
    {i}Ma copine est tellement mignonne{/i}"""

    c_bomi "H-Hey!!"

    playerName "T'inquetes, t'inquetes... C'est une bonne photo."

    "{i}Tu lui montre la photo."

    c_bomi "...

    Je peux la poster?" 
    scene black with fade
    narrateur "YOU WON!!!!!"