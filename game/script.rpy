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
# always start with this, it hides the regular text box, brings up the phone and has a short delay 
# most of these calls include delays to make this look nicer
# you can find the code behind these calls in options.rpy
call phone_start

# this brings up the message, first slot is the name, and second is the content
# notice how it has _start at the end, the first one is special as there are no delays before it. use this for the first message
call message_start("nadia", "hey, this is a phone texting thingy")

# added an alternate way to reply from the player perspective, this time the name doesnt show if you think its extra
call reply_message("oh really? what does it do lol")

# this one is the same as the above one, but instead it has one more place for you to set an image
# you have to make the image be small enough to fit the screen or its gonna stretch weird!
call message_img("nadia", "it works with images too!","images/pic1.png")
call message("nadia", "the text box changes depending on how much content there is. dont put too big images or its gonna look weeeeiiiird")
call message("nadia", "you can also do menus here")

# the next line is the menu system, first and third slot are the menu options, second and fourth one are what happens when you click it

# i made a special reply menu called phone_reply3 which can use 3. if you wish to have more you can make a new reply4 and see how i modified the code between the first reply code
call screen phone_reply("awesome!","choice1","lame","choice2")
# i made a special reply menu called phone_reply3 which can use 3. if you wish to have more you can make a new reply4 and see how i modified the code between the first reply code
##call screen phone_reply3("awesome!","choice1","lame","choice2","im gay","choice3")

label choice1:    
    # always add this for both choices after the menu, this hides the previous message that we left visible during the menu
    call phone_after_menu
    
    # whenever you put the sender name to be "me" it is the player characters own message!
    call message_start("me", "awesome")
    call message("nadia", "i hope you like it")

    jump aftermenu
    
label choice2:
    call phone_after_menu
    call message_start("me", "lame")
    call message("nadia", "well, its a shame but your feelings are valid")
    
    jump aftermenu

label choice3:
    call phone_after_menu
    call message_start("me", "im gay")
    call message("nadia", "nice")
    
    jump aftermenu    
    
label aftermenu:
    call message("nadia", "check the code for comments on how the code works, thanks for your time!")
    call message("nadia", "the base for this code and this stretched phone background comes from cute demon crashers")
    call message("nadia", "the images were drawn by my gf @sloppydraws")
    
    # this one puts away the phone!
    call phone_end
    
    window hide
    show screen Day
    pause

    return