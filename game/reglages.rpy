#region Variables

define hasPlayBefore = True

define defaultPlayerName = "Shujin"
define playerName = defaultPlayerName
define LovePoints = {"Akane":0, "Bomi":0, "Himeno":0}
define charactersColors = {"Akane":"#efc87e", "Bomi":0, "Himeno":0}

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

define c_bomi = Character("Bomi", who_color="pink")

#endregion

#region Immages:

#Akane
image akane armscrossed noeyes = "images/Characters/Akane/akane_armscrossed_noeyes.png"
image akane chin noeyes = "images/Characters/Akane/akane_chin_noeyes.png"

#Bomi
image bomi armsback noeyes = "images/Characters/Bomi/bomi_armsback_noeyes.png"
image bomi question noeyes = "images/Characters/Bomi/bomi_question_noeyes.png"

#Himeno
image himeno driveout noeyes = "images/Characters/Himeno/himeno_driveout_noeyes.png"
image himeno phone noeyes = "images/Characters/Himeno/himeno_phone_noeyes.png"

#endregion