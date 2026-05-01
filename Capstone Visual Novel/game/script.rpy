# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Ether", color="#b6aeeb")
define md = Character("Mr. Duras", color="#8f671e")
define r = Character("Rajah", color="#ed6328")
define b = Character("Blaire", color="#eba2e1")
define v = Character("Video", color="#7a7976")
define s = Character("-", color="#7a7976")
define n = Character("Random Students", color="#7a7976")
define em = Character("Ether's Mom")
define ed = Character("Ether's Dad")
define ch = Character("Cheng lao Shi", color="#69300d")
define an = Character("Antimony", color="#801d26")
define ej = Character("Ether - Journaling", color="#b6aeeb")

transform zoom_center: 
    zoom 0.35 #adjust as required
    center
    ypos 1500

transform zoom_center2: 
    zoom 0.35 #adjust as required
    center

    
# transform cls_right: 
#     zoom 0.35 #adjust as required
#     # right

# transform h_left:
#     zoom 0.2
#     # left

label start:
    # DAY 1
    scene bg bedroom
    # ----------------------------- begin
    show ether test at zoom_center
    e "{alpha=0.5}{i}wakes up{/i}{/alpha}"
    e "Time for class already? Ugh..."
    e "{alpha=0.5}{i}gets ready for school and goes to class{/i}{/alpha}"
    e "I have Government first. Hopefully, it'll be easy..."
    e "{alpha=0.5}{i}barely gets to class on time{/i}{/alpha}"

    scene bg govclassroom
    # ------------------------------------- start class
    show duras test at zoom_center2
    md "Good morning, class! Thank you all for making it on time."
    hide duras
    show ether test at zoom_center
    e "{i}Mr. Duras is dressed up today! That means we're going to do something fun today! I wanna see what he has planned..!{/i}"
    hide ether
    show duras test at zoom_center2
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
    scene bg govclassroom
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
    scene bg govclassroom
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
    scene bg govclassroom
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
    scene bg govclassroom
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
    scene bg govclassroom
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
    scene bg schoolhallway
    e "{i}Finally, I get to go home.....{/i}"
    e "{i}No homework today! Wait, no... I have that government worksheet to do, dang it!{/i}"
    e "{i}Mr. Duras said it wasn't supposed to take too long, though, so maybe it'll be easy.{/i}"
    e "{i}But he also said that it was almost exactly like the worksheet, and I didn't finish that..{/i}"
    e "{i}Ack. I'd better get home to finish it, then.{/i}"
    # ------------- (reaches home)
    scene bg househallway
    e "{i}Home sweet home..{/i}"
    e "{i}I'd better get started on that worksheet.{/i}"
    e "{alpha=0.5}{i}goes up to his room{/i}{/alpha}"
    scene bg bedroom
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
    e "96 percent (A) in Calculus, 94 percent (A) in Mandarin... 90.2 percent (A-) in Government? How did my grade drop 5 percent in a day? It used to be almost 96 percent..."
    e "Oh, Mr. Duras gave me a C on the classwork... 70/100... I didn't know it was weighted that heavily! Dang it.... What am I supposed to do?"
    e "What if my parents find out about this?!"
    e "They're going to be so mad...."
    e "I didn't spend all year keeping it at an A just for it to drop right before the marking period ends!"
    e "I'll have to ask Mr. Duras if I can make up the credit. And I can't mess up any more assignments, or it'll drop to a B...."
    e "I'll just try finishing the homework in the meantime...."
    jump start_day2
    return

label start_day2:
    scene bg schoolhallway
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
    scene bg schoolhallway
    e "{i}I can ask Rajah what he got on the homework during class. I'd best ask Mr. Duras now, since he might busy later.{/i}"
    e "{alpha=0.5}{i}enters the room{/i}{/alpha}"
    scene bg govclassroom
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
    jump day2_start_class
    return

label ask_rajah_if_finished:
    scene bg schoolhallway
    e "Hi Rajah-"
    r "{alpha=0.5}{i}looking up{/i}{/alpha}"
    r "Yo."
    e "Did you finish the homework from yesterday?"
    r "{alpha=0.5}{i}thinking for a moment{/i}{/alpha}"
    r "You mean the worksheet?"
    e "Yeah."
    r "No, I didn't. I didn't even finish the classwork either. Mr. Duras was going wayyy too fast."
    e "I know, right? And he was moving around so much that I kept getting distracted."
    r "That man was talking at the speed of light."
    b "Really?"
    r "Not-"
    r "{alpha=0.5}{i}sighs{/i}{/alpha}"
    r "Hello, Blaire."
    b "I thought Mr. Duras was talking just fine. It wasn't that hard to understand."
    r "Uh huh."
    b "Mr. Duras gave us detailed explanations for everything, and practically gave us all the answers on the worksheet. I even finished it with 15 minutes left to spare. Maybe you guys weren't trying hard enough."
    md "Alright, class, come on in. The bell will ring soon, so let's get started for today."
    jump day2_start_class
    return

label day2_start_class:
    scene bg govclassroom
    e "{alpha=0.5}{i}sits down in his seat{/i}{/alpha}"
    md "Alright, class, we're going to skip the warm-up for today and continue where we left off-"
    md "Yes, Rajah?"
    r "Mr. Duras, could you try going a little slower this time?"
    md "{alpha=0.5}{i}hesitating{/i}{/alpha}"
    md "Well, Rajah, we have a lot to get through, but you can let me know if you need extra time to get the notes down."
    md  "So, last we left off on how the 3 branches of government were established. Today, we're going to get into the important cases concerning the 3 branches."
    md "But first! Let's go over the answers to yesterday's classwork."
    e "{i}Okay, so this was all the stuff I didn't know yesterday. I need to write this down.{/i}"
    md "Who can tell me what the Legislative Branch does?"
    md "Yes, Blaire."
    b "The Legislative branch creates laws."
    e "{alpha=0.5}{i}furiously scribbling{/i}{/alpha}"
    e "{i}Legislative Branch. Creates laws. Got it.{/i}"
    md 'Excellent! The word "Legislative" means to "do with the law". Alright, now who can tell me how many departments the Executive Branch controls?'
    md "That's correct, Danny! But please raise your hand next time."
    e "{i}I couldn't even hear what Danny said...{/i}"
    md "For those who couldn't hear Danny, the Executive Branch controls 15 departments. You'll be required to name some of these departments on the upcoming quiz. Who can name an Executive Department? Shout it out!"
    e "{i}There's a quiz on this?!{/i}"
    e "{i}There's so many people shouting that I can't even hear any single one of the departments...{/i}"
    md "I see you all will do just excellent on the quiz!"
    e "{i}No, I won't....{/i}"
    md "Now, how about an example of how the Judicial Branch's judgment influenced an Executive Order?"
    e '{i}What does he mean when he says "influenced"? How did it affect the Executive Order?{/i}'
    md "Yes, Blaire, that {i}is{/i} an example... There was a time when the Judicial Branch declared the president's tariffs unconstitutional! What did the president do afterward?"
    r "{alpha=0.5}{i}whispering{/i}{/alpha}"
    r "Ether, do you get the unconstitutional part?"
    e "No...... Maybe you should ask him?"
    r "{alpha=0.5}{i}raises hand{/i}{/alpha}"
    md "Yes, Rajah?"
    r "Why is it important that the president's actions were declared unconstitutional?"
    md 'Well, declaring something "unconstitutional" means that it goes against the Constitution!'
    r "......"
    md "Is that clear?"
    r "..Why is it important that something is against the Constitution?"
    md "Ah! We covered this last class. Our government principles run by the Constitution, and if something is declared against the Constitution, it goes against everything the government stands for."
    r "Oh, yeah, that makes... sense...."
    r "{alpha=0.5}{i}to Ether{/i}{/alpha}"
    r "I felt so stupid asking that, and I'm still not sure I understand it..."
    md "Great! Now, back to what Blaire was saying. In the case against the tariffs, did the president take any action?"
    md "Right, Roger, they didn't. This case wouldn't necessarily have been directly affected by the Judicial Branch's judgement, but I would've accepted that as an answer if you clarified that the Executive Order hadn't changed after the Judicial Branch's judgment."
    md "Do you have another question, Rajah?"
    r "Wait, so if the Judicial Branch couldn't do anything, then what about the Executive Order changed?"
    md "Nothing!"
    r "Huh??"
    md "All the Judicial Branch does is pass judgement. The branches that enforce that judgement are the Legislative and Executive."
    r "So... wouldn't the other branches just be able to ignore the Judicial Branch?"
    md "In essence, yes."
    r ".. If it can be ignored...."
    r "... then why does it exist?"
    s "{alpha=0.5}{i}the class laughs{/i}{/alpha}"
    r "{alpha=0.5}{i}embarrassed{/i}{/alpha}"
    r "Never asking again."
    md "And that's why our lesson today will be about the cases that demonstrate just how important the Judicial Branch is. So, without any further ado, let's jump into our first case!"
    md "The first one we'll be talking about is Shaw v. Rucker. The case goes like this: When Zebulon was first split into its colonies, the population of the colony decided how many votes they would get out of the entire planet..."
    e "{alpha=0.5}{i}whispering{/i}{/alpha}"
    e "Mr. Duras keeps accidentally blocking the screen with his hands..."
    r "Hey, you could tell him to stop. I don't wanna look stupid again."
    e "You didn't look that dumb... Doesn't Mr. Duras' constant walking around bother you?"
    r "No one else has a problem with it, so I guess it's just us."
    e "Did you get the rest of the notes down?"
    r "Like, a bit, I'd say? Not all of it. Here, you can take a look."
    md ".... Shaw v. Rucker abolished the use of gerrymandering by species! Ether, are you paying attention?"
    e "Uh, yes, sir."
    md "Good, good. Could you explain to me, in your words, why Shaw v. Rucker matters?"
    e "It.... didn't let us group certain districts?"
    md "Close. It didn't let us group certain districts to skew the vote. Now, next, we'll go onto the case Zebulon v. Lopez.... Oh, dear, this room is getting a little cold. I'll turn on the heater before we go on."
    md "{alpha=0.5}{i}click{/i}{/alpha}"
    md "Alright, so back to Zebulon v. Lopez, where a young boy brought weapons to school..."
    e "{i}I can't listen to what he's saying AND write down the notes- it's either one or the other! And that heater is really loud...... Argh. No, I just need to focus.{/i}"
    md "... The Supreme Courts initially couldn't decide of Lopez had broken the state or federal law, so it was undecided whether he would stand trial under the nation or the state jurisdiction. Remember, jurisdiction is---"
    e "{i}I can still hear the heater grumbling in the background.. it's so distracting. I'm getting a little sweaty too. I'll take off my jacket.{/i}"
    md "The government got into a scuffle with the colony Lopez had been from. It had almost been like this-"
    md "{alpha=0.5}{i}walking to a map by the board{/i}{/alpha}"
    md "So here was the colony Lopez was from. The government met state officials here, here, and here to-"
    e "{i}What am I supposed to be looking at? He's pointing at the map too quickly- You know what, maybe I'll just focus on the notes instead.{/i}"
    e "{i}But I can't even focus on what I'm writing down because Mr. Duras keeps talking and tapping the map so loudly... and this room keeps getting warmer....{/i}"
    md ".. And that'll wrap up the lecture for today."
    e "{i}Finally. We're done.{/i}"
    jump worksheet_assigned
    return

label worksheet_assigned:
    scene bg govclassroom
    md "Now, it's time for you to apply what you learned in this worksheet I'm about to pass out! It'll help you prepare for the quiz next week."
    e "{i}THE QUIZ IS NEXT WEEK?! Didn't we just start learning this stuff?{/i}"
    md "You should be able to finish the worksheet before the end of class. It is just as long as the last one."
    #insert existential dread here
    e "{alpha=0.5}{i}reading the questions...{/i}{/alpha}"
    e "{i}I really can't do this alone…. I'll need help.......{/i}"
    menu:
        "Ask Blaire again":
            jump ask_blaire_again
        "Ask Mr. Duras again":
            jump ask_duras_again
    return

label ask_blaire_again:
    scene bg govclassroom
    e "Blaire..?"
    b "{alpha=0.5}{i}distantly talking with other people{/i}{/alpha}"
    e "{i}She looks busy… maybe I shouldn't bother her...{/i}"
    e "{i}But how am I going to prepare for the test if I don't ask for help{/i}"
    e "{i}No, I can do this....{/i}"
    e "Blaire!"
    b "And then I-"
    b "{alpha=0.5}{i}turns{/i}{/alpha}"
    b "Oh, hi again, Ether."
    e "{i}I really don't want to take up her time... I already feel bad for asking....{/i}"
    e "Can I borrow your notes?"
    b "{alpha=0.5}{i}handing over the notebook{/i}{/alpha}"
    b "Don't tell me you didn't understand today's class either?"
    b "Ugh, fine, here you go. Knock yourself out."
    e "{i}Her notes are.... A little messy. But she did write down a lot more than I did, so this should be helpful.{/i}"
    e "{i}The first question asks about the case Shaw v. Rucker... I know it was something about gerrymandering, but what was the difference between that and redistricting? They both redraw the district lines...{/i}"
    e "{i}All she wrote was that it ruled against racial gerrymandering. I'll just write that down, then.{/i}"
    e "{i}The next question is about the independent regulatory commissions and executive regulatory commissions... her notes have a lot less words than the slides...{/i}"
    b "You're not still struggling, are you?"
    e "Uh... well..."
    b "Here, just copy mine. It'll make sense afterward."
    e "Oh, okay... thanks..."
    e "{i}I guess I'll at least get a good grade on this worksheet, so my grade won't drop any lower yet, but will it matter if I fail the quiz?{/i}"
    e "{i}Blaire said it would make sense once I read through it properly. I'll copy down her notes too, since she lent me her notebook already.{/i}"
    e "{alpha=0.5}{i}visible frustration{/i}{/alpha}"
    e "{i}There are too many people talking, and I can't even comprehend what I'm reading.... it's too loud...{/i}"
    e "{i}How did Blaire manage to get this done when the room's so loud?{/i}"
    e "{i}Is it just me? Is there something wrong with me that makes it so hard to do anything in this class?{/i}"
    b "Ether-"
    e "{i}I wish I was.. I don't know, smart enough to know how to handle this stuff?{/i}"
    e "Ether!"
    e "Yes? Sorry, I was trying to understand your notes."
    b "It's time to turn in the worksheet. Did you finish yours?"
    e "Yes, thank you."
    e "{i}But I was only able to finish it with help....{/i}"
    e "{i}What does that say about me as a student? Am I just slow?{/i}"
    jump worksheet_turned_in
    return

label ask_duras_again:
    scene bg govclassroom
    e "Mr. Duras, could I get some help on the worksheet?"
    md ".....Ether, how long have you spent on the worksheet?"
    e "I read the questions, and tried to reread my notes, but I didn't fully understand what happened for the Shaw v. Rucker case in the first question."
    md "Why don't you bring your notebook over and tell me what you wrote down for that case?"
    e "I wrote down that it ruled against gerrymandering, but I didn't get enough down to understand why that was the case."
    md "Were you really paying attention during class?"
    e "Yes. But there was just a lot going on, and I couldn't hear what you were trying to say while you were explaining the slides, and it was really hard for me to focus."
    md "Are you sure? I see you talking to Rajah quite often while I am lecturing."
    e "It's because I was trying to get the notes from him-"
    md "I am beginning to believe that perhaps you were not trying at all. If you are having side conversations in class, it is only natural that you would lose focus. You can not expect me to help you when you are not making a concerted effort to do well in class."
    e "But I-"
    md "Now, if you'll excuse me, Ether, I see Roger has his hand raised. I will come back to you once you have shown me that you are trying in this class."
    e "But.. I am.."
    md "{alpha=0.5}{i}walking away{/i}{/alpha}"
    e "... trying...."
    e "{alpha=0.5}{i}walking back to seat{/i}{/alpha}"
    e "{i}I didn't understand the notes either, and I hadn't been talking to Rajah at all during that class....{/i}"
    e "{i}Am I wrong for asking for help?{/i}"
    e "{i}I guess it's my own fault I'm falling behind, huh?{/i}"
    r "Ether! Ether!"
    e "Yeah?"
    r "Danny gave me all the answers to the worksheet. Here, copy them down while you still have time-"
    e "Oh, thanks. Do you understand the answers, though?"
    r "No. but I'd rather get a good grade on the worksheet right now and figure it out later. It's not like I'd understand it even if I asked Danny to explain every single one of them. Even Roger understood what Duras was trying to explain. I just gave up."
    e "I don't know if that's.."
    r "Just copy it down for now, ask questions later. You've got 10 minutes left to finish it."
    e "{alpha=0.5}{i}while copying{/i}{/alpha}"
    e "{i}I don't like how little of this I understand....{/i}"
    e "{i}How has everyone else been able to understand it so far?{/i}"
    e "{i}At least I'm not the only one....{/i}"
    r "{alpha=0.5}{i}grumbling to himself{/i}{/alpha}"
    r "How was I supposed to explain how the judicial branch was important when it's been ignored so many times???"
    r "{alpha=0.5}{i}checking time{/i}{/alpha}"
    r "Ether! There's like 5 more minutes left of class. You done yet?"
    e "Almost-"
    jump worksheet_turned_in
    return

label worksheet_turned_in:
    scene bg govclassroom
    md "Okay class, our time for today has come to a close. Please turn in the worksheet and study for the quiz next class!"
    r "Mr. Duras!"
    md "Yes, Rajah?"
    r "Uh, is the quiz multiple choice?"
    md "Yes, there will multiple of those questions, but they will not make up a majority of the quiz since I would like to test your understanding of the content rather than your guessing abilities. Most of the test will be short-answer questions. It will also be closed-note."
    r "How many questiions are there?"
    md "Ah, I'll have to check.... it should take you no longer than 45 minutes to finish, though."
    r "Good to know."
    r "{alpha=0.5}{i}muttering to Ether{/i}{/alpha}"
    r "I am so flunking this quiz....."
    e "{alpha=0.5}{i}timidly raising hand{/i}{/alpha}"
    md "......."
    md "Yes, Ether?"
    e "Will there be retakes or corrections on this quiz?"
    md "..."
    md "No, there will not."
    md "Are there any other questions?"
    e "{i}He looks annoyed with me....{/i}"
    e "{i}But I genuinely didn't understand any of the content, and I'll need help anyway...{/i}"
    md "If there are no other questions, you are all dismissed. Please turn in the homework from yesterday and the worksheet from today in the box by the door. Have a good day, everyone, and remember to study!"
    e "{i}Okay... now, do I want to ask Mr. Duras for help?{/i}"
    menu:
        "Ask Mr. Duras for quiz help":
            jump ask_md_for_quiz_help
        "Give up on Mr. Duras entirely":
            jump give_up_on_md
    return

label ask_md_for_quiz_help:
    scene bg govclassroom
    e "{i}I'm afraid to ask Mr. Duras for help... but I really don't want to get a bad grade on this quiz.{/i}"
    e "{i}Asking him for help can't be too bad. There's nothing for me to lose.{/i}"
    e "{alpha=0.5}{i}approaching the desk{/i}{/alpha}"
    e "Mr. Duras?"
    md "Hello, Ether. How may I help you?"
    e "I want help understanding the content that will be on the quiz."
    md "Alright."
    md "..."
    md "What is confusing to you?"
    e "The functions of the three branches are hard for me to understand, and even more to remember. I was wondering if you could post a study guide or practice questions like the ones on the quiz? Maybe even the slides you used?"
    md "Even if I were to post such resources for you, how could I be sure that you would use them?"
    e ".... What do you mean?"
    md "I have seen you consistently have side conversations during lecture. When you're given work time, you do not seem to use it wisely. From what I see, you only sit there. I also believe I saw you copying off one of your peers' papers."
    e "I-"
    md "You may not cheat on the quiz, Ether. Whatever good you believe copying will do, get it out of your head. Copying is a student's way of benefitting from other people's work when you don't want to use the energy to do it yourself."
    e "Mr. Duras, I understand that copying is wrong, but I didn't understand the content and I was afraid to get a bad grade on the worksheet and-"
    md "Grades should not be worth sacrificing academic integrity for."
    e "Yes. I know. I understand."
    e "{i}He thinks I'm not trying at all.{/i}"
    e "Can you at least.... post the slides? So I can... catch up on the notes?"
    md "........"
    md "Fine, Ether. But I will remind you that I have no tolerance for cheating, and if I catch you doing so on the quiz, you will get a zero without any chance of redoing it."
    e "Yes... I know. I don't intend to."
    md "I would hope not."
    md "Run along now, I'd like to eat my lunch. The slides are available on google classroom."
    e "The quiz is on everything we've covered so far, right?"
    md "Yes. Have a good rest of your day, Ether."
    e "You too."
    e "{alpha=0.5}{i}turning to leave{/i}{/alpha}"
    e "{i}No wonder Rajah doesn't want to ask Mr. Duras for help anymore. Mr. Duras just makes me feel small and insignificant.{/i}"
    jump goes_home_to_study
    return

label give_up_on_md:
    scene bg govclassroom
    e "{i}No, I don't want to bother him even more....{/i}"
    jump goes_home_to_study
    return

label goes_home_to_study:
    scene bg street
    e "{i}I have to go home to study for this quiz....{/i}"
    e "{i}Where do I even start?{/i}"
    e "{i}I am definitely not asking Mr. Duras for any sort of help from now on...{/i}"
    r "Ether!"
    r "Hey, you look a little depressed. What're you thinking about?"
    e "Just worried about the quiz in Government... "
    r "It's JUST a quiz. It'll probably be fine."
    e "I mean, yeah, but if we fail, our grades are going to drop a decent amount.... Plus, I barely understood what Mr. Duras was saying, and he makes me feel stupid for even trying to ask."
    r "I feel you, bro. But..."
    e "How do you plan to study for the test?"
    r "..."
    r ".. Guess...?"
    e "You can't be serious."
    r "I {i}thought{/i} about asking Blaire or Danny for help, but........ then I got a little self-conscious and I thought eh, my grade could probably tank it anyway!"
    e "Is that a good line of thinking for long-term?"
    r "Probably not, but sometimes you gotta live in the present instead of stressing over the future, y'know?"
    e "I'm pretty sure that's not what the quote was for-"
    r "Look, Ether, it's a problem for next class. So I'll start worrying about it- {i}next class{/i}."
    e "{i}I wish I had that kind of luxury..... To be brave enough to put off academic work. Hah.{/i}"

    # -------- Ether arrives home
    scene bg bedroom
    e "{i}To get a good grade on the test, I should start studying as soon as I finish everything else.{/i}"
    e "{i}Maybe if I spend more time studying, I'll absorb more of the content!{/i}"
    e "{i}Let's see if Mr. Duras posted anything to help me study on the quiz...{/i}"
    e "Here we go.."
    e '"Hello, class! As I told you in class today, there will be a quiz the next time I see you. Please study the following topics in order to succeed:"'
    e "Functions of 3 branches.... Articles of Colonies... Zebulon's important court cases, including Shaw v. Rucker.... so everything he's ever mentioned the last two days."
    e "I genuinely didn't get enough of the notes down, though... maybe there's some resource online I could find that can help me understand what he was trying to teach."
    e "Maybe I'll try looking it up on YouTube again...."
    e "Here's one. I hope it's better than the one I found yesterday..."
    e "The Legislative Branch creates laws. Yes, that is one of the few things I actually remember."
    e "The Executive Branch... carries out the law. They just enforce whatever laws are created using the Departments... ohhh..... that's not even that hard to understand! How come I didn't get it during class?"
    e "The Judicial Branch sets precedents with their decisions that influence future cases... also can rule anything unconstitutional for the Executive to strike down. Yeah, this really isn't hard to understand when the person in this video is the one explaining it."
    e "Maybe it's because he's not moving around as much as Mr. Duras is... and it's much quieter in my room than in the classroom...."
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
    scene bg schoolhallway
    e "{i}Today's the day of the quiz and I am so going to fail but no no I will not fail I can not afford to fail-{/i}"
    e "{i}I've looked up so much of the notes... I should be fine, right?{/i}"
    e "{alpha=0.5}{i}walking down the hallway{/i}{/alpha}"
    e "{i}Oh, there's Blaire. She doesn't seem worried at all. But why would she, when she's been talking about how easy the work's been?{/i}"
    e "{i}Rajah's early too. He's just scrolling on his phone.. I wish I could be confident enough to do that.. but I've spent the last night worrying so much about the quiz that I feel like I barely slept at all...{/i}"
    e "{i}I'm just going to review the notes I found on the topics while I wait... the more time spent cramming, the better, right?{/i}"
    jump quiz_starts
    return

label quiz_starts:
    scene bg govclassroom
    md "Alright, class. Come on in."
    e "{i}It's starting it's starting it's starting I am sooooo doomed-{/i}"
    md "I hope you all studied for the quiz today! But before we get to that event of the day, we'll have a short warm-up to help you prepare for it."
    md "I'll just review a couple of concepts, and you all can shout out the answers."
    e "{i}No- I can never focus when there's that many people talking-{/i}"
    md "So for our first question... Can anyone explain to me why the Articles of Colonies didn't work?"
    n "--Because it didn't coin money-"
    n "--Couldn't regulate trade---"
    n "--No enforcement--"
    n "--fhdskjfgdshfbdkjvidshiusdfjsdfbnkjsdf-"
    n "--dsfhdskjfbdsfbs,mfrbewfiuisfndjsfnsdfnjksdf--"
    n  "--fnjdskbfsdkfbksdbfkjsdbfkjsdfhhsdfdmfbdsfbkj--"
    n "--hsdkjfdhsvfvdooosd--"
    e "{i}It's too loud----{/i}"
    md "Excellent, class!"
    e "{i}Great, it's over-{/i}"
    md "Now for the next question-"
    e "{i}NO-{/i}"
    md "Who can name the court case that outlawed species based gerymandering?"
    n "--hffuysuidhfkefbbebnd--"
    n "--fhdskjfkkfbbfdnsfbdnhxbe--"
    n "--dafwawfcdahjvhdvwfgwggdsb--"
    e "{i}Shaw.. Shaw v. something.... I'll probably recognize it on the quiz-{/i}"
    md "Now, last question! Who can tell me why the Bill of Rights was established?"
    n "--hfbkjsdbfe,mnfojodnc,xsncdjkfnejnj--"
    md "{alpha=0.5}{i}clapping his hands together{/i}{/alpha}"
    md "Yes! Exactly! I saw those were the most missed questions on the last couple worksheets I assigned to you, and you answered them beautifully! Now, it's time for the quiz!"
    r "{alpha=0.5}{i}muttering next to Ether{/i}{/alpha}"
    r "'Answered them beautifully?' I didn't even know half of what everyone was saying because everyone was shouting over each other!"
    e "I know..... I couldn't focus much on anything anyone said-"
    md "I'm coming around to pass out the quiz now. You have until the end of class to finish it."
    md "Rajah, Ether, if you could please stop talking until I finish passing out the quiz."
    md "If I catch anyone else talking during the quiz, I will give you a zero."
    r "{alpha=0.5}{i}shuts up, looking embarrassed{/i}{/alpha}"
    e "{i}Okay. Quiz. I really didn't hear anything anyone was saying, but maybe I don't need to. I.. think I could've answered all those questions by myself-{/i}"
    md "Ether. Eyes on your own paper, please."
    e "{i}But I wasn't-{/i}"
    e "{alpha=0.5}{i}stares down at the paper{/i}{/alpha}"
    e "{i}I'll just try answering these questions.{/i}"
    e "{i}Question 1: Describe the three branches (Legislative, Executive, and Judicial) and their purposes.{/i}"
    e "{i}I remember there was a question like this on the worksheet- but what was it? I think it was just about the Legislative branch...{/i}"
    e "{i}Legislative... I remembered looking this up the other day too.. It was either creating or enforcing the law, right? And then I remember Judicial was passing judgement or something like that, because Rajah asked why it was so useless one time-{/i}"
    e "{i}Maybe I'll just come back to this. The answer might come back to me later.{/i}"
    e "{i}Next question: Oh, I don't even understand half the words in this one. Mr. Duras never mentioned 'Confederation', or the 'United Alliance' in any of these, did he?{/i}"
    e "{i}Another question to come back to-{/i}"
    e "{i}Third question: What is the point of the government?{/i}"
    e "{i}Was this a topic I missed on Mr. Duras' post? I could've sworn I didn't see it there- Am I stupid?{/i}"
    e "{i}I can probably make up an answer for that question, but I don't know if it'll be right...{/i}"
    e "{i}Let's just go through the rest of the questions-{/i}"
    e "{i}What is unethical about gerrymandering?{/i}"
    e "{i}Describe the rationale for the attempted coup against Zebulon's government in the 1880s-{/i}"
    e "{i}I'll just... come back to all the free response questions later-{/i}"
    e "{i}Oh, multiple choice! At least I actually have a shot of answering these questions correctly-{/i}"
    e "{i}I'm just going to circle the answer that looks the most accurate, and hope for the best... And then I'll go back and fill in an answer for the short answer questions...{/i}"
    e "{i}My grade is going to fall because I can't figure out how to pay proper attention in class... Mr. Duras doesn't even seem to like me anymore anyway, so he hasn't been the most helpful either....{/i}"
    e "{i}No, I can't be blaming Mr. Duras. It's my own stupid fault that I can't understand what he's saying, and there's no one in the universe I can blame for my own mistakes but myself.{/i}"
    e "{i}Why... why did I have to be like this? Why couldn't I just be like everyone else.. and be smarter?{/i}"
    s "{alpha=0.5}{i}..... later....{/i}{/alpha}"
    jump e_walks_home
    return

label e_walks_home:
    scene bg street
    s "{alpha=0.5}{i}on the way home....{/i}{/alpha}"
    r "---so Blaire and I were arguing about who was supposed to turn in the slideshow for history, but we couldn't even come to an agreement because she was being SO unreasonable- "
    r "She literally said she didn't trust anyone in the group to turn it in, but she somehow trusted me enough to do it? I thought that implied she'd do it!"
    e "That's not good..."
    r "No, it really wasn't. We were arguing about it all the way to Calculus, and Ms. Fong had to tell both of us to shut the hell up. I was so sure she was about to give us a zero on the quiz..."
    e "Good thing she didn't...."
    menu:
        "Bring up the quiz":
            jump bring_up_quiz
        "Choose to stay quiet":
            jump stay_quiet
    return       

label bring_up_quiz:
    scene bg street
    e "Speaking of quizzes, how do you think you did on the Government quiz?"
    r "It was... "
    r "....definitely something."
    e "'Definitely something'?"
    r "Terrible."
    e "... Did you study?"
    r "I tried for... 10 minutes, and then I gave up because I felt too much like an idiot to keep trying."
    r "I will never understand how Blaire understands everything in that class so easily when Duras doesn't like re-explaining himself."
    e "...."
    e "Yeah....."
    r "It's alright, I've already accepted that I'm too stupid to thrive in that class. C's get degrees, right?"
    e "Absolutely...."
    r "Was the quiz any better for you, Ether?"
    menu:
        "Ether tells them he thinks he failed.":
            jump think_e_failed
        "Choose to stay quiet":
            jump stay_quiet
    return

label stay_quiet:
    scene bg street
    e "I think it was... okay."
    r "Hey, better than me, at least. I spent all of yesterday evening watching SladeSlice because I gave up trying to study the damn thing. You should watch him sometime- he makes gaming videos, has some really funny reaction videos-"
    e "{i}I don't know if I'd be able to do that without feeling guilty about not trying harder, but sure, Rajah.{/i}"
    e "{i}I wish I could talk about it without feeling embarrassed.. because I sure can't bring it up to my parents.{/i}"
    e "{i}My parents would never understand how a teacher could be bad, because they'd just think I'm not trying.{/i}"
    e "{i}Just like Mr. Duras...{/i}"
    e "{i}And when they see my grade drop, they'll just blame me.{/i}"
    e "{i}What would I even tell them anyway? That I can't focus because Mr. Duras is moving around too much? That I can only focus on either the notes he wants us to take, or the lecture he's giving at the same time?{/i}"
    e "{i}No, that just sounds like an excuse.... I'll just have to hope they don't find out....{/i}"
    r "Aight, Ether, I'm gonna head home from here now. See ya tomorrow, alright? Good talk today?"
    e "See you tomorrow, Rajah!"
    e "{i}Good talk? I hardly said anything...{/i}"
    e "{i}It's fine. I have bigger priorities, anyway. Like the huge homework load I need to get done...{/i}"
    jump e_returns_home
    return
    
label think_e_failed:
    scene bg street
    e "I think I failed the quiz....."
    r "Mhm..."
    e "I feel like I guessed pretty much all the questions, even though I genuinely did try to look up everything Duras taught.."
    e "I was sure I'd at least be somewhat fine with all the YouTube videos I watched, but..."
    r "Mhm...."
    e "I just wish Mr. Duras didn't assume I wasn't trying. It's so annoying, to put all your effort into a class and the teacher just decides to not really help you because you didn't immediately understand everything they were saying."
    r "Yup."
    r "Relatable."
    r "{alpha=0.5}{i}checking phone{/i}{/alpha}"
    r "Dang, they already dropped a new video?"
    e "{alpha=0.5}{i}momentarily stunned{/i}{/alpha}"
    e "Who dropped a new video?"
    r "There's this YouTuber I found the other day called SladeSlice who does gaming and their videos are so funny-"
    r "you know, this one time, they trolled someone in minecraft by pretending to be a water block and that person couldn't find them for so long-"
    e "That's... great...."
    r "They play a lot of different games, too. You know that new game Little Nightmares that came out recently? They have a whole reaction series to it and they say the most outlandish things- it's hilarious."
    r "You should try watching them sometime!"
    e ".... How long have you been watching them?"
    e "{i}If I knew Rajah would get distracted this easily, I wouldn't have said anything...{/i}"
    r "Like... couple days ago? I think the day Duras told us there was a quiz, I tried to study, gave up, then started bingewatching this guy instead because watching someone die repeatedly in hardcore is way funnier than trying to understand how our government works."
    e "I see..."
    r "They've already done collabs with people like Pewdiepie and Jacksepticeye and it's great-"
    e "{i}Look at Rajah... he doesn't understand much from Government either, but he seems so accepting of it... he doesn't seem worried at all...{/i}"
    e "{i}School probably doesn't matter to him as much it does to me...{/i}"
    e "{i}I just won't bring it up next time...{/i}"
    r "You good? You look like your dog just died."
    e "No, I'm fine."
    e "{alpha=0.5}{i}smiles{/i}{/alpha}"
    e "Carry on..."
    jump e_returns_home
    return

label e_returns_home:
    scene bg househallway
    e "{alpha=0.5}{i}closing door{/i}{/alpha}"
    e "Okay, I'm home."
    e "It is... 4:15. That leaves me... with 6 hours to finish up everything, and 8 if I need to stay up until 12."
    e "But I really don't want to do homework... "
    e "And 6 hours is a lot of time..."
    e "No, Ether, do it for the grade..."
    e "{alpha=0.5}{i}walks up to his room{/i}{/alpha}"
    scene bg bedroom
    e "Where do I start....."
    e "Maybe Government? Not sure I want to think about Duras right now, though..."
    e "Let's do some math instead.. the answers shouldn't be too hard to figure out, right?"
    e "Hmmm..... the notes she gave us are confusing me..."
    e "I'll just try a problem and check the answer key."
    e "Nope, that was wrong... did I forget a step?"
    e "Yep, forgot to bring the denominator down... "
    e "That's still not it..."
    e "I'll just skip this one and come back to it later- maybe I just need to do some different ones to better understand it first...."
    e "That's not good.... that is a completely different coefficient than it's supposed to be.."
    e "The answer key has a 1/2 in front... Where did that even come from?"
    e "Is this the start of my academic downfall? Government's just the start, and my grades start falling for all my other classes too?"
    e "So I really just am incapable of paying attention in class, huh? I was so distracted by how badly I did on the Government quiz that I couldn't even focus during math class anyway...."
    e "Argh, maybe I'll just take a break. I'm probaly still too distraught by the government quiz today to focus..."
    e "Maybe I'll just watch one SladeSlice video and see what Rajah like so much about him."
    v "Alright. guys, welcome back to another video of me trying to beat Minecraf-"
    v "WHY WAS THERE A SKELETON THER-"
    e "{alpha=0.5}{i}starts laughing{/i}{/alpha}"
    e "What is that cut-off scream??"
    e "He did NOT just slip that reference in there-"
    e "That was- {alpha=0.5}{i}dies laughing{/i}{/alpha} -so stupid-"
    e "Why are you saying it like that?"
    e "Okay, nevermind, I see where Rajah's coming from. This dude IS funny."
    e "That video was only 10 ish minutes.. He has some shorts on here too-"
    v "Why there is a skeleton there- NO-"
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
    e "IT'S ALMOST 10?? I still haven't finished any homework at all-"
    e "I'm just gonna show a bit of work then copy off the answer key- the work just needs to be done, not necessarily done well."
    e "Alright, time to sleep...."
    e "Thank goodness I finished my homework in time..."
    jump next_day
    return

label next_day:
    scene bg bedroom
    e "I don't want to go to school again..."
    e "{alpha=0.5}{i}gets up{/i}{/alpha}"
    e "I slept late yesterday....."
    e "Anyway.. to Government we go..."

    # -------------------------------------- time skip
    scene bg govclassroom
    md "-- and today we're going to cover the Bill of Rights---"
    md "---- should know the first ten Amendments---"
    e "{i}I still can't understand anything he's saying because he's moving around so much... and there's so much text on that slide that it's overwhelming...{/i}"
    e "{i}Mr. Duras, why... can you just stop moving so I can actually focus...{/i}"
    # Sytle note: make the classroom and md low opacity or darker to show that ether is out of it
    md "----who can tell me which side voted for the Bill of Rights---"
    md "----Not quite---"
    e "{i}There is no hope for me in this class...{/i}"
    e "{i}Mr. Duras won't want to help me... and apparently I can't absorb anything he's saying while I'm copying down the notes...{/i}"
    e "{i}I keep phasing in and out between listening to him talk and actually copying down the notes...{/i}"
    e "{i}If only I could multi-task as well as everyone else in this class--{/i}"
    md "---I'll pass out a worksheet for you all to do while I continue the notes---"
    e "{i}I can't concentrate on reading anything on this worksheet because Duras keeps talking so much...{/i}"
    e "{i}Maybe I'll just pay attention to what he says instead?{/i}"
    md "---and that's why the answer to the first question is what it is---"
    e "{i}I didn't even... catch the answer...{/i}"
    md "--- Second one should be the case we went over that concerns the Equal Protection Clause--"
    e "{i}I'll just write that down.. and only that, because I couldn't catch anything else he said--{/i}"
    md "-----Moving on to our first ten amendmends, which are the Bill of Rights--"
    e "{i}You know what, maybe I'll just give up because I'm not going to end up finishing this anyway....{/i}"
    e "{i}I just want to disappear...{/i}"
    md "---And that's it for today! Please turn in the worksheet as you head out the door and complete the homework before you come in next class!"
    e "{i}Sure, Mr. Duras.. whatever you wish....{/i}"

    # -------------------------------------- time skip
    scene bg bedroom
    e "{alpha=0.5}{i}coming home from school{/i}{/alpha}"
    e "{i}I'm beginning to realize how much I don't like going to Government.. and Calculus...{/i}"
    e "{i}It's been a week since that quiz.. Mr. Duras graded the quiz yesterday..{/i}"
    e "{i}I have a B in Government now.. and a B+ in Stats... my other grades are beginning to drop too....{/i}"
    e "{i}This is hopeless...{/i}"
    e "{i}I'm so tired of feeling like an idiot....{/i}"
    e "{i}At least when I'm on YouTube, I don't think about how screwed I am for my classes...{/i}"
    e "{alpha=0.5}{i}checking the time{/i}{/alpha}"
    e "{i}I still got a couple hours... and I finished work last time within an hour.. I can afford to watch some more SladeSlice...{/i}"
    jump after_another_couple_days
    return

label after_another_couple_days:
    # ------------------------------------------ more time skip
    scene bg bedroom
    e "{i}Back home, finally...... I don't wanna go to school anymore...{/i}"
    e "{i}I just wanna finish watching that video from earlier- and scroll through the shorts-{/i}"
    em "ETHER!"
    e "{i}She's back early today?{/i}"
    e "{i}.. why is she back so early today? She usually doesn't come home until I'm asleep-{/i}"
    e ".. Yes, Mom?"
    em "Why are your grades so low?"
    e "{alpha=0.5}{i}blinking wearily{/i}{/alpha}"
    e "Oh.. I've just been... struggling in some classes. It's just Government-"
    em "Why are you struggling in Government {i}now{/i}? You had an A in that class just two weeks ago!"
    e ".... Mr. Duras keeps assigning work I don't understand-"
    em "Did you ask him for help?"
    e "Yes, but-"
    em "This is ridiculous, Ether. I come home late from work every day to keep you fed, and you can't even keep your grades up?"
    e "...."
    em "Why have you been slacking off? I expected better from you!"
    e "I.. I'm trying, Mom-"
    em "Then you must not be trying hard enough!"
    e "....."
    em "I didn't raise you to be this incompotent. Those grades better be back up by the time your father gets back from his business trip."
    e "... yes, Mom."
    em "Don't just 'yes, Mom' me. Do better, Ether."
    em "{alpha=0.5}{i}scoffs{/i}{/alpha}"
    e "I..."
    e "I'll try harder, Mom....."
    e "{i}It's just like Mr. Duras, all over again...{/i}"
    e "{alpha=0.5}{i}trudging up to his room{/i}{/alpha}"
    e "I guess I should start with doing the homework..."
    e "But there's so much to do...."
    e "I just have to choose one and start, right?"
    e "Maybe I'll just do the hard one first... so... Government....."
    e "I have to take out my notes for this....."
    e "Notes.. notes.. where are you...?"
    e "Here..... okay, first question asks about the first Amendment... where did I write that? Here.... I don't even understand what I wrote.. There's the cases about the Amendment, but not the amendment itself....."
    e "I bet Mr. Duras just said it aloud and I wasn't paying attention..."
    e "I'll just.. Google it or something...."
    e "That.. looks confusing.... I'll just write it down, doesn't matter..."
    e "I don't that question, or the question after that, or any of these..."
    e "I really don't want to do any homework......."
    e "I don't want to ask anyone for help... I feel stupid enough...."
    e "Let's check my grades and see how bad it is..."
    e "A C in Government, B in Stats... B in Mandarin, too? Wow, I really am losing my edge..."
    e "Maybe if I take a break, I'll be able to focus...."
    e "Just a short little break. One video. Just one, and I'll do some work."
    jump the_next_day
    return

label the_next_day:
    scene bg schoolhallway
    e "{i}Back to school again....{/i}"
    r "Ether!"
    e "Hi-"
    r "I found this really goofy clip you gotta watch it please it's so funny-"
    e "What the- where did you even find this?"
    r "Dunno, but the algorithm found it for me somehow- Look at this dumb idiot HAHA-"
    r "Ah hold on my dad's texting me, give me a sec-"
    r "{alpha=0.5}{i}checks his phone{/i}{/alpha}"
    r "{alpha=0.5}{i}snorts{/i}{/alpha}"
    r "{alpha=0.5}{i}chuckles{/i}{/alpha}"
    e "{i}......He went back to scrolling, didn't he?{/i}"
    e "{i}I might as well, too-{/i}"
    e "{i}Wait- Google classroom says this thing is due today??{/i}"
    e "{i}Oh I didn't finish any work last night because I got so distracted-{/i}"
    e "{i}Do I really wanna try doing it all now, though...?{/i}"
    e "{i}I already know I'm not going to finish it all.{/i}"
    menu:
        "Go on his phone":
            jump e_goes_on_phone
        "Try to finish the work he didn't finish the night before":
            jump e_trys_to_do_work
    return

label e_goes_on_phone:
    scene bg schoolhallway
    e "{i}Eh, it's fine... just another 15 minutes before class starts won't make a huge difference, right?{/i}"
    e "{alpha=0.5}{i}takes out phone to scroll{/i}{/alpha}"
    e "{i}Wow, that really IS funny-{/i}"
    e "{i}I can show this to Rajah later-{/i}"
    s "{alpha=0.5}{i}bell rings{/i}{/alpha}"
    md "Alright, everyone, come in! Let's start class today~"
    e "{i}I.. really don't want to be here...{/i}"
    e "{i}I can never grasp anything he's saying because he's always DOING SO MUCH...{/i}"
    e "{i}Try and focus, Ether. Just try to focus. One thing at a time-{/i}"
    md "And now, we're going to go over the Amendments from the Bill of Rights- I expect you all to know all of them by now! So the first one is-"
    e "{i}I would ask him if he could stay on that slide longer... but I don't think he'd do anything to help me anyway since he thinks I'm not trying...{/i}"
    e "{i}Honestly... screw this class, I'll just do my Mandarin homework. It's not like I'll understand anything Duras is saying regardless.{/i}"
    jump mandarin_class_continues
    return

label e_trys_to_do_work:
    scene bg schoolhallway
    e "{i}Agh, I really don't wanna to get yelled at again, so I might as well try to do what I can-{/i}"
    e "{i}I know Ms. Fong won't be collecting the work today, so I've got some more time to do calc-{/i}"
    e "{i}I have Government first, so I'll just try getting this worksheet done first-{/i}"
    e "{i}... I forgot how little of the content I understood.... I can't answer these questions without understanding what it's asking, and since I don't....{/i}"
    e "{i}Maybe I could ask someone for help?{/i}"
    menu:
        "Ask for help?":
            jump ask_for_help
        "Go on his phone":
            jump e_goes_on_phone
    return

label ask_for_help:
    scene bg schoolhallway
    e "{i}Asking for help? Really? Probably not a good idea, since Mr. Duras'll just think I cheated off someone anyway and dock me points for it.{/i}"
    e "{i}I.. don't want to be called out by Mr. Duras again...{/i}"
    e "{i}I mean... it doesn't matter what I do anyway, since Mr. Duras thinks I'm not trying...{/i}"
    e "{alpha=0.5}{i}glancing over at Rajah{/i}{/alpha}"
    r "Pfffft-"
    e "{i}He's still on his phone.... without a care in the world....{/i}"
    e "{i}Maybe I should just go on my phone too, since I'm not going to get anything done anyway...{/i}"
    jump e_goes_on_phone
    return

label mandarin_class_continues:
    scene bg schoolhallway
    e "{i}At least I can finish Mandarin homework...{/i}"
    e "{i}Is it really just Duras' class that just makes me feel super stupid?{/i}"
    e "{i}Good thing this class is finally over, good grief...{/i}"
    e "{i}To Mandarin I go...{/i}"
    scene bg chineseclassroom
    ch "Welcome, welcome, everyone! Good morning, Danny- oh hello, Blaire-"
    ch "Aiyah, Rajah, what is that godforsaken thing you have in your mouth?"
    r "It's just a...... ring pop, Cheng Lao Shi-"
    ch "A ring pop?"
    r "It's like candy on a ring- you can wear it....?"
    ch "How odd! Please make sure it goes into the trash when you finish it."
    r "I will, don't worry...."
    ch "Welcome in, Ether!"
    e "G'morning, Cheng Lao Shi.."
    ch "Alright, alright, settle down, everyone. We're going to start by going through yesterday's homework, that I hope you all finished?"
    ch "I will be verrrryyyy disappointed if you didn't~"
    e "{i}Presentations... this should be easy to sit through, since we won't be doing anything-{/i}"
    ch "I expect you all to be paying verrrrryyyyy close attention-"
    e "{i}I.. will try. After struggling in something as supposedly easy as Government, I don't think I can muster the energy to try for Mandarin.{/i}"
    ch "Rajah! Why don't you start us off by reading the lesson for today? Read loud and clear!"
    e "{i}I'm already getting distracted... Should I keep trying to pay attention? Being on YouTube was way better than this.....{/i}"
    menu:
        "Keep trying to pay attention":
            jump keep_trying_to_pay_attention
        "Sneak his phone out. It was way more entertaining anyway.":
            jump sneak_phone_out
    return

label keep_trying_to_pay_attention:
    scene bg chineseclassroom
    e "{i}No, no, I should try. I'm not flunking Mandarin yet. I think Cheng Lao Shi will at least give me a chance.{/i}"
    ch "--- and now, because of this Chinese cultural tradition, you should ALWAYS give your enemies a clock to wish on their downfall!"
    ch "Can anyone name another gift that means bad luck?"
    e "Pears?"
    ch "Excellent! Ether!"
    e "{i}Oh no-{/i}"
    ch "Can you tell us why pears mean bad luck?"
    e "Uhhhh-"
    e "{i}Don't say that aloud-{/i}"
    e "Because... they're yellow?"
    ch "Sometimes, they are indeed yellow. But why is that bad?"
    e ".... Yellow.... is bad luck?"
    ch "Nope!"
    ch "This is what happens when you {i}don't{/i} pay attention in class-"
    e "{i}... Not this again--{/i}"
    e "{i}This is exactly how Mr. Duras phrased it too-{/i}"
    ch "---pears are bad luck because their pronunciation, 'li', is similar to the word, part, or 'li kai', so giving someone pears is like hoping they end up losing all their friends and family."
    ch "Great for enemies, terrible for people you're close to B)"
    ch "Ether, did you get that?"
    e "I... Yes, I think so."
    ch "Can you tell me why pears are considered bad luck in Chinese culture?"
    e ".. they.... sound like parting...?"
    ch "Haiya! Close enough. I expect you to pay better attention next time!"
    e "Yes, Cheng Lao Shi...."
    e "{i}Pretty much what Mr. Duras said too....{/i}"
    e "{i}I guess this is the start of my academic downfall, huh?{/i}"
    e "{i}Why am I struggling in everything all of a sudden?{/i}"
    e "{i}It was just government... and then calculus... and now Mandarin...{/i}"
    e "{i}I used to think this was the easiest class I had, but I'm struggling to pay attention even now...{/i}"
    e "{i}Argh, just focus!{/i}"
    e "{i}Just because Cheng Lao Shi thinks you weren't trying, exactly like Mr. Duras accused you of being lazy, doesn't mean that you're stupid.....{/i}"
    e "{i}Right......?/i}"
    e "{i}Just get through this class, Ether, and you can watch all the YouTube you want during lunch....{/i}"
    e "{i}Just get through the class...{/i}"
    ch "Okayyyyyy, you little gremlins, I have a worksheet for you that's due at the end of class! It's based on what we just read, so let me know if you have any questions! Don't be afraid to ask for help!"
    e "....."
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
    e "{i}Screw it, I already spent all of Government doing the Mandarin work. It's not like it's gonna change anything even if I tried-{/i}"
    e "{alpha=0.5}{i}takes out phone{/i}{/alpha}"
    e "{i}As long as I keep it under my desk, Cheng Lao Shi probably won't notice..{/i}"
    e "{i}Heh-{/i}"
    ch "Oh Etherrrrrrrr-"
    e "{alpha=0.5}{i}quickly hiding phone{/i}{/alpha}"
    e "Hello, Cheng Lao Shi."
    ch "Was that a phone I {i}just{/i} saw?"
    e "..... no?"
    ch "Haiya, you're not slick at all! You've barely done any work on the classwork! I better not see it out again!"
    e "Okay..."
    e "{alpha=0.5}{i}Or I can just wait until he goes away...{/i}{/alpha}"
    menu:
        "Try doing the work":
            jump try_doing_the_work
        "Put away his phone briefly then take it out one Cheng Lao Shi isnt looking":
            jump take_out_phone_when_ch_not_looking
    return

label try_doing_the_work:
    scene bg chineseclassroom
    e "{i}No... I should actually try.. and show Cheng Lao Shi I'm actually trying...{/i}"
    e "{i}This worksheet... oh, I can actually answer the first question.{/i}"
    e "{i}The second one I think I understand, but I should probably check to make sure.../i}"
    e "...."
    e "{i}I don't want to ask Cheng Lao Shi for help......{/i}"
    e "{i}Or anyone else....{/i}"
    e "{i}He's just going to tell me I'm not trying like Mr. Duras said...{/i}"
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
    e "{i}No.. I should... keep trying....{/i}"
    e "{i}I don't wanna try anymore....{/i}"
    ch "I'm coming around to check on your first page! I hopeeeeeee you're workinggggg, little gremlins!"
    ch "Ah, yes, that looks good."
    ch "Excellent!"
    ch "You might want to double check that- oh, where is it? It's right here- no it's okay, you must've just missed it in the textbook..."
    ch "Ether!"
    e "{alpha=0.5}{i}swiveling around{/i}{/alpha}"
    e "Hi, Cheng Lao Shi."
    ch "How's the worksheet?"
    ch "Can I see what you have?"
    e "Can I have more time on it? I didn't... finish the front side-"
    ch "That's perfectly fineeeeeeee. Do you need any help?"
    jump ch_offers_help_on_ws
    return

label take_out_phone_when_ch_not_looking:
    scene bg chineseclassroom
    e "{i}Yeah, I'll just wait until they're on the other side of the classroom...{/i}"
    e "{alpha=0.5}{i}takes out phone again{/i}{/alpha}"
    ch "Etherrrrrr-"
    e "{alpha=0.5}{i}quickly puts phone away{/i}{/alpha}"
    ch "Why'd you take your phone out again, child?"
    e "...."
    ch "You can't be on your phone during class... ai yai yai... Ether, you know this. How come you're not doing any of the work? Do you need any help?"
    jump ch_offers_help_on_ws
    return

label ch_offers_help_on_ws:
    scene bg chineseclassroom
    e "Um-"
    e "{i}Wow, I didn't actually think he'd ask to help me.{/i}"
    e "I....."
    menu:
        "Yes, he's struggling":
            jump yes_struggling
        "No, he doesn't want to talk to Cheng Lao Shi after that callout.":
            jump no_help
    return

label yes_struggling:
    scene bg chineseclassroom
    e "Yes, I need help...."
    ch "That's okay! What question did you stop at?"
    ch "Hmmmmm, yes... unlucky number...... I did not think it would be hard to grasp-"
    e "I'm really sorry I didn't understand- I.... kept getting distracted."
    ch "Oh, I seeeee. Anywhos, can you tell me what the unlucky number in Chinese culture is?"
    e "{i}What if I'm wrong{/i}"
    ch "You can guess!"
    e "{i}But what if I'm wrong?{/i}"
    e "Uh.... it's.. four, right?"
    ch "Yup! You already understand half of it! The other half of the question is asking about why four is considered unlucky."
    e "{i}The part I'm not sure I understand.{/i}"
    e "Does it have something to do with how it sounds? Like the pears?"
    ch "Yes! See, you DOOO understand some of this :D"
    ch "So now tell me, what word sounds like 'si'?"
    e "I don't.. I'm not sure...."
    ch "Why don't you look at the terms learned and see if any of them have the same pronunciation?"
    e "{i}I feel so dumb.............{/i}"
    e "{i}Maybe I'm just forever short on brain cells or something...{/i}"
    e "{i}Where is the page I'm looking for?{/i}"
    e "{i}This one?{/i}"
    e "... I think it's the word for dying?"
    ch "Thereeee you go! Four is unlucky because Chinese people associate it with death."
    e "Ohhh, that makes sense.... are all lucky and unlucky items like that? They sound like a certain word?"
    ch "Exactly!"
    ch "Ah, there goes the godforsaken bell."
    ch "{alpha=0.5}{i}to the other students{/i}{/alpha} HAIYA DON'T JUST RUN OUT THE DOOR- CLEAN UP AFTER YOURSELVES!!!"
    ch "{alpha=0.5}{i}to Ether{/i}{/alpha} Class is over now, but you can come in during lunch! I would like you to come back, seeing as you haven't finished."
    menu:
        "Ether ends up going back during lunch":
            jump e_goes_back_to_ch
        "Ether just goes to lunch":
            jump just_goes_to_lunch
    return

label no_help:
    scene bg chineseclassroom
    e "No, I'm okay. I think I can figure it out."
    ch "Are you sure?"
    e "{i}I don't want to be antagonized for not trying...{/i}"
    e "{i}He's already suspicious of me.{/i}"
    e "{i}I'd rather finish this alone than be called out in front of the whole class again...{/i}"
    e "{i}I don't want this to end up the same way it did with Mr. Duras...{/i}"
    e "Yes, I can do it on my own. Thank you, though."
    ch "Alrrright, child."
    ch "Just give Cheng Lao Shi a holler whenever you need help, okay?"
    e "{alpha=0.5}{i}nods{/i}{/alpha}"
    e "I will."
    e "{i}I don't think I will.{/i}"
    jump just_goes_to_lunch
    return

label e_goes_back_to_ch:
    scene bg cafeteria
    s "During lunch...."
    e "{i}Dang, calculus was brutal....{/i}"
    e "{i}Good thing it's finally lunch.. and I can finally relax....{/i}"
    e "{i}Wait, there's Cheng Lao Shi talking to Blaire. I forgot I didn't finish that worksheet from his class...{/i}"
    e "{i}He did say I could go back during lunch....{/i}"
    e "{i}Gods, do I really want to spend my lunch period in class?{/i}"
    e "{i}I should really finish that worksheet, though.. and Cheng Lao Shi did offer to help...{/i}"
    e "{alpha=0.5}{i}walking into the classroom{/i}{/alpha}"
    scene bg chineseclassroom
    ch "Ether! Welcome back!"
    e "Hi, Cheng Lao Shi. I'm here to finish the worksheet from today's class..?"
    ch "Ah, yes, yes, I remember."
    ch "Sit down, sit down! I have your worksheet on my desk. You can grab a textbook from the shelf while I go heat up my lunch-"
    ch "Haiya, I'm so hungry!"
    ch "Don't worry, Ether, I'll be back in five minutes!"
    e "{alpha=0.5}{i}chuckling a little{/i}{/alpha}"
    e "Okay-"
    ch "MY RICE AWAITS MEEEEEEE-"
    e "{alpha=0.5}{i}grabbing his worksheet{/i}{/alpha}"
    e "Here's my worksheet-"
    e "And here's a textbook-"
    e "{i}Okay. I have all 30 minutes of lunch to finish this.{/i}"
    e "{i}It shouldn't be too hard, right?{/i}"
    ch "I'm back-- I'm back!"
    ch "Oh, my beautiful, beautiful lunch...."
    ch "Ether! Did you eat yet?"
    e "Uh, no-"
    ch "Aiyah, why not?"
    e "I was planning to finish the worksheet before I went to lunch-"
    ch "You should eat first! How can you think on an empty stomach, lah?"
    e "I will! I just want to get my work done first-"
    ch "We can go through the questions while you eat, and you can write them down after. I can even write you a pass if it cuts into passing period, just eat your food! How can you think on an empty stomach?"
    e "Okay...."
    e "{alpha=0.5}{i}taking out lunch{/i}{/alpha}"
    e "Here, I'm eating."
    ch "Excellent! Now, where did you stop on the worksheet?"
    e "Number three?"
    ch "Ah, the one about the color red. The other ones should be about the new year traditions. Do you remember why it's important?"
    e "It's a lucky color, I think?"
    ch "Yes! Black and white are considered unlucky. Do you remember the other traditions we do every year for good luck?"
    e "Uh........ something about firecrackers?"
    e "I'm not.. great at remembering them."
    ch "No worries! Let ol' Cheng Lao Shi tell you a little story, eh?"
    ch "Once upon a time, there was a big scary monster named Nian who would terrorize the nearby villages."
    e "{i}I think this is the story he told earlier too...{/i}"
    ch "See, Nian really really liked human meat, so it would constantly drag away unsuspecting humans for its next meal!"
    ch "The people were terrified!"
    ch "They didn't want to be torn apart by some beast! So of course, they tried to murder the beast by beating it with frying pans!"
    e "Uh- Did it work?"
    e "{i}That wasn't in the first telling-{/i}"
    ch "Ah, no, it didn't. It was quite disappointing, really. They put in so much effort to fight Nian, but it just swallowed all its attackers whole. So you know what they tried to do next?"
    e "What'd... they do?"
    ch "They lure the beast off the edge of a mountain!"
    ch "But Nian was clever, and knocked people off instead! It must've had fun watching everyone go splat."
    e "Oh...."
    ch "Anyways! The village people were getting desperate, but they had no idea what to do! Luckily, an old monk came and advised the village people to put up red banners and make loud noises to scare Nian away!"
    ch "Can you imagine almost dying to Nian multiple times and someone just comes along and tells you 'Oh, just put up some red banners! It'll definitely scare Nian away!'"
    ch "Regardless, when the village people put up those red banners and set off fire crackers, Nian ran for the hills and never came back!"
    e "So putting up things that are red is to scare off Nian....."
    ch "Exactly! Do you understand now?"
    e "Wait- so they put up red and set off firecrackers to scare away the beast called Year?"
    ch "No, no. Think of Nian as the year's bad luck, and the traditions as the mechanisms that scare off the bad luck!"
    e "Ooohhhh..."
    e "That makes sense!"
    ch "Yes, yes, I'm glad! That should explain the rest of the worksheet."
    e "Let's see- In Chinese culture, which color is considered luck- it's red..."
    e "Explain the myth that makes red the lucky color- Oh, I can answer that now!"
    e "I finished the worksheet!"
    ch "Excellent! Hand it over, child."
    ch "Thank you! The bell just rang, so you should hurry along to class now."
    e "Okay, Cheng Lao Shi-"
    e "Have a nice rest of your day!"
    ch "You too, gremlin! Remember Cheng Lao Shi will always be here to help you during lunch!"
    jump next_day_accepted_help
    return

label just_goes_to_lunch:
    scene bg cafeteria
    e "{i}Finally lunch time...{/i}"
    e "{i}I should find Rajah....{/i}"
    e "{i}Where is he?{/i}"
    e "{i}Oh, he's in the corner over there....{/i}"
    e "{i}There's a lot of people over there with him...{/i}"
    e "{i}I don't want to go over there....{/i}"
    e "{i}It's fine, I'll just sit by myself today.....{/i}"
    e "{i}I can finish that compilation I was watching earlier anyway, since I don't need to talk to anyone.{/i}"
    e "{alpha=0.5}{i}going on his phone{/i}{/alpha}"
    e "{i}Wow, this is really funny....{/i}"
    e "{i}Maybe I could send this to Rajah?{/i}"
    e "{i}No, he's busy...{/i}"
    e "{i}Oh, that was the bell, wasn't it?{/i}"
    e "{i}Is lunch already over?{/i}"
    e "{i}Time for class, I guess...{/i}"
    e "{i}I can see Rajah walking away with his big group of friends.{/i}"
    e "{i}Something about seeing him so carefree makes me feel empty inside.{/i}"
    e "{i}Eh, whatever, I can finish watching this video while I walk to class.{/i}"
    e "{i}I would rather know how this ends anyway than try to shoulder my way through Rajah's friend group.{/i}"
    jump next_day_no_help
    return 

# ALTERNATE ENDING START --> GOOD OR BAD
label next_day_no_help:
    # (The next day)
    scene bg chineseclassroom
    e "{i}Okay, I survived Government. I should be able to just sleaze through Mandarin.{/i}"
    ch "----worksheet due at the end of class today!---"
    ch "---can ask Cheng Lao Shi for your peers for help! Now remember--"
    e "{i}This worksheet is kind of long....{/i}"
    e "{i}I'll just....{/i}"
    menu:
        "Talk to Rajah":
            jump talk_to_rajah
        "Go on phone":
            jump go_on_phone_
    return

label talk_to_rajah:
    scene bg chineseclassroom
    e "Hey Rajah, did you start the worksheet?"
    r "We have a worksheet?"
    e "... You really weren't paying attention, were you?"
    r "Honestly, no. I was trying to predict the ending of the Gilded Stars episode because I didn't get a chance to finish it but I really really wish I had-"
    e "The Gilded Stars? I'm still on the Bronze Beast one-"
    r "Ooooh, you better catch up FAST, Ether. The plot twists there are insane I swear the creator just loves to torment us-"
    e "I'm trying- I just started it a day ago-"
    r "Pfft. I was binging it all morning."
    r "We're not doing anything else in this class anyway, so you might as well finish it!"
    e "{i}This is probably when I should say no and do the work but....{/i}"
    e "{i}I'm so tired of trying...{/i}"
    e "Yes, sure, why not..."
    jump go_on_phone_
    return

label go_on_phone_:
    scene bg chineseclassroom
    e "{i}My grade can probably tank this if I don't do it...{/i}"
    e "{i}Nothing I do will save it anyway when my parents yell at me everyday for it...{/i}"
    e "{i}I should.. probably ask someone for help. But who would I even ask?{/i}"
    e "{i}It's fine. Surely, I deserve to have a break...{/i}"
    e "{alpha=0.5}{i}takes out phone{/i}{/alpha}"
    jump spiral_into_isolation
    return

label spiral_into_isolation:
    scene bg chineseclassroom
    e "{i}Heh-{/i}"
    ch "Ai, Ether, what is that I see out? Surely, you didn't pull out your phone again during Cheng Lao Shi's class again, did you?"
    # pose should be off phone
    e "No....."
    ch "Oh! Then what was that black rectangular device in your hand?"
    e "My calculator?"
    ch "Why would you have a calculator out for this class, child?"
    e "....."
    ch "You can not learn if you do not try."
    e "{i}Almost like Mr. Duras said....{/i}"
    ch "If I see your phone out again, I'm taking i for the rest of the day."
    ch "Understood?"
    e "Yes, Cheng Lao Shi...."
    ch "Argh... those wretched devices and their brainwashing....."
    e "......"
    e "{alpha=0.5}{i}glancing at the worksheet{/i}{/alpha}"
    e "{i}I'm so tired of school.... I don't want to be here anymore...{/i}"
    e "{i}I just want to disappear.......{/i}"
    e "{i}There's no one for me to turn to anyway...{/i}"
    e "{i}Hey, Rajah's not doing any work either...... Oh, Cheng Lao Shi's telling him off too...{/i}"
    e "{i}I guess I should try doing the worksheet...{/i}"
    e "{i}Why don't I recognize any of these concepts?{/i}"
    e "{i}I remember when I thought this class was easy....{/i}"
    e "{i}When did this get so hard?{/i}"
    e "{i}When did everything.... get so hard?{/i}"
    e "{i}Rajah's on his phone again. And Cheng Lao Shi is on the other side of the room....{/i}"
    e "{i}Maybe it's fine if I.....{/i}"
    e "{alpha=0.5}{i}going on phone{/i}{/alpha}"
    ch "HAAAAAAAAAAAAIYAAAAAAAAAAAAAAAAAA- This is ridiculous-"
    ch "Rajah, Ether, go wait outside. Cheng Lao Shi needs to have a verrrrrry stern talk with you both about your wretched devices."
    e "...."
    e "{i}Well, my parents are going to throw a fit once they find out about this.....{/i}"
    jump confrontation
    return

label confrontation:
    scene bg schoolhallway
    e "{alpha=0.5}{i}walking into the hallway{/i}{/alpha}"
    r "Damn.. he's good....."
    e "We're in trouble."
    # (Sprites - It would be preferable if Rajah and Cheng Lao Shi alternate, and Ether is visible but greyed out and/or lower opacity. )
    r "Eh. Yeah."
    r "I guess we are."
    e "Aren't you worried?"
    r "What would I be worried about?"
    e "....."
    e "{i}Cheng Lao Shi punishing us? Phoning our parents? Grade backlash?{/i}"
    ch "Alright, you two MISCHEVIOUS gremlins."
    ch "You've been on your phones for TOO LONG this class."
    e "...."
    ch "So tell Cheng Lao Shi why you two were on your phones."
    r "Frankly, Cheng Lao Shi, I was bored out of my mind."
    ch "You didn't even finish the worksheet!"
    r "See, I tried to do it.. and then I gave up."
    ch "You gave up?"
    r "....."
    r "Yes."
    ch "Why did you give up? The worksheet only had four questions on it! It was not supposed to take more than 15 minutes to finish!"
    r "I just. I don't know, I just didn't have motivation to finish it."
    ch "So you decided to seek refuge on that phone of yours instead?"
    r "........... yeah, pretty much."
    ch "Why didn't you ask for help?"
    # thinking pose?
    r "........"
    r "I guess I didn't think about doing that."
    ch "Aiya.... Rajah-"
    ch "No, both of you could have asked anyone in the class, including me, for help. I'm sure your comrades would be willing to lend you a hand if you tried."
    ch "Do you understand that by choosing your phone over your work, your grades will decline?"
    ch "Your grades do not need to suffer such needless grief!"
    r "Mhm."
    ch "You have all day after school to be on your phone. I only need you to do work for 15 minutes."
    r "Mhm."
    ch "Do you expect to pass the class without trying?"
    r "......"
    e "........"
    ch "{alpha=0.5}{i}SIGHHHHHH{/i}{/alpha}"
    ch "You two were doing well in the beginning of the year. What changed?"
    r "....... guess I just lost the will to try in school, Cheng Lao Shi. I dunno what else to tell ya."
    ch "Is that all you are going to say?"
    r "{alpha=0.5}{i}shrugs{/i}{/alpha}"
    ch "Alrrrright. Rajah, go back inside and ask someone for help. I expect that worksheet to be done by the end of class."
    r "Yes, sir...."
    r "{alpha=0.5}{i}leaves{/i}{/alpha}"
    ch "So... Ether."
    ch "Cheng Lao Shi notices you haven't said anything at all."
    e "......"
    ch "Cheng Lao Shi also notices your grade was very good until the last several days."
    ch "Did something happen?"
    e "........"
    e "I just...."
    e "{i}What am I supposed to say?{/i}"
    e "{i}That I lost motivation to try?{/i}"
    ch "Ai... Ether, can you at least answer me this? Are you struggling in the class?"
    e "A.. little...."
    ch "Remember, Ether, you can always come in during lunch to ask for help."
    ch "Cheng Lao Shi knows you can be better than this."
    e "Okay....."
    ch "Do you need help on today's worksheet?"
    e "... no ...."
    e "I can do it on my own...."
    ch "Fineeee.. I trust you.."
    ch "But remember, you can always come in during lunch to ask me for help, yes?"
    e "{alpha=0.5}{i}nods{/i}{/alpha}"
    menu:
        "Consider Cheng Lao Shi's words":
            jump consider_ch_words
        "Don't listen to Cheng Lao Shi":
            jump dont_listen_ch
    return

label consider_ch_words:
    #-----------------------------------------------after class
    scene bg chineseclassroom
    s "{alpha=0.5}{i}bell ringing{/i}{/alpha}"
    ch "That's it for class today! Cheng Lao Shi expects you to turn in the worksheet in the basket by the door and eat a big, healthy lunch!"
    ch "Go munch munch, you gremlins!"
    r "It's lunch already? I'm not even done with the worksheet yet-"
    e "How far did you get?"
    r "I have one more to finish- you?"
    e "After I finish this sentence, I'm done."
    r "Nice. Can ya show me what ya wrote for the last one?"
    e "Here."
    r "Oh that makes sense- damn I really should've figured that out earlier but it's fine-"
    r "Alright, I'm done. You want me to turn yours in too?"
    e "That would be great, thanks!"
    e "{alpha=0.5}{i}walking into the hallway{/i}{/alpha}"
    scene bg schoolhallway
    r "Phew, we're done with that class for today."
    r "Usually, I don't care so much about Cheng Lao Shi's class, but him pulling us both out of class had me on edge the entire period."
    r "What'd he say to you after I left?"
    e "......"
    e "About the same thing. He just said 'oh you used to be so much better', 'i know you can do more than this', stuff like that."
    e "He still told me to finish the worksheet like he told you before he sent you back inside."
    r "That's it?"
    e "He also told me I could come into his room during lunch to ask him for help...."
    r "Are you gonna consider it?"
    e "Maybe....."
    e "Would you?"
    r "Honestly, Ether, after the entire Duras situation, I'm not exactly looking to spend extra time with teachers."
    e "Cheng Lao Shi seems a little more reasonable."
    e "Cheng Lao Shi actually offered to help. Mr. Duras didn't."
    r "Eh. Teachers. Adults. They're all the same. You take your chances if you want. I'll pass."
    e "{i}Rajah doesn't think Cheng Lao Shi will really be any different from Mr. Duras, huh?{/i}"
    e "{i}But.. They aren't the same.{/i}"
    e "{i}I want to give Cheng Lao Shi a chance.{/i}"
    jump stops_phone_addiction_from_going_too_far
    return

label dont_listen_ch:
    scene bg chineseclassroom
    e "{i}Come in during lunch?{/i}"
    e "{i}If I learned anything from Mr. Duras.....{/i}"
    e "{i}It's that teachers don't care.{/i}"
    e "{i}Here's the worksheet.{/i}"
    e "{i}It's.....{/i}"
    e "{i}I don't want to do it.{/i}"
    e "{i}My grade in government is already dropping. It doesn't matter how low my Mandarin grade is if my parents are going to get mad with me regardless.{/i}"
    e "{i}Even Rajah isn't actually working... Is he on his phone?{/i}"
    e "{i}And everyone around is just talking anyway ....{/i}"
    e "{i}Did they finish already?{/i}"
    e "{i}If no one's working.....{/i}"
    e "{i}Then why should I?{/i}"
    e "{i}I'll just go on my phone...{/i}"
    e "{i}Oh, Rajah sent me something!{/i}"
    e "{i}This reminds me of Blaire- Oh that's hilarious-{/i}"
    e "{i}The short right under is by the same creator! I wonder if Rajah would like that-{/i}"
    ch "Ether!"
    # ether afraid
    e "Hi, Cheng Lao Shi-"
    ch "Hello, Ether."
    ch "Could you come outside with me again?"
    e "{i}I should've been more careful...{/i}"
    e "{i}Rajah just put his phone away as Cheng Lao Shi walked by...{/i}"
    e "{i}He didn't get caught.....{/i}"
    # --in the hallway--
    scene bg schoolhallway
    ch "So Ether..."
    ch "Did you finish the work for today?"
    e "Not yet..."
    ch "I see you were not working on it."
    e "No.... I wasn't...."
    ch "Do you want to explain why you were on your phone instead of doing the work again?"
    e "....."
    ch "Cheng Lao Shi stands by what he said before. Cheng Lao Shi believes you have done better before."
    e "....."
    ch "So why was Ether on his phone?"
    e "......"
    ch "....."
    e "......"
    ch "... I will not understand if you do not tell me, Ether."
    e "....."
    e "I.. have a hard time grasping content sometimes."
    ch "Oh?"
    e "Nevermind. I'll do the worksheet-"
    ch "No. You stay here."
    ch "You can do the worksheet right now, but the problem that led you to go on your phone will not be solved."
    ch "You only started going on your phone excessively in the last week. What happened last week?"
    e "....."
    e "{i}Should I tell him about Mr. Duras?{/i}"
    e "{i}No, that would be embarassing...{/i}"
    e ".. I don't know."
    ch "How can I help you if you do not tell me?"
    e "It's fine. I'll just go back in and do the worksheet."
    e "I am sorry for being off-task."
    e "{i}I don't need your help, Cheng Lao Shi. My phone can help me just fine.{/i}"
    ch "...."
    ch "I am going to send you to the counselor's office."
    e "Oh, okay."
    e "{i}I guess I'm really in trouble now, huh?{/i}"
    e "{i}But if I was getting sent home, wouldn't he have sent me to the principal instead?{/i}"
    ch "Here you go. Take your things with you!"
    e "{i}And now I leave...{/i}"
    e "{i}Probably to get chewed out by more adults....{/i}"
    e "{i}I really don't want to be here anymore.......{/i}"
    jump go_to_counselor
    return

label go_to_counselor:
    scene bg schoolhallway
    # (Note - he's on his phone before arriving at the office)
    e "{i}The counselor's office is here.....{/i}"
    e "{i}I've never actually had a real conversation with Ms. Antimony before.{/i}"
    e "{i}But I don't think this is going to going well...{/i}"
    e "{alpha=0.5}{i}walking in{/i}{/alpha}"
    scene bg counseloroffice
    an "Hello, Ether."
    e "Hi Ms. Antimony."
    e "Cheng Lao Shi sent me here for the period."
    an "I see."
    an "I just received a message that he did send you here just before you came in."
    e "Oh."
    e "That's good to know."
    e "{i}I already want to leave.{/i}"
    an "Do you know why Cheng Lao Shi sent you here?"
    e "Well....."
    e "I already know what I did wrong, so I don't think I have to be here...."
    e "I can go back to class and work on the stuff he wanted me to do anyway."
    an "Interestingly, Cheng Lao Shi's reason for sending you here actually has nothing to do with you not doing work in class."
    an "It has to do with... your phone addiction."
    e "Oh."
    e "Did he say anything else?"
    an "Cheng Lao Shi tells me your phone addiction only started recently. Is this true?"
    e "Yes...."
    an "Could you tell me more about when you started going on your phone during class?"
    e "What do you mean?"
    an "Why did you start going on your phone during class?"
    e "I... didn't feel as though the effort I was putting into class was worth it."
    an "What made you think it wasn't worth it?"
    e "...."
    e "{i}Do I tell them about Mr. Duras?{/i}"
    e "{i}They might think I'm being unreasonable, though.{/i}"
    e "{i}They usually believe the adult over the student...{/i}"
    an "This is a safe space, Ether. Anything you tell me here will be confidential, unless you mention self-harm or harming anyone else."
    e "I don't plan to hurt anyone...."
    an "I'm glad you don't."
    an "Could you tell me why you didn't think the effort you put in class wasn't 'worth it'?"
    e "I felt like the teacher wasn't giving me a chance."
    an "Cheng Lao Shi wasn't giving you a chance?"
    e "Um, no. Not Cheng Lao Shi. Mr. Duras."
    an "How so?"
    e "...."
    e "I tried asking him for help during class, because I couldn't catch up with the lecture, and he told me to ask someone else for help since it was my own fault I wasn't paying attention."
    an "Could you tell me about the Mr. Duras' lectures? What made it hard to catch up?"
    e ".. when Mr. Duras is lecturing, he's always doing multiple things at once. While he talks, he points to the slides, walks around, waves his hands, and he expects us to be able to copy and process everything on the slides at the same time."
    e "There's always so much going on."
    e "I tried to tell him that I couldn't focus because everything was so distracting, but he just told me it was because I wasn't trying."
    an "I see.... "
    an "How does that make you feel?"
    e "It makes me feel a little dumb. Because everyone else is able to catch up on everything Mr. Duras wants us to do just fine, so why can't I?"
    e "Is there something wrong with me?"
    an "I don't think so, Ether."
    e "How do you know?"
    e "My grade in Mr. Duras' class keeps dropping, and all my other class grades are slowly dropping too...."
    an "Do you only have trouble focusing in Mr. Duras' class?"
    e "Sometimes......"
    an "When did you start turning to your phone during class?"
    e "....."
    e "{i}That's.... a good question...{/i}"
    e "{i}I'm not sure I can answer...{/i}"
    an "Let's go back to the class questions first."
    an "So to reiterate, you felt that Mr. Duras wasn't giving you a chance, correct?"
    e "Yes.... I have tried talking to him about it... but he doesn't like listening...."
    an "Are there any other teachers you have that teach the same way Mr. Duras does? For example, does Cheng Lao Shi make you feel the same way?"
    e "Cheng Lao Shi usually doesn't have so many things going on while he teaches..."
    e "Cheng Lao Shi also offers to help a lot in class. Mr. Duras doesn't necessarily do that."
    an "Hmmmmmmmm."
    an "Do you think it's easier to learn in Cheng Lao Shi's class, compared to Mr. Duras' class?"
    e "A little bit, yes. I feel like it's a lot easier to process what Cheng Lao Shi is saying because he doesn't expect us to multitask during his lectures."
    e "Then I start wondering if I'm just really stupid in Government, but that's probably just me being slow."
    an "Hm. Okay."
    an "Ether, I'd like to introduce a term to you. It's called 'overstimulation'. When a person is overstimulated, it's because there's too much going on for the person to process. Do you feel like that's what happens to you in Mr. Duras' class?"
    e "Yes. In Ms. Fong's class too, she's always going too fast and I never fully understand anything she teaches until I ask someone else to explain it much slower to me."
    e "There's so much going on, and not enough time for me to comprehend everything!"
    an "Understandably so. Do any of your other peers seem to struggle the same way you do?"
    e "Not a lot of them, no."
    e "Is there something wrong with me, Ms. Antimony?"
    an "No. I don't think so."
    an "I just think that certain teaching styles don't work for you, Ether, and that's okay, because everyone's brain works differently. You process information a little differently than everyone else, and that's what makes it hard to learn."
    e "Neurodivergent."
    e "Wait, so does that mean I'm autistic or something?"
    e "{i}I don't want to be autistic...{/i}"
    an "Not at all. It just means you learn differently. You're just as 'smart' as any other student at this school."
    an "How does this make you feel?"
    e "That explains some things...."
    an "A lot of neurodivergent individuals, like you, also have learning struggles in school. Many of them, similar to you, also get frustrated, and turn in different mechanisms to help them deal with it."
    an "How have you been dealing with your frustration with school lately?"
    e "I dunno."
    e "Going on the internet and watching YouTube, I suppose."
    an "Do you feel that's helping you deal with your emotions?"
    e "Yes."
    e "It helps me mentally escape school, because it never seems to end."
    an "Did you often watch YouTube at school for the same reason?"
    e "...."
    e "{alpha=0.5}{i}thinking{/i}{/alpha}"
    e "Yes...."
    an "Do you think this is healthy for you?"
    e "I feel like it's fine...."
    an "Have you noticed any changes in your general behavior lately?"
    e "Uh....."
    an "Have you been eating and sleeping the same amount? Do you feel any better about school when you're not on your phone?"
    e "I {i}have{/i} been sleeping a little later than usual... waking up a little more tired..."
    e "My feelings about school haven't changed much since I started going on my phone..."
    an "Have you been talking to many people since you started going on your phone?"
    e "No... I just.. go on my phone.."
    an "Have you asked anyone for help with school since going on your phone?"
    e "A couple times before... but not really, no..."
    an "Do you think you could tell me why?"
    e "I.... don't.. really want to talk to people about school."
    an "Why not?"
    e "I'm... not quite sure. They make me feel stupid...."
    an "How much do you personally care about school?"
    e "I know it's important I graduate so I can find a good career..."
    e "I know being on my phone during class isn't good, but it feels like it's the only thing that helps me deal with how I feel about school."
    an "Would you be open to exploring other ways to dealing with your frustration?"
    e "Uh... sure....."
    e "{i}I'm already tired of being here...{/i}"
    an "Being on your phone for extended periods of time can worsen your sleep schedule, mental health, and lead to social isolation. I'd like to encourage you to find a healthier means of dealing with your frustration."
    e "... okay, Ms. Antimony..."
    an "One of the best ways to deal with emotions is to write them down. You mentioned that your feelings about school didn't change much after being on your phone?"
    e "Yes...."
    e "I guess that now that I think about it, I'm not really expressing them..."
    an "This is where you can start journaling to help process how you're really feeling. Studies have shown that a lot of people like you have tried writing, and it has helped them understand how they're feeling and why they're feeling that way."
    an "It's also a good way to self-reflect on how you're doing in school and at home."
    an "How would you feel about trying it?"
    e "....I'll think about it..."
    an "It's completely okay if it doesn't work for you. You can come back, and we'll find something that does! But I want you to try journaling later today in this notebook I'm going to give you and see how you feel afterward. Does that sound okay to you?"
    e "Okay..."
    an "I believe the lunch bell has just rang. Have a good day, Ether."
    e "You too, Ms. Antimony...."
    # ------ (At home)
    scene bg bedroom
    e "The day's finally over...."
    e "I really don't want to do homework yet...."
    e "Maybe I'll just watch some more SladeSlice and scroll for a bit-"
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
    e "Well.. it's not like I could feel any worse..."
    e "There's that notebook Ms. Antimony gave me..."
    e "Oh, there's a prompt on this page!"
    e "There's a different prompt on every page..."
    e " 'How are you feeling today?' "
    s "-Journal-"
    ej "I feel... tired. I went on my phone during Mandarin today, but Cheng Lao Shi pulled me out of class to tell me to go to Ms. Antimony's office. Ms. Antimony to try writing about my feelings so I could get resolve my... 'phone addiction'."
    ej "I guess Ms. Antimony thought that me being on my phone for too long was bad for me, so here I am. I guess it's helping a little, to write about how I feel."
    ej "I'm honestly at the point where I just don't like going to school anymore because nothing I do feels like it has much value... I don't know how I feel abot Ms. Antimony telling me I'm 'neurodivergent' because it doesn't really change anything."
    ej "If I tried telling Mr. Duras that I haven't been 'paying attention' during his class because I was neurodivergent, I don't think he would believe me. He'd probably tell me I made up the word or something."
    ej "You know, I'm beginning to realize most of this is really just Mr. Duras. Mr. Duras is the only teacher that makes me feel like I'm doing something wrong. I think now that I'm really thinking about it, Cheng Lao Shi genuinely wanted to help me. I just didn't want to tell him anything."
    s "-End journal-"
    e "Huh... I guess it really did help. I feel... calmer? it feels like there's not as much going on in my head now that I've written some of it down."
    e "Ms. Antimony was right. Maybe I'll go see her tomorrow."
    jump e_keeps_journaling
    return

label e_keeps_journaling:
    #----- (the next day- bg is school hallway)
    scene bg schoolhallway
    r "Ether! Where'd ya go after Cheng Lao Shi pulled ya out of class?"
    e "I was in Ms. Antimony's office. I'm about to go to her office, actually."
    r "Dang, what for?"
    e "Yesterday, Cheng Lao Shi sent me to Ms. Antimony's office because he was concerned about my phone addiction. Ms. Antimony suggested I journal to deal with how I was feeling better."
    e "I tried journaling too, and it did feel better than going on my phone."
    e "I feel like when I'm going on my phone, I'm just ignoring how I feel. I think it makes me feel more stressed, actually, because I'm consuming so much content. When I write it down I can acknowledge and process it so I feel more at ease."
    r "Huh. Glad it works for you."
    r "Cheng Lao Shi sent me to Ms. Antimony's office for the same reason. I realy didn't like journaling though, 'cause I find writing boring."
    e "Have you thought of going back to try other things?"
    e "I'm sure there has to be something else that could help you!"
    r "Eh.. maybe...."
    r "Ms. Antimony's not the first one to tell me my phone isn't good for me either. My parents have been yelling at me for not sleeping enough."
    r "I've been more tired and depressed lately, so I'm not convinced anything is really going to work."
    e "Didn't Ms. Antimony mention that being on your phone worsens your mental health?"
    r "Huh?"
    r "Oh, yeah, I guess she did say that..."
    e "Come on, we can go see Ms. Antimony together."
    jump good_ending
    return

label good_ending:
#    ---------------- One month later --
    scene bg bedroom
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
    s "Good Ending Reached!"
    return
#end of good ending

#Bad ending Start
label do_not_journal:
    scene bg bedroom
    e "Right, because writing things down is going to make me feel better about school?"
    e "No."
    e "It's not like anything I write is going to make a difference to Mr. Duras, who's still going to fail me whether or not I'm trying in his class anyway."
    e "No, I'm just going to scroll. At least {i}that{/i} doesn't feel like a waste of time...."
    #-------------------------- (the next day)
    scene bg schoolhallway
    r "Yo! Ether!"
    e "Hi Rajah!"
    r "Where'd Cheng Lao Shi send you yesterday?"
    e "Oh, he sent me to the counselor's office."
    e "Ms. Antimony said it was something about a phone addiction...."
    r "Yeah, Cheng Lao Shi sent me over to her office once too. She told me it was bad to be on your phone all the time, bad for your physical and mental health and sleep schedule yada yada yada I could've cared less..."
    r "She told me to try journaling to 'deal with my emotions' better."
    e "She told me the same thing too!"
    e "Did you end up trying it?"
    r "Lowkey I just wrote two sentences and lost motivation because writing is really boring to me..."
    r "I'm not gonna lie, I didn't see how it was supposed to help me."
    r "Don't tell me you actually tried it?"
    e "I thought about it.... but I just ended up watching YouTube all night instead."
    e "I mean, it was a little more entertaining than writing anyway..."
    r "Ha! You and me both, bud."
    r "You're still nowhere close to my level, though. Catch up!"
    e "Don't worry, I will!"
    jump bad_ending
    return

label bad_ending:
    # ------- (one month later...)
    scene bg bedroom
    e "{alpha=0.5}{i}scrolling on social media{/i}{/alpha}"
    #gradually getting more sad
    e "Oh, it looks like Blaire, Danny, and Roger went bowling yesterday. They seemed to have a lot of fun."
    e "They got to go on a field trip for that? Lucky."
    e "I wish I could go on that field trip... but.. well...."
    e "It's 2 AM. I should probably go to bed. Better for my health."
    e "Eh, whatever. My grades are already trash, my parents hate me, and the only thing I can do to escape all that is going on my phone."
    e "It's like no one even needs me...."
    e "What is there to live for anyway?"
    e "I can go to sleep, but I'd still be tired the next morning."
    e "I can go to school, but all I do is get yelled at. I don't even have anyone to talk to."
    e "There's nothing for me to strive for anymore."
    e "Nothing at all......"
    e "What... am I supposed.. to do...?"
    s "Bad Ending Reached!"
    return
#bad ending end

# NEUTRAL ENDING STARTTTTTTTT
label next_day_accepted_help:
    # --------------------------------------------------------------- (During lunch the next day...)
    scene bg cafeteria
    r "Ether!"
    e "Hi Rajah!"
    r "Where were you at lunch yesterday! I couldn't find you."
    e "I was in Cheng Lao Shi's classroom finishing the worksheet from class."
    r "Oh, nice!"
    r "Did you finish?"
    e "Yeah! Cheng Lao Shi was actually really nice about explaining things to me."
    e "I was initially afraid to ask him because I thought he'd be like Mr. Duras...."
    r "That's exactly why {i}I{/i} didn't bother asking Cheng Lao Shi..."
    e "No, you should ask him for help! He'll probably make fun of you, but he won't shut you down like Mr. Duras."
    r "Eh.... I'll think about it..."
    e "I'm going to go to his room right now so I can ask about what we talked about during class today. Do you want to come with?"
    r "I'm gooooooooooooooooooooooooooood-"
    e "I'll see you in history?"
    r "Yup."
    r "See ya later!"
    jump e_keeps_going_to_ch_for_help
    return

label e_keeps_going_to_ch_for_help:
    # -------- (walking into Mandarin classroom)
    scene bg chineseclassroom
    e "Hi Cheng Lao Shi!"
    ch "Ether! Hello hello!"
    ch "How can I help you today, child?"
    e "I wanted to make sure I understood all the vocabulary words for this week so I could use them in sentences for the homework."
    ch "Ah, of course! I'm glad you're willing to come back to get help."
    ch "Which words are confusing to you?"
    e "I think 3 and 4....?"
    ch "The two transaction words.. yes... mǎi and mài!"
    e "They sound the same, they look almost the same... How do you tell the difference?"
    ch "They are very similar, aren't they?"
    ch "Tell me, Ether. What differences do you notice?"
    e "One character has some extra marks on the header...."
    ch "Yes! Don't those extra marks look a little like the character for ten?"
    e "Yes..."
    ch "The one with the ten, mài, means to sell! You can think of it as an angry little peddler trying to make sales!"
    ch "If you look hard enough, the ten almost looks like a little man showing off the entire character as if he's trying to sell it!"
    e "Cheng Lao Shi- the ten is a cross-"
    ch "Yes! Those are his little arms! And because he's being so showy, you can remember that he's trying to aggressively rake in sales, so it's said in the fourth tone: mài!"
    e "Okay, I can't unsee the little man now...."
    ch "Good! That is how you will remember!"
    ch "The other character, mǎi, means to buy. You can think of the word with its third tone as deliberation as you try to figure out if the fries from the store across the street are worth buying."
    e "Oh?"
    ch "The third tone goes down, then back up! So maybe, it's like someone going 'hmmm, I want chips.. no, wait, the Oreos are cheaper!' After all, you should always be financially responsible and chase discounts like your life depends on it!"
    e "{alpha=0.5}{i}laughing{/i}{/alpha}"
    e "Okay, okay."
    ch "Does that make sense?"
    e "Yup. Aggressive little man trying to sell things versus little man trying to save money."
    ch "Precisely! Is there anything else you need help with?"
    e "Uhh...."
    e "Not for this class, at least...."
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
    e "{i}Do I want to tell Cheng Lao Shi about my other classes?{/i}"
    e "{i}Cheng Lao Shi has been pretty supportive of me so far, maybe he'd understand...{/i}"
    e "Yes.. see.. for Mandarin, I can come in during lunch... it's Government that's making me lose my mind. And my Calculus grade is about to drop another letter if I don't pass the next test..."
    ch "Hmmm... is the class hard?"
    e "Yeah.. a little bit....."
    e "It's hard to focus because Mr. Duras is always moving his hands around while explaining the notes. I can't read the notes {i}and{/i} listen to him at the same time, and I'm starting to think it's because I'm stupid or something, because most of the class is able to keep up just fine!"
    ch "Hmmm... have you talked to Mr. Duras about it? Or asked him for help?"
    e "I have....."
    e "He just tells me he doesn't think I'm trying."
    e "And I {i}am{/i} trying- I look up what he explained online when I get home and I understand it much better than in his classroom!"
    ch "Tsk. Duras, that idiot."
    ch "You are a clever child, Ether. I think that hairy man's classroom is against you."
    e "His classroom or my brain?"
    ch "Aiya.... You are not the first to complain to me about Duras' class... "
    ch "The man is just... insensitive...."
    ch "After teaching for so long, you would think he's better at his job!"
    e "Oh....."
    e "What do you think I should do?"
    ch "If Duras continues to be a stubborn mule, I think you should self-study or ask one of your peers for help."
    ch "Terrible, terrible man....."
    ch "It is not your fault his teach style does not work for you."
    ch "You can always come in during lunch to ask me for help."
    ch "Cheng Lao Shi can explain the government far better than the stinky, hairy man..."
    e "{alpha=0.5}{i}laughs{/i}{/alpha}"
    e "Cheng Lao Shi, I don't think you should be saying that about him-"
    ch "Ay, don't tell Cheng Lao Shi what he can and can not do."
    ch "If Duras thinks you're not trying, tell me again and Cheng Lao Shi will drop Duras a line about his terrible teaching---"
    ch "Ah, there's the bell. I will have to prepare for class now."
    e "Okay, I'll go to class now. Thank you, Cheng Lao Shi!"
    ch "Yes, yes, I will see you tomorrow!"
    jump stops_phone_addiction_from_going_too_far
    return

label dont_tell_ch_abt_gov:
    s "Is Ether going back to Mandarin class for more help?"
    menu:
        "Yes":
            jump stops_phone_addiction_from_going_too_far
        "No":
            jump next_day_no_help
    return

label stops_phone_addiction_from_going_too_far:
    # (walking home)
    scene bg street
    r "Oi! Ether!"
    e "Hi Rajah!"
    r "I've barely seen you at lunch the last couple days- where the hell have ya been?"
    e "I've been in Cheng Lao Shi's classroom asking for help on Government..."
    r "You asked Cheng Lao Shi for {i}Government{/i} help?"
    e "Hey! In my defense, Cheng Lao Shi is way better at explaining things than Mr. Duras."
    e "Duras keeps waving his arms and talking and telling us to write down the notes on the slides."
    e "Cheng Lao Shi just talks about it and brings up pictures when necessary."
    e "I actually memorized the first ten Amendments with his help!"
    r "That's great!"
    r "Meanwhile, I got kicked out of Ms. Fong's room for being on my phone...."
    e "You were on your phone? In Ms. Fong's class?!"
    r "Let's just say I really wanted to finish SladeSlice's shorts series..."
    r "Anyway, she sent me out of the room and told me to go to the counselor's office! You know Ms. Antimony, the counselor?"
    e "Yes?"
    r "She asked me why I was constantly on my phone 'cause I guess Ms. Fong told her-"
    r "Anyway, I was like... I can't focus and I thought she'd be like Duras and y'know, say I'm not trying...."
    r "Then she asked {i}why{/i} I couldn't focus and I started complaining about Duras and I {i}really{/i} thought she'd like, slap me or something but she didn't, surprisingly."
    r "She just told me I was likely neurodivergent or something like that, whatever that means."
    e "Neurodivergent?"
    r "Yeah."
    r "Apparently it means I process information differently or something like that- she was trying to explain to me why I had so much trouble focusing on Duras' nonstop yap."
    e "That makes sense, actually. I can usually focus in my other classes, too. It's really just Duras' class I struggle with."
    r "Right, right."
    r "You know what she made me do after that?"
    r "She suggested I journal to get the frustration with Duras out of my system. She yapped a crazy amount about how being on my phone was going to lead to negative mental health and less sleep... she actually wasn't wrong about the sleep part. I slept like, maybe 4 hours yesterday."
    e "So did you journal?"
    r "I mean. She kinda sorta made me try it. It was helpful, I guess, but I only wrote down two sentences before I got bored and antsy."
    r "She basically just told me to write down how I feel and stuff like that."
    r "I didn't like it, but maybe it'll work better for you since you're more patient than I am."
    e "Hmmmm.. I'll try it and let you know how it goes."
    e "Did Ms. Antimony suggest anything else for you to try?"
    r "She had me try some fidget toys too. If you ask me, those worked way better than journaling."
    e "Hmmmm.. okay, I'll try them when I get home."
    r "A'ight. This is my stop. See ya tomorrow, Ether."
    e "See you, Rajah!"
    jump neutral_ending
    return

label neutral_ending:
    scene bg bedroom
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
