label route_B:
    label RA1:
        define good_points = 0
        
        narrateur "Pour une raison inconnue, vous décidez d'aller parler à Bomi."

        c_bomi "Salut, ça vas?"
        c_bomi "Tu es le nouveau non? Bienvenue à l'école X. J'espère que tu passera une bonne fin d'année ici."
        c_bomi "..."
        playerName "..."
        c_bomi "Tu as vu mon téléphone non?"
        playerName "..."
        
        menu:
            c_bomi "..."

            "Hey Bomi, pourquoi tu te caches?":
                $ good_points += 1
                c_bomi "Ah, tu l'as remarqué?"
                # Blushes (kind of)
            
            "Hé bien madame la déléguée, tu n'as pas du tout la même tête en vrai.":
                #looks down
                c_bomi "..."
            
        c_bomi "Ecoute, je suis désollé de t'avoir menti"
        c_bomi "J'admire beaucoup Akane. Elle est intelligente, elle est belle, elle est confiante..."
        c_bomi "Mon seul atout est mon niveau scolaire."
        c_bomi "Comparé à elle, ce n'est pas grand chose."

        menu:
            c_bomi "..."

            "Je pense que chacun a son charme.":
                $ good_points += 1
                playerName "Je pense que chacun a son charme."
                playerName "Je suis sûr que tu es tout aussi adorable"
                c_bomi "Peut-être que tu a raison..."

            "C'est vrais qu'elle est impressionnante":
                jump .after_menu

        c_bomi "De toute façon, je ne suis pas la seule à l'admirer. Beaucoup de gens voudraient être à sa place ou avec elle."
        c_bomi "..."
        c_bomi "Est-ce que je devrais me coifer?"

        menu:
            "Oui":
                playerName "À mon avis, tu devrais faire ce que tu veux, c'est juste une coupe de cheveux après tout."
                c_bomi "Oui..."
                c_bomi "C'est ça..."
            
            "Non":
                $ good_points += 1
                playerName "J'aime ta coupe. Je ne pense pas que tu devrais les couper pour l'instant"
                c_bomi "Je sais mais..."
                c_bomi "Elle à l'air si sure d'elle comme ça..."
        
        c_bomi "..."
        c_bomi "Bon, je dois y aller..."
        c_bomi "A demain."


        jump route_A