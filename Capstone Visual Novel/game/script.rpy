# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ether")
define md = Character("Mr. Duras")
define r = Character("Rajah")
define b = Character("Blaire")

transform cls_center: 
    zoom 0.35 #adjust as required
    center
    
transform cls_right: 
    zoom 0.35 #adjust as required
    right

transform h_left:
    zoom 0.2
    left

label start:

    scene bg spacytest
    # ----------------------------- begin
    e "{i}wakes up{/i}"
    e "Time for class already? Ugh..."
    e "{i}gets ready for school and goes to class{/i}"
    e "I have Government first. Hopefully, it'll be easy..."
    e "{i}barely gets to class on time{/i}"

    scene bg classroomtest
    # ------------------------------------- start class
    md "Good morning, class! Thank you all for making it on time."
    e "{i}Mr. Duras is dressed up today! That means we're going to do something fun today! I wanna see what he has planned..!{/i}"
    md "If you could all complete the warm-up...."
    e "{i}reading aloud{/i}"
    e "If you could meet anyone in the world, who would it be?"
    r "ooooohhhh.... Mr. Duras, when you mean {i}anyone{/i}, does that also include talking animals?"
    md "Er.... Rajah, who do you have in mind?"
    r "I want to meet the cockroach in YIPPEEE meme."
    e "... Of all things you could've chosen, you'd meet THAT cockroach? You could've met Albert Einstein, or Eleanor Roosevelt, or-"
    r "Nah. The cockroach in that meme is far more interesting."
    md "Ah, I see... Ether, what would be your answer to the question?"
    e "Uh...... Hm......"
    e "I think I'd meet.... Zephyr Zebulon, the founder of the school. I'd want to know they created the first interstellar school during their era, when interstellar technology was just discovered."
    md "Excellent answer! I'm glad you're interested in the origins of our wonderful school."
    md "Blaire, I see you have your hand raised. How would you answer the warm up question?"
    b "I'd meet Taylor Swift."
    md "Taylor Swift? I don't think I've heard that name before. Could you remind me who that is?"
    b "Really? She's only the most popular pop star from Earth."
    r "{i}muttering{/i}"
    r "Of course..."
    md "What was that, Rahja?"
    r "Nothing! Just expressing appreciation for Blaire's taste."
    e "{i}quietly snickering{/i} Really?"
    md "Anyway, let's wrap this up and move on to the lesson for today. As you can probably tell, I've dressed up today! Does anyone want to guess who I'm dressed up as?"
    md "Yes, Rajah?"
    r "A colonel?"
    md "You're close! Good guess."
    r "A lieutenant? A general?"
    md "A general indeed! But from where?"
    e "{i}quietly{/i} Zebulon?"
    md "What was that, Ether?"
    e "{i}embarrassed{/i} Um, I don't know if I'd be right-"
    r "He said Zebulon."
    md "Correct! I'm dressed up as one of Zebulon's Generals, General Slade. He's not as well known as George Washingtsing or Alixandre Hannibal, but he did lead the creation of Zebulon's government to what it is today. Now, let's get to the notes!"

    return


# # The game starts here.
# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg classroomtest

#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show chenglaoshi rest at cls_center
#     c "Ahem"

#     show chenglaoshi rest:
#         ypos 850    
#     with move
#     c "Hi, I'm Cheng Lao Shi."

#     c "Welcome to Mandarin class *wink*"

#     c "Are you excited for class?"
#     menu:
#         "Uh yeah!":
#             jump Choice_1
#         "Um.. not really.":
#             jump Choice_2
#     return

# label Choice_1:
#     c "Hooray!"
#     jump start2
# label Choice_2:
#     c "I'm sure you'll end up having fun!"
#     jump start2
    

# label start2:
#     show chenglaoshi rest at cls_right
#     show hawk curious at h_left

#     c "Hey puppers."
#     h "Arf!"
#     return
