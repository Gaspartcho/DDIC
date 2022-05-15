screen Day:
    text "{color=#fff}Test hello world{/color}" xpos 0.5 ypos 0.5

label start:

    "Sylvie" "Hi there! How was class?"

    "Me" "I hate you"

    "Sylvie" "I can't bring myself to admit that it all went in one ear and out the other."

    "Me" "Are you going home now? Wanna walk back with me?"

    "Sylvie" "Sure!"

    "Sylvie" "Did you ever hear Lincon's famous saying, \"The problem with Internet quotations is that many of them are not genuine.\""

    "cunt" "pussy flap"
    
# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.

    $ player_name = renpy.input("What is your name?")

    $ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
    if player_name == "":
        $ player_name="Shuji"

# And get a nostalgic sigh from Seasons of Sakura fans!
    
# Now the other characters in the game can greet the player.
  
    "Sylvie" "Pleased to meet you, %(player_name)s!"
    
    window hide
    show screen Day
    pause

    return

