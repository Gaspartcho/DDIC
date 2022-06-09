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
    define usraf = "akanekouseii"
    
#endregion

#region Images

# Akane
    image apc = "images/Characters/Akane/akane_default.png"
    image apr = "images/Characters/Akane/akane_chin.png"

    image abn = "images/Characters/Akane/expression/akane_eyebrows_happy.png"
    image abm = "images/Characters/Akane/expression/akane_eyebrows_mad.png"
    image abs = "images/Characters/Akane/expression/akane_eyebrows_neutral.png"
    image aeb = "images/Characters/Akane/expression/akane_eyes_blink.png"
    image ael = "images/Characters/Akane/expression/akane_eyes_left.png"
    image aea = "images/Characters/Akane/expression/akane_eyes_right.png"
    image amn = "images/Characters/Akane/expression/akane_mouth_neutral.png"
    image ams = "images/Characters/Akane/expression/akane_mouth_smile.png"
    image amt = "images/Characters/Akane/expression/akane_mouth_talk.png"
    image av = "images/Characters/Akane/expression/Akane_vein.png"

# Bomi
    image bpb = "images/Characters/Bomi/bomi_armsback.png"
    image bpf = "images/Characters/Bomi/bomi_fingie.png"
    image bpbb = "images/Characters/Bomi/bomi_armsback_blue.png"
    image bpfb = "images/Characters/Bomi/bomi_fingie_blue.png"

    image bbm = "images/Characters/Bomi/expressions/bomi_eyebrows_mad.png"
    image bbn = "images/Characters/Bomi/expressions/bomi_eyebrows_neutral.png"
    image bbs = "images/Characters/Bomi/expressions/bomi_eyebrows_sad.png"
    image beb = "images/Characters/Bomi/expressions/bomi_eyes_blink.png"
    image bea = "images/Characters/Bomi/expressions/bomi_eyes_left.png"
    image bel = "images/Characters/Bomi/expressions/bomi_eyes_right.png"
    image bmh = "images/Characters/Bomi/expressions/bomi_mouth_happy.png"
    image bmn = "images/Characters/Bomi/expressions/bomi_mouth_neutral.png"
    image bms = "images/Characters/Bomi/expressions/bomi_mouth_sad.png"
    image bmt = "images/Characters/Bomi/expressions/bomi_mouth_talk.png"
    image bmw = "images/Characters/Bomi/expressions/bmn.png"
    image bmf = "images/Characters/Bomi/expressions/bmf.png"

# Himeno
    image hpw = "images/Characters/Himeno/himeno_driveout.png"
    image hph = "images/Characters/Himeno/himeno_phone.png"

    image hbn = "images/Characters/Himeno/expressions/hbn.png"
    image hea = "images/Characters/Himeno/expressions/hea.png"
    image heb = "images/Characters/Himeno/expressions/heb.png"
    image hel = "images/Characters/Himeno/expressions/hel.png"
    image hes = "images/Characters/Himeno/expressions/hes.png"
    image hmd = "images/Characters/Himeno/expressions/hmd.png"
    image hmf = "images/Characters/Himeno/expressions/hmf.png"
    image hml = "images/Characters/Himeno/expressions/hml.png"
    image hmm = "images/Characters/Himeno/expressions/hmm.png"
    image hmn = "images/Characters/Himeno/expressions/hmn.png"
    image hms = "images/Characters/Himeno/expressions/hms.png"
    image hmt = "images/Characters/Himeno/expressions/hmt.png"
    image hba = "images/Characters/Himeno/expressions/hba.png"
    image hbs = "images/Characters/Himeno/expressions/hbs.png"
    image hlc = "images/Characters/Himeno/expressions/hlc.png"
    image hbc = "images/Characters/Himeno/expressions/hbc.png" 

# Insta
    image insta bomi1 = "images/instagram/B1_insta.png"
    image insta bomi2 = "images/instagram/B2_insta.png"
    image insta akane1 = "images/instagram/A1_insta.png"
    image insta akane2 = "images/instagram/A2_insta.png"
    image insta himeno1 = "images/instagram/H1_insta.png"
    image insta himeno2 = "images/instagram/H2_insta.png"

    image Bomi pfp = "images/Phone/Bomi_Pfp.png"
    image Akane pfp = "images/Phone/Akane_Pfp.png"
    image Himeno pfp = "images/Phone/Himeno_Pfp.png"

# Background
    image classroom day = "images/scenes/classroom_day.png"
    image classroom late = "images/scenes/classroom_late.png"
    image bedroom = "images/scenes/bedroom.png"
    image hallway day = "images/scenes/hallway_day.png"
    image hallway late = "images/scenes/hallway_late.png"
    image park = "images/scenes/park.png"
    image HB1 = "images/scenes/himeno_b1.png"
    image HB2 = "images/scenes/himeno_b2.png"
    image HGE = "images/scenes/himeno_ge.png"
    image BB1 = "images/scenes/bomi_b1.png"
    image BB2 = "images/scenes/bomi_b2.png"
    image BGE = "images/scenes/bomi_ge.png"
    image AB1 = "images/scenes/akane_b1.png"
    image AB2 = "images/scenes/akane_b2.png"
    image AGE = "images/scenes/akane_ge.png"

#endregion

#regions Sons et musiques

    define audio.MisteriousMan_theme = "audio/musics/Ambiant_misterious.mp3"

    define audio.phone_jingle = "audio/sound_effects/notification_sound.mp3"
    define audio.class_bell = "audio/sound_effects/School Bell.mp3"
    define audio.camera_effect = "audio/sound_effects/Camera_effect.mp3"

#endregion

#region Autres

    transform image_choose_path:
        xalign 0.5
        yalign 0.5
        xpos 0.5
        ypos 0.4

    transform image_choose_path_h:
        zoom 0.85
        xalign 0.5
        yalign 0.5
        xpos 0.5
        ypos 0.45
    
    transform character_expression_pos(p):
        xalign 0.5
        yalign 0.5

    transform p_center:
        xpos 0.8

    transform p_left:
        xpos 0.5

    transform p_right:
        xpos 1.1

    transform h_center:
        ypos 0.5

    transform h_down:
        ypos 0.65
    
    screen cexp(c=None, m=None, e=None, eb=None, o=None, t=None, p=p_center, h=h_center):
        modal False
        fixed at character_expression_pos, p, h:
            add c
            add m
            add e
            add eb
            add o
            add t

    screen mlt:
        use cexp("apr", "ael", "ams", "abn", p=p_left)
        use cexp("bpf", "bel", "bmh", "bbn", p=p_center)
        use cexp("hph", "hel", "hms", "hbn", p=p_right)
    
    screen h_and_bomi:
        use cexp("hph", "hel", "hmf", "hbs", p=p_right)
        use cexp("bpfb", "bbm", "bel", "bmt", p=p_left, h=h_down)

#endregion