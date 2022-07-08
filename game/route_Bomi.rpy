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
    define ptsb2 = 0
    narrateur "Le lendemain."
    scene classroom day with fade

    "???" "Hey! [playerName]!"
    show screen cexp("bpb", "bel", "bmh", "bbn", h=h_down)
    c_bomi "J'ai retiré mes extensions."
    show screen cexp("bpf", "beb", "bmh", "bbs", h=h_down)
    c_bomi "Elles commençaient à devenir lourdes haha..."
    show screen cexp("bpf", "bea", "bms", "bbs", h=h_down)
    menu:
        c_bomi "..."
        "Je suis sûr qu'elle ne l'a pas encore postée":
            show screen cexp("bpf", "bel", "bms", "bbs", h=h_down)
            playerName "Je suis sûr qu'elle ne l'a pas encore postée."
            
        "Allons chercher Himeno":
            show screen cexp("bpf", "bel", "bms", "bbs", h=h_down)
            playerName "Allons chercher Himeno"
            $ ptsb2 += 1
    show screen cexp("bpf", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    show screen cexp("bpf", "bel", "bmt", "bbs", h=h_down)
    c_bomi "Je pense qu'elle est sur le toit en train de déjeuner et de prendre des photos pour Instagram."
    show screen cexp("bpf", "bel", "bms", "bbs", h=h_down)
    "{i} A-t-elle déjà posté?"
    narrateur """Tu sors ton tel pour vérifier.
    D'abord, tu regardes le compte de Bomi"""
    show screen cexp("bpf", "bea", "bms", "bbs", h=h_down)
    "{i}Wow..."
    "{i}Ces commentaires sont stupides et méchants..."
    "{i}Himeno n'a aucune pitié."
    "..."
    show screen cexp("bpb", "beb", "bms", "bbs", h=h_down)
    narrateur "Tu trouves la photo de Bomi avec ses extensions de cheveux, postée et virale."
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)
    c_bomi "Ah..."
    show screen cexp("bpb", "bea", "bmf", "bbs", h=h_down)
    c_bomi "J'espérais que tu n'allais pas la voir..."
    show screen cexp("bpb", "beb", "bmf", "bbs", h=h_down)
    c_bomi "Je ne pensais pas que c'était si reconnaissable..."
    show screen cexp("bpb", "bel", "bms", "bbs", h=h_down)
    menu:
        c_bomi "..."
        "Tu devrais y repondre":
            playerName "Tu devrais y repondre"
            playerName "Et aller la confronter dirrectement!"

        "N'y fais pas attention.":
            $ ptsb2 += 1
            playerName "N'y fais pas attention."
            playerName "On devrait signaler l'incident sur instagram et à l'administration."

    show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    playerName "Bon, allons voir Himeno."
    show screen cexp("bpb", "bel", "bmt", "bbs", h=h_down)
    c_bomi "Non!!" 
    show screen cexp("bpf", "bea", "bmt", "bbs", h=h_down)
    c_bomi "J-je veux dire qu'on ne devrait pas."
    show screen cexp("bpf", "bel", "bmt", "bbs", h=h_down)
    c_bomi "Ça deviendrait plus compliqué que voulu."
    show screen cexp("bpb", "bea", "bmt", "bbs", h=h_down)
    c_bomi "Ça passera... n'est-ce pas ?"
    show screen cexp("bpb", "bel", "bms", "bbs", h=h_down)

    menu:
        c_bomi "..."
        "Ouais. T'as juste à les ignorer et garder une preuve qu'on t'a envoyé de la haine.":
            $ ptsb2 += 1
            playerName "Ouais. T'as juste à les ignorer et garder une preuve qu'on t'a envoyé de la haine."
            playerName "Elle finira par payer de toute façon."

        "Defends-toi. ":
            playerName "Defends-toi. "
            playerName "Ils finiront par te croire."
            playerName "Himeno aura ce quelle mérite!"

    show screen cexp("bpb", "bea", "bmf", "bbs", h=h_down)
    c_bomi "Oui mais..."
    show screen cexp("bpb", "beb", "bmf", "bbs", h=h_down)
    c_bomi "Je voudrais pas lui attirer de problèmes..."
    show screen cexp("bpb", "bel", "bms", "bbs", h=h_down)
    playerName "On dois lui faire comprendre que chaque actions a des conséquences!"
    show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    playerName "Comment tu te sens?"
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)
    c_bomi "Mal."
    show screen cexp("bpb", "bea", "bmf", "bbs", h=h_down)
    c_bomi "C'est atroce."
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)
    c_bomi "J'ai l'impression que ces commentaires me hantent..."
    show screen cexp("bpb", "beb", "bmf", "bbs", h=h_down)
    c_bomi "Ils m'ont empêché de dormir hier soir."
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)

    menu:
        c_bomi "Et chaque fois que j'en lis, je me sens encore moins bien."
        "On devrait aller voir la psychologue scolaire.":
            playerName "On devrait aller voir la psychologue scolaire."
            $ ptsb2 += 1
            show screen cexp("bpb", "bel", "bmt", "bbn", h=h_down)
            c_bomi "Et risquer qu'ils le disent à ma famille ?"
            show screen cexp("bpb", "bea", "bmt", "bbs", h=h_down)
            c_bomi "Certainement pas!"
            show screen cexp("bpb", "bel", "bms", "bbs", h=h_down)
            playerName "Oui mais c'est important d'en parler à des personnes qualifiées..."
            playerName "Ils pouront t'aider beaucoup mieux que moi et te donner des vrais conseils!"
            show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
            c_bomi "..."
        
        "Ils ne veulent rien dire. Ça ira.":
            playerName "Ils ne veulent rien dire. Ça ira."
            show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
            c_bomi "..." 
    show screen cexp("bpb", "bel", "bmf", "bbs", h=h_down)
    c_bomi "Bon ok."
    c_bomi "Je ferai ce que tu m'as dit."
    show screen cexp("bpf", "bel", "bmt", "bbs", h=h_down)
    c_bomi "J'espère que tu as raison."
    hide screen cexp 
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
    show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    show screen cexp("bpb", "bel", "bms", "bbs", h=h_down)
    c_bomi "..."
    show screen cexp("bpb", "bea", "bms", "bbs", h=h_down)
    c_bomi "..."
    "{i}Au fil des jours, elle semblait se sentir de plus en plus mal."
    hide screen cexp
    scene BB2 with fade
    """{i}À la fin, elle n'est plus venue en cours.{/i}

    {i}Personne n'a entendu parler d'elle depuis et je pense que la majorité n'ont rien fait pour essayer de prendre de ses nouvelles.{/i}

    {i}Sa chaise est vide, ramassant la poussière au fil du temps.{/i}"""

    window hide
    pause
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
    
    window hide
    pause
    jump happy_ending