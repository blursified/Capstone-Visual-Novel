# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hawk")
define c = Character("Cheng Lao Shi")

transform cls_center: 
    zoom 0.35 #adjust as required
    center
    
transform cls_right: 
    zoom 0.35 #adjust as required
    right

transform h_left:
    zoom 0.2
    left

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroomtest

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chenglaoshi rest at cls_center
    c "Ahem"

    show chenglaoshi rest:
        ypos 850    
    with move
    c "Hi, I'm Cheng Lao Shi."

    c "Welcome to Mandarin class *wink*"

    c "Are you excited for class?"
    menu:
        "Uh yeah!":
            jump Choice_1
        "Um.. not really.":
            jump Choice_2
    return

label Choice_1:
    c "Hooray!"
    jump start2
label Choice_2:
    c "I'm sure you'll end up having fun!"
    jump start2
    

label start2:
    show chenglaoshi rest at cls_right
    show hawk curious at h_left

    c "Hey puppers."
    h "Arf!"
    return
