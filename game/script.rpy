
screen Day:
    text "{color=#fff}Test hello world{/color}" xpos 0.5 ypos 0.5

label start:

    define s = Character('Sylvie', color="#c8ffc8", what_slow_cps=text_speed)
    define m = Character('Me', color="#c8c8ff", what_slow_cps=text_speed)

    s "hello there, welcome to the game" 
    m "thank you"
    s "test test..."

    return