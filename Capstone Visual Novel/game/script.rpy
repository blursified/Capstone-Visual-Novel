# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hawk")


# The game starts here.
transform half_size: 
    zoom 0.5 #adjust as required
    center

transform more_zoomed:
    zoom 0.2
    center

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroomtest

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hawk happy at half_size

    # These display lines of dialogue.

    h "yaaaaaaaaaaaaaaaaaay"

    show hawk curious at more_zoomed

    h "Arrooo?"

    # This ends the game.

    return
