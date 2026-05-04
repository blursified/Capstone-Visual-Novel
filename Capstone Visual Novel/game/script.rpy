# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ether", color="#b6aeeb")
define md = Character("Mr. Duras", color="#acde6f")
define r = Character("Rajah", color="#ed6328")
define b = Character("Blaire", color="#b30971")
define v = Character("Video", color="#7a7976")
define s = Character("-", color="#7a7976")
define n = Character("Random Students", color="#7a7976")
define em = Character("Ether's Mom", color="#265469")
define ch = Character("Cheng lao Shi", color="#f24005")
define an = Character("Antimony", color="#940440")
define ej = Character("Ether - Journaling", color="#b6aeeb")

transform zoom_center: 
    # mainly for ether
    zoom 0.7#adjust as required
    center
    ypos 1600

transform zoom_right: 
    # mainly for ether
    zoom 0.7#adjust as required
    right
    ypos 1600

transform zoom_center2: 
    #used for: duras
    zoom 0.7 #adjust as required
    ypos 1300
    center

transform ant_center: 
    #used for: antimony
    zoom 0.55 #adjust as required
    ypos 40
    center

transform zoom_right2: 
    #used for: duras
    zoom 0.7 #adjust as required
    ypos 1300
    right

transform zoom_left2: 
    #used for: duras
    zoom 0.7 #adjust as required
    ypos 1300
    left

transform zoom_center_r:
    # mainly for rajah
    zoom 0.7#adjust as required
    center
    ypos 1800

transform zoom_left_r:
    # mainly for rajah
    zoom 0.7#adjust as required
    left
    ypos 1800

transform zoom_center_b:
    zoom 0.7#adjust as required
    center
    ypos 1300

transform zoom_right_b:
     # mainly for ether
    zoom 0.7#adjust as required
    right
    ypos 1300
    
transform cls_center: 
    zoom 0.35 #adjust as required
    ypos 300
    center

transform cls_center_q:
    ypos 100
    center

transform cls_center_s:
    zoom 1.5
    ypos 300
    center

transform cls_left: 
    zoom 0.35 #adjust as required
    ypos 300
    left

# transform h_left:
#     zoom 0.2
#     # left

label start:
    # DAY 1
    scene bg bedroom
    # ----------------------------- begin
    show ether base at zoom_center
    e "{alpha=0.5}{i}wakes up{/i}{/alpha}"
    hide ether
    show ether annoyed at zoom_center
    e "Time for class already? Ugh..."
    e "{alpha=0.5}{i}gets ready for school and goes to class{/i}{/alpha}"
    e "I have Government first. Hopefully, it'll be easy..."
    e "{alpha=0.5}{i}barely gets to class on time{/i}{/alpha}"

    scene bg govclassroom
    # ------------------------------------- start class
    show duras base at zoom_center2
    md "Good morning, class! Thank you all for making it on time."
    hide duras
    show ether happy at zoom_center
    e "{i}Mr. Duras is dressed up today! That means we're going to do something fun today! I wanna see what he has planned..!{/i}"
    hide ether
    show duras base at zoom_center2
    md "If you could all complete the warm-up...."
    hide duras
    show ether base at zoom_center
    e "{alpha=0.5}{i}reading aloud{/i}{/alpha}"
    e "If you could meet anyone in the world, who would it be?"
    hide ether
    show rajah blushing at zoom_left_r
    show duras base at zoom_right2
    r "ooooohhhh.... Mr. Duras, when you mean {i}anyone{/i}, does that also include talking animals?"
    md "Er.... Rajah, who do you have in mind?"
    hide duras
    show ether base at zoom_right
    r "I want to meet the cockroach in YIPPEEE meme."
    e "... Of all things you could've chosen, you'd meet THAT cockroach? You could've met Albert Einstein, or Eleanor Roosevelt, or-"
    r "Nah. The cockroach in that meme is far more interesting."
    hide rajah
    show duras base at zoom_left2
    show ether base at zoom_right
    md "Ah, I see... Ether, what would be your answer to the question?"
    e "Uh...... Hm......"
    hide ether
    show ether happy at zoom_right
    e "I think I'd meet.... Zephyr Zebulon, the founder of the school. I'd want to know they created the first interstellar school during their era, when interstellar technology was just discovered."
    hide duras
    show duras blush at zoom_left2
    md "Excellent answer! I'm glad you're interested in the origins of our wonderful school."
    hide duras
    hide ether
    show duras base at zoom_left2
    show blaire base at zoom_right_b
    md "Blaire, I see you have your hand raised. How would you answer the warm up question?"
    b "I'd meet Taylor Swift."
    md "Taylor Swift? I don't think I've heard that name before. Could you remind me who that is?"
    b "Really? She's only the most popular pop star from Earth."
    hide duras
    hide blaire
    show rajah base at zoom_center_r
    r "{alpha=0.5}{i}muttering{/i}{/alpha}"
    r "Of course..."
    hide rajah
    show duras base at zoom_center2
    md "What was that, Rajah?"
    hide duras
    show rajah blushing at zoom_center_r
    r "Nothing! Just expressing appreciation for Blaire's taste."
    hide rajah
    show ether happy at zoom_center
    e "{alpha=0.5}{i}quietly snickering{/i}{/alpha}"
    e "Really?"
    hide ether
    show duras base at zoom_center2
    md "Anyway, let's wrap this up and move on to the lesson for today. As you can probably tell, I've dressed up today! Does anyone want to guess who I'm dressed up as?"
    md "Yes, Rajah?"
    hide duras
    show rajah base at zoom_center_r
    r "A person?"
    hide rajah
    show duras base at zoom_center2
    md "No, Rajah.. but good guess..."
    hide duras
    show rajah base at zoom_center_r
    r "A government teacher? Isn't this what you wear every day?"
    hide rajah
    show duras blush at zoom_center2
    md "Not quite.... I'm dressed up as someone from a different planet!"
    hide duras
    show ether base at zoom_center
    e "{alpha=0.5}{i}quietly{/i}{/alpha} Earth?"
    hide ether
    show duras base at zoom_center2
    md "What was that, Ether?"
    hide duras
    show ether coveringface at zoom_center
    e "{alpha=0.5}{i}embarrassed{/i}{/alpha} \nUm, I don't know if I'd be right-"
    hide ether
    show rajah base at zoom_center_r
    r "He said Earth."
    hide rajah
    show duras blush at zoom_center2
    md "Correct! I'm dressed up as one of Earth's generals, who later helped found Zebulon. When Zebulon was first colonized, they had a system called the Articles of Colonies that was loosely distributed across the Great Galaxy."
    md "However, the Articles of Colonies has many faults- including-"
    hide duras
    show ether upset at zoom_center
    e "{i}I can't keep up! I've barely written down the first ten words, and he's already moving on?{/i}"
    e "{i}I'll just have to write faster-{/i}"
    hide ether
    show duras base at zoom_center2
    md "Now, once we abolished the Articles of Colonies in 40XX-"
    hide duras
    show ether upset at zoom_center
    e "{i}40- when? I didn't hear the last part- It's fine, I'll just try copying everything down-{/i}"
    hide ether
    show duras base at zoom_center2
    md "And so, the first government resembling what we have today has three branches, the Legistlative, Executive, and Judicial branches-"
    hide duras
    show ether upset at zoom_center
    e "{i}Why is he moving around so much?{/i}"
    hide ether
    show duras base at zoom_center2
    md "Yes, Blaire, excellent point! Everyone, be sure to jot that down-"
    hide duras
    show ether upset at zoom_center
    e "{i}What did she even say? I couldn't catch it-{/i}"
    hide ether
    show duras base at zoom_center2
    md "No, no, that's not quite what happened, Roger. See, General Spike did end up leading the entire planet, but he set the framework."
    hide duras
    show ether coveringface at zoom_center
    e "{i}There's so much happening and I can't focus on the slides- There's too much color and too many voices-{/i}"
    hide ether
    show duras base at zoom_center2
    md "Onto our last section, the Executive branch was headed by someone named the President, who attempted a coupe to assassinate the head Generals-"
    md "Yes, Danny. That is precisely what happened! There you go, Roger, that's how-"
    hide duras
    show ether upset at zoom_center
    e "{i}I'm losing track of everything..... I want Mr. Duras to stop moving around so much- and for everyone to be quiet-{/i}"
    hide ether
    show duras base at zoom_center2
    md "Alright, class, that wraps our notes for today! I'll pass out a worksheet so you can practice applying what you learned today. It's due at the end of class!"
    md "And remember, class-"
    hide duras
    show ether upset at zoom_center
    e "{i}We have a worksheet for this?? I was so distracted that I didn't get half the notes down!{/i}"
    hide ether
    show rajah base at zoom_center_r
    r "Psst. Ether."
    hide rajah
    show ether coveringface at zoom_center
    e "{i}What am I going to do-{/i}"
    hide ether
    show rajah nervous at zoom_center_r
    r "Ether, pal, you in there?"
    hide rajah
    show ether base at zoom_center
    e "{alpha=0.5}{i}shaking himself out of the daze{/i}{/alpha}"
    e "Yes?"
    hide ether
    show rajah base at zoom_center_r
    r "How much of the notes did you get down?"
    hide rajah
    show ether base at zoom_center
    e "Um....."
    hide ether
    show rajah nervous at zoom_center_r
    r "Dang, you wrote down less than me! Nevermind, I didn't realize you were more behind than I was-"
    hide rajah
    show ether upset at zoom_center
    e "{i}Yeah, I was behind, wasn't I...{/i}"
    jump choosehelp
    return

label choosehelp:
    scene bg govclassroom
    show rajah base at zoom_center_r
    # Government teacher assigns a worksheet on the 3 branches of government, specifically on its functions. Ether, who didn’t get the notes down, struggles to complete it
    r "Oh, there's the worksheet. It doesn't look too long...."
    hide rajah
    show ether base at zoom_center
    e "{alpha=0.5}{i}takes the paper, looking at the first question{/i}{/alpha}"
    e "{i}What is the purpose of the Legislative Branch?{/i}"
        #note - these lines may be inner monologue, may need to be italicized
    e "Oh, I was in the middle of writing down the branch name before Mr. Duras moved on... Maybe I can come back to it later?"
    e "Next question: {i}How many departments does the Executive Branch control?{/i}"
    hide ether
    show ether upset at zoom_center
    e "I... didn't even get to writing that part in the notes either...."
    hide ether
    show ether base at zoom_center
    e "Question after: {i}Provide an example of when the Judicial branch's judgement influenced an Executive Order..{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}Um.... I can't answer any of these questions at all... I should probably ask for help... Maybe Rajah would know?{/i}"
    hide ether
    show ether base at zoom_center
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
    scene bg govclassroom
    show ether base at zoom_center
    e "Hey, Blaire-"
    hide ether
    show blaire base at zoom_center_b
    b "Yeah?"
    hide blaire
    show ether upset at zoom_center
    e "Um... could you help me with the worksheet?"
    hide ether
    show blaire annoyed at zoom_center_b
    b "The worksheet? I finished it in ten minutes because it was so easy!"
    hide blaire
    show ether base at zoom_center
    e "{i}It was easy?{/i}"
    e "Do you remember what the answer to the first question was?"
    hide ether
    show blaire annoyed at zoom_center_b
    b "To make laws, obviously. Mr. Duras just explained that 'Legislative' means relating to the law."
    hide blaire
    show ether upset at zoom_center
    e "He did? I didn't hear him..."
    hide ether
    show blaire annoyed at zoom_center_b
    b "Really? You probably weren't paying attention then."
    hide blaire
    show ether upset at zoom_center
    e "Oh.... um, would you happen to know the answer to the next question too?"
    hide ether
    show blaire base at zoom_center_b
    b "The Departments of the Executive Branch?"
    hide blaire
    show ether base at zoom_center
    e ".... Yes?"
    hide ether
    show blaire annoyed at zoom_center_b
    b "I thought that part was pretty self-explanatory, but since you seem to be a little slow, why don't you tell me how many Departments the school works with?"
    hide blaire
    show ether base at zoom_center
    e "... The school..?"
    e "What does that have to do with the government?"
    hide ether
    show blaire base at zoom_center_b
    b "Well-"
    jump turn_in_unfinished_work
    return

label ask_duras_choice:
    scene bg govclassroom
    show ether base at zoom_center
    e "Maybe I can ask Mr. Duras for help...."
    e "{alpha=0.5}{i}gets up{/i}{/alpha}"
    e "{alpha=0.5}{i}walks over to Mr. Duras' desk{/i}{/alpha}"
    e "Mr. Duras?"
    hide ether
    show duras blush at zoom_center2
    md "{alpha=0.5}{i}looking up from his work{/i}{/alpha}"
    hide duras
    show duras base at zoom_center2
    md "Ah, Ether! How can I help you?"
    hide duras
    show ether base at zoom_center
    e "Um, I'm really confused about the worksheet because I didn't get all the notes down."
    hide ether
    show duras base at zoom_center2
    md "I see. Why don't I go over the questions with you, then?"
    hide duras
    show ether base at zoom_center
    e "{alpha=0.5}{i}nods{/i}{/alpha}"
    hide ether
    show duras base at zoom_center2
    md "Remind me what the first one is?"
    hide duras
    show ether base at zoom_center
    e "What is the purpose of the Legislative Branch?"
    hide ether
    show duras base at zoom_center2
    md "Alright, Ether, think of it this way. Where does the word 'legislative' come from?"
    hide duras
    show ether upset at zoom_center
    e "I.. don't know."
    hide ether
    show duras base at zoom_center2
    md 'Well, the word comes from the Latin word {i}latus{/i}, which means "to carry or bring". Then, that word eventually gave way to another word, {i}lator{/i}. That is the {i}lator{/i} part of the word {i}legislator{/i}.'
    hide duras
    show ether upset at zoom_center
    e "{i}He's moving his hands a lot again...{/i}"
    hide ether
    show duras base at zoom_center2
    md 'Now, "{i}legis{/i}" part of the word "legislator" comes from the Roman concept of {i}legis latio{/i}, which is the act of enacting law. And the "ator" simply describes someone who does so. Now, if you put those two together, what do you suppose they represent?'
    hide duras
    show ether base at zoom_center
    e ".. Legislator?"
    hide ether
    show duras base at zoom_center2
    md 'That is true, but we are trying to find the meaning of the word. Think about it. You have the law, and the the word "to carry or bring". What do you think a legislator would do?'
    hide duras
    show ether base at zoom_center
    e "Carry the law?"
    hide ether
    show duras blush at zoom_center2
    md "Precisely! That answers your first question."
    hide duras
    show ether base at zoom_center
    e "The Legislative Branch.. carries the law?"
    e "{i}How does that even make sense? How does the law get carried?{/i}"
    hide ether
    show duras base at zoom_center2
    md "See. Ether, the Legislative branch-"
    hide duras
    show duras unsettled at zoom_center2
    md "No, Roger, you may not use the restroom. There are only five more minutes left of class!"
    md "No, don't tell me you need go now! I'm quite sure you can wait!"
    hide duras
    show duras base at zoom_center2
    md "{alpha=0.5}{i}turns back to Ether and smiles{/i}{/alpha}"
    md "I'll have to start wrapping up now, Ether. Why don't you go back to your seat and work through the rest of the questions?"
    md "{alpha=0.5}{i}gets up and leaves Ether by his desk{/i{/alpha}}"
    hide duras 
    show ether upset at zoom_center
    e "Oh... kay...."
    e "{alpha=0.5}{i}returns to his seat{/i}{/alpha}"
    jump turn_in_unfinished_work
    return

label do_alone_choice:
    scene bg govclassroom
    show ether base at zoom_center
    e "{i}Oh, I can probably wait until he comes back. I'll just work through the rest of it.{/i}"
    e "{i}re-reading the first question: What is the purpose of the Legislative Branch?{/i}"
    e "{i}Legislative.... that's a long word. It looks a little weird on paper.{/i}"
    e "{i}So what does this branch do?{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I don't remember....{/i}"
    e "{i}The group behind me is talking really loudly.. Focus, Ether, you have work to do.{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}But I can't.. Argh. Legislative. Legislative. What does it do?{/i}"
    e "{i}C'mon, maybe the information is just lodged in your brain, and doesn't want to come out.{/i}"
    e "{i}Think, Ether, think. Ignore the noise, because it shouldn't affect you. Cut it out.{/i}"
    e "{i}I've been staring at this paper for so long that 'Legislative' doesn't even look like a word anymore.{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Maybe it'll come to me later. I really wish I could work with Rajah, but I don't even know where he went...{/i}"
    e "{i}Next question. Departments of the Executive Branch.{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I.. also can not think of anything for that question. This is amazing.{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Maybe I'll just go back to the first one...{/i}"
    jump turn_in_unfinished_work
    return

label turn_in_unfinished_work:
    scene bg govclassroom
    show duras base at zoom_center2
    md "Alright, class, our time together for today is coming to an end. Please finish up your last thoughts and prepare to turn in what you have finished."
    hide duras
    show ether base at zoom_center
    e "I haven't finished it, though..."
    hide ether
    show duras base at zoom_center2
    md "I'm coming around with today's homework. It is similar to today's worksheet, so it shouldn't take you too long to finish."
    md "On the way out, please drop off the classwork from today and have a great rest of your day!"
    hide duras
    show ether upset at zoom_center
    e "{i}Oh no.....{/i}"
    hide ether
    show rajah base at zoom_center_r
    r "Ether!"
    hide rajah
    show ether base at zoom_center
    e "Oh, hi Rajah. I was looking for you earlier."
    hide ether
    show rajah base at zoom_center_r
    r "Ah. Well, I went to ask Danny for help. She was able to talk me and Gabby through most of it, but I still don't fully understand every single word that came out of her mouth."
    hide rajah
    show rajah annoyed at zoom_center_r
    r "Why'd the government have to be so complicated?"
    hide rajah
    show ether base at zoom_center
    e "You should ask General Spike that."
    hide ether
    show rajah annoyed at zoom_center_r
    r "These old geezers just wanted to make it hard to understand on purpose! Well, anyway, we should turn in the worksheet now. Don't forget to grab the homework! I'll wait for you outside."
    jump end_of_day1
    return

label end_of_day1:
    # Later.. (afterschool):
    scene bg blackscreen
    s "Later afterschool.."
    scene bg street
    show ether base at zoom_center
    e "{i}Finally, I get to go home.....{/i}"
    e "{i}No homework today! Wait, no... I have that government worksheet to do, dang it!{/i}"
    e "{i}Mr. Duras said it wasn't supposed to take too long, though, so maybe it'll be easy.{/i}"
    e "{i}But he also said that it was almost exactly like the worksheet, and I didn't finish that..{/i}"
    e "{i}Ack. I'd better get home to finish it, then.{/i}"
    # ------------- (reaches home)
    scene bg blackscreen
    s "Reaches home"
    scene bg househallway
    show ether happy at zoom_center
    e "{i}Home sweet home..{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}I'd better get started on that worksheet.{/i}"
    e "{alpha=0.5}{i}goes up to his room{/i}{/alpha}"
    scene bg bedroom
    show ether base at zoom_center
    e "{alpha=0.5}{i}pulls out his homework{/i}{/alpha}"
    e "Alright, first question. How does the Bureaucracy interact with the 3 branches of government?"
    hide ether 
    show ether annoyed at zoom_center
    e "I think I remember writing this down in my notes. It was in here somewhere..."
    hide ether
    show ether base at zoom_center
    e "Aha! The Bureaucracy is primarily kept in check by the Legislative and Executive Branches."
    e "Er, okay. Did I write down any more details?"
    e "..... The rest of this page is blank...."
    e "Maybe I can just google it and write it down!" 
    e "Let's see.. {i}The Executive Branch appoints the heads of each individual department, and the Legislative Branch controls the funding and regulations for each department. Thus, the Executive Branch has a lasting influence on each of the agencies, and the Legislative Branch is able to influence the agenda of each separate department.{/i}"
    e "Okay, so the Executive Branch picks leaders. The Legislative Branch gives them the money and rules. That's easy enough."
    e "Next question: {i}Explain how the interactions between the Bureaucracy and the 3 branches of Government encourage federalism.{/i}"
    e "Federalism? Did Mr. Duras even talk about that?"
    hide ether
    show ether upset at zoom_center
    e "It's not in my notes, so I'll just google it again..."
    hide ether
    show ether base at zoom_center
    e "Federalism: {i}a principle or system of government in which several states form a unity but remain independent in internal affairs{/i}. Why are there so many big words?"
    e 'Federalism: simple definition. "{i}A system where power is divided and shared between a central government and state governments{/i}."'
    e "Oh. Okay. But isn't the Bureaucracy and the 3 branches just government?"
    e "Maybe I'll just put the entire question into Google and see what it gives me.."
    e "That is.... a lot of words, that does not answer my question. I'll look up a YouTube video. Maybe that'll help."
    e "These videos are all over an hour long! {i}Federalism Explained in Detail-- Specifically for Scholars{/i}. {i}The Government's Faults{/i}. This one looks helpful: {i}How the Government Interacts with the States Explained{/i}. It's only around 10 minutes, too."
    hide ether
    show ether annoyed at zoom_center
    e "Of course the first thing it shows me is an ad.. Skip-"
    e "There's another one??"
    e "And a third... 1 minute unskippable should be criminal..."
    hide ether
    show ether base at zoom_center
    e "Okay! Finally, the video's starting!"
    e "Why does it start with a sponsorship?"
    e "Fine, I'll just skip that too... fast forward, fast forward, fast forward-"
    hide ether
    show ether annoyed at zoom_center
    e "The sponsorship is still going?"
    e "Fast forward, fast forward, fast forward..."
    e "Why does it go into the 5 minute mark? That's already half the video!"
    e "Fast forward some more- Here's what I'm looking for!"
    hide ether
    show ether base at zoom_center
    v "{i}The government and its 3 branches encourage federalism by interacting with the states! That's all for today! Like if you enjoyed, and subscribe for more!{/i}"
    e "Interacting with the states? Of course they interact with the states- that's what federalism is, right?"
    hide ether
    show ether coveringface at zoom_center
    e "{alpha=0.5}{i}groans{/i}{/alpha}"
    hide ether 
    show ether annoyed at zoom_center
    e "I really wish I had taken more notes...."
    hide ether
    show ether happy at zoom_center
    e "Wow, the comments are just as annoyed as I am, hah..."
    hide ether
    show ether base at zoom_center
    e "Maybe I need a break and do something else for a little bit."
    e "Let's see how my grades are doing."
    hide ether
    show ether phone at zoom_center
    e "96 percent (A) in Calculus, 94 percent (A) in Mandarin... 90.2 percent (A-) in Government? How did my grade drop 5 percent in a day? It used to be almost 96 percent..."
    hide ether
    show ether upset at zoom_center
    e "Oh, Mr. Duras gave me a C on the classwork... 70/100... I didn't know it was weighted that heavily! Dang it.... What am I supposed to do?"
    e "What if my parents find out about this?!"
    hide ether
    show ether coveringface at zoom_center
    e "They're going to be so mad...."
    e "I didn't spend all year keeping it at an A just for it to drop right before the marking period ends!"
    hide ether
    show ether upset at zoom_center
    e "I'll have to ask Mr. Duras if I can make up the credit. And I can't mess up any more assignments, or it'll drop to a B...."
    e "I'll just try finishing the homework in the meantime...."
    jump start_day2
    return

label start_day2:
    scene bg blackscreen
    s "The next day.."
    scene bg schoolhallway
    show ether base at zoom_center
    e "{alpha=0.5}{i}arriving at school{/i}{/alpha}"
    e "{i}Oh, I'm early. Let's see if Mr. Duras is here yet.{/i}"
    e "{alpha=0.5}{i}walks down the hall{/i}{/alpha}"
    hide ether
    show ether happy at zoom_center
    e "{i}Great, his door is open. He must be here!{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Rajah's standing right next to door, too. Maybe I can compare answers to the homework with him while I wait for the bell to ring.{/i}"
    menu:
        "Ask Mr. Duras if they can redo worksheet":
            jump ask_duras_to_redo
        "Ask Rajah is he finished the homework":
            jump ask_rajah_if_finished
    return

label ask_duras_to_redo:
    scene bg schoolhallway
    show ether base at zoom_center
    e "{i}I can ask Rajah what he got on the homework during class. I'd best ask Mr. Duras now, since he might busy later.{/i}"
    e "{alpha=0.5}{i}enters the room{/i}{/alpha}"
    scene bg govclassroom
    show duras base at zoom_center2
    md "Good morning, Ether. You're early today."
    hide duras
    show ether base at zoom_center
    e "Hello, Mr. Duras."
    hide ether
    show duras base at zoom_center2
    md "How are you doing?"
    hide duras
    show ether annoyed at zoom_center
    e "{i}I really just want to get to the point already...{/i}"
    hide ether
    show ether base at zoom_center
    e "Good, uh, how about you?"
    hide ether
    show duras base at zoom_center2
    md "I'm doing just fine. Is there anything you needed?"
    hide duras
    show ether base at zoom_center
    e "...."
    e "I was checking my grades yesterday and I saw that you graded the worksheet from yesterday."
    hide ether
    show duras base at zoom_center2
    md "Yes, I did. What about it?"
    hide duras
    show ether base at zoom_center
    e "Is there any way for me to make up the points I lost on the worksheet?"
    hide ether
    show duras unsettled at zoom_center2
    md "You had nearly 45 minutes to complete the worksheet, and there were only three questions on it."
    hide duras
    show ether annoyed at zoom_center
    e "Yes, I know, but I didn't get the notes down because you were going too fast."
    hide ether
    show duras base at zoom_center2
    md "Have you gotten the notes from anyone else?"
    hide duras
    show ether base at zoom_center
    e "..."
    e "No..."
    hide ether
    show duras base at zoom_center2
    md "Isn't Blaire at your table? You could've asked her for help. She finished the worksheet in 15 minutes. She should've gotten most, if not all the notes down."
    hide duras
    show ether base at zoom_center
    e "{alpha=0.5}{i}nods{/i}{/alpha} I'll ask her then."
    e "Could I still redo the worksheet, though?"
    hide ether
    show duras base at zoom_center2
    md "Unfortunately, no. But I encourage you to study the notes, since we'll have multiple assignments on them in the coming weeks."
    hide duras
    show ether annoyed at zoom_center
    e "Okay....."
    hide ether
    show duras unsettled at zoom_center2
    md "Oh, dear, the bell's about to ring in five minutes. Get ready for class, Ether, while I gather the rest of the class."
    md "{alpha=0.5}{i}leaves the room{/i}{/alpha}"
    jump day2_start_class
    return

label ask_rajah_if_finished:
    scene bg schoolhallway
    show ether base at zoom_center
    e "Hi Rajah-"
    hide ether
    show rajah base at zoom_center_r
    r "{alpha=0.5}{i}looking up{/i}{/alpha}"
    r "Yo."
    hide rajah
    show ether base at zoom_center
    e "Did you finish the homework from yesterday?"
    hide ether
    show rajah base at zoom_center_r
    r "{alpha=0.5}{i}thinking for a moment{/i}{/alpha}"
    r "You mean the worksheet?"
    hide rajah
    show ether base at zoom_center
    e "Yeah."
    hide ether
    show rajah nervous at zoom_center_r
    r "No, I didn't. I didn't even finish the classwork either. Mr. Duras was going wayyy too fast."
    hide rajah
    show ether upset at zoom_center
    e "I know, right? And he was moving around so much that I kept getting distracted."
    hide ether
    show rajah annoyed at zoom_center_r
    r "That man was talking at the speed of light."
    hide rajah
    show blaire annoyed at zoom_center_b
    b "Really?"
    hide blaire
    show rajah annoyed at zoom_center_r
    r "Not-"
    hide rajah
    show rajah nervous at zoom_center_r
    r "{alpha=0.5}{i}sighs{/i}{/alpha}"
    hide rajah
    show rajah base at zoom_center_r
    r "Hello, Blaire."
    hide rajah
    show blaire base at zoom_center_b
    b "I thought Mr. Duras was talking just fine. It wasn't that hard to understand."
    hide blaire
    show rajah annoyed at zoom_center_r
    r "Uh huh."
    hide rajah
    show blaire annoyed at zoom_center_b
    b "Mr. Duras gave us detailed explanations for everything, and practically gave us all the answers on the worksheet. I even finished it with 15 minutes left to spare. Maybe you guys weren't trying hard enough."
    hide blaire
    show duras base at zoom_center2
    md "Alright, class, come on in. The bell will ring soon, so let's get started for today."
    jump day2_start_class
    return

label day2_start_class:
    scene bg govclassroom
    show ether base at zoom_center
    e "{alpha=0.5}{i}sits down in his seat{/i}{/alpha}"
    hide ether
    show duras base at zoom_center2
    md "Alright, class, we're going to skip the warm-up for today and continue where we left off-"
    md "Yes, Rajah?"
    hide duras
    show rajah blushing at zoom_center_r
    r "Mr. Duras, could you try going a little slower this time?"
    hide rajah
    show duras unsettled at zoom_center2
    md "{alpha=0.5}{i}hesitating{/i}{/alpha}"
    md "Well, Rajah, we have a lot to get through, but you can let me know if you need extra time to get the notes down."
    hide duras
    show duras base at zoom_center2
    md "So, last we left off on how the 3 branches of government were established. Today, we're going to get into the important cases concerning the 3 branches."
    md "But first! Let's go over the answers to yesterday's classwork."
    hide duras
    show ether base at zoom_center
    e "{i}Okay, so this was all the stuff I didn't know yesterday. I need to write this down.{/i}"
    hide ether
    show duras base at zoom_center2
    md "Who can tell me what the Legislative Branch does?"
    md "Yes, Blaire."
    hide duras
    show blaire base at zoom_center_b
    b "The Legislative branch creates laws."
    hide blaire
    show ether upset at zoom_center
    e "{alpha=0.5}{i}furiously scribbling{/i}{/alpha}"
    hide ether
    show ether base at zoom_center
    e "{i}Legislative Branch. Creates laws. Got it.{/i}"
    hide ether
    show duras base at zoom_center2
    md 'Excellent! The word "Legislative" means to "do with the law". Alright, now who can tell me how many departments the Executive Branch controls?'
    md "That's correct, Danny! But please raise your hand next time."
    hide duras
    show ether coveringface at zoom_center
    e "{i}I couldn't even hear what Danny said...{/i}"
    hide ether
    show duras base at zoom_center2
    md "For those who couldn't hear Danny, the Executive Branch controls 15 departments. You'll be required to name some of these departments on the upcoming quiz. Who can name an Executive Department? Shout it out!"
    hide duras
    show ether upset at zoom_center
    e "{i}There's a quiz on this?!{/i}"
    e "{i}There's so many people shouting that I can't even hear any single one of the departments...{/i}"
    hide ether
    show duras base at zoom_center2
    md "I see you all will do just excellent on the quiz!"
    hide duras
    show ether coveringface at zoom_center
    e "{i}No, I won't....{/i}"
    hide ether
    show duras base at zoom_center2
    md "Now, how about an example of how the Judicial Branch's judgment influenced an Executive Order?"
    hide duras
    show ether base at zoom_center
    e '{i}What does he mean when he says "influenced"? How did it affect the Executive Order?{/i}'
    hide ether
    show duras base at zoom_center2
    md "Yes, Blaire, that {i}is{/i} an example... There was a time when the Judicial Branch declared the president's tariffs unconstitutional! What did the president do afterward?"
    hide duras
    show rajah nervous at zoom_center_r
    r "{alpha=0.5}{i}whispering{/i}{/alpha}"
    r "Ether, do you get the unconstitutional part?"
    hide rajah
    show ether base at zoom_center
    e "No...... Maybe you should ask him?"
    hide ether
    show rajah blushing at zoom_center_r
    r "{alpha=0.5}{i}raises hand{/i}{/alpha}"
    hide rajah
    show duras base at zoom_center2
    md "Yes, Rajah?"
    hide duras
    show rajah nervous at zoom_center_r
    r "Why is it important that the president's actions were declared unconstitutional?"
    hide rajah
    show duras base at zoom_center2
    md 'Well, declaring something "unconstitutional" means that it goes against the Constitution!'
    hide duras
    show rajah nervous at zoom_center_r
    r "......"
    hide rajah
    show duras unsettled at zoom_center2
    md "Is that clear?"
    hide duras
    show rajah nervous at zoom_center_r
    r "..Why is it important that something is against the Constitution?"
    hide rajah
    show duras base at zoom_center2
    md "Ah! We covered this last class. Our government principles run by the Constitution, and if something is declared against the Constitution, it goes against everything the government stands for."
    hide duras
    show rajah nervous at zoom_center_r
    r "Oh, yeah, that makes... sense...."
    r "{alpha=0.5}{i}to Ether{/i}{/alpha}"
    hide rajah
    show rajah blushing at zoom_center_r
    r "I felt so stupid asking that, and I'm still not sure I understand it..."
    hide rajah
    show duras base at zoom_center2
    md "Great! Now, back to what Blaire was saying. In the case against the tariffs, did the president take any action?"
    md "Right, Roger, they didn't. This case wouldn't necessarily have been directly affected by the Judicial Branch's judgement, but I would've accepted that as an answer if you clarified that the Executive Order hadn't changed after the Judicial Branch's judgment."
    md "Do you have another question, Rajah?"
    hide duras
    show rajah base at zoom_center_r
    r "Wait, so if the Judicial Branch couldn't do anything, then what about the Executive Order changed?"
    hide rajah
    show duras blush at zoom_center2
    md "Nothing!"
    hide duras
    show rajah annoyed at zoom_center_r
    r "Huh??"
    hide rajah
    show duras base at zoom_center2
    md "All the Judicial Branch does is pass judgement. The branches that enforce that judgement are the Legislative and Executive."
    hide duras
    show rajah base at zoom_center_r
    r "So... wouldn't the other branches just be able to ignore the Judicial Branch?"
    hide rajah
    show duras base at zoom_center2
    md "In essence, yes."
    hide duras
    show rajah nervous at zoom_center_r
    r ".. If it can be ignored...."
    r "... then why does it exist?"
    s "{alpha=0.5}{i}the class laughs{/i}{/alpha}"
    hide rajah
    show rajah blushing at zoom_center_r
    r "{alpha=0.5}{i}embarrassed{/i}{/alpha}"
    r "Never asking again."
    hide rajah
    show duras base at zoom_center2
    md "And that's why our lesson today will be about the cases that demonstrate just how important the Judicial Branch is. So, without any further ado, let's jump into our first case!"
    md "The first one we'll be talking about is Shaw v. Rucker. The case goes like this: When Zebulon was first split into its colonies, the population of the colony decided how many votes they would get out of the entire planet..."
    hide duras
    show ether annoyed at zoom_center
    e "{alpha=0.5}{i}whispering{/i}{/alpha}"
    e "Mr. Duras keeps accidentally blocking the screen with his hands..."
    hide ether
    show rajah annoyed at zoom_center_r
    r "Hey, you could tell him to stop. I don't wanna look stupid again."
    hide rajah
    show ether base at zoom_center
    e "You didn't look that dumb... Doesn't Mr. Duras' constant walking around bother you?"
    hide ether
    show rajah blushing at zoom_center_r
    r "No one else has a problem with it, so I guess it's just us."
    hide rajah
    show ether base at zoom_center
    e "Did you get the rest of the notes down?"
    hide ether
    show rajah base at zoom_center_r
    r "Like, a bit, I'd say? Not all of it. Here, you can take a look."
    hide rajah
    show duras base at zoom_center2
    md ".... Shaw v. Rucker abolished the use of gerrymandering by species! Ether, are you paying attention?"
    hide duras
    show ether upset at zoom_center
    e "Uh, yes, sir."
    hide ether
    show duras base at zoom_center2
    md "Good, good. Could you explain to me, in your words, why Shaw v. Rucker matters?"
    hide duras
    show ether base at zoom_center
    e "It.... didn't let us group certain districts?"
    hide ether
    show duras base at zoom_center2
    md "Close. It didn't let us group certain districts to skew the vote. Now, next, we'll go onto the case Zebulon v. Lopez.... Oh, dear, this room is getting a little cold. I'll turn on the heater before we go on."
    md "{alpha=0.5}{i}click{/i}{/alpha}"
    md "Alright, so back to Zebulon v. Lopez, where a young boy brought weapons to school..."
    hide duras
    show ether upset at zoom_center
    e "{i}I can't listen to what he's saying AND write down the notes- it's either one or the other! And that heater is really loud...... Argh. No, I just need to focus.{/i}"
    hide ether
    show duras base at zoom_center2
    md "... The Supreme Courts initially couldn't decide of Lopez had broken the state or federal law, so it was undecided whether he would stand trial under the nation or the state jurisdiction. Remember, jurisdiction is---"
    hide duras
    show ether coveringface at zoom_center
    e "{i}I can still hear the heater grumbling in the background.. it's so distracting. I'm getting a little sweaty too. I'll take off my jacket.{/i}"
    hide ether
    show duras base at zoom_center2
    md "The government got into a scuffle with the colony Lopez had been from. It had almost been like this-"
    md "{alpha=0.5}{i}walking to a map by the board{/i}{/alpha}"
    md "So here was the colony Lopez was from. The government met state officials here, here, and here to-"
    hide duras
    show ether upset at zoom_center
    e "{i}What am I supposed to be looking at? He's pointing at the map too quickly- You know what, maybe I'll just focus on the notes instead.{/i}"
    e "{i}But I can't even focus on what I'm writing down because Mr. Duras keeps talking and tapping the map so loudly... and this room keeps getting warmer....{/i}"
    hide ether
    show duras base at zoom_center2
    md ".. And that'll wrap up the lecture for today."
    hide duras
    show ether base at zoom_center
    e "{i}Finally. We're done.{/i}"
    jump worksheet_assigned
    return

label worksheet_assigned:
    scene bg govclassroom
    show duras base at zoom_center2
    md "Now, it's time for you to apply what you learned in this worksheet I'm about to pass out! It'll help you prepare for the quiz next week."
    hide duras
    show ether upset at zoom_center
    e "{i}THE QUIZ IS NEXT WEEK?! Didn't we just start learning this stuff?{/i}"
    hide ether
    show duras base at zoom_center2
    md "You should be able to finish the worksheet before the end of class. It is just as long as the last one."
    #insert existential dread here
    hide duras
    show ether upset at zoom_center
    e "{alpha=0.5}{i}reading the questions...{/i}{/alpha}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I really can't do this alone…. I'll need help.......{/i}"
    menu:
        "Ask Blaire again":
            jump ask_blaire_again
        "Ask Mr. Duras again":
            jump ask_duras_again
    return

label ask_blaire_again:
    scene bg govclassroom
    show ether base at zoom_center
    e "Blaire..?"
    hide ether
    show blaire annoyed at zoom_center_b
    b "{alpha=0.5}{i}distantly talking with other people{/i}{/alpha}"
    hide blaire
    show ether upset at zoom_center
    e "{i}She looks busy… maybe I shouldn't bother her...{/i}"
    e "{i}But how am I going to prepare for the test if I don't ask for help{/i}"
    e "{i}No, I can do this....{/i}"
    hide ether
    show ether base at zoom_center
    e "Blaire!"
    hide ether
    show blaire base at zoom_center_b
    b "And then I-"
    b "{alpha=0.5}{i}turns{/i}{/alpha}"
    b "Oh, hi again, Ether."
    hide blaire
    show ether upset at zoom_center
    e "{i}I really don't want to take up her time... I already feel bad for asking....{/i}"
    e "Can I borrow your notes?"
    hide ether
    show blaire base at zoom_center_b
    b "{alpha=0.5}{i}handing over the notebook{/i}{/alpha}"
    b "Don't tell me you didn't understand today's class either?"
    hide blaire
    show blaire annoyed at zoom_center_b
    b "Ugh, fine, here you go. Knock yourself out."
    hide blaire
    show ether base at zoom_center
    e "{i}Her notes are.... A little messy. But she did write down a lot more than I did, so this should be helpful.{/i}"
    e "{i}The first question asks about the case Shaw v. Rucker... I know it was something about gerrymandering, but what was the difference between that and redistricting? They both redraw the district lines...{/i}"
    e "{i}All she wrote was that it ruled against racial gerrymandering. I'll just write that down, then.{/i}"
    e "{i}The next question is about the independent regulatory commissions and executive regulatory commissions... her notes have a lot less words than the slides...{/i}"
    hide ether
    show blaire base at zoom_center_b
    b "You're not still struggling, are you?"
    hide blaire
    show ether upset at zoom_center
    e "Uh... well..."
    hide ether
    show blaire base at zoom_center_b
    b "Here, just copy mine. It'll make sense afterward."
    hide blaire
    show ether base at zoom_center
    e "Oh, okay... thanks..."
    e "{i}I guess I'll at least get a good grade on this worksheet, so my grade won't drop any lower yet, but will it matter if I fail the quiz?{/i}"
    e "{i}Blaire said it would make sense once I read through it properly. I'll copy down her notes too, since she lent me her notebook already.{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{alpha=0.5}{i}visible frustration{/i}{/alpha}"
    e "{i}There are too many people talking, and I can't even comprehend what I'm reading.... it's too loud...{/i}"
    e "{i}How did Blaire manage to get this done when the room's so loud?{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}Is it just me? Is there something wrong with me that makes it so hard to do anything in this class?{/i}"
    hide ether
    show blaire base at zoom_center_b
    b "Ether-"
    hide blaire
    show ether upset at zoom_center
    e "{i}I wish I was.. I don't know, smart enough to know how to handle this stuff?{/i}"
    hide ether
    show blaire annoyed at zoom_center_b
    b "Ether!"
    hide blaire
    show ether upset at zoom_center
    e "Yes? Sorry, I was trying to understand your notes."
    hide ether
    show blaire base at zoom_center_b
    b "It's time to turn in the worksheet. Did you finish yours?"
    hide blaire
    show ether base at zoom_center
    e "Yes, thank you."
    hide ether
    show ether coveringface at zoom_center
    e "{i}But I was only able to finish it with help....{/i}"
    e "{i}What does that say about me as a student? Am I just slow?{/i}"
    jump worksheet_turned_in
    return

label ask_duras_again:
    scene bg govclassroom
    show ether base at zoom_center
    e "Mr. Duras, could I get some help on the worksheet?"
    hide ether
    show duras unsettled at zoom_center2
    md ".....Ether, how long have you spent on the worksheet?"
    hide duras
    show ether base at zoom_center
    e "I read the questions, and tried to reread my notes, but I didn't fully understand what happened for the Shaw v. Rucker case in the first question."
    hide ether
    show duras base at zoom_center2
    md "Why don't you bring your notebook over and tell me what you wrote down for that case?"
    hide duras
    show ether base at zoom_center
    e "I wrote down that it ruled against gerrymandering, but I didn't get enough down to understand why that was the case."
    hide ether
    show duras base at zoom_center2
    md "Were you really paying attention during class?"
    hide duras
    show ether upset at zoom_center
    e "Yes. But there was just a lot going on, and I couldn't hear what you were trying to say while you were explaining the slides, and it was really hard for me to focus."
    hide ether
    show duras unsettled at zoom_center2
    md "Are you sure? I see you talking to Rajah quite often while I am lecturing."
    hide duras
    show ether base at zoom_center
    e "It's because I was trying to get the notes from him-"
    hide ether
    show duras base at zoom_center2
    md "I am beginning to believe that perhaps you were not trying at all. If you are having side conversations in class, it is only natural that you would lose focus. You can not expect me to help you when you are not making a concerted effort to do well in class."
    hide duras
    show ether base at zoom_center
    e "But I-"
    hide ether
    show duras base at zoom_center2
    md "Now, if you'll excuse me, Ether, I see Roger has his hand raised. I will come back to you once you have shown me that you are trying in this class."
    hide duras
    show ether base at zoom_center
    e "But.. I am.."
    hide ether
    show duras base at zoom_center2
    md "{alpha=0.5}{i}walking away{/i}{/alpha}"
    hide duras
    show ether upset at zoom_center
    e "... trying...."
    e "{alpha=0.5}{i}walking back to seat{/i}{/alpha}"
    e "{i}I didn't understand the notes either, and I hadn't been talking to Rajah at all during that class....{/i}"
    e "{i}Am I wrong for asking for help?{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I guess it's my own fault I'm falling behind, huh?{/i}"
    hide ether
    show rajah base at zoom_center_r
    r "Ether! Ether!"
    hide rajah
    show ether base at zoom_center
    e "Yeah?"
    hide ether
    show rajah base at zoom_center_r
    r "Danny gave me all the answers to the worksheet. Here, copy them down while you still have time-"
    hide rajah
    show ether base at zoom_center
    e "Oh, thanks. Do you understand the answers, though?"
    hide ether
    show rajah blushing at zoom_center_r
    r "No. but I'd rather get a good grade on the worksheet right now and figure it out later. It's not like I'd understand it even if I asked Danny to explain every single one of them. Even Roger understood what Duras was trying to explain. I just gave up."
    hide rajah
    show ether base at zoom_center
    e "I don't know if that's.."
    hide ether
    show rajah base at zoom_center_r
    r "Just copy it down for now, ask questions later. You've got 10 minutes left to finish it."
    hide rajah
    show ether base at zoom_center
    e "{alpha=0.5}{i}while copying{/i}{/alpha}"
    hide ether
    show ether upset at zoom_center
    e "{i}I don't like how little of this I understand....{/i}"
    e "{i}How has everyone else been able to understand it so far?{/i}"
    e "{i}At least I'm not the only one....{/i}"
    hide ether
    show rajah annoyed at zoom_center_r
    r "{alpha=0.5}{i}grumbling to himself{/i}{/alpha}"
    r "How was I supposed to explain how the judicial branch was important when it's been ignored so many times???"
    r "{alpha=0.5}{i}checking time{/i}{/alpha}"
    hide rajah
    show rajah base at zoom_center_r
    r "Ether! There's like 5 more minutes left of class. You done yet?"
    hide rajah
    show ether base at zoom_center
    e "Almost-"
    jump worksheet_turned_in
    return

label worksheet_turned_in:
    scene bg govclassroom
    show duras base at zoom_center2
    md "Okay class, our time for today has come to a close. Please turn in the worksheet and study for the quiz next class!"
    hide duras
    show rajah base at zoom_center_r
    r "Mr. Duras!"
    hide rajah
    show duras base at zoom_center2
    md "Yes, Rajah?"
    hide duras
    show rajah base at zoom_center_r
    r "Uh, is the quiz multiple choice?"
    hide rajah
    show duras base at zoom_center2
    md "Yes, there will multiple of those questions, but they will not make up a majority of the quiz since I would like to test your understanding of the content rather than your guessing abilities. Most of the test will be short-answer questions. It will also be closed-note."
    hide duras
    show rajah base at zoom_center_r
    r "How many questiions are there?"
    hide rajah
    show duras base at zoom_center2
    md "Ah, I'll have to check.... it should take you no longer than 45 minutes to finish, though."
    hide duras
    show rajah base at zoom_center_r
    r "Good to know."
    r "{alpha=0.5}{i}muttering to Ether{/i}{/alpha}"
    hide rajah
    show rajah nervous at zoom_center_r
    r "I am so flunking this quiz....."
    hide rajah
    show ether upset at zoom_center
    e "{alpha=0.5}{i}timidly raising hand{/i}{/alpha}"
    hide ether
    show duras unsettled at zoom_center2
    md "......."
    md "Yes, Ether?"
    hide duras
    show ether upset at zoom_center
    e "Will there be retakes or corrections on this quiz?"
    hide ether
    show duras base at zoom_center2
    md "..."
    md "No, there will not."
    md "Are there any other questions?"
    hide duras
    show ether upset at zoom_center
    e "{i}He looks annoyed with me....{/i}"
    e "{i}But I genuinely didn't understand any of the content, and I'll need help anyway...{/i}"
    hide ether
    show duras base at zoom_center2
    md "If there are no other questions, you are all dismissed. Please turn in the homework from yesterday and the worksheet from today in the box by the door. Have a good day, everyone, and remember to study!"
    hide duras
    show ether base at zoom_center
    e "{i}Okay... now, do I want to ask Mr. Duras for help?{/i}"
    menu:
        "Ask Mr. Duras for quiz help":
            jump ask_md_for_quiz_help
        "Give up on Mr. Duras entirely":
            jump give_up_on_md
    return

label ask_md_for_quiz_help:
    scene bg govclassroom
    show ether upset at zoom_center
    e "{i}I'm afraid to ask Mr. Duras for help... but I really don't want to get a bad grade on this quiz.{/i}"
    e "{i}Asking him for help can't be too bad. There's nothing for me to lose.{/i}"
    e "{alpha=0.5}{i}approaching the desk{/i}{/alpha}"
    e "Mr. Duras?"
    hide ether
    show duras base at zoom_center2
    md "Hello, Ether. How may I help you?"
    hide duras
    show ether base at zoom_center
    e "I want help understanding the content that will be on the quiz."
    hide ether
    show duras base at zoom_center2
    md "Alright."
    md "..."
    md "What is confusing to you?"
    hide duras
    show ether base at zoom_center
    e "The functions of the three branches are hard for me to understand, and even more to remember. I was wondering if you could post a study guide or practice questions like the ones on the quiz? Maybe even the slides you used?"
    hide ether
    show duras unsettled at zoom_center2
    md "Even if I were to post such resources for you, how could I be sure that you would use them?"
    hide duras
    show ether base at zoom_center
    e ".... What do you mean?"
    hide ether
    show duras unsettled at zoom_center2
    md "I have seen you consistently have side conversations during lecture. When you're given work time, you do not seem to use it wisely. From what I see, you only sit there. I also believe I saw you copying off one of your peers' papers."
    hide duras
    show ether upset at zoom_center
    e "I-"
    hide ether
    show duras unsettled at zoom_center2
    md "You may not cheat on the quiz, Ether. Whatever good you believe copying will do, get it out of your head. Copying is a student's way of benefitting from other people's work when you don't want to use the energy to do it yourself."
    hide duras
    show ether upset at zoom_center
    e "Mr. Duras, I understand that copying is wrong, but I didn't understand the content and I was afraid to get a bad grade on the worksheet and-"
    hide ether
    show duras base at zoom_center2
    md "Grades should not be worth sacrificing academic integrity for."
    hide duras
    show ether base at zoom_center
    e "Yes. I know. I understand."
    e "{i}He thinks I'm not trying at all.{/i}"
    e "Can you at least.... post the slides? So I can... catch up on the notes?"
    hide ether
    show duras unsettled at zoom_center2
    md "........"
    md "Fine, Ether. But I will remind you that I have no tolerance for cheating, and if I catch you doing so on the quiz, you will get a zero without any chance of redoing it."
    hide duras
    show ether base at zoom_center
    e "Yes... I know. I don't intend to."
    hide ether
    show duras base at zoom_center2
    md "I would hope not."
    md "Run along now, I'd like to eat my lunch. The slides are available on google classroom."
    hide duras
    show ether base at zoom_center
    e "The quiz is on everything we've covered so far, right?"
    hide ether
    show duras base at zoom_center2
    md "Yes. Have a good rest of your day, Ether."
    hide duras
    show ether base at zoom_center
    e "You too."
    e "{alpha=0.5}{i}turning to leave{/i}{/alpha}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}No wonder Rajah doesn't want to ask Mr. Duras for help anymore. Mr. Duras just makes me feel small and insignificant.{/i}"
    jump goes_home_to_study
    return

label give_up_on_md:
    scene bg govclassroom
    show ether upset at zoom_center
    e "{i}No, I don't want to bother him even more....{/i}"
    jump goes_home_to_study
    return

label goes_home_to_study:
    scene bg street
    show ether base at zoom_center
    e "{i}I have to go home to study for this quiz....{/i}"
    e "{i}Where do I even start?{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I am definitely not asking Mr. Duras for any sort of help from now on...{/i}"
    hide ether
    show rajah base at zoom_center_r
    r "Ether!"
    hide rajah
    show rajah nervous at zoom_center_r
    r "Hey, you look a little depressed. What're you thinking about?"
    hide rajah
    show ether upset at zoom_center
    e "Just worried about the quiz in Government... "
    hide ether
    show rajah nervous at zoom_center_r
    r "It's JUST a quiz. It'll probably be fine."
    hide rajah
    show ether upset at zoom_center
    e "I mean, yeah, but if we fail, our grades are going to drop a decent amount.... Plus, I barely understood what Mr. Duras was saying, and he makes me feel stupid for even trying to ask."
    hide ether
    show rajah nervous at zoom_center_r
    r "I feel you, bro. But..."
    hide rajah
    show ether base at zoom_center
    e "How do you plan to study for the test?"
    hide ether
    show rajah blushing at zoom_center_r
    r "..."
    r ".. Guess...?"
    hide rajah
    show ether coveringface at zoom_center
    e "You can't be serious."
    hide ether
    show rajah blushing at zoom_center_r
    r "I {i}thought{/i} about asking Blaire or Danny for help, but........ then I got a little self-conscious and I thought eh, my grade could probably tank it anyway!"
    hide rajah
    show ether base at zoom_center
    e "Is that a good line of thinking for long-term?"
    hide ether
    show rajah base at zoom_center_r
    r "Probably not, but sometimes you gotta live in the present instead of stressing over the future, y'know?"
    hide rajah
    show ether base at zoom_center
    e "I'm pretty sure that's not what the quote was for-"
    hide ether
    show rajah blushing at zoom_center_r
    r "Look, Ether, it's a problem for next class. So I'll start worrying about it- {i}next class{/i}."
    hide rajah
    show ether upset at zoom_center
    e "{i}I wish I had that kind of luxury..... To be brave enough to put off academic work. Hah.{/i}"

    # -------- Ether arrives home
    scene bg bedroom
    show ether base at zoom_center
    e "{i}To get a good grade on the test, I should start studying as soon as I finish everything else.{/i}"
    e "{i}Maybe if I spend more time studying, I'll absorb more of the content!{/i}"
    e "{i}Let's see if Mr. Duras posted anything to help me study on the quiz...{/i}"
    e "Here we go.."
    e '"Hello, class! As I told you in class today, there will be a quiz the next time I see you. Please study the following topics in order to succeed:"'
    e "Functions of 3 branches.... Articles of Colonies... Zebulon's important court cases, including Shaw v. Rucker.... so everything he's ever mentioned the last two days."
    hide ether
    show ether upset at zoom_center
    e "I genuinely didn't get enough of the notes down, though... maybe there's some resource online I could find that can help me understand what he was trying to teach."
    hide ether 
    show ether base at zoom_center
    e "Maybe I'll try looking it up on YouTube again...."
    e "Here's one. I hope it's better than the one I found yesterday..."
    e "The Legislative Branch creates laws. Yes, that is one of the few things I actually remember."
    e "The Executive Branch... carries out the law. They just enforce whatever laws are created using the Departments... ohhh..... that's not even that hard to understand! How come I didn't get it during class?"
    e "The Judicial Branch sets precedents with their decisions that influence future cases... also can rule anything unconstitutional for the Executive to strike down. Yeah, this really isn't hard to understand when the person in this video is the one explaining it."
    hide ether 
    show ether happy at zoom_center
    e "Maybe it's because he's not moving around as much as Mr. Duras is... and it's much quieter in my room than in the classroom...."
    hide ether 
    show ether base at zoom_center
    e "It shouldn't have made that much of a difference, though? The material was still easy for me to pick up when it was explained by the video........ maybe I'm just slow or something..."
    e "I've been studying this for about thirty minutes- I'll take a break to check my grades."
    e "Oh, it looks like Mr. Duras already graded the stuff we turned in today....."
    e "I got full points on the classwork, but I only got 75 percent on the homework from yesterday..."

    e "Now my grade dropped to a B.. I didn't know each of the individual worksheets were worth so much-"
    e "{alpha=0.5}{i}sighs{/i}{/alpha}"
    e "It's fine. I'll do well on the quiz, and the grade will go right back up. I just have to find better resouces to help me with the quiz....."
    e "{alpha=0.5}{i}looking back at the screen{/i}{/alpha}"
    e "I HAVE to do well on this quiz. It's the only way I'm going to get it back to an A before my parents find out..."
    e "Can I really, though...... Mr. Duras really thought I wasn't trying in his class. How... how would I try harder? His teaching style is just... so distracting. Could I have... tried harder to focus?"
    e "It doesn't matter. I'll do well on this quiz, and my grade will go back up. It'll be just fine."
    jump couple_days_pass
    return

label couple_days_pass:
    # ADD IN TIME SKIP SCREEN HERE
    scene bg blackscreen
    s "A couple days pass.."
    scene bg schoolhallway
    show ether coveringface at zoom_center 
    e "{i}Today's the day of the quiz and I am so going to fail but no no I will not fail I can not afford to fail-{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}I've looked up so much of the notes... I should be fine, right?{/i}"
    hide ether
    show ether base at zoom_center
    e "{alpha=0.5}{i}walking down the hallway{/i}{/alpha}"
    e "{i}Oh, there's Blaire. She doesn't seem worried at all. But why would she, when she's been talking about how easy the work's been?{/i}"
    e "{i}Rajah's early too. He's just scrolling on his phone.. I wish I could be confident enough to do that.. but I've spent the last night worrying so much about the quiz that I feel like I barely slept at all...{/i}"
    e "{i}I'm just going to review the notes I found on the topics while I wait... the more time spent cramming, the better, right?{/i}"
    jump quiz_starts
    return

label quiz_starts:
    scene bg govclassroom
    show duras base at zoom_center2
    md "Alright, class. Come on in."
    hide duras
    show ether upset at zoom_center
    e "{i}It's starting it's starting it's starting I am sooooo doomed-{/i}"
    hide ether
    show duras base at zoom_center2
    md "I hope you all studied for the quiz today! But before we get to that event of the day, we'll have a short warm-up to help you prepare for it."
    md "I'll just review a couple of concepts, and you all can shout out the answers."
    hide duras
    show ether coveringface at zoom_center
    e "{i}No- I can never focus when there's that many people talking-{/i}"
    hide ether
    show duras base at zoom_center2
    md "So for our first question... Can anyone explain to me why the Articles of Colonies didn't work?"
    n "--Because it didn't coin money-"
    n "--Couldn't regulate trade---"
    n "--No enforcement--"
    n "--fhdskjfgdshfbdkjvidshiusdfjsdfbnkjsdf-"
    n "--dsfhdskjfbdsfbs,mfrbewfiuisfndjsfnsdfnjksdf--"
    n  "--fnjdskbfsdkfbksdbfkjsdbfkjsdfhhsdfdmfbdsfbkj--"
    n "--hsdkjfdhsvfvdooosd--"
    hide duras
    show ether coveringface at zoom_center
    e "{i}It's too loud----{/i}"
    hide ether
    show duras blush at zoom_center2
    md "Excellent, class!"
    hide duras
    show ether base at zoom_center
    e "{i}Great, it's over-{/i}"
    hide ether
    show duras base at zoom_center2
    md "Now for the next question-"
    hide duras
    show ether coveringface at zoom_center
    e "{i}NO-{/i}"
    hide ether
    show duras base at zoom_center2
    md "Who can name the court case that outlawed species based gerymandering?"
    n "--hffuysuidhfkefbbebnd--"
    n "--fhdskjfkkfbbfdnsfbdnhxbe--"
    n "--dafwawfcdahjvhdvwfgwggdsb--"
    hide duras
    show ether upset at zoom_center
    e "{i}Shaw.. Shaw v. something.... I'll probably recognize it on the quiz-{/i}"
    hide ether
    show duras base at zoom_center2
    md "Now, last question! Who can tell me why the Bill of Rights was established?"
    n "--hfbkjsdbfe,mnfojodnc,xsncdjkfnejnj--"
    hide duras
    show duras blush at zoom_center2
    md "{alpha=0.5}{i}clapping his hands together{/i}{/alpha}"
    md "Yes! Exactly! I saw those were the most missed questions on the last couple worksheets I assigned to you, and you answered them beautifully! Now, it's time for the quiz!"
    hide duras
    show rajah nervous at zoom_center_r
    r "{alpha=0.5}{i}muttering next to Ether{/i}{/alpha}"
    hide rajah
    show rajah annoyed at zoom_center_r
    r "'Answered them beautifully?' I didn't even know half of what everyone was saying because everyone was shouting over each other!"
    hide rajah
    show ether annoyed at zoom_center
    e "I know..... I couldn't focus much on anything anyone said-"
    hide ether
    show duras base at zoom_center2
    md "I'm coming around to pass out the quiz now. You have until the end of class to finish it."
    hide duras
    show duras unsettled at zoom_center2
    md "Rajah, Ether, if you could please stop talking until I finish passing out the quiz."
    md "If I catch anyone else talking during the quiz, I will give you a zero."
    hide duras
    show rajah annoyed at zoom_center_r
    r "{alpha=0.5}{i}shuts up, looking embarrassed{/i}{/alpha}"
    hide rajah
    show ether base at zoom_center
    e "{i}Okay. Quiz. I really didn't hear anything anyone was saying, but maybe I don't need to. I.. think I could've answered all those questions by myself-{/i}"
    hide ether
    show duras base at zoom_center2
    md "Ether. Eyes on your own paper, please."
    hide duras
    show ether annoyed at zoom_center
    e "{i}But I wasn't-{/i}"
    hide ether
    show ether base at zoom_center
    e "{alpha=0.5}{i}stares down at the paper{/i}{/alpha}"
    e "{i}I'll just try answering these questions.{/i}"
    e "{i}Question 1: Describe the three branches (Legislative, Executive, and Judicial) and their purposes.{/i}"
    e "{i}I remember there was a question like this on the worksheet- but what was it? I think it was just about the Legislative branch...{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}Legislative... I remembered looking this up the other day too.. It was either creating or enforcing the law, right? And then I remember Judicial was passing judgement or something like that, because Rajah asked why it was so useless one time-{/i}"
    e "{i}Maybe I'll just come back to this. The answer might come back to me later.{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Next question: Oh, I don't even understand half the words in this one. Mr. Duras never mentioned 'Confederation', or the 'United Alliance' in any of these, did he?{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}Another question to come back to-{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Third question: What is the point of the government?{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}Was this a topic I missed on Mr. Duras' post? I could've sworn I didn't see it there- Am I stupid?{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}I can probably make up an answer for that question, but I don't know if it'll be right...{/i}"
    e "{i}Let's just go through the rest of the questions-{/i}"
    e "{i}What is unethical about gerrymandering?{/i}"
    e "{i}Describe the rationale for the attempted coup against Zebulon's government in the 1880s-{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}I'll just... come back to all the free response questions later-{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Oh, multiple choice! At least I actually have a shot of answering these questions correctly-{/i}"
    e "{i}I'm just going to circle the answer that looks the most accurate, and hope for the best... And then I'll go back and fill in an answer for the short answer questions...{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}My grade is going to fall because I can't figure out how to pay proper attention in class... Mr. Duras doesn't even seem to like me anymore anyway, so he hasn't been the most helpful either....{/i}"
    e "{i}No, I can't be blaming Mr. Duras. It's my own stupid fault that I can't understand what he's saying, and there's no one in the universe I can blame for my own mistakes but myself.{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}Why... why did I have to be like this? Why couldn't I just be like everyone else.. and be smarter?{/i}"
    scene bg blackscreen
    s "{alpha=0.5}{i}..... later....{/i}{/alpha}"
    jump e_walks_home
    return

label e_walks_home:
    scene bg street
    s "{alpha=0.5}{i}on the way home....{/i}{/alpha}"
    show rajah annoyed at zoom_center_r
    r "---so Blaire and I were arguing about who was supposed to turn in the slideshow for history, but we couldn't even come to an agreement because she was being SO unreasonable- "
    r "She literally said she didn't trust anyone in the group to turn it in, but she somehow trusted me enough to do it? I thought that implied she'd do it!"
    hide rajah
    show ether base at zoom_center
    e "That's not good..."
    hide ether
    show rajah annoyed at zoom_center_r
    r "No, it really wasn't. We were arguing about it all the way to Calculus, and Ms. Fong had to tell both of us to shut the hell up. I was so sure she was about to give us a zero on the quiz..."
    hide rajah
    show ether base at zoom_center
    e "Good thing she didn't...."
    menu:
        "Bring up the quiz":
            jump bring_up_quiz
        "Choose to stay quiet":
            jump stay_quiet
    return       

label bring_up_quiz:
    scene bg street
    show ether base at zoom_center
    e "Speaking of quizzes, how do you think you did on the Government quiz?"
    hide ether
    show rajah nervous at zoom_center_r
    r "It was... "
    r "....definitely something."
    hide rajah
    show ether base at zoom_center
    e "'Definitely something'?"
    hide ether
    show rajah blushing at zoom_center_r
    r "Terrible."
    hide rajah
    show ether base at zoom_center
    e "... Did you study?"
    hide ether
    show rajah nervous at zoom_center_r
    r "I tried for... 10 minutes, and then I gave up because I felt too much like an idiot to keep trying."
    r "I will never understand how Blaire understands everything in that class so easily when Duras doesn't like re-explaining himself."
    hide rajah
    show ether base at zoom_center
    e "...."
    hide ether
    show ether upset at zoom_center
    e "Yeah....."
    hide ether
    show rajah blushing at zoom_center_r
    r "It's alright, I've already accepted that I'm too stupid to thrive in that class. C's get degrees, right?"
    hide rajah
    show ether base at zoom_center
    e "Absolutely...."
    hide ether
    show rajah base at zoom_center_r
    r "Was the quiz any better for you, Ether?"
    menu:
        "Ether tells them he thinks he failed.":
            jump think_e_failed
        "Choose to stay quiet":
            jump stay_quiet
    return

label stay_quiet:
    scene bg street
    show ether base at zoom_center
    e "The quiz.. I think it was... okay."
    hide ether
    show rajah nervous at zoom_center_r
    r "Hey, better than me, at least. I spent all of yesterday evening watching SladeSlice because I gave up trying to study the damn thing. You should watch him sometime- he makes gaming videos, has some really funny reaction videos-"
    hide rajah
    show ether upset at zoom_center
    e "{i}I don't know if I'd be able to do that without feeling guilty about not trying harder, but sure, Rajah.{/i}"
    e "{i}I wish I could talk about it without feeling embarrassed.. because I sure can't bring it up to my parents.{/i}"
    e "{i}My parents would never understand how a teacher could be bad, because they'd just think I'm not trying.{/i}"
    e "{i}Just like Mr. Duras...{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}And when they see my grade drop, they'll just blame me.{/i}"
    e "{i}What would I even tell them anyway? That I can't focus because Mr. Duras is moving around too much? That I can only focus on either the notes he wants us to take, or the lecture he's giving at the same time?{/i}"
    e "{i}No, that just sounds like an excuse.... I'll just have to hope they don't find out....{/i}"
    hide ether
    show rajah nervous at zoom_center_r
    r "Aight, Ether, I'm gonna head home from here now. See ya tomorrow, alright? Good talk today?"
    hide rajah
    show ether base at zoom_center
    e "See you tomorrow, Rajah!"
    hide ether
    show ether upset at zoom_center
    e "{i}Good talk? I hardly said anything...{/i}"
    e "{i}It's fine. I have bigger priorities, anyway. Like the huge homework load I need to get done...{/i}"
    jump e_returns_home
    return
    
label think_e_failed:
    scene bg street
    show ether upset at zoom_center
    e "I think I failed the quiz....."
    hide ether
    show rajah nervous at zoom_center_r
    r "Mhm..."
    hide rajah
    show ether upset at zoom_center
    e "I feel like I guessed pretty much all the questions, even though I genuinely did try to look up everything Duras taught.."
    e "I was sure I'd at least be somewhat fine with all the YouTube videos I watched, but..."
    hide ether
    show rajah nervous at zoom_center_r
    r "Mhm...."
    hide rajah
    show ether annoyed at zoom_center
    e "I just wish Mr. Duras didn't assume I wasn't trying. It's so annoying, to put all your effort into a class and the teacher just decides to not really help you because you didn't immediately understand everything they were saying."
    hide ether
    show rajah base at zoom_center_r
    r "Yup."
    r "Relatable."
    hide rajah
    show rajah onphone at zoom_center_r
    r "{alpha=0.5}{i}checking phone{/i}{/alpha}"
    r "Dang, they already dropped a new video?"
    hide rajah
    show ether base at zoom_center
    e "{alpha=0.5}{i}momentarily stunned{/i}{/alpha}"
    e "Who dropped a new video?"
    hide ether
    show rajah blushing at zoom_center_r
    r "There's this YouTuber I found the other day called SladeSlice who does gaming and their videos are so funny-"
    r "you know, this one time, they trolled someone in minecraft by pretending to be a water block and that person couldn't find them for so long-"
    hide rajah
    show ether base at zoom_center
    e "That's... great...."
    hide ether
    show rajah blushing at zoom_center_r
    r "They play a lot of different games, too. You know that new game Little Nightmares that came out recently? They have a whole reaction series to it and they say the most outlandish things- it's hilarious."
    r "You should try watching them sometime!"
    hide rajah
    show ether base at zoom_center
    e ".... How long have you been watching them?"
    e "{i}If I knew Rajah would get distracted this easily, I wouldn't have said anything...{/i}"
    hide ether
    show rajah onphone at zoom_center_r
    r "Like... couple days ago? I think the day Duras told us there was a quiz, I tried to study, gave up, then started bingewatching this guy instead because watching someone die repeatedly in hardcore is way funnier than trying to understand how our government works."
    hide rajah
    show ether base at zoom_center
    e "I see..."
    hide ether
    show rajah blushing at zoom_center_r
    r "They've already done collabs with people like Pewdiepie and Jacksepticeye and it's great-"
    hide rajah
    show ether upset at zoom_center
    e "{i}Look at Rajah... he doesn't understand much from Government either, but he seems so accepting of it... he doesn't seem worried at all...{/i}"
    e "{i}School probably doesn't matter to him as much it does to me...{/i}"
    e "{i}I just won't bring it up next time...{/i}"
    hide ether
    show rajah nervous at zoom_center_r
    r "You good? You look like your dog just died."
    hide rajah
    show ether coveringface at zoom_center
    e "No, I'm fine."
    hide rajah
    show ether happy at zoom_center
    e "{alpha=0.5}{i}smiles{/i}{/alpha}"
    hide rajah
    show ether base at zoom_center
    e "Carry on..."
    jump e_returns_home
    return

label e_returns_home:
    scene bg blackscreen
    s "Back at home.."
    scene bg househallway
    show ether base at zoom_center
    e "{alpha=0.5}{i}closing door{/i}{/alpha}"
    e "Okay, I'm home."
    e "It is... 4:15. That leaves me... with 6 hours to finish up everything, and 8 if I need to stay up until 12."
    hide ether
    show ether coveringface at zoom_center
    e "But I really don't want to do homework... "
    e "And 6 hours is a lot of time..."
    hide ether
    show ether base at zoom_center
    e "No, Ether, do it for the grade..."
    e "{alpha=0.5}{i}walks up to his room{/i}{/alpha}"
    scene bg bedroom
    show ether base at zoom_center
    e "Where do I start....."
    e "Maybe Government? Not sure I want to think about Duras right now, though..."
    e "Let's do some math instead.. the answers shouldn't be too hard to figure out, right?"
    hide ether
    show ether upset at zoom_center
    e "Hmmm..... the notes she gave us are confusing me..."
    hide ether
    show ether base at zoom_center
    e "I'll just try a problem and check the answer key."
    e "Nope, that was wrong... did I forget a step?"
    e "Yep, forgot to bring the denominator down... "
    e "That's still not it..."
    e "I'll just skip this one and come back to it later- maybe I just need to do some different ones to better understand it first...."
    hide ether
    show ether upset at zoom_center
    e "That's not good.... that is a completely different coefficient than it's supposed to be.."
    hide ether
    show ether base at zoom_center
    e "The answer key has a 1/2 in front... Where did that even come from?"
    hide ether
    show ether upset at zoom_center
    e "Is this the start of my academic downfall? Government's just the start, and my grades start falling for all my other classes too?"
    hide ether
    show ether coveringface at zoom_center
    e "So I really just am incapable of paying attention in class, huh? I was so distracted by how badly I did on the Government quiz that I couldn't even focus during math class anyway...."
    e "Argh, maybe I'll just take a break. I'm probaly still too distraught by the government quiz today to focus..."
    hide ether
    show ether phone at zoom_center
    e "Maybe I'll just watch one SladeSlice video and see what Rajah like so much about him."
    v "Alright. guys, welcome back to another video of me trying to beat Minecraf-"
    v "WHY WAS THERE A SKELETON THER-"
    hide ether
    show ether laughingphone at zoom_center
    e "{alpha=0.5}{i}starts laughing{/i}{/alpha}"
    e "What is that cut-off scream??"
    e "He did NOT just slip that reference in there-"
    e "That was- {alpha=0.5}{i}dies laughing{/i}{/alpha} -so stupid-"
    e "Why are you saying it like that?"
    e "Okay, nevermind, I see where Rajah's coming from. This dude IS funny."
    hide ether
    show ether phone at zoom_center
    e "That video was only 10 ish minutes.. He has some shorts on here too-"
    v "Why there is a skeleton there- NO-"
    hide ether
    show ether laughingphone at zoom_center
    e "This is funnier without context- Haha-"
    e "I have time to watch another....."
    e "Tehehehheh-"
    e "Pfffft-"
    e "Why did he just {i}jump off{/i}?"
    e "{alpha=0.5}{i}wheezing{/i}{/alpha}"
    e "No- don't- HAH-"
    e "I need to see part two of this-"
    e "WHERE DID THE CAT COME FROM???"
    e "{alpha=0.5}{i}WHEEZES{/i}{/alpha}"
    e "Oh he died to another skeleton-"
    e "Where does he keep coming up with these insults?! I wish I was that creative-"
    e "Ah, that was funny... "
    hide ether
    show ether upset at zoom_center
    e "IT'S ALMOST 10?? I still haven't finished any homework at all-"
    e "I'm just gonna show a bit of work then copy off the answer key- the work just needs to be done, not necessarily done well."
    e "Alright, time to sleep...."
    e "Thank goodness I finished my homework in time..."
    jump next_day
    return

label next_day:
    scene bg blackscreen
    s "The next morning.."
    scene bg bedroom
    show ether annoyed at zoom_center
    e "I don't want to go to school again..."
    e "{alpha=0.5}{i}gets up{/i}{/alpha}"
    hide ether
    show ether coveringface at zoom_center
    e "I slept late yesterday....."
    hide ether
    show ether base at zoom_center
    e "Anyway.. to Government we go..."
    # -------------------------------------- time skip
    scene bg blackscreen
    s "Later in government class.."
    scene bg govclassroom
    show duras base at zoom_center2
    md "-- and today we're going to cover the Bill of Rights---"
    md "---- should know the first ten Amendments---"
    hide duras
    show ether upset at zoom_center
    e "{i}I still can't understand anything he's saying because he's moving around so much... and there's so much text on that slide that it's overwhelming...{/i}"
    e "{i}Mr. Duras, why... can you just stop moving so I can actually focus...{/i}"
    # Sytle note: make the classroom and md low opacity or darker to show that ether is out of it
    hide ether
    show duras base at zoom_center2
    md "----who can tell me which side voted for the Bill of Rights---"
    md "----Not quite---"
    hide duras
    show ether upset at zoom_center
    e "{i}There is no hope for me in this class...{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}Mr. Duras won't want to help me... and apparently I can't absorb anything he's saying while I'm copying down the notes...{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I keep phasing in and out between listening to him talk and actually copying down the notes...{/i}"
    e "{i}If only I could multi-task as well as everyone else in this class--{/i}"
    hide ether
    show duras base at zoom_center2
    md "---I'll pass out a worksheet for you all to do while I continue the notes---"
    hide duras
    show ether annoyed at zoom_center
    e "{i}I can't concentrate on reading anything on this worksheet because Duras keeps talking so much...{/i}"
    e "{i}Maybe I'll just pay attention to what he says instead?{/i}"
    hide ether
    show duras base at zoom_center2
    md "---and that's why the answer to the first question is what it is---"
    hide duras
    show ether upset at zoom_center
    e "{i}I didn't even... catch the answer...{/i}"
    hide ether
    show duras base at zoom_center2
    md "--- Second one should be the case we went over that concerns the Equal Protection Clause--"
    hide duras
    show ether upset at zoom_center
    e "{i}I'll just write that down.. and only that, because I couldn't catch anything else he said--{/i}"
    hide ether
    show duras base at zoom_center2
    md "-----Moving on to our first ten amendmends, which are the Bill of Rights--"
    hide duras
    show ether upset at zoom_center
    e "{i}You know what, maybe I'll just give up because I'm not going to end up finishing this anyway....{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I just want to disappear...{/i}"
    hide ether
    show duras base at zoom_center2
    md "---And that's it for today! Please turn in the worksheet as you head out the door and complete the homework before you come in next class!"
    hide duras
    show ether annoyed at zoom_center
    e "{i}Sure, Mr. Duras.. whatever you wish....{/i}"
    # -------------------------------------- time skip
    scene bg blackscreen
    s "Later afterschool.."
    scene bg bedroom
    show ether base at zoom_center
    e "{alpha=0.5}{i}coming home from school{/i}{/alpha}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I'm beginning to realize how much I don't like going to Government.. and Calculus...{/i}"
    e "{i}It's been a week since that quiz.. Mr. Duras graded the quiz yesterday..{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}I have a B in Government now.. and a B+ in Stats... my other grades are beginning to drop too....{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}This is hopeless...{/i}"
    e "{i}I'm so tired of feeling like an idiot....{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}At least when I'm on YouTube, I don't think about how screwed I am for my classes...{/i}"
    hide ether
    show ether phone at zoom_center
    e "{alpha=0.5}{i}checking the time{/i}{/alpha}"
    e "{i}I still got a couple hours... and I finished work last time within an hour.. I can afford to watch some more SladeSlice...{/i}"
    jump after_another_couple_days
    return

label after_another_couple_days:
    # ------------------------------------------ more time skip
    scene bg blackscreen
    s "A couples days later.."
    scene bg bedroom
    show ether coveringface at zoom_center
    e "{i}Back home, finally...... I don't wanna go to school anymore...{/i}"
    e "{i}I just wanna finish watching that video from earlier- and scroll through the shorts-{/i}"
    em "ETHER!"
    hide ether
    show ether upset at zoom_center
    e "{i}She's back early today?{/i}"
    e "{i}.. why is she back so early today? She usually doesn't come home until I'm asleep-{/i}"
    hide ether
    show ether annoyed at zoom_center
    e ".. Yes, Mom?"
    em "Why are your grades so low?"
    hide ether
    show ether upset at zoom_center
    e "{alpha=0.5}{i}blinking wearily{/i}{/alpha}"
    e "Oh.. I've just been... struggling in some classes. It's just Government-"
    em "Why are you struggling in Government {i}now{/i}? You had an A in that class just two weeks ago!"
    hide ether
    show ether annoyed at zoom_center
    e ".... Mr. Duras keeps assigning work I don't understand-"
    em "Did you ask him for help?"
    hide ether
    show ether coveringface at zoom_center
    e "Yes, but-"
    em "This is ridiculous, Ether. I come home late from work every day to keep you fed, and you can't even keep your grades up?"
    hide ether
    show ether annoyed at zoom_center
    e "...."
    em "Why have you been slacking off? I expected better from you!"
    e "I.. I'm trying, Mom-"
    em "Then you must not be trying hard enough!"
    hide ether
    show ether upset at zoom_center
    e "....."
    em "I didn't raise you to be this incompotent. Those grades better be back up by the time your father gets back from his business trip."
    e "... yes, Mom."
    em "Don't just 'yes, Mom' me. Do better, Ether."
    em "{alpha=0.5}{i}scoffs{/i}{/alpha}"
    hide ether
    show ether annoyed at zoom_center
    e "I..."
    e "I'll try harder, Mom....."
    hide ether
    show ether coveringface at zoom_center
    e "{i}It's just like Mr. Duras, all over again...{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{alpha=0.5}{i}trudging up to his room{/i}{/alpha}"
    hide ether
    show ether base at zoom_center
    e "I guess I should start with doing the homework..."
    e "But there's so much to do...."
    e "I just have to choose one and start, right?"
    e "Maybe I'll just do the hard one first... so... Government....."
    e "I have to take out my notes for this....."
    e "Notes.. notes.. where are you...?"
    e "Here..... okay, first question asks about the first Amendment... where did I write that? Here.... I don't even understand what I wrote.. There's the cases about the Amendment, but not the amendment itself....."
    hide ether
    show ether upset at zoom_center
    e "I bet Mr. Duras just said it aloud and I wasn't paying attention..."
    e "I'll just.. Google it or something...."
    e "That.. looks confusing.... I'll just write it down, doesn't matter..."
    e "I don't understand that question, or the question after that, or any of these..."
    hide ether
    show ether annoyed at zoom_center
    e "I really don't want to do any homework......."
    hide ether
    show ether coveringface at zoom_center
    e "I don't want to ask anyone for help... I feel stupid enough...."
    hide ether
    show ether phone at zoom_center
    e "Let's check my grades and see how bad it is..."
    e "A C in Government, B in Stats... B in Mandarin, too? Wow, I really am losing my edge..."
    hide ether
    show ether coveringface at zoom_center
    e "Maybe if I take a break, I'll be able to focus...."
    hide ether
    show ether phone at zoom_center
    e "Just a short little break. One video. Just one, and I'll do some work."
    jump the_next_day
    return

label the_next_day:
    scene bg blackscreen
    s "The next day at school.."
    scene bg schoolhallway
    show ether base at zoom_center
    e "{i}Back to school again....{/i}"
    hide ether
    show rajah base at zoom_center_r
    r "Ether!"
    hide rajah
    show ether base at zoom_center
    e "Hi-"
    hide ether
    s "-They go inside the classroom early-"
    scene bg govclassroom
    show rajah onphone at zoom_center_r
    r "I found this really goofy clip you gotta watch it please it's so funny-"
    hide rajah
    show ether laughingphone at zoom_center
    e "What the- where did you even find this?"
    hide ether
    show rajah blushing at zoom_center_r
    r "Dunno, but the algorithm found it for me somehow- Look at this dumb idiot HAHA-"
    r "Ah hold on my dad's texting me, give me a sec-"
    hide rajah
    show rajah onphone at zoom_center_r
    r "{alpha=0.5}{i}checks his phone{/i}{/alpha}"
    r "{alpha=0.5}{i}snorts{/i}{/alpha}"
    r "{alpha=0.5}{i}chuckles{/i}{/alpha}"
    hide rajah
    show ether base at zoom_center
    e "{i}......He went back to scrolling, didn't he?{/i}"
    hide ether
    show ether phone at zoom_center
    e "{i}I might as well, too-{/i}"
    e "{i}Wait- Google classroom says this thing is due today??{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}Oh I didn't finish any work last night because I got so distracted-{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Do I really wanna try doing it all now, though...?{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}I already know I'm not going to finish it all.{/i}"
    menu:
        "Go on his phone":
            jump e_goes_on_phone
        "Try to finish the work he didn't finish the night before":
            jump e_trys_to_do_work
    return

label e_goes_on_phone:
    scene bg govclassroom
    show ether base at zoom_center
    e "{i}Eh, it's fine... just another 15 minutes before class starts won't make a huge difference, right?{/i}"
    hide ether
    show ether phone at zoom_center
    e "{alpha=0.5}{i}takes out phone to scroll{/i}{/alpha}"
    hide ether
    show ether laughingphone at zoom_center
    e "{i}Wow, that really IS funny-{/i}"
    e "{i}I can show this to Rajah later-{/i}"
    s "{alpha=0.5}{i}bell rings{/i}{/alpha}"
    hide ether
    show duras base at zoom_center2
    md "Alright, everyone, come in! Let's start class today~"
    hide duras
    show ether annoyed at zoom_center
    e "{i}I.. really don't want to be here...{/i}"
    e "{i}I can never grasp anything he's saying because he's always DOING SO MUCH...{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Try and focus, Ether. Just try to focus. One thing at a time-{/i}"
    hide ether
    show duras base at zoom_center2
    md "And now, we're going to go over the Amendments from the Bill of Rights- I expect you all to know all of them by now! So the first one is-"
    hide duras
    show ether annoyed at zoom_center
    e "{i}I would ask him if he could stay on that slide longer... but I don't think he'd do anything to help me anyway since he thinks I'm not trying...{/i}"
    e "{i}Honestly... screw this class, I'll just do my Mandarin homework. It's not like I'll understand anything Duras is saying regardless.{/i}"
    jump mandarin_class_continues
    return

label e_trys_to_do_work:
    scene bg govclassroom
    show ether base at zoom_center
    e "{i}Agh, I really don't wanna to get yelled at again, so I might as well try to do what I can-{/i}"
    e "{i}I know Ms. Fong won't be collecting the work today, so I've got some more time to do calc-{/i}"
    e "{i}I have Government first, so I'll just try getting this worksheet done first-{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}... I forgot how little of the content I understood.... I can't answer these questions without understanding what it's asking, and since I don't....{/i}"
    e "{i}Maybe I could ask someone for help?{/i}"
    menu:
        "Ask for help?":
            jump ask_for_help
        "Go on his phone":
            jump e_goes_on_phone
    return

label ask_for_help:
    scene bg govclassroom
    show ether annoyed at zoom_center
    e "{i}Asking for help? Really? Probably not a good idea, since Mr. Duras'll just think I cheated off someone anyway and dock me points for it.{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I.. don't want to be called out by Mr. Duras again...{/i}"
    e "{i}I mean... it doesn't matter what I do anyway, since Mr. Duras thinks I'm not trying...{/i}"
    hide ether
    show ether base at zoom_center
    e "{alpha=0.5}{i}glancing over at Rajah{/i}{/alpha}"
    hide ether
    show rajah onphone at zoom_center_r
    r "Pfffft-"
    hide rajah
    show ether base at zoom_center
    e "{i}He's still on his phone.... without a care in the world....{/i}"
    e "{i}Maybe I should just go on my phone too, since I'm not going to get anything done anyway...{/i}"
    jump e_goes_on_phone
    return

label mandarin_class_continues:
    scene bg govclassroom
    show ether base at zoom_center
    e "{i}At least I can finish Mandarin homework...{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}Is it really just Duras' class that just makes me feel super stupid?{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Good thing this class is finally over, good grief...{/i}"
    e "{i}To Mandarin I go...{/i}"
    scene bg chineseclassroom
    show chenglaoshi base at cls_left
    ch "Welcome, welcome, everyone! Good morning, Danny- oh hello, Blaire-"
    hide chenglaoshi
    show chenglaoshi questioning at cls_center_q
    ch "Aiyah, Rajah, what is that godforsaken thing you have in your mouth?"
    hide chenglaoshi
    show rajah nervous at zoom_center_r
    r "It's just a...... ring pop, Cheng Lao Shi-"
    hide rajah
    show chenglaoshi questioning at cls_center_q
    ch "A ring pop?"
    hide chenglaoshi
    show rajah blushing at zoom_center_r
    r "It's like candy on a ring- you can wear it....?"
    hide rajah
    show chenglaoshi base at cls_center
    ch "How odd! Please make sure it goes into the trash when you finish it."
    hide chenglaoshi
    show rajah blushing at zoom_center_r
    r "I will, don't worry...."
    hide rajah
    show chenglaoshi base at cls_center
    ch "Welcome in, Ether!"
    hide chenglaoshi
    show ether base at zoom_center
    e "G'morning, Cheng Lao Shi.."
    hide ether
    show chenglaoshi base at cls_center
    ch "Alright, alright, settle down, everyone. We're going to start by going through yesterday's homework, that I hope you all finished?"
    hide chenglaoshi
    show chenglaoshi sideeye at cls_center_q
    ch "I will be verrrryyyy disappointed if you didn't~"
    hide chenglaoshi
    show ether happy at zoom_center
    e "{i}Presentations... this should be easy to sit through, since we won't be doing anything-{/i}"
    hide ether
    show chenglaoshi sideeye at cls_center_q
    ch "I expect you all to be paying verrrrryyyyy close attention-"
    hide chenglaoshi
    show ether base at zoom_center
    e "{i}I.. will try. After struggling in something as supposedly easy as Government, I don't think I can muster the energy to try for Mandarin.{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "Rajah! Why don't you start us off by reading the lesson for today? Read loud and clear!"
    hide chenglaoshi
    show ether base at zoom_center
    e "{i}I'm already getting distracted... Should I keep trying to pay attention? Being on YouTube was way better than this.....{/i}"
    menu:
        "Keep trying to pay attention":
            jump keep_trying_to_pay_attention
        "Sneak his phone out. It was way more entertaining anyway.":
            jump sneak_phone_out
    return

label keep_trying_to_pay_attention:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "{i}No, no, I should try. I'm not flunking Mandarin yet. I think Cheng Lao Shi will at least give me a chance.{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "--- and now, because of this Chinese cultural tradition, you should ALWAYS give your enemies a clock to wish on their downfall!"
    ch "Can anyone name another gift that means bad luck?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Pears?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Excellent! Ether!"
    hide chenglaoshi
    show ether upset at zoom_center
    e "{i}Oh no-{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "Can you tell us why pears mean bad luck?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Uhhhh-"
    hide ether
    show ether upset at zoom_center
    e "{i}Don't say that aloud-{/i}"
    hide ether
    show ether base at zoom_center
    e "Because... they're yellow?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Sometimes, they are indeed yellow. But why is that bad?"
    hide chenglaoshi
    show ether base at zoom_center
    e ".... Yellow.... is bad luck?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Nope!"
    hide chenglaoshi
    show chenglaoshi sideeye at cls_center_q
    ch "This is what happens when you {i}don't{/i} pay attention in class-"
    hide chenglaoshi
    show ether upset at zoom_center
    e "{i}... Not this again--{/i}"
    e "{i}This is exactly how Mr. Duras phrased it too-{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "---pears are bad luck because their pronunciation, 'li', is similar to the word, part, or 'li kai', so giving someone pears is like hoping they end up losing all their friends and family."
    ch "Great for enemies, terrible for people you're close to B)"
    ch "Ether, did you get that?"
    hide chenglaoshi
    show ether base at zoom_center
    e "I... Yes, I think so."
    hide ether
    show chenglaoshi base at cls_center
    ch "Can you tell me why pears are considered bad luck in Chinese culture?"
    hide chenglaoshi
    show ether base at zoom_center
    e ".. they.... sound like parting...?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Haiya! Close enough. I expect you to pay better attention next time!"
    hide chenglaoshi
    show ether annoyed at zoom_center
    e "Yes, Cheng Lao Shi...."
    e "{i}Pretty much what Mr. Duras said too....{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I guess this is the start of my academic downfall, huh?{/i}"
    e "{i}Why am I struggling in everything all of a sudden?{/i}"
    e "{i}It was just government... and then calculus... and now Mandarin...{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}I used to think this was the easiest class I had, but I'm struggling to pay attention even now...{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}Argh, just focus!{/i}"
    e "{i}Just because Cheng Lao Shi thinks you weren't trying, exactly like Mr. Duras accused you of being lazy, doesn't mean that you're stupid.....{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}Right......?/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}Just get through this class, Ether, and you can watch all the YouTube you want during lunch....{/i}"
    e "{i}Just get through the class...{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "Okayyyyyy, you little gremlins, I have a worksheet for you that's due at the end of class! It's based on what we just read, so let me know if you have any questions! Don't be afraid to ask for help!"
    hide chenglaoshi
    show ether upset at zoom_center
    e "....."
    hide ether
    show ether base at zoom_center
    e "{i}I can probably just copy off Rajah later...{/i}"
    e "{i}Maybe if I sneak my phone out for just a couple minutes, Cheng Lao Shi won't notice...{/i}"
    menu:
        "Sneak his phone out. It was way more entertaining anyway.":
            jump sneak_phone_out
        "Try doing the work":
            jump try_doing_the_work
    return

label sneak_phone_out:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "{i}Screw it, I already spent all of Government doing the Mandarin work. It's not like it's gonna change anything even if I tried-{/i}"
    hide ether
    show ether phone at zoom_center
    e "{alpha=0.5}{i}takes out phone{/i}{/alpha}"
    hide ether
    show ether base at zoom_center
    e "{i}As long as I keep it under my desk, Cheng Lao Shi probably won't notice..{/i}"
    hide ether
    show ether happy at zoom_center
    e "{i}Heh-{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "Oh Etherrrrrrrr-"
    hide chenglaoshi
    show ether upset at zoom_center
    e "{alpha=0.5}{i}quickly hiding phone{/i}{/alpha}"
    hide ether
    show ether base at zoom_center
    e "Hello, Cheng Lao Shi."
    hide ether
    show chenglaoshi questioning at cls_center_q
    ch "Was that a phone I {i}just{/i} saw?"
    hide chenglaoshi
    show ether upset at zoom_center
    e "..... no?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Haiya, you're not slick at all! You've barely done any work on the classwork! I better not see it out again!"
    hide chenglaoshi
    show ether annoyed at zoom_center
    e "Okay..."
    e "{i}Or I can just wait until he goes away...{/i}"
    menu:
        "Try doing the work":
            jump try_doing_the_work
        "Put away his phone briefly then take it out one Cheng Lao Shi isn't looking":
            jump take_out_phone_when_ch_not_looking
    return

label try_doing_the_work:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "{i}No... I should actually try.. and show Cheng Lao Shi I'm actually trying...{/i}"
    e "{i}This worksheet... oh, I can actually answer the first question.{/i}"
    e "{i}The second one I think I understand, but I should probably check to make sure...{/i}"
    e "...."
    hide ether
    show ether annoyed at zoom_center
    e "{i}I don't want to ask Cheng Lao Shi for help......{/i}"
    e "{i}Or anyone else....{/i}"
    e "{i}He's just going to tell me I'm not trying like Mr. Duras said...{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}This worksheet is pretty short. Half credit on this won't drop my grade down too much...{/i}"
    e "{i}I've done enough work to go on my phone, right?{/i}"
    menu:
        "Still try working":
            jump still_try_working
        "Sneak his phone out. It was way more entertaining anyway.":
            jump sneak_phone_out
    return

label still_try_working:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "{i}No.. I should... keep trying....{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I don't wanna try anymore....{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "I'm coming around to check on your first page! I hopeeeeeee you're workinggggg, little gremlins!"
    ch "Ah, yes, that looks good."
    ch "Excellent!"
    ch "You might want to double check that- oh, where is it? It's right here- no it's okay, you must've just missed it in the textbook..."
    ch "Ether!"
    hide chenglaoshi
    show ether base at zoom_center
    e "{alpha=0.5}{i}swiveling around{/i}{/alpha}"
    e "Hi, Cheng Lao Shi."
    hide ether
    show chenglaoshi base at cls_center
    ch "How's the worksheet?"
    ch "Can I see what you have?"
    hide chenglaoshi
    show ether upset at zoom_center
    e "Can I have more time on it? I didn't... finish the front side-"
    hide ether
    show chenglaoshi base at cls_center
    ch "That's perfectly fineeeeeeee. Do you need any help?"
    jump ch_offers_help_on_ws
    return

label take_out_phone_when_ch_not_looking:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "{i}Yeah, I'll just wait until they're on the other side of the classroom...{/i}"
    hide ether
    show ether phone at zoom_center
    e "{alpha=0.5}{i}takes out phone again{/i}{/alpha}"
    hide ether
    show chenglaoshi sideeye at cls_center_q
    ch "Etherrrrrr-"
    hide chenglaoshi
    show ether upset at zoom_center
    e "{alpha=0.5}{i}quickly puts phone away{/i}{/alpha}"
    hide ether
    show chenglaoshi serious at cls_center_s
    ch "Why'd you take your phone out again, child?"
    hide chenglaoshi
    show ether upset at zoom_center
    e "...."
    hide ether
    show chenglaoshi base at cls_center
    ch "You can't be on your phone during class... ai yai yai... Ether, you know this. How come you're not doing any of the work? Do you need any help?"
    jump ch_offers_help_on_ws
    return

label ch_offers_help_on_ws:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "Um-"
    e "{i}Wow, I didn't actually think he'd ask to help me.{/i}"
    e "I....what's going on..?"
    menu:
        "Yes, he's struggling":
            jump yes_struggling
        "No, he doesn't want to talk to Cheng Lao Shi after that callout.":
            jump no_help
    return

label yes_struggling:
    scene bg chineseclassroom
    show ether upset at zoom_center
    e "Yes, I need help...."
    hide ether
    show chenglaoshi base at cls_center
    ch "That's okay! What question did you stop at?"
    ch "Hmmmmm, yes... unlucky number...... I did not think it would be hard to grasp-"
    hide chenglaoshi
    show ether base at zoom_center
    e "I'm really sorry I didn't understand- I.... kept getting distracted."
    hide ether
    show chenglaoshi base at cls_center
    ch "Oh, I seeeee. Anywhos, can you tell me what the unlucky number in Chinese culture is?"
    hide chenglaoshi
    show ether upset at zoom_center
    e "{i}What if I'm wrong{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "You can guess!"
    hide chenglaoshi
    show ether upset at zoom_center
    e "{i}But what if I'm wrong?{/i}"
    hide ether
    show ether base at zoom_center
    e "Uh.... it's.. four, right?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Yup! You already understand half of it! The other half of the question is asking about why four is considered unlucky."
    hide chenglaoshi
    show ether base at zoom_center
    e "{i}The part I'm not sure I understand.{/i}"
    e "Does it have something to do with how it sounds? Like the pears?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Yes! See, you DOOO understand some of this :D"
    ch "So now tell me, what word sounds like 'si'?"
    hide chenglaoshi
    show ether base at zoom_center
    e "I don't.. I'm not sure...."
    hide ether
    show chenglaoshi base at cls_center
    ch "Why don't you look at the terms learned and see if any of them have the same pronunciation?"
    hide chenglaoshi
    show ether coveringface at zoom_center
    e "{i}I feel so dumb.............{/i}"
    e "{i}Maybe I'm just forever short on brain cells or something...{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Where is the page I'm looking for?{/i}"
    e "{i}This one?{/i}"
    e "... I think it's the word for dying?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Thereeee you go! Four is unlucky because Chinese people associate it with death."
    hide chenglaoshi
    show ether base at zoom_center
    e "Ohhh, that makes sense.... are all lucky and unlucky items like that? They sound like a certain word?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Exactly!"
    ch "Ah, there goes the godforsaken bell."
    hide chenglaoshi
    show chenglaoshi serious at cls_center_s
    ch "{alpha=0.5}{i}to the other students{/i}{/alpha} HAIYA DON'T JUST RUN OUT THE DOOR- CLEAN UP AFTER YOURSELVES!!!"
    hide chenglaoshi
    show chenglaoshi base at cls_center
    ch "{alpha=0.5}{i}to Ether{/i}{/alpha} Class is over now, but you can come in during lunch! I would like you to come back, seeing as you haven't finished."
    menu:
        "Ether ends up going back during lunch":
            jump e_goes_back_to_ch
        "Ether just goes to lunch":
            jump just_goes_to_lunch
    return

label no_help:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "No, I'm okay. I think I can figure it out."
    hide ether
    show chenglaoshi base at cls_center
    ch "Are you sure?"
    hide chenglaoshi
    show ether annoyed at zoom_center
    e "{i}I don't want to be antagonized for not trying...{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}He's already suspicious of me.{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}I'd rather finish this alone than be called out in front of the whole class again...{/i}"
    e "{i}I don't want this to end up the same way it did with Mr. Duras...{/i}"
    hide ether
    show ether base at zoom_center
    e "Yes, I can do it on my own. Thank you, though."
    hide ether
    show chenglaoshi base at cls_center
    ch "Alrrright, child."
    ch "Just give Cheng Lao Shi a holler whenever you need help, okay?"
    hide chenglaoshi
    show ether base at zoom_center
    e "{alpha=0.5}{i}nods{/i}{/alpha}"
    e "I will."
    hide ether
    show ether annoyed at zoom_center
    e "{i}I don't think I will.{/i}"
    jump just_goes_to_lunch
    return

label e_goes_back_to_ch:
    scene bg cafeteria
    s "During lunch...."
    show ether coveringface at zoom_center
    e "{i}Dang, calculus was brutal....{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Good thing it's finally lunch.. and I can finally relax....{/i}"
    e "{i}Wait, there's Cheng Lao Shi talking to Blaire. I forgot I didn't finish that worksheet from his class...{/i}"
    e "{i}He did say I could go back during lunch....{/i}"
    e "{i}Gods, do I really want to spend my lunch period in class?{/i}"
    e "{i}I should really finish that worksheet, though.. and Cheng Lao Shi did offer to help...{/i}"
    e "{alpha=0.5}{i}walking into the classroom{/i}{/alpha}"
    scene bg chineseclassroom
    show chenglaoshi base at cls_center
    ch "Ether! Welcome back!"
    hide chenglaoshi
    show ether base at zoom_center
    e "Hi, Cheng Lao Shi. I'm here to finish the worksheet from today's class..?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Ah, yes, yes, I remember."
    ch "Sit down, sit down! I have your worksheet on my desk. You can grab a textbook from the shelf while I go heat up my lunch-"
    ch "Haiya, I'm so hungry!"
    ch "Don't worry, Ether, I'll be back in five minutes!"
    hide chenglaoshi
    show ether happy at zoom_center
    e "{alpha=0.5}{i}chuckling a little{/i}{/alpha}"
    e "Okay-"
    hide ether
    show chenglaoshi base at cls_center
    ch "MY RICE AWAITS MEEEEEEE-"
    hide chenglaoshi
    show ether base at zoom_center
    e "{alpha=0.5}{i}grabbing his worksheet{/i}{/alpha}"
    e "Here's my worksheet-"
    e "And here's a textbook-"
    e "{i}Okay. I have all 30 minutes of lunch to finish this.{/i}"
    e "{i}It shouldn't be too hard, right?{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "I'm back-- I'm back!"
    ch "Oh, my beautiful, beautiful lunch...."
    hide chenglaoshi
    show chenglaoshi questioning at cls_center_q
    ch "Ether! Did you eat yet?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Uh, no-"
    hide ether
    show chenglaoshi base at cls_center
    ch "Aiyah, why not?"
    hide chenglaoshi
    show ether base at zoom_center
    e "I was planning to finish the worksheet before I went to lunch-"
    hide ether
    show chenglaoshi serious at cls_center_s
    ch "You should eat first! How can you think on an empty stomach, lah?"
    hide chenglaoshi
    show ether base at zoom_center
    e "I will! I just want to get my work done first-"
    hide ether
    show chenglaoshi base at cls_center
    ch "We can go through the questions while you eat, and you can write them down after. I can even write you a pass if it cuts into passing period, just eat your food! How can you think on an empty stomach?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Okay...."
    e "{alpha=0.5}{i}taking out lunch{/i}{/alpha}"
    hide ether
    show ether happy at zoom_center
    e "Here, I'm eating."
    hide ether
    show chenglaoshi base at cls_center
    ch "Excellent! Now, where did you stop on the worksheet?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Number three?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Ah, the one about the color red. The other ones should be about the new year traditions. Do you remember why it's important?"
    hide chenglaoshi
    show ether base at zoom_center
    e "It's a lucky color, I think?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Yes! Black and white are considered unlucky. Do you remember the other traditions we do every year for good luck?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Uh........ something about firecrackers?"
    hide ether
    show ether upset at zoom_center
    e "I'm not.. great at remembering them."
    hide ether
    show chenglaoshi base at cls_center
    ch "No worries! Let ol' Cheng Lao Shi tell you a little story, eh?"
    ch "Once upon a time, there was a big scary monster named Nian who would terrorize the nearby villages."
    hide chenglaoshi
    show ether base at zoom_center
    e "{i}I think this is the story he told earlier too...{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "See, Nian really really liked human meat, so it would constantly drag away unsuspecting humans for its next meal!"
    ch "The people were terrified!"
    ch "They didn't want to be torn apart by some beast! So of course, they tried to murder the beast by beating it with frying pans!"
    hide chenglaoshi
    show ether base at zoom_center
    e "Uh- Did it work?"
    e "{i}That wasn't in the first telling-{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "Ah, no, it didn't. It was quite disappointing, really. They put in so much effort to fight Nian, but it just swallowed all its attackers whole. So you know what they tried to do next?"
    hide chenglaoshi
    show ether base at zoom_center
    e "What'd... they do?"
    hide ether
    show chenglaoshi base at cls_center
    ch "They lure the beast off the edge of a mountain!"
    ch "But Nian was clever, and knocked people off instead! It must've had fun watching everyone go splat."
    hide chenglaoshi
    show ether base at zoom_center
    e "Oh...."
    hide ether
    show chenglaoshi base at cls_center
    ch "Anyways! The village people were getting desperate, but they had no idea what to do! Luckily, an old monk came and advised the village people to put up red banners and make loud noises to scare Nian away!"
    ch "Can you imagine almost dying to Nian multiple times and someone just comes along and tells you 'Oh, just put up some red banners! It'll definitely scare Nian away!'"
    ch "Regardless, when the village people put up those red banners and set off fire crackers, Nian ran for the hills and never came back!"
    hide chenglaoshi
    show ether base at zoom_center
    e "So putting up things that are red is to scare off Nian....."
    hide ether
    show chenglaoshi base at cls_center
    ch "Exactly! Do you understand now?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Wait- so they put up red and set off firecrackers to scare away the beast called Year?"
    hide ether
    show chenglaoshi base at cls_center
    ch "No, no. Think of Nian as the year's bad luck, and the traditions as the mechanisms that scare off the bad luck!"
    hide chenglaoshi
    show ether base at zoom_center
    e "Ooohhhh..."
    hide ether
    show ether happy at zoom_center
    e "That makes sense!"
    hide ether
    show chenglaoshi base at cls_center
    ch "Yes, yes, I'm glad! That should explain the rest of the worksheet."
    hide chenglaoshi
    show ether base at zoom_center
    e "Let's see- In Chinese culture, which color is considered luck- it's red..."
    hide ether
    show ether happy at zoom_center
    e "Explain the myth that makes red the lucky color- Oh, I can answer that now!"
    e "I finished the worksheet!"
    hide ether
    show chenglaoshi base at cls_center
    ch "Excellent! Hand it over, child."
    ch "Thank you! The bell just rang, so you should hurry along to class now."
    hide chenglaoshi
    show ether happy at zoom_center
    e "Okay, Cheng Lao Shi-"
    e "Have a nice rest of your day!"
    hide ether
    show chenglaoshi base at cls_center
    ch "You too, gremlin! Remember Cheng Lao Shi will always be here to help you during lunch!"
    jump next_day_accepted_help
    return

label just_goes_to_lunch:
    scene bg cafeteria
    show ether base at zoom_center
    e "{i}Finally lunch time...{/i}"
    e "{i}I should find Rajah....{/i}"
    e "{i}Where is he?{/i}"
    e "{i}Oh, he's in the corner over there....{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}There's a lot of people over there with him...{/i}"
    e "{i}I don't want to go over there....{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}It's fine, I'll just sit by myself today.....{/i}"
    e "{i}I can finish that compilation I was watching earlier anyway, since I don't need to talk to anyone.{/i}"
    hide ether
    show ether phone at zoom_center
    e "{alpha=0.5}{i}going on his phone{/i}{/alpha}"
    hide ether
    show ether laughingphone at zoom_center
    e "{i}Wow, this is really funny....{/i}"
    e "{i}Maybe I could send this to Rajah?{/i}"
    hide ether
    show ether phone at zoom_center
    e "{i}No, he's busy...{/i}"
    e "{i}Oh, that was the bell, wasn't it?{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Is lunch already over?{/i}"
    e "{i}Time for class, I guess...{/i}"
    e "{i}I can see Rajah walking away with his big group of friends.{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}Something about seeing him so carefree makes me feel empty inside.{/i}"
    hide ether
    show ether phone at zoom_center
    e "{i}Eh, whatever, I can finish watching this video while I walk to class.{/i}"
    e "{i}I would rather know how this ends anyway than try to shoulder my way through Rajah's friend group.{/i}"
    jump next_day_no_help
    return 

# ALTERNATE ENDING START --> GOOD OR BAD
label next_day_no_help:
    # (The next day)
    scene bg blackscreen
    s "The next day.."
    scene bg chineseclassroom
    show ether base at zoom_center
    e "{i}Okay, I survived Government. I should be able to just sleaze through Mandarin.{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "----worksheet due at the end of class today!---"
    ch "---can ask Cheng Lao Shi for your peers for help! Now remember--"
    hide chenglaoshi
    show ether annoyed at zoom_center
    e "{i}This worksheet is kind of long....{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}I'll just....{/i}"
    menu:
        "Talk to Rajah":
            jump talk_to_rajah
        "Go on phone":
            jump go_on_phone_
    return

label talk_to_rajah:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "Hey Rajah, did you start the worksheet?"
    hide ether
    show rajah base at zoom_center_r 
    r "We have a worksheet?"
    hide rajah
    show ether base at zoom_center
    e "... You really weren't paying attention, were you?"
    hide ether
    show rajah blushing at zoom_center_r
    r "Honestly, no. I was trying to predict the ending of the Gilded Stars episode because I didn't get a chance to finish it but I really really wish I had-"
    hide rajah
    show ether base at zoom_center
    e "The Gilded Stars? I'm still on the Bronze Beast one-"
    hide ether
    show rajah blushing at zoom_center_r
    r "Ooooh, you better catch up FAST, Ether. The plot twists there are insane I swear the creator just loves to torment us-"
    hide rajah
    show ether annoyed at zoom_center
    e "I'm trying- I just started it a day ago-"
    hide ether
    show rajah blushing at zoom_center_r
    r "Pfft. I was binging it all morning."
    r "We're not doing anything else in this class anyway, so you might as well finish it!"
    hide rajah
    show ether base at zoom_center
    e "{i}This is probably when I should say no and do the work but....{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}I'm so tired of trying...{/i}"
    hide ether
    show ether base at zoom_center
    e "Yes, sure, why not..."
    jump go_on_phone_
    return

label go_on_phone_:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "{i}My grade can probably tank this if I don't do it...{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}Nothing I do will save it anyway when my parents yell at me everyday for it...{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}I should.. probably ask someone for help. But who would I even ask?{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}It's fine. Surely, I deserve to have a break...{/i}"
    hide ether
    show ether phone at zoom_center
    e "{alpha=0.5}{i}takes out phone{/i}{/alpha}"
    jump spiral_into_isolation
    return

label spiral_into_isolation:
    scene bg chineseclassroom
    hide ether
    show ether laughingphone at zoom_center
    e "{i}Heh-{/i}"
    hide ether
    show chenglaoshi questioning at cls_center_q
    ch "Ai, Ether, what is that I see out? Surely, you didn't pull out your phone again during Cheng Lao Shi's class again, did you?"
    # pose should be off phone
    hide chenglaoshi
    show ether upset at zoom_center
    e "No....."
    hide ether
    show chenglaoshi questioning at cls_center_q
    ch "Oh! Then what was that black rectangular device in your hand?"
    hide chenglaoshi
    show ether base at zoom_center
    e "My calculator?"
    hide ether
    show chenglaoshi serious at cls_center_s
    ch "Why would you have a calculator out for this class, child?"
    hide chenglaoshi
    show ether upset at zoom_center
    e "....."
    hide ether
    show chenglaoshi base at cls_center
    ch "You can not learn if you do not try."
    hide chenglaoshi
    show ether upset at zoom_center
    e "{i}Almost like Mr. Duras said....{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "If I see your phone out again, I'm taking i for the rest of the day."
    ch "Understood?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Yes, Cheng Lao Shi...."
    hide ether
    show chenglaoshi base at cls_center
    ch "Argh... those wretched devices and their brainwashing....."
    hide chenglaoshi
    show ether upset at zoom_center
    e "......"
    e "{alpha=0.5}{i}glancing at the worksheet{/i}{/alpha}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I'm so tired of school.... I don't want to be here anymore...{/i}"
    e "{i}I just want to disappear.......{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}There's no one for me to turn to anyway...{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Hey, Rajah's not doing any work either...... Oh, Cheng Lao Shi's telling him off too...{/i}"
    e "{i}I guess I should try doing the worksheet...{/i}"
    e "{i}Why don't I recognize any of these concepts?{/i}"
    e "{i}I remember when I thought this class was easy....{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}When did this get so hard?{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}When did everything.... get so hard?{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Rajah's on his phone again. And Cheng Lao Shi is on the other side of the room....{/i}"
    e "{i}Maybe it's fine if I.....{/i}"
    hide ether 
    show ether phone at zoom_center
    e "{alpha=0.5}{i}going on phone{/i}{/alpha}"
    hide ether
    show chenglaoshi serious at cls_center_s
    ch "HAAAAAAAAAAAAIYAAAAAAAAAAAAAAAAAA- This is ridiculous-"
    ch "Rajah, Ether, go wait outside. Cheng Lao Shi needs to have a verrrrrry stern talk with you both about your wretched devices."
    hide chenglaoshi
    show ether upset at zoom_center
    e "...."
    e "{i}Well, my parents are going to throw a fit once they find out about this.....{/i}"
    jump confrontation
    return

label confrontation:
    scene bg schoolhallway
    show ether base at zoom_center
    e "{alpha=0.5}{i}walking into the hallway{/i}{/alpha}"
    hide ether
    show rajah annoyed at zoom_center_r
    r "Damn.. he's good....."
    hide rajah
    show ether coveringface at zoom_center
    e "We're in trouble."
    # (Sprites - It would be preferable if Rajah and Cheng Lao Shi alternate, and Ether is visible but greyed out and/or lower opacity. )
    hide ether
    show rajah base at zoom_center_r
    r "Eh. Yeah."
    r "I guess we are."
    hide rajah
    show ether base at zoom_center
    e "Aren't you worried?"
    hide ether
    show rajah base at zoom_center_r
    r "What would I be worried about?"
    hide rajah
    show ether coveringface at zoom_center
    e "....."
    e "{i}Cheng Lao Shi punishing us? Phoning our parents? Grade backlash?{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "Alright, you two MISCHEVIOUS gremlins."
    hide chenglaoshi
    show chenglaoshi serious at cls_center_s
    ch "You've been on your phones for TOO LONG this class."
    hide chenglaoshi
    show ether upset at zoom_center
    e "...."
    hide ether
    show chenglaoshi base at cls_center
    ch "So tell Cheng Lao Shi why you two were on your phones."
    hide chenglaoshi
    show rajah annoyed at zoom_center_r
    r "Frankly, Cheng Lao Shi, I was bored out of my mind."
    hide rajah
    show chenglaoshi sideeye at cls_center_q
    ch "You didn't even finish the worksheet!"
    hide chenglaoshi
    show rajah nervous at zoom_center_r
    r "See, I tried to do it.. and then I gave up."
    hide rajah
    show chenglaoshi sideeye at cls_center_q
    ch "You gave up?"
    hide chenglaoshi
    show rajah annoyed at zoom_center_r
    r "....."
    r "Yes."
    hide rajah
    show chenglaoshi questioning at cls_center_q
    ch "Why did you give up? The worksheet only had four questions on it! It was not supposed to take more than 15 minutes to finish!"
    hide chenglaoshi
    show rajah blushing at zoom_center_r
    r "I just. I don't know, I just didn't have motivation to finish it."
    hide rajah
    show chenglaoshi serious at cls_center_s
    ch "So you decided to seek refuge on that phone of yours instead?"
    hide chenglaoshi
    show rajah nervous at zoom_center_r
    r "........... yeah, pretty much."
    hide rajah
    show chenglaoshi questioning at cls_center_q
    ch "Why didn't you ask for help?"
    # thinking pose?
    hide chenglaoshi
    show rajah blushing at zoom_center_r
    r "........"
    r "I guess I didn't think about doing that."
    hide rajah
    show chenglaoshi base at cls_center
    ch "Aiya.... Rajah-"
    ch "No, both of you could have asked anyone in the class, including me, for help. I'm sure your comrades would be willing to lend you a hand if you tried."
    ch "Do you understand that by choosing your phone over your work, your grades will decline?"
    ch "Your grades do not need to suffer such needless grief!"
    hide chenglaoshi
    show rajah base at zoom_center_r
    r "Mhm."
    hide rajah
    show chenglaoshi base at cls_center
    ch "You have all day after school to be on your phone. I only need you to do work for 15 minutes."
    hide chenglaoshi
    show rajah base at zoom_center_r
    r "Mhm."
    hide rajah
    show chenglaoshi questioning at cls_center_q
    ch "Do you expect to pass the class without trying?"
    hide chenglaoshi
    show rajah base at zoom_center_r
    r "......"
    hide rajah
    show ether base at zoom_center
    e "........"
    hide ether
    show chenglaoshi serious at cls_center_s
    ch "{alpha=0.5}{i}SIGHHHHHH{/i}{/alpha}"
    hide chenglaoshi
    show chenglaoshi base at cls_center
    ch "You two were doing well in the beginning of the year. What changed?"
    hide chenglaoshi
    show rajah nervous at zoom_center_r
    r "....... guess I just lost the will to try in school, Cheng Lao Shi. I dunno what else to tell ya."
    hide rajah
    show chenglaoshi serious at cls_center_s
    ch "Is that all you are going to say?"
    hide chenglaoshi
    show rajah nervous at zoom_center_r
    r "{alpha=0.5}{i}shrugs{/i}{/alpha}"
    hide rajah
    show chenglaoshi base at cls_center
    ch "Alrrrright. Rajah, go back inside and ask someone for help. I expect that worksheet to be done by the end of class."
    hide chenglaoshi
    show rajah blushing at zoom_center_r
    r "Yes, sir...."
    r "{alpha=0.5}{i}leaves{/i}{/alpha}"
    hide rajah
    show chenglaoshi sideeye at cls_center_q
    ch "So... Ether."
    hide chenglaoshi
    show chenglaoshi base at cls_center
    ch "Cheng Lao Shi notices you haven't said anything at all."
    hide chenglaoshi
    show ether upset at zoom_center
    e "......"
    hide ether
    show chenglaoshi base at cls_center
    ch "Cheng Lao Shi also notices your grade was very good until the last several days."
    ch "Did something happen?"
    hide chenglaoshi
    show ether upset at zoom_center
    e "........"
    hide ether
    show ether coveringface at zoom_center
    e "I just...."
    e "{i}What am I supposed to say?{/i}"
    e "{i}That I lost motivation to try?{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "Ai... Ether, can you at least answer me this? Are you struggling in the class?"
    hide chenglaoshi
    show ether base at zoom_center
    e "A.. little...."
    hide ether
    show chenglaoshi base at cls_center
    ch "Remember, Ether, you can always come in during lunch to ask for help."
    ch "Cheng Lao Shi knows you can be better than this."
    hide chenglaoshi
    show ether base at zoom_center
    e "Okay....."
    hide ether
    show chenglaoshi base at cls_center
    ch "Do you need help on today's worksheet?"
    hide chenglaoshi
    show ether upset at zoom_center
    e "... no ...."
    hide ether
    show ether annoyed at zoom_center
    e "I can do it on my own...."
    hide ether
    show chenglaoshi base at cls_center
    ch "Fineeee.. I trust you.."
    ch "But remember, you can always come in during lunch to ask me for help, yes?"
    hide chenglaoshi
    show ether base at zoom_center
    e "{alpha=0.5}{i}nods{/i}{/alpha}"
    menu:
        "Consider Cheng Lao Shi's words":
            jump consider_ch_words
        "Don't listen to Cheng Lao Shi":
            jump dont_listen_ch
    return

label consider_ch_words:
    #-----------------------------------------------after class
    scene bg blackscreen
    s "After class.."
    scene bg chineseclassroom
    s "{alpha=0.5}{i}bell ringing{/i}{/alpha}"
    show chenglaoshi base at cls_center
    ch "That's it for class today! Cheng Lao Shi expects you to turn in the worksheet in the basket by the door and eat a big, healthy lunch!"
    ch "Go munch munch, you gremlins!"
    hide chenglaoshi
    show rajah annoyed at zoom_center_r
    r "It's lunch already? I'm not even done with the worksheet yet-"
    hide rajah
    show ether base at zoom_center
    e "How far did you get?"
    hide ether
    show rajah base at zoom_center_r
    r "I have one more to finish- you?"
    hide rajah
    show ether base at zoom_center
    e "After I finish this sentence, I'm done."
    hide ether
    show rajah nervous at zoom_center_r
    r "Nice. Can ya show me what ya wrote for the last one?"
    hide rajah
    show ether base at zoom_center
    e "Here."
    hide ether
    show rajah blushing at zoom_center_r
    r "Oh that makes sense- damn I really should've figured that out earlier but it's fine-"
    hide rajah
    show rajah base at zoom_center_r
    r "Alright, I'm done. You want me to turn yours in too?"
    hide rajah
    show ether base at zoom_center
    e "That would be great, thanks!"
    e "{alpha=0.5}{i}walking into the hallway{/i}{/alpha}"
    scene bg schoolhallway
    show rajah base at zoom_center_r
    r "Phew, we're done with that class for today."
    hide rajah
    show rajah blushing at zoom_center_r
    r "Usually, I don't care so much about Cheng Lao Shi's class, but him pulling us both out of class had me on edge the entire period."
    hide rajah
    show rajah base at zoom_center_r
    r "What'd he say to you after I left?"
    hide rajah
    show ether base at zoom_center
    e "......"
    hide ether
    show ether annoyed at zoom_center
    e "About the same thing. He just said 'oh you used to be so much better', 'i know you can do more than this', stuff like that."
    hide ether
    show ether base at zoom_center
    e "He still told me to finish the worksheet like he told you before he sent you back inside."
    hide ether
    show rajah base at zoom_center_r
    r "That's it?"
    hide rajah
    show ether base at zoom_center
    e "He also told me I could come into his room during lunch to ask him for help...."
    hide ether
    show rajah base at zoom_center_r
    r "Are you gonna consider it?"
    hide rajah
    show ether base at zoom_center
    e "Maybe....."
    e "Would you?"
    hide ether
    show rajah nervous at zoom_center_r
    r "Honestly, Ether, after the entire Duras situation, I'm not exactly looking to spend extra time with teachers."
    hide rajah
    show ether base at zoom_center
    e "Cheng Lao Shi seems a little more reasonable."
    e "Cheng Lao Shi actually offered to help. Mr. Duras didn't."
    hide ether
    show rajah annoyed at zoom_center_r
    r "Eh. Teachers. Adults. They're all the same. You take your chances if you want. I'll pass."
    hide rajah
    show ether base at zoom_center
    e "{i}Rajah doesn't think Cheng Lao Shi will really be any different from Mr. Duras, huh?{/i}"
    e "{i}But.. They aren't the same.{/i}"
    e "{i}I want to give Cheng Lao Shi a chance.{/i}"
    jump stops_phone_addiction_from_going_too_far
    return

label dont_listen_ch:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "{i}Come in during lunch?{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}If I learned anything from Mr. Duras.....{/i}"
    e "{i}It's that teachers don't care.{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Here's the worksheet.{/i}"
    e "{i}It's.....{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}I don't want to do it.{/i}"
    e "{i}My grade in government is already dropping. It doesn't matter how low my Mandarin grade is if my parents are going to get mad with me regardless.{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}Even Rajah isn't actually working... Is he on his phone?{/i}"
    e "{i}And everyone around is just talking anyway ....{/i}"
    e "{i}Did they finish already?{/i}"
    e "{i}If no one's working.....{/i}"
    e "{i}Then why should I?{/i}"
    e "{i}I'll just go on my phone...{/i}"
    hide ether
    show ether phone at zoom_center
    e "{i}Oh, Rajah sent me something!{/i}"
    hide ether
    show ether laughingphone at zoom_center
    e "{i}This reminds me of Blaire- Oh that's hilarious-{/i}"
    e "{i}The short right under is by the same creator! I wonder if Rajah would like that-{/i}"
    hide ether
    show chenglaoshi serious at cls_center_s
    ch "Ether!"
    # ether afraid
    hide chenglaoshi
    show ether upset at zoom_center
    e "Hi, Cheng Lao Shi-"
    hide ether
    show chenglaoshi base at cls_center
    ch "Hello, Ether."
    ch "Could you come outside with me again?"
    hide chenglaoshi
    show ether upset at zoom_center
    e "{i}I should've been more careful...{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}Rajah just put his phone away as Cheng Lao Shi walked by...{/i}"
    e "{i}He didn't get caught.....{/i}"
    # --in the hallway--
    scene bg schoolhallway
    s "--In the hallway--"
    show chenglaoshi base at cls_center
    ch "So Ether..."
    ch "Did you finish the work for today?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Not yet..."
    hide ether
    show chenglaoshi sideeye at cls_center_q
    ch "I see you were not working on it."
    hide chenglaoshi
    show ether upset at zoom_center
    e "No.... I wasn't...."
    hide ether
    show chenglaoshi base at cls_center
    ch "Do you want to explain why you were on your phone instead of doing the work again?"
    hide chenglaoshi
    show ether base at zoom_center
    e "....."
    hide ether
    show chenglaoshi base at cls_center
    ch "Cheng Lao Shi stands by what he said before. Cheng Lao Shi believes you have done better before."
    hide chenglaoshi
    show ether base at zoom_center
    e "....."
    hide ether
    show chenglaoshi base at cls_center
    ch "So why was Ether on his phone?"
    hide chenglaoshi
    show ether base at zoom_center
    e "......"
    hide ether
    show chenglaoshi base at cls_center
    ch "....."
    hide chenglaoshi
    show ether base at zoom_center
    e "......"
    hide ether
    show chenglaoshi base at cls_center
    ch "... I will not understand if you do not tell me, Ether."
    hide chenglaoshi
    show ether coveringface at zoom_center
    e "....."
    e "I.. have a hard time grasping content sometimes."
    hide ether
    show chenglaoshi base at cls_center
    ch "Oh?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Nevermind. I'll do the worksheet-"
    hide ether
    show chenglaoshi base at cls_center
    ch "No. You stay here."
    ch "You can do the worksheet right now, but the problem that led you to go on your phone will not be solved."
    ch "You only started going on your phone excessively in the last week. What happened last week?"
    hide chenglaoshi
    show ether upset at zoom_center
    e "....."
    e "{i}Should I tell him about Mr. Duras?{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}No, that would be embarassing...{/i}"
    e ".. I don't know."
    hide ether
    show chenglaoshi base at cls_center
    ch "How can I help you if you do not tell me?"
    hide chenglaoshi
    show ether base at zoom_center
    e "It's fine. I'll just go back in and do the worksheet."
    e "I am sorry for being off-task."
    hide ether
    show ether annoyed at zoom_center
    e "{i}I don't need your help, Cheng Lao Shi. My phone can help me just fine.{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "...."
    ch "I am going to send you to the counselor's office."
    hide chenglaoshi
    show ether base at zoom_center
    e "Oh, okay."
    hide ether
    show ether annoyed at zoom_center
    e "{i}I guess I'm really in trouble now, huh?{/i}"
    hide ether
    show ether base at zoom_center
    e "{i}But if I was getting sent home, wouldn't he have sent me to the principal instead?{/i}"
    hide ether
    show chenglaoshi base at cls_center
    ch "Here you go. Take your things with you!"
    hide chenglaoshi
    show ether base at zoom_center
    e "{i}And now I leave...{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}Probably to get chewed out by more adults....{/i}"
    hide ether
    show ether coveringface at zoom_center
    e "{i}I really don't want to be here anymore.......{/i}"
    jump go_to_counselor
    return

label go_to_counselor:
    scene bg blackscreen
    s "On the way to the counselor's office.."
    scene bg schoolhallway
    # (Note - he's on his phone before arriving at the office)
    show ether phone at zoom_center
    e "{i}The counselor's office is here.....{/i}"
    e "{i}I've never actually had a real conversation with Ms. Antimony before.{/i}"
    hide ether
    show ether upset at zoom_center
    e "{i}But I don't think this is going to going well...{/i}"
    e "{alpha=0.5}{i}walking in{/i}{/alpha}"
    scene bg counseloroffice
    show antimony base at ant_center
    an "Hello, Ether."
    hide antimony
    show ether base at zoom_center
    e "Hi Ms. Antimony."
    e "Cheng Lao Shi sent me here for the period."
    hide ether
    show antimony base at ant_center
    an "I see."
    an "I just received a message that he did send you here just before you came in."
    hide antimony
    show ether base at zoom_center
    e "Oh."
    e "That's good to know."
    hide ether
    show ether annoyed at zoom_center
    e "{i}I already want to leave.{/i}"
    hide ether
    show antimony base at ant_center
    an "Do you know why Cheng Lao Shi sent you here?"
    hide antimony
    show ether base at zoom_center
    e "Well....."
    hide ether
    show ether annoyed at zoom_center
    e "I already know what I did wrong, so I don't think I have to be here...."
    e "I can go back to class and work on the stuff he wanted me to do anyway."
    hide ether
    show antimony base at ant_center
    an "Interestingly, Cheng Lao Shi's reason for sending you here actually has nothing to do with you not doing work in class."
    an "It has to do with... your phone addiction."
    hide antimony
    show ether base at zoom_center
    e "Oh."
    e "Did he say anything else?"
    hide ether
    show antimony base at ant_center
    an "Cheng Lao Shi tells me your phone addiction only started recently. Is this true?"
    hide antimony
    show ether base at zoom_center
    e "Yes...."
    hide ether
    show antimony base at ant_center
    an "Could you tell me more about when you started going on your phone during class?"
    hide antimony
    show ether base at zoom_center
    e "What do you mean?"
    hide ether
    show antimony base at ant_center
    an "Why did you start going on your phone during class?"
    hide antimony
    show ether coveringface at zoom_center
    e "I... didn't feel as though the effort I was putting into class was worth it."
    hide ether
    show antimony base at ant_center
    an "What made you think it wasn't worth it?"
    hide antimony
    show ether upset at zoom_center
    e "...."
    e "{i}Do I tell them about Mr. Duras?{/i}"
    e "{i}They might think I'm being unreasonable, though.{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "{i}They usually believe the adult over the student...{/i}"
    hide ether
    show antimony base at ant_center
    an "This is a safe space, Ether. Anything you tell me here will be confidential, unless you mention self-harm or harming anyone else."
    hide antimony
    show ether base at zoom_center
    e "I don't plan to hurt anyone...."
    hide ether
    show antimony base at ant_center
    an "I'm glad you don't."
    an "Could you tell me why you didn't think the effort you put in class wasn't 'worth it'?"
    hide antimony
    show ether base at zoom_center
    e "I felt like the teacher wasn't giving me a chance."
    hide ether
    show antimony base at ant_center
    an "Cheng Lao Shi wasn't giving you a chance?"
    hide antimony
    show ether base at zoom_center
    e "Um, no. Not Cheng Lao Shi. Mr. Duras."
    hide ether
    show antimony base at ant_center
    an "How so?"
    hide antimony
    show ether base at zoom_center
    e "...."
    hide ether 
    show ether annoyed at zoom_center
    e "I tried asking him for help during class, because I couldn't catch up with the lecture, and he told me to ask someone else for help since it was my own fault I wasn't paying attention."
    hide ether
    show antimony base at ant_center
    an "Could you tell me about the Mr. Duras' lectures? What made it hard to catch up?"
    hide antimony
    show ether annoyed at zoom_center
    e ".. when Mr. Duras is lecturing, he's always doing multiple things at once. While he talks, he points to the slides, walks around, waves his hands, and he expects us to be able to copy and process everything on the slides at the same time."
    hide ether 
    show ether coveringface at zoom_center
    e "There's always so much going on."
    hide ether 
    show ether annoyed at zoom_center
    e "I tried to tell him that I couldn't focus because everything was so distracting, but he just told me it was because I wasn't trying."
    hide ether
    show antimony base at ant_center
    an "I see.... "
    an "How does that make you feel?"
    hide antimony
    show ether base at zoom_center
    e "It makes me feel a little dumb. Because everyone else is able to catch up on everything Mr. Duras wants us to do just fine, so why can't I?"
    hide ether 
    show ether coveringface at zoom_center
    e "Is there something wrong with me?"
    hide ether
    show antimony base at ant_center
    an "I don't think so, Ether."
    hide antimony
    show ether base at zoom_center
    e "How do you know?"
    hide ether 
    show ether upset at zoom_center
    e "My grade in Mr. Duras' class keeps dropping, and all my other class grades are slowly dropping too...."
    hide ether
    show antimony base at ant_center
    an "Do you only have trouble focusing in Mr. Duras' class?"
    hide antimony
    show ether base at zoom_center
    e "Sometimes......"
    hide ether
    show antimony base at ant_center
    an "When did you start turning to your phone during class?"
    hide antimony
    show ether base at zoom_center
    e "....."
    e "{i}That's.... a good question...{/i}"
    e "{i}I'm not sure I can answer...{/i}"
    hide ether
    show antimony base at ant_center
    an "Let's go back to the class questions first."
    an "So to reiterate, you felt that Mr. Duras wasn't giving you a chance, correct?"
    hide antimony
    show ether annoyed at zoom_center
    e "Yes.... I have tried talking to him about it... but he doesn't like listening...."
    hide ether
    show antimony base at ant_center
    an "Are there any other teachers you have that teach the same way Mr. Duras does? For example, does Cheng Lao Shi make you feel the same way?"
    hide antimony
    show ether base at zoom_center
    e "Cheng Lao Shi usually doesn't have so many things going on while he teaches..."
    e "Cheng Lao Shi also offers to help a lot in class. Mr. Duras doesn't necessarily do that."
    hide ether
    show antimony base at ant_center
    an "Hmmmmmmmm."
    an "Do you think it's easier to learn in Cheng Lao Shi's class, compared to Mr. Duras' class?"
    hide antimony
    show ether base at zoom_center
    e "A little bit, yes. I feel like it's a lot easier to process what Cheng Lao Shi is saying because he doesn't expect us to multitask during his lectures."
    e "Then I start wondering if I'm just really stupid in Government, but that's probably just me being slow."
    hide ether
    show antimony base at ant_center
    an "Hm. Okay."
    an "Ether, I'd like to introduce a term to you. It's called 'overstimulation'. When a person is overstimulated, it's because there's too much going on for the person to process. Do you feel like that's what happens to you in Mr. Duras' class?"
    hide antimony
    show ether annoyed at zoom_center
    e "Yes. In Ms. Fong's class too, she's always going too fast and I never fully understand anything she teaches until I ask someone else to explain it much slower to me."
    e "There's so much going on, and not enough time for me to comprehend everything!"
    hide ether
    show antimony base at ant_center
    an "Understandably so. Do any of your other peers seem to struggle the same way you do?"
    hide antimony
    show ether base at zoom_center
    e "Not a lot of them, no."
    hide ether 
    show ether coveringface at zoom_center
    e "Is there something wrong with me, Ms. Antimony?"
    hide ether
    show antimony base at ant_center
    an "No. I don't think so."
    an "I just think that certain teaching styles don't work for you, Ether, and that's okay, because everyone's brain works differently. You process information a little differently than everyone else, and that's what makes it hard to learn."
    hide antimony
    show ether base at zoom_center
    e "Neurodivergent."
    e "Wait, so does that mean I'm autistic or something?"
    e "{i}I don't want to be autistic...{/i}"
    hide ether
    show antimony base at ant_center
    an "Not at all. It just means you learn differently. You're just as 'smart' as any other student at this school."
    an "How does this make you feel?"
    hide antimony
    show ether base at zoom_center
    e "That explains some things...."
    hide ether
    show antimony base at ant_center
    an "A lot of neurodivergent individuals, like you, also have learning struggles in school. Many of them, similar to you, also get frustrated, and turn in different mechanisms to help them deal with it."
    an "How have you been dealing with your frustration with school lately?"
    hide antimony
    show ether base at zoom_center
    e "I dunno."
    e "Going on the internet and watching YouTube, I suppose."
    hide ether
    show antimony base at ant_center
    an "Do you feel that's helping you deal with your emotions?"
    hide antimony
    show ether base at zoom_center
    e "Yes."
    e "It helps me mentally escape school, because it never seems to end."
    hide ether
    show antimony base at ant_center
    an "Did you often watch YouTube at school for the same reason?"
    hide antimony
    show ether upset at zoom_center
    e "...."
    e "{alpha=0.5}{i}thinking{/i}{/alpha}"
    hide ether 
    show ether base at zoom_center
    e "Yes...."
    hide ether
    show antimony base at ant_center
    an "Do you think this is healthy for you?"
    hide antimony
    show ether base at zoom_center
    e "I feel like it's fine...."
    hide ether
    show antimony base at ant_center
    an "Have you noticed any changes in your general behavior lately?"
    hide antimony
    show ether base at zoom_center
    e "Uh....."
    hide ether
    show antimony base at ant_center
    an "Have you been eating and sleeping the same amount? Do you feel any better about school when you're not on your phone?"
    hide antimony
    show ether base at zoom_center
    e "I {i}have{/i} been sleeping a little later than usual... waking up a little more tired..."
    e "My feelings about school haven't changed much since I started going on my phone..."
    hide ether
    show antimony base at ant_center
    an "Have you been talking to many people since you started going on your phone?"
    hide antimony
    show ether base at zoom_center
    e "No... I just.. go on my phone.."
    hide ether
    show antimony base at ant_center
    an "Have you asked anyone for help with school since going on your phone?"
    hide antimony
    show ether base at zoom_center
    e "A couple times before... but not really, no..."
    hide ether
    show antimony base at ant_center
    an "Do you think you could tell me why?"
    hide antimony
    show ether annoyed at zoom_center
    e "I.... don't.. really want to talk to people about school."
    hide ether
    show antimony base at ant_center
    an "Why not?"
    hide antimony
    show ether coveringface at zoom_center
    e "I'm... not quite sure. They make me feel stupid...."
    hide ether
    show antimony base at ant_center
    an "How much do you personally care about school?"
    hide antimony
    show ether base at zoom_center
    e "I know it's important I graduate so I can find a good career..."
    hide ether 
    show ether upset at zoom_center
    e "I know being on my phone during class isn't good, but it feels like it's the only thing that helps me deal with how I feel about school."
    hide ether
    show antimony base at ant_center
    an "Would you be open to exploring other ways to dealing with your frustration?"
    hide antimony
    show ether base at zoom_center
    e "Uh... sure....."
    hide ether 
    show ether annoyed at zoom_center
    e "{i}I'm already tired of being here...{/i}"
    hide ether
    show antimony base at ant_center
    an "Being on your phone for extended periods of time can worsen your sleep schedule, mental health, and lead to social isolation. I'd like to encourage you to find a healthier means of dealing with your frustration."
    hide antimony
    show ether base at zoom_center
    e "... okay, Ms. Antimony..."
    hide ether
    show antimony base at ant_center
    an "One of the best ways to deal with emotions is to write them down. You mentioned that your feelings about school didn't change much after being on your phone?"
    hide antimony
    show ether base at zoom_center
    e "Yes...."
    e "I guess that now that I think about it, I'm not really expressing them..."
    hide ether
    show antimony base at ant_center
    an "This is where you can start journaling to help process how you're really feeling. Studies have shown that a lot of people like you have tried writing, and it has helped them understand how they're feeling and why they're feeling that way."
    an "It's also a good way to self-reflect on how you're doing in school and at home."
    an "How would you feel about trying it?"
    hide antimony
    show ether base at zoom_center
    e "....I'll think about it..."
    hide ether
    show antimony base at ant_center
    an "It's completely okay if it doesn't work for you. You can come back, and we'll find something that does! But I want you to try journaling later today in this notebook I'm going to give you and see how you feel afterward. Does that sound okay to you?"
    hide antimony
    show ether base at zoom_center
    e "Okay..."
    hide ether
    show antimony base at ant_center
    an "I believe the lunch bell has just rung. Have a good day, Ether."
    hide antimony
    show ether base at zoom_center
    e "You too, Ms. Antimony...."
    # ------ (At home)
    scene bg blackscreen
    s "At home.."
    scene bg bedroom
    show ether base at zoom_center
    e "The day's finally over...."
    hide ether 
    show ether annoyed at zoom_center
    e "I really don't want to do homework yet...."
    hide ether 
    show ether happy at zoom_center
    e "Maybe I'll just watch some more SladeSlice and scroll for a bit-"
    hide ether 
    show ether base at zoom_center
    e "... I already know that's bad for me. Maybe I shouldn't do that..."
    e "Ms. Antimony suggested I try journaling, but that sounds a little silly to me. Should I...?"
    menu:
        "Try journaling":
            jump e_journals
        "Do not journal":
            jump do_not_journal
    return

#Good ending start
label e_journals:
    scene bg bedroom
    show ether base at zoom_center
    e "Well.. it's not like I could feel any worse..."
    e "There's that notebook Ms. Antimony gave me..."
    e "Oh, there's a prompt on this page!"
    hide ether 
    show ether happy at zoom_center
    e "There's a different prompt on every page..."
    hide ether 
    show ether base at zoom_center
    e " 'How are you feeling today?' "
    s "-Journal-"
    ej "I feel... tired. I went on my phone during Mandarin today, but Cheng Lao Shi pulled me out of class to tell me to go to Ms. Antimony's office. Ms. Antimony to try writing about my feelings so I could get resolve my... 'phone addiction'."
    ej "I guess Ms. Antimony thought that me being on my phone for too long was bad for me, so here I am. I guess it's helping a little, to write about how I feel."
    ej "I'm honestly at the point where I just don't like going to school anymore because nothing I do feels like it has much value... I don't know how I feel abot Ms. Antimony telling me I'm 'neurodivergent' because it doesn't really change anything."
    ej "If I tried telling Mr. Duras that I haven't been 'paying attention' during his class because I was neurodivergent, I don't think he would believe me. He'd probably tell me I made up the word or something."
    ej "You know, I'm beginning to realize most of this is really just Mr. Duras. Mr. Duras is the only teacher that makes me feel like I'm doing something wrong. I think now that I'm really thinking about it, Cheng Lao Shi genuinely wanted to help me. I just didn't want to tell him anything."
    s "-End journal-"
    hide ether 
    show ether happy at zoom_center
    e "Huh... I guess it really did help. I feel... calmer? it feels like there's not as much going on in my head now that I've written some of it down."
    e "Ms. Antimony was right. Maybe I'll go see her tomorrow."
    jump e_keeps_journaling
    return

label e_keeps_journaling:
    #----- (the next day- bg is school hallway)
    scene bg blackscreen
    s "The next day.."
    scene bg schoolhallway
    show rajah base at zoom_center_r
    r "Ether! Where'd ya go after Cheng Lao Shi pulled ya out of class?"
    hide rajah
    show ether base at zoom_center
    e "I was in Ms. Antimony's office. I'm about to go to her office, actually."
    hide ether
    show rajah base at zoom_center_r
    r "Dang, what for?"
    hide rajah
    show ether base at zoom_center
    e "Yesterday, Cheng Lao Shi sent me to Ms. Antimony's office because he was concerned about my phone addiction. Ms. Antimony suggested I journal to deal with how I was feeling better."
    hide ether 
    show ether happy at zoom_center
    e "I tried journaling too, and it did feel better than going on my phone."
    e "I feel like when I'm going on my phone, I'm just ignoring how I feel. I think it makes me feel more stressed, actually, because I'm consuming so much content. When I write it down I can acknowledge and process it so I feel more at ease."
    hide ether
    show rajah base at zoom_center_r
    r "Huh. Glad it works for you."
    hide rajah
    show rajah annoyed at zoom_center_r
    r "Cheng Lao Shi sent me to Ms. Antimony's office for the same reason. I realy didn't like journaling though, 'cause I find writing boring."
    hide rajah
    show ether base at zoom_center
    e "Have you thought of going back to try other things?"
    hide ether 
    show ether happy at zoom_center
    e "I'm sure there has to be something else that could help you!"
    hide ether
    show rajah base at zoom_center_r
    r "Eh.. maybe...."
    hide rajah
    show rajah annoyed at zoom_center_r
    r "Ms. Antimony's not the first one to tell me my phone isn't good for me either. My parents have been yelling at me for not sleeping enough."
    r "I've been more tired and depressed lately, so I'm not convinced anything is really going to work."
    hide rajah
    show ether base at zoom_center
    e "Didn't Ms. Antimony mention that being on your phone worsens your mental health?"
    hide ether
    show rajah nervous at zoom_center_r
    r "Huh?"
    r "Oh, yeah, I guess she did say that..."
    hide rajah
    show ether happy at zoom_center
    e "Come on, we can go see Ms. Antimony together."
    jump good_ending
    return

label good_ending:
#    ---------------- One month later --
    scene bg blackscreen
    s "One month later.."
    scene bg bedroom
    show ether happy at zoom_center
    ej "11/01/XXXX"
    ej "Dear Journal,"
    ej "I have great news! I've finally gotten my grade for Government back up to an A!"
    ej "I'm so glad I stopped relying on just Mr. Duras to help me in Government. Rajah was the one who suggested asking Danny instead, and Danny can actually explain things way more slowly than Mr. Duras. I'll have to get him something as a thank you later."
    ej "I'm realizing that since I started writing, I've felt a lot better about myself! I started looking up what it meant to be 'neurodivergent' since it still didn't make a whole lot of sense to me. I brought it up to my parents once, and they thought that meant I had ADHD or something like that."
    ej "It turns out that neurodivergence is an umbrella term for things {i}like{/i} OCD, autism, and ADHD. Someone who has those things is neurodivergent, but not every neurodivergent person has those exact disorders."
    ej "I'm really grateful to Cheng Lao Shi for giving me a chance. If Cheng Lao Shi had shut me down just like Mr. Duras had so long ago, I think I would've lost all hope in school."
    ej "Compared to a month ago, I feel a lot calmer and collected. It's really cool to explore my thoughts by writing. It's like I'm getting to know myself by doing this. Ms. Antimony tells me that it's called 'writing therapy'."
    ej "It turns out there's different types of writing too! Expressive writing is the kind I've been doing with Ms. Antimony, where she gives me a prompt and I write about it. I've also tried control writing, but the rules are little bit more strict."
    ej "Anyhow, it's been great to see my progress. Any time I want, I can flip through the pages and reread my entries to see how far I've come. I used to be a little unsure of myself, but now I'm talking to more people in my classes to connect with them."
    ej "That's all for today. See you soon, Journal!"
    ej "Signing off,\nEther"
    scene bg blackscreen
    s "Good Ending Reached!"
    return
#end of good ending

#Bad ending Start
label do_not_journal:
    scene bg bedroom
    show ether annoyed at zoom_center
    e "Right, because writing things down is going to make me feel better about school?"
    e "No."
    e "It's not like anything I write is going to make a difference to Mr. Duras, who's still going to fail me whether or not I'm trying in his class anyway."
    hide ether 
    show ether phone at zoom_center
    e "No, I'm just going to scroll. At least {i}that{/i} doesn't feel like a waste of time...."
    #-------------------------- (the next day)
    scene bg blackscreen
    s "The next day.."
    scene bg schoolhallway
    show rajah base at zoom_center_r
    r "Yo! Ether!"
    hide rajah
    show ether base at zoom_center
    e "Hi Rajah!"
    hide ether
    show rajah base at zoom_center_r
    r "Where'd Cheng Lao Shi send you yesterday?"
    hide rajah
    show ether annoyed at zoom_center
    e "Oh, he sent me to the counselor's office."
    e "Ms. Antimony said it was something about a phone addiction...."
    hide ether
    show rajah annoyed at zoom_center_r
    r "Yeah, Cheng Lao Shi sent me over to her office once too. She told me it was bad to be on your phone all the time, bad for your physical and mental health and sleep schedule yada yada yada I could've cared less..."
    r "She told me to try journaling to 'deal with my emotions' better."
    hide rajah
    show ether base at zoom_center
    e "She told me the same thing too!"
    e "Did you end up trying it?"
    hide ether
    show rajah blushing at zoom_center_r
    r "Lowkey I just wrote two sentences and lost motivation because writing is really boring to me..."
    r "I'm not gonna lie, I didn't see how it was supposed to help me."
    hide rajah
    show rajah nervous at zoom_center_r
    r "Don't tell me you actually tried it?"
    hide rajah
    show ether base at zoom_center
    e "I thought about it.... but I just ended up watching YouTube all night instead."
    e "I mean, it was a little more entertaining than writing anyway..."
    hide ether
    show rajah nervous at zoom_center_r
    r "Ha! You and me both, bud."
    hide rajah
    show rajah blushing at zoom_center_r
    r "You're still nowhere close to my level, though. Catch up!"
    hide rajah
    show ether happy at zoom_center
    e "Don't worry, I will!"
    jump bad_ending
    return

label bad_ending:
    # ------- (one month later...)
    scene bg blackscreen
    s "One month later..."
    scene bg bedroom
    show ether phone at zoom_center
    e "{alpha=0.5}{i}scrolling on social media{/i}{/alpha}"
    #gradually getting more sad
    e "Oh, it looks like Blaire, Danny, and Roger went bowling yesterday. They seemed to have a lot of fun."
    e "They got to go on a field trip for that? Lucky."
    hide ether 
    show ether upset at zoom_center
    e "I wish I could go on that field trip... but.. well...."
    hide ether 
    show ether coveringface at zoom_center
    e "It's 2 AM. I should probably go to bed. Better for my health."
    e "Eh, whatever. My grades are already trash, my parents hate me, and the only thing I can do to escape all that is going on my phone."
    e "It's like no one even needs me...."
    hide ether 
    show ether upset at zoom_center
    e "What is there to live for anyway?"
    hide ether 
    show ether annoyed at zoom_center
    e "I can go to sleep, but I'd still be tired the next morning."
    e "I can go to school, but all I do is get yelled at. I don't even have anyone to talk to."
    hide ether 
    show ether coveringface at zoom_center
    e "There's nothing for me to strive for anymore."
    e "Nothing at all......"
    e "What... am I supposed.. to do...?"
    scene bg blackscreen
    s "Bad Ending Reached!"
    return
#bad ending end

# NEUTRAL ENDING STARTTTTTTTT
label next_day_accepted_help:
    # --------------------------------------------------------------- (During lunch the next day...)
    scene bg blackscreen
    s "During lunch the next day..."
    scene bg cafeteria
    show rajah base at zoom_center_r
    r "Ether!"
    hide rajah
    show ether base at zoom_center
    e "Hi Rajah!"
    hide ether
    show rajah base at zoom_center_r
    r "Where were you at lunch yesterday! I couldn't find you."
    hide rajah
    show ether base at zoom_center
    e "I was in Cheng Lao Shi's classroom finishing the worksheet from class."
    hide ether
    show rajah base at zoom_center_r
    r "Oh, nice!"
    r "Did you finish?"
    hide rajah
    show ether happy at zoom_center
    e "Yeah! Cheng Lao Shi was actually really nice about explaining things to me."
    hide ether 
    show ether upset at zoom_center
    e "I was initially afraid to ask him because I thought he'd be like Mr. Duras...."
    hide ether
    show rajah annoyed at zoom_center_r
    r "That's exactly why {i}I{/i} didn't bother asking Cheng Lao Shi..."
    hide rajah
    show ether happy at zoom_center
    e "No, you should ask him for help! He'll probably make fun of you, but he won't shut you down like Mr. Duras."
    hide ether
    show rajah nervous at zoom_center_r
    r "Eh.... I'll think about it..."
    hide rajah
    show ether happy at zoom_center
    e "I'm going to go to his room right now so I can ask about what we talked about during class today. Do you want to come with?"
    hide ether
    show rajah blushing at zoom_center_r
    r "I'm gooooooooooooooooooooooooooood-"
    hide rajah
    show ether base at zoom_center
    e "I'll see you in history?"
    hide ether
    show rajah base at zoom_center_r
    r "Yup."
    r "See ya later!"
    jump e_keeps_going_to_ch_for_help
    return

label e_keeps_going_to_ch_for_help:
    # -------- (walking into Mandarin classroom)
    scene bg chineseclassroom
    show ether happy at zoom_center
    e "Hi Cheng Lao Shi!"
    hide ether
    show chenglaoshi base at cls_center
    ch "Ether! Hello hello!"
    ch "How can I help you today, child?"
    hide chenglaoshi
    show ether base at zoom_center
    e "I wanted to make sure I understood all the vocabulary words for this week so I could use them in sentences for the homework."
    hide ether
    show chenglaoshi base at cls_center
    ch "Ah, of course! I'm glad you're willing to come back to get help."
    ch "Which words are confusing to you?"
    hide chenglaoshi
    show ether base at zoom_center
    e "I think 3 and 4....?"
    hide ether
    show chenglaoshi base at cls_center
    ch "The two transaction words.. yes... mǎi and mài!"
    hide chenglaoshi
    show ether base at zoom_center
    e "They sound the same, they look almost the same... How do you tell the difference?"
    hide ether
    show chenglaoshi base at cls_center
    ch "They are very similar, aren't they?"
    ch "Tell me, Ether. What differences do you notice?"
    hide chenglaoshi
    show ether base at zoom_center
    e "One character has some extra marks on the header...."
    hide ether
    show chenglaoshi base at cls_center
    ch "Yes! Don't those extra marks look a little like the character for ten?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Yes..."
    hide ether
    show chenglaoshi base at cls_center
    ch "The one with the ten, mài, means to sell! You can think of it as an angry little peddler trying to make sales!"
    ch "If you look hard enough, the ten almost looks like a little man showing off the entire character as if he's trying to sell it!"
    hide chenglaoshi
    show ether base at zoom_center
    e "Cheng Lao Shi- the ten is a cross-"
    hide ether
    show chenglaoshi base at cls_center
    ch "Yes! Those are his little arms! And because he's being so showy, you can remember that he's trying to aggressively rake in sales, so it's said in the fourth tone: mài!"
    hide chenglaoshi
    show ether happy at zoom_center
    e "Okay, I can't unsee the little man now...."
    hide ether
    show chenglaoshi base at cls_center
    ch "Good! That is how you will remember!"
    ch "The other character, mǎi, means to buy. You can think of the word with its third tone as deliberation as you try to figure out if the fries from the store across the street are worth buying."
    hide chenglaoshi
    show ether base at zoom_center
    e "Oh?"
    hide ether
    show chenglaoshi base at cls_center
    ch "The third tone goes down, then back up! So maybe, it's like someone going 'hmmm, I want chips.. no, wait, the Oreos are cheaper!' After all, you should always be financially responsible and chase discounts like your life depends on it!"
    hide chenglaoshi
    show ether happy at zoom_center
    e "{alpha=0.5}{i}laughing{/i}{/alpha}"
    e "Okay, okay."
    hide ether
    show chenglaoshi base at cls_center
    ch "Does that make sense?"
    hide chenglaoshi
    show ether happy at zoom_center
    e "Yup. Aggressive little man trying to sell things versus little man trying to save money."
    hide ether
    show chenglaoshi base at cls_center
    ch "Precisely! Is there anything else you need help with?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Uhh...."
    e "Not for this class, at least...."
    hide ether
    show chenglaoshi base at cls_center
    ch "Aww."
    ch "If you ever want to talk about it, Cheng Lao Shi is always willing to pow pow someone for you. What about your other classes?"
    menu:
        "Tell Cheng Lao Shi about Government":
            jump tell_ch_abt_gov
        "Don't tell Cheng Lao Shi about Government":
            jump dont_tell_ch_abt_gov
    return 

label tell_ch_abt_gov:
    scene bg chineseclassroom
    show ether base at zoom_center
    e "{i}Do I want to tell Cheng Lao Shi about my other classes?{/i}"
    hide ether 
    show ether happy at zoom_center
    e "{i}Cheng Lao Shi has been pretty supportive of me so far, maybe he'd understand...{/i}"
    hide ether
    show ether annoyed at zoom_center
    e "Yes.. see.. for Mandarin, I can come in during lunch... it's Government that's making me lose my mind. And my Calculus grade is about to drop another letter if I don't pass the next test..."
    hide ether
    show chenglaoshi base at cls_center
    ch "Hmmm... is the class hard?"
    hide chenglaoshi
    show ether base at zoom_center
    e "Yeah.. a little bit....."
    hide ether 
    show ether annoyed at zoom_center
    e "It's hard to focus because Mr. Duras is always moving his hands around while explaining the notes. I can't read the notes {i}and{/i} listen to him at the same time, and I'm starting to think it's because I'm stupid or something, because most of the class is able to keep up just fine!"
    hide ether
    show chenglaoshi base at cls_center
    ch "Hmmm... have you talked to Mr. Duras about it? Or asked him for help?"
    hide chenglaoshi
    show ether annoyed at zoom_center
    e "I have....."
    hide ether 
    show ether coveringface at zoom_center
    e "He just tells me he doesn't think I'm trying."
    hide ether 
    show ether annoyed at zoom_center
    e "And I {i}am{/i} trying- I look up what he explained online when I get home and I understand it much better than in his classroom!"
    hide ether
    show chenglaoshi serious at cls_center_s
    ch "Tsk. Duras, that idiot."
    hide chenglaoshi
    show chenglaoshi base at cls_center
    ch "You are a clever child, Ether. I think that hairy man's classroom is against you."
    hide chenglaoshi
    show ether base at zoom_center
    e "His classroom or my brain?"
    hide ether
    show chenglaoshi base at cls_center
    ch "Aiya.... You are not the first to complain to me about Duras' class... "
    ch "The man is just... insensitive...."
    ch "After teaching for so long, you would think he's better at his job!"
    hide chenglaoshi
    show ether base at zoom_center
    e "Oh....."
    e "What do you think I should do?"
    hide ether
    show chenglaoshi base at cls_center
    ch "If Duras continues to be a stubborn mule, I think you should self-study or ask one of your peers for help."
    ch "Terrible, terrible man....."
    ch "It is not your fault his teach style does not work for you."
    ch "You can always come in during lunch to ask me for help."
    ch "Cheng Lao Shi can explain the government far better than the stinky, hairy man..."
    hide chenglaoshi
    show ether happy at zoom_center
    e "{alpha=0.5}{i}laughs{/i}{/alpha}"
    e "Cheng Lao Shi, I don't think you should be saying that about him-"
    hide ether
    show chenglaoshi base at cls_center
    ch "Ay, don't tell Cheng Lao Shi what he can and can not do."
    ch "If Duras thinks you're not trying, tell me again and Cheng Lao Shi will drop Duras a line about his terrible teaching---"
    ch "Ah, there's the bell. I will have to prepare for class now."
    hide chenglaoshi
    show ether happy at zoom_center
    e "Okay, I'll go to class now. Thank you, Cheng Lao Shi!"
    hide ether
    show chenglaoshi base at cls_center
    ch "Yes, yes, I will see you tomorrow!"
    jump stops_phone_addiction_from_going_too_far
    return

label dont_tell_ch_abt_gov:
    scene bg chineseclassroom
    s "Is Ether going back to Mandarin class for more help?"
    menu:
        "Yes":
            jump stops_phone_addiction_from_going_too_far
        "No":
            jump next_day_no_help
    return

label stops_phone_addiction_from_going_too_far:
    # (walking home)
    scene bg blackscreen
    s "A few weeks later.."
    scene bg street
    show rajah base at zoom_center_r
    r "Oi! Ether!"
    hide rajah
    show ether base at zoom_center
    e "Hi Rajah!"
    hide ether
    show rajah nervous at zoom_center_r
    r "I've barely seen you at lunch the last couple days- where the hell have ya been?"
    hide rajah
    show ether base at zoom_center
    e "I've been in Cheng Lao Shi's classroom asking for help on Government..."
    hide ether
    show rajah nervous at zoom_center_r
    r "You asked Cheng Lao Shi for {i}Government{/i} help?"
    hide rajah
    show ether happy at zoom_center
    e "Hey! In my defense, Cheng Lao Shi is way better at explaining things than Mr. Duras."
    hide ether 
    show ether annoyed at zoom_center
    e "Duras keeps waving his arms and talking and telling us to write down the notes on the slides."
    hide ether 
    show ether happy at zoom_center
    e "Cheng Lao Shi just talks about it and brings up pictures when necessary."
    e "I actually memorized the first ten Amendments with his help!"
    hide ether
    show rajah base at zoom_center_r
    r "That's great!"
    hide rajah
    show rajah annoyed at zoom_center_r
    r "Meanwhile, I got kicked out of Ms. Fong's room for being on my phone...."
    hide rajah
    show ether base at zoom_center
    e "You were on your phone? In Ms. Fong's class?!"
    hide ether
    show rajah blushing at zoom_center_r
    r "Let's just say I really wanted to finish SladeSlice's shorts series..."
    hide rajah
    show rajah base at zoom_center_r
    r "Anyway, she sent me out of the room and told me to go to the counselor's office! You know Ms. Antimony, the counselor?"
    hide rajah
    show ether base at zoom_center
    e "Yes?"
    hide ether
    show rajah base at zoom_center_r
    r "She asked me why I was constantly on my phone 'cause I guess Ms. Fong told her-"
    r "Anyway, I was like... I can't focus and I thought she'd be like Duras and y'know, say I'm not trying...."
    hide rajah
    show rajah blushing at zoom_center_r
    r "Then she asked {i}why{/i} I couldn't focus and I started complaining about Duras and I {i}really{/i} thought she'd like, slap me or something but she didn't, surprisingly."
    r "She just told me I was likely neurodivergent or something like that, whatever that means."
    hide rajah
    show ether base at zoom_center
    e "Neurodivergent?"
    hide ether
    show rajah base at zoom_center_r
    r "Yeah."
    r "Apparently it means I process information differently or something like that- she was trying to explain to me why I had so much trouble focusing on Duras' nonstop yap."
    hide rajah
    show ether base at zoom_center
    e "That makes sense, actually. I can usually focus in my other classes, too. It's really just Duras' class I struggle with."
    hide ether
    show rajah base at zoom_center_r
    r "Right, right."
    r "You know what she made me do after that?"
    r "She suggested I journal to get the frustration with Duras out of my system. She yapped a crazy amount about how being on my phone was going to lead to negative mental health and less sleep... she actually wasn't wrong about the sleep part. I slept like, maybe 4 hours yesterday."
    hide rajah
    show ether base at zoom_center
    e "So did you journal?"
    hide ether
    show rajah blushing at zoom_center_r
    r "I mean. She kinda sorta made me try it. It was helpful, I guess, but I only wrote down two sentences before I got bored and antsy."
    r "She basically just told me to write down how I feel and stuff like that."
    hide rajah
    show rajah annoyed at zoom_center_r
    r "I didn't like it, but maybe it'll work better for you since you're more patient than I am."
    hide rajah
    show ether base at zoom_center
    e "Hmmmm.. I'll try it and let you know how it goes."
    e "Did Ms. Antimony suggest anything else for you to try?"
    hide ether
    show rajah base at zoom_center_r
    r "She had me try some fidget toys too. If you ask me, those worked way better than journaling."
    hide rajah
    show ether base at zoom_center
    e "Hmmmm.. okay, I'll try them when I get home."
    hide ether
    show rajah base at zoom_center_r
    r "A'ight. This is my stop. See ya tomorrow, Ether."
    hide rajah
    show ether base at zoom_center
    e "See you, Rajah!"
    jump neutral_ending
    return

label neutral_ending:
    scene bg bedroom
    show ether base at zoom_center
    ej "11/02/2XXX"
    ej "Dear Journal,"
    ej "Hi! This is Ether. Rajah told me about journaling today, so I thought I'd try it. Before I even got out this journal though, I decided to look up the word 'neurodivergent' because I didn't completely understand what it meant. While Rajah was right that it referred to people's brains developing differently, neurodivergence also refers to a lot of different conditions that lead to the difference in development."
    ej "There were a lot of sources I found, but one of the pages I found most reliable was from a health clinic. And one term the health clinic's page mentioned is 'sensory overload', which means that when someone is given more information than their senses can process, they get 'overstimulated' and can't intake anything at all. That really resonated with me because that really describes how I feel in Mr. Duras' class a lot."
    ej "Then I started wondering why I only got overstimulated in Duras' class and not anyone else's, like Cheng Lao Shi's. I think I can say that it's because Cheng Lao Shi only does one thing at a time, while Mr. Duras does too much at once. I don't know how I'd ever tell Mr. Duras that, though."
    ej "I started Googling how to manage overstimulation, and one of the things I saw crop up a lot was to leave the stimulating environment. I'll have to ask Mr. Duras if I can leave midway during his lectures to calm myself."
    ej "I think I'll ask Ms. Antimony what I should do about my sensory overloads in Mr. Duras' class and see what he thinks. I do feel a lot better, now that I know what I'm going through isn't uncommon. It's good to know that I'm not stupid. I just process things differently, and I'll have Mr. Duras know somehow."
    ej "Thank you for listening, Journal!"
    ej "Signing off,\nEther"
    s "Neutral Ending Reached!"
    return
# END OF NEUTRAL ENDING