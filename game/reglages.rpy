#region Variables

define hasPlayBefore = False

define defaultPlayerName = "Shujin"
define playerName = defaultPlayerName
define LovePoints = {"Akane":0, "Bomi":0, "Himeno":0}

#endregion

#region Randoms Functions

init python:
    def beepy_voice(event, interact=True, sound="audio/Narator_U_Voice.mp3", **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play(sound, loop=True)
        elif event == "slow_done":
            renpy.sound.stop()

#endregion

#region Characters

define c_mysteriousMan = Character("???", who_color="#000")
define narrateur = Character(" ", callback=beepy_voice("audio/Narator_U_Voice.mp3"))

define c_bomi = Character("Bomi", who_color="779b5a")

#endregion

#region Images:

#Akane
image akane armscrossed = "images/Characters/Akane/akane_armscrossed.png"
image akane chin = "images/Characters/Akane/akane_chin.png"

#Bomi
image bomi armsback = "images/Characters/Bomi/bomi_armsback.png"
image bomi fingie = "images/Characters/Bomi/bomi_fingie.png"

#Himeno
image himeno driveout = "images/Characters/Himeno/himeno_driveout.png"
image himeno phone = "images/Characters/Himeno/himeno_phone.png"

#endregion