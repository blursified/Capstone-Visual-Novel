# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ether", color="#b6aeeb")
define md = Character("Mr. Duras", color="#8f671e")
define r = Character("Rajah", color="#ed6328")
define b = Character("Blaire", color="#eba2e1")
define v = Character("Video", color="#7a7976")

transform zoom_center: 
    zoom 0.35 #adjust as required
    center
    ypos 1500
    
# transform cls_right: 
#     zoom 0.35 #adjust as required
#     # right

# transform h_left:
#     zoom 0.2
#     # left

label start:
    # DAY 1
    scene bg bedroomtest
    # ----------------------------- begin
    show ether test at zoom_center
    e "{alpha=0.5}{i}wakes up{/i}{/alpha}"
    e "Time for class already? Ugh..."
    e "{alpha=0.5}{i}gets ready for school and goes to class{/i}{/alpha}"
    e "I have Government first. Hopefully, it'll be easy..."
    e "{alpha=0.5}{i}barely gets to class on time{/i}{/alpha}"

    scene bg classroomtest
    # ------------------------------------- start class
    show ether test at zoom_center
    md "Good morning, class! Thank you all for making it on time."
    e "{i}Mr. Duras is dressed up today! That means we're going to do something fun today! I wanna see what he has planned..!{/i}"
    md "If you could all complete the warm-up...."
    e "{alpha=0.5}{i}reading aloud{/i}{/alpha}"
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
    r "{alpha=0.5}{i}muttering{/i}{/alpha}"
    r "Of course..."
    md "What was that, Rahja?"
    r "Nothing! Just expressing appreciation for Blaire's taste."
    e "{alpha=0.5}{i}quietly snickering{/i}{/alpha} Really?"
    md "Anyway, let's wrap this up and move on to the lesson for today. As you can probably tell, I've dressed up today! Does anyone want to guess who I'm dressed up as?"
    md "Yes, Rajah?"
    r "A colonel?"
    md "You're close! Good guess."
    r "A lieutenant? A general?"
    md "A general indeed! But from where?"
    e "{alpha=0.5}{i}quietly{/i}{/alpha} Zebulon?"
    md "What was that, Ether?"
    e "{alpha=0.5}{i}embarrassed{/i}{/alpha} Um, I don't know if I'd be right-"
    r "He said Zebulon."
    md "Correct! I'm dressed up as one of Zebulon's Generals, General Slade. He's not as well known as George Washingtsing or Alixandre Hannibal, but he did lead the creation of Zebulon's government to what it is today. Now, let's get to the notes!"
    md "On the slides, you can see his contributions to the government. When Zebulon was first colonized, they had a system called the Articles of Colonies that was loosely distributed across the Great Galaxy."
    md "However, the Articles of Colonies has many faults- including-"
    e "{i}I can't keep up! I've barely written down the first ten words, and he's already moving on?{/i}"
    e "{i}I'll just have to write faster-{/i}"
    md "Now, once we abolished the Articles of Colonies in 40XX-"
    e "{i}40- when? I didn't hear the last part- It's fine, I'll just try copying everything down-{/i}"
    md "And so, the first government resembling what we have today has three branches, the Legistlative, Executive, and Judicial branches-"
    e "{i}Why is he moving around so much?{/i}"
    md "Yes, Blaire, excellent point! Everyone, be sure to jot that down-"
    e "{i}What did she even say? I couldn't catch it-{/i}"
    md "No, no, that's not quite what happened, Roger. See, General Slade did end up leading the entire planet, but he set the framework."
    e "{i}There's so much happening and I can't focus on the slides- There's too much color and too many voices-{/i}"
    md "Onto our last section, the Executive branch was headed by someone named the President, who attempted a coupe to assassinate the head Generals-"
    md "Yes, Danny. That is precisely what happened! There you go, Roger, that's how-"
    e "{i}I'm losing track of everything..... I want Mr. Duras to stop moving around so much- and for everyone to be quiet-{/i}"
    md "Alright, class, that wraps our notes for today! I'll pass out a worksheet so you can practice applying what you learned today. It's due at the end of class!"
    md "And remember, class-"
    e "{i}We have a worksheet for this?? I was so distracted that I didn't get half the notes down!{/i}"
    r "Psst. Ether."
    e "{i}What am I going to do-{/i}"
    r "Ether, pal, you in there?"
    e "{alpha=0.5}{i}shaking himself out of the daze{/i}{/alpha}"
    e "Yes?"
    r "How much of the notes did you get down?"
    e "Um....."
    r "Dang, you wrote down less than me! Nevermind, I didn't realize you were more behind than I was-"
    e "{i}Yeah, I was behind, wasn't I...{/i}"
    jump choosehelp
    return

label choosehelp:
    show ether test at zoom_center
    # Government teacher assigns a worksheet on the 3 branches of government, specifically on its functions. Ether, who didn’t get the notes down, struggles to complete it
    r "Oh, there's the worksheet. It doesn't look too long...."
    e "{alpha=0.5}{i}takes the paper, looking at the first question{/i}{/alpha}"
    e "{i}What is the purpose of the Legislative Branch?{/i}"
        #note - these lines may be inner monologue, may need to be italicized
    e "Oh, I was in the middle of writing down the branch name before Mr. Duras moved on... Maybe I can come back to it later?"
    e "Next question: {i}How many departments does the Executive Branch control?{/i}"
    e "I... didn't even get to writing that part in the notes either...."
    e "Question after: {i}Provide an example of when the Judicial branch's judgement influenced an Executive Order..{/i}"
    e "{i}Um.... I can't answer any of these questions at all... I should probably ask for help... Maybe Rajah would know?{/i}"
    e "Rajah, did you get the answer to the first question?"
    e "Where'd he even go?"
    menu:
        "Ask Blaire":
            jump ask_blaire_choice
        "Ask Mr. Duras":
            jump ask_duras_choice
        "Do worksheet alone":
            jump do_alone_choice
    return

label ask_blaire_choice:
    show ether test at zoom_center
    e "Hey, Blaire-"
    b "Yeah?"
    e "Um... could you help me with the worksheet?"
    b "The worksheet? I finished it in ten minutes because it was so easy!"
    e "{i}It was easy?{/i}"
    e "Do you remember what the answer to the first question was?"
    b "To make laws, obviously. Mr. Duras just explained that 'Legislative' means relating to the law."
    e "He did? I didn't hear him..."
    b "Really? You probably weren't paying attention then."
    e "Oh.... um, would you happen to know the answer to the next question too?"
    b "The Departments of the Executive Branch?"
    e ".... Yes?"
    b "I thought that part was pretty self-explanatory, but since you seem to be a little slow, why don't you tell me how many Departments the school works with?"
    e "... The school..?"
    e "What does that have to do with the government?"
    b "Well-"
    jump turn_in_unfinished_work
    return
label ask_duras_choice:
    show ether test at zoom_center
    e "Maybe I can ask Mr. Duras for help...."
    e "{alpha=0.5}{i}gets up{/i}{/alpha}"
    e "{alpha=0.5}{i}walks over to Mr. Duras' desk{/i}{/alpha}"
    e "Mr. Duras?"
    md "{alpha=0.5}{i}looking up from his work{/i}{/alpha}"
    md "Ah, Ether! How can I help you?"
    e "Um, I'm really confused about the worksheet because I didn't get all the notes down."
    md "I see. Why don't I go over the questions with you, then?"
    e "{alpha=0.5}{i}nods{/i}{/alpha}"
    md "Remind me what the first one is?"
    e "What is the purpose of the Legislative Branch?"
    md "Alright, Ether, think of it this way. Where does the word 'legislative' come from?"
    e "I.. don't know."
    md 'Well, the word comes from the Latin word {i}latus{/i}, which means "to carry or bring". Then, that word eventually gave way to another word, {i}lator{/i}. That is the {i}lator{/i} part of the word {i}legislator{/i}.'
    e "{i}He's moving his hands a lot again...{/i}"
    md 'Now, "{i}legis{/i}" part of the word "legislator" comes from the Roman concept of {i}legis latio{/i}, which is the act of enacting law. And the "ator" simply describes someone who does so. Now, if you put those two together, what do you suppose they represent?'
    e ".. Legislator?"
    md 'That is true, but we are trying to find the meaning of the word. Think about it. You have the law, and the the word "to carry or bring". What do you think a legislator would do?'
    e "Carry the law?"
    md "Precisely! That answers your first question."
    e "The Legislative Branch.. carries the law?"
    e "{i}How does that even make sense? How does the law get carried?{/i}"
    md "See. Ether, the Legislative branch-"
    md "No, Roger, you may not use the restroom. There are only five more minutes left of class!"
    md "No, don't tell you need go now! I'm quite sure you can wait!"
    md "{alpha=0.5}{i}turns back to Ether and smiles{/i}{/alpha}"
    md "I'll have to start wrapping up now, Ether. Why don't you go back to your seat and work through the rest of the questions?"
    md "{alpha=0.5}{i}gets up and leaves Ether by his desk{/i{/alpha}}"
    e "Oh... kay...."
    e "{alpha=0.5}{i}returns to his seat{/i}{/alpha}"
    jump turn_in_unfinished_work
    return

label do_alone_choice:
    show ether test at zoom_center
    e "{i}Oh, I can probably wait until he comes back. I'll just work through the rest of it.{/i}"
    e "{i}re-reading the first question: What is the purpose of the Legislative Branch?{/i}"
    e "{i}Legislative.... that's a long word. It looks a little weird on paper.{/i}"
    e "{i}So what does this branch do?{/i}"
    e "{i}I don't remember....{/i}"
    e "{i}The group behind me is talking really loudly.. Focus, Ether, you have work to do.{/i}"
    e "{i}But I can't.. Argh. Legislative. Legislative. What does it do?{/i}"
    e "{i}C'mon, maybe the information is just lodged in your brain, and doesn't want to come out.{/i}"
    e "{i}Think, Ether, think. Ignore the noise, because it shouldn't affect you. Cut it out.{/i}"
    e "{i}I've been staring at this paper for so long that 'Legislative' doesn't even look like a word anymore.{/i}"
    e "{i}Maybe it'll come to me later. I really wish I could work with Rajah, but I don't even know where he went...{/i}"
    e "{i}Next question. Departments of the Executive Branch.{/i}"
    e "{i}I.. also can not think of anything for that question. This is amazing.{/i}"
    e "{i}Maybe I'll just go back to the first one...{/i}"
    jump turn_in_unfinished_work
    return

label turn_in_unfinished_work:
    show ether test at zoom_center
    md "Alright, class, our time together for today is coming to an end. Please finish up your last thoughts and prepare to turn in what you have finished."
    e "I haven't finished it, though..."
    md "I'm coming around with today's homework. It is similar to today's worksheet, so it shouldn't take you too long to finish."
    md "On the way out, please drop off the classwork from today and have a great rest of your day!"
    e "{i}Oh no.....{/i}"
    r "Ether!"
    e "Oh, hi Rajah. I was looking for you earlier."
    r "Ah. Well, I went to ask Danny for help. She was able to talk me and Gabby through most of it, but I still don't fully understand every single word that came out of her mouth."
    r "Why'd the government have to be so complicated?"
    e "You should ask General Slade that."
    r "These old geezers just wanted to make it hard to understand on purpose! Well, anyway, we should turn in the worksheet now. Don't forget to grab the homework! I'll wait for you outside."
    jump end_of_day1
    return

label end_of_day1:
    # Later.. (afterschool):
    e "{i}Finally, I get to go home.....{/i}"
    e "{i}No homework today! Wait, no... I have that government worksheet to do, dang it!{/i}"
    e "{i}Mr. Duras said it wasn't supposed to take too long, though, so maybe it'll be easy.{/i}"
    e "{i}But he also said that it was almost exactly like the worksheet, and I didn't finish that..{/i}"
    e "{i}Ack. I'd better get home to finish it, then.{/i}"
    # ------------- (reaches home)
    e "{i}Home sweet home..{/i}"
    e "{i}I'd better get started on that worksheet.{/i}"
    e "{alpha=0.5}{i}goes up to his room{/i}{/alpha}"
    e "{alpha=0.5}{i}pulls out his homework{/i}{/alpha}"
    e "Alright, first question. How does the Bureaucracy interact with the 3 branches of government?"
    e "I think I remember writing this down in my notes. It was in here somewhere..."
    e "Aha! The Bureaucracy is primarily kept in check by the Legislative and Executive Branches."
    e "Er, okay. Did I write down any more details?"
    e "..... The rest of this page is blank...."
    e "Maybe I can just google it and write it down!" 
    e "Let's see.. {i}The Executive Branch appoints the heads of each individual department, and the Legislative Branch controls the funding and regulations for each department. Thus, the Executive Branch has a lasting influence on each of the agencies, and the Legislative Branch is able to influence the agenda of each separate department.{/i}"
    e "Okay, so the Executive Branch picks leaders. The Legislative Branch gives them the money and rules. That's easy enough."
    e "Next question: {i}Explain how the interactions between the Bureaucracy and the 3 branches of Government encourage federalism.{/i}"
    e "Federalism? Did Mr. Duras even talk about that?"
    e "It's not in my notes, so I'll just google it again..."
    e "Federalism: {i}a principle or system of government in which several states form a unity but remain independent in internal affairs{/i}. Why are there so many big words?"
    e 'Federalism: simple definition. "{i}A system where power is divided and shared between a central government and state governments{/i}."'
    e "Oh. Okay. But isn't the Bureaucracy and the 3 branches just government?"
    e "Maybe I'll just put the entire question into Google and see what it gives me.."
    e "That is.... a lot of words, that does not answer my question. I'll look up a YouTube video. Maybe that'll help."
    e "These videos are all over an hour long! {i}Federalism Explained in Detail-- Specifically for Scholars{/i}. {i}The Government's Faults{/i}. This one looks helpful: {i}How the Government Interacts with the States Explained{/i}. It's only around 10 minutes, too."
    e "Of course the first thing it shows me is an ad.. Skip-"
    e "There's another one??"
    e "And a third... 1 minute unskippable should be criminal..."
    e "Okay! Finally, the video's starting!"
    e "Why does it start with a sponsorship?"
    e "Fine, I'll just skip that too... fast forward, fast forward, fast forward-"
    e "The sponsorship is still going?"
    e "Fast forward, fast forward, fast forward..."
    e "Why does it go into the 5 minute mark? That's already half the video!"
    e "Fast forward some more- Here's what I'm looking for!"
    v "{i}The government and its 3 branches encourage federalism by interacting with the states! That's all for today! Like if you enjoyed, and subscribe for more!{/i}"
    e "Interacting with the states? Of course they interact with the states- that's what federalism is, right?"
    e "{alpha=0.5}{i}groans{/i}{/alpha}"
    e "I really wish I had taken more notes...."
    e "Wow, the comments are just as annoyed as I am, hah..."
    e "Maybe I need a break and do something else for a little bit."
    e "Let's see how my grades are doing."
    e "96% (A) in Statistics, 94% (A) in Mandarin... 90.2% (A-) in Government? How did my grade drop 5% in a day? It used to be almost 96%..."
    e "Oh, Mr. Duras gave me a C on the classwork... 70/100... I didn't know it was weighted that heavily! Dang it.... What am I supposed to do?"
    e "What if my parents find out about this?!"
    e "They're going to be so mad...."
    e "I didn't spend all year keeping it at an A just for it to drop right before the marking period ends!"
    e "I'll have to ask Mr. Duras if I can make up the credit. And I can't mess up any more assignments, or it'll drop to a B...."
    e "I'll just try finishing the homework in the meantime...."
    jump
    return

label start_day2:
    e "{alpha=0.5}{i}arriving at school{/i}{/alpha}"
    e "{i}Oh, I'm early. Let's see if Mr. Duras is here yet.{/i}"
    e "{alpha=0.5}{i}walks down the hall{/i}{/alpha}"
    e "{i}Great, his door is open. He must be here!{/i}"
    e "{i}Rajah's standing right next to door, too. Maybe I can compare answers to the homework with him while I wait for the bell to ring.{/i}"
    menu:
        "Ask Mr. Duras if they can redo worksheet":
            jump ask_duras_to_redo
        "Ask Rajah is he finished the homework":
            jump ask_rajah_if_finished
    return

label ask_duras_to_redo:
    e "{i}I can ask Rajah what he got on the homework during class. I'd best ask Mr. Duras now, since he might busy later.{/i}"
    e "{alpha=0.5}{i}enters the room{/i}{/alpha}"
    md "Good morning, Ether. You're early today."
    e "Hello, Mr. Duras."
    md "How are you doing?"
    e "{i}I really just want to get to the point already...{/i}"
    e "Good, uh, how about you?"
    md "I'm doing just fine. Is there anything you needed?"
    e "...."
    e "I was checking my grades yesterday and I saw that you graded the worksheet from yesterday."
    md "Yes, I did. What about it?"
    e "Is there any way for me to make up the points I lost on the worksheet?"
    md "You had nearly 45 minutes to complete the worksheet, and there were only three questions on it."
    e "Yes, I know, but I didn't get the notes down because you were going too fast."
    md "Have you gotten the notes from anyone else?"
    e "..."
    e "No..."
    md "Isn't Blaire at your table? You could've asked her for help. She finished the worksheet in 15 minutes. She should've gotten most, if not all the notes down."
    e "{alpha=0.5}{i}nods{/i}{/alpha} I'll ask her then."
    e "Could I still redo the worksheet, though?"
    md "Unfortunately, no. But I encourage you to study the notes, since we'll have multiple assignments on them in the coming weeks."
    e "Okay....."
    md "Oh, dear, the bell's about to ring in five minutes. Get ready for class, Ether, while I gather the rest of the class."
    md "{alpha=0.5}{i}leaves the room{/i}{/alpha}"
    jump
    return

label ask_rajah_if_finished:
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
