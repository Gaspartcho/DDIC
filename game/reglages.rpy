label after_load:

#region Variables

    define hasPlayBefore = False

    define defaultPlayerName = "Shujin"
    define playerName = defaultPlayerName
    define LovePoints = {"Akane":0, "Bomi":0, "Himeno":0}

#endregion

#region Randoms Functions

    init python:
        from functools import partial

        def beepy_voice(event, interact=True, sound="audio/Narator_U_Voice.mp3", level=1.0, **kwargs):
            if not interact:
                return

            if event == "show_done":
                renpy.sound.play(sound, loop=True, relative_volume=level)
            elif event == "slow_done":
                renpy.sound.stop()

#endregion

#region Characters

    define c_mysteriousMan = Character("???", who_color="#000", callback=partial(beepy_voice, sound="audio/voices/MisteriousMan_voice.mp3", level=0.15))
    define narrateur = Character(" ", callback=partial(beepy_voice, sound="audio/voices/Narator_U_Voice.mp3", level=0.5))

    define c_bomi = Character("Bomi", who_color="779b5a")
    define c_akane = Character("Akane", who_color="6d7aad")
    define c_himeno = Character("Himeno", who_color="db4cad")
    define tpb = "Bomi"
    define tpa = "Akane"
    define tph = "Himeno"
    define usrb = "bombomii"
    define usra = "kousei.akane"
    define usrh = "yuzu.himi"
    
#endregion

#region Images

# Akane
    image akane armscrossed = "images/Characters/Akane/akane_armscrossed.png"
    image akane chin = "images/Characters/Akane/akane_chin.png"

    image akane = "images/Characters/Akane/akane_default.png"

# Bomi
    image bomi armsback = "images/Characters/Bomi/bomi_armsback.png"
    image bomi fingie = "images/Characters/Bomi/bomi_fingie.png"

    image bomi = "images/Characters/Bomi/bomi_default.png"

# Himeno
    image himeno driveout = "images/Characters/Himeno/himeno_driveout.png"
    image himeno phone = "images/Characters/Himeno/himeno_phone.png"

    image himeno = "images/Characters/Himeno/himeno_default.png"

# Insta
    image insta bomi1 = "images/instagram/B1_insta.png"
    image insta bomi2 = "images/instagram/B2_insta.png"
    image insta akane1 = "images/instagram/A1_insta.png"
    image insta akane2 = "images/instagram/A2_insta.png"
    image insta himeno1 = "images/instagram/H1_insta.png"
    image insta himeno2 = "images/instagram/H2_insta.png"

# Background
    image classroom day = "images/scenes/classroom_day.png"
    image classroom late = "images/scenes/classroom_late.png"
    image bedroom = "images/scenes/bedroom.png"
    image hallway day = "images/scenes/hallway_day.png"
    image hallway late = "images/scenes/hallway_late.png"
    image park = "images/scenes/park.png"
    image BH1 = "images/scenes/BH1.png"


#endregion

#regions Sons et musiques

    define audio.MisteriousMan_theme = "audio/musics/Ambiant_misterious.mp3"

    define audio.phone_jingle = "audio/sound_effects/notification_sound.mp3"
    define audio.class_bell = "audio/sound_effects/School Bell.mp3"

#endregion

#region Autres

    transform image_choose_path:
        xalign 0.5
        yalign 0.5
        xpos 0.5
        ypos 0.4

    transform image_choose_path_h:
        xsize 0.7
        ysize 0.7
        xalign 0.5
        yalign 0.5
        xpos 0.5
        ypos 0.4
            
#endregion