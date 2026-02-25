# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hawk")
define c = Character("Cheng Lao Shi")

transform half_size: 
    zoom 0.5 #adjust as required
    center

transform more_zoomed:
    zoom 0.2
    center
# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroomtest

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chenglaoshi rest

    # These display lines of dialogue.

    c "Ahem"

    c "Hi, I'm Cheng Lao Shi."

    c "Welcome to Mandarin class *wink*"

    # h "Can you take me for a walk?"
    # menu:
    #     "Sure!":

    #     "F Nah":
    # This ends the game.
    return
