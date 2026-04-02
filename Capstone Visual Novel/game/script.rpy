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
    jump day2_start_class
    return

label ask_rajah_if_finished:
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
    e "{i}No, I don't want to bother him even more....{/i}"
    jump goes_home_to_study
    return

label goes_home_to_study:
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
    e "{i}Today's the day of the quiz and I am so going to fail but no no I will not fail I can not afford to fail-{/i}"
    e "{i}I've looked up so much of the notes... I should be fine, right?{/i}"
    e "{alpha=0.5}{i}walking down the hallway{/i}{/alpha}"
    e "{i}Oh, there's Blaire. She doesn't seem worried at all. But why would she, when she's been talking about how easy the work's been?{/i}"
    e "{i}Rajah's early too. He's just scrolling on his phone.. I wish I could be confident enough to do that.. but I've spent the last night worrying so much about the quiz that I feel like I barely slept at all...{/i}"
    e "{i}I'm just going to review the notes I found on the topics while I wait... the more time spent cramming, the better, right?{/i}"
    jump quiz_starts
    return

label quiz_starts:
    md "Alright, class. Come on in."
    e "{i}It's starting it's starting it's starting I am sooooo doomed-{/i}"
    md "I hope you all studied for the quiz today! But before we get to that event of the day, we'll have a short warm-up to help you prepare for it."
    md "I'll just review a couple of concepts, and you all can shout out the answers."
    e "{i}No- I can never focus when there's that many people talking-{/i}"
    md "So for our first question... Can anyone explain to me why the Articles of Colonies didn't work?"
    n "--Because it didn't coin money-"
    n "--Couldn't regulate trade---"
    n "--No enforcement--"
    n "--Ca̶̠̍ǔ̷̻s̴͓̐ẽ̶̫d̵̄ ̵͔̍c̴̦̅o̴̫͗nfl̷̜͋i̶̛̮c̴̜͆t̵̯͝ b̸͔̌ė̶̡t̵̡͂ẉ̶̚een ̶̙̍t̷̼̽h̶̳͝e ̶͖͆staṱ̸̂ȇ̸͓ś̵͉-"
    n "-̸̨͊-̵͓̀ ̵̺̃C̶͓̐o̴̹̍ṵ̸͝l̶̹͘ḓ̵͛ǹ̴̖'̶̡̐t̶̡̊ ̷̲͗a̵̠̓d̴̯͆d̸̮͆r̴̙̃e̷̹͝ś̵͔s̸͇̓ ̶̥̕p̶̪̈r̵̞̾è̴͕s̴̗̀s̴͎̽i̴͙̍n̴̦̈́g̶̬̈ ̵̝̂t̵̗́ḩ̶̾r̷͇͛ẽ̴͖a̸̝͋t̷̻̍s̸͚͆-̸̧́-̷̝̑ "
    n  "-̸̬̮̤̣̖̀̀C̵̞̏̓̀̾̓͒ờ̵͕͖̳̀̓͗̄u̸͚̟̟͓̓̎̾l̶̢̩̙̯̕͜d̶̳͓͈̠͛ñ̴̰͖͚̹͙̲̾͠'̴̢̭̖̅͝t̶̞̭̪͇͊͆͐̚ b̴̛̙͖̥̦̼̿̑͜ȇ̷̡̜͈̭͉̅̇̅͆̋͜ r̶̖̳̈́̔͂̿̊̄ͅȩ̸̛̟̬̩̘̓̓v̴̧͈̜̯́͆̈́̕͠í̵̺̏̕ṡ̶̩͋͠e̸̗̹͍̝̟̾͌̀͌͝͠d̸̲̺̫̩̆́̇̍̎͜ ̴̡̢̛͈͓͎͙͐̽͌̒ę̸̦̞̏͂a̶̡̰͍͐̍̄s̷̟͕̮̏̾̇̑i̴̝͙̅ḽ̷̡̨̫̲̈́y̷̐̉͒̒͝ "
    n "-̷̠̭͉̯͚͉͓͊-̵̨̛̛̼̗̝̟͖͍̦̤̮̲̭̯̓̌̔̇͊̆̽͑͌̑͝ ̵̳̅̀̾͑͗͆͌̌͜͜͝͝͝W̴̻̝͒̐̄̅̔͛͐̽̅͆̕E̵̡̱̘̖̙̖͉̓͋͝A̴̧͋͗͋Ķ̵̩͔̖̓̾̐̎͘͠͝ ̴̱̱͙̤͎̩̹̹͈͇̋̀̽̐̚C̵̨̱͎̩̩͉͎̟͍̦͍̖͇̍͂́͌̔̄̿̈́͌͝E̵͆̍́̈́̽̈́̓͛͆̓̀̚ͅN̴̦̓͒̋́̂͊͌̊̑̈́̌̀͜T̷̡̹͚̥͚̤͔͚̋Ȑ̵̨̻̘̖̘̼̟͓̬̲̊A̴̛̛͚̟͔͎͎̝̗̓̆̋͗͆̏̓̽͗͆Ļ̷̪̬͓̮̲̭͖͕͜͝ͅ ̴̢̨̧̦͉̯̱̓̌̏̒̈̆̾͜G̴̲̗͙̦͇͍͉̟̰̪̤̮̦̿͆͋̑O̸̜̯͕͍̰̥̓V̴̜̺̯̫̤̋͠E̸̲̺̳̠̭̠̰̤̦̼̾̈́̃̈́͛̀͒̊̐̉͠ͅR̷̨͕̳̫̖͙̫̣̰̆̾Ṋ̸͓̰͐̈́̋̌̏̐́̕͘̕̚M̵̧̛̬̮̓͂̆̒̽͗̿̇͝E̶͕͔̥̞̬̬̹̣͍͒̀͛̿̂́͒̚N̷̙̞̰̞̖̠͆̏̍̂̈́͋̋́͛̀̚Ţ̷̫͛--"
    e "{i}It's too loud----{/i}"
    md "Excellent, class!"
    e "{i}Great, it's over-{/i}"
    md "Now for the next question-"
    e "{i}NO-{/i}"
    md "Who can name the court case that outlawed species based gerymandering?"
    n "-̶̦͝-̵̢͆ ̶͍͛Ṡ̷͈h̷̦̾a̶̘̚w̸̜̅ ̷̛̪v̶͓̕.̴̫̋ ̷̰̅R̴̻͝u̶̞͌c̸̲̀k̸̻͊é̷̟r̵̢̎-̸̧̾-̸̮̓""
    n "-̷̫̩̪͎̤́̇̑-̷̢̲͆̚ ̵̧̤̻͔͝͝S̵̫̭͓̣̃́̋͜h̶̪̜̺̘́̿͠a̷̭͋̈́̒͝ẇ̵̥̲̮͐͌͘ ̷̦͇̖͔̹͐͋͗͠͝v̸̮̪͉͚̄̇͜͝.̶̰̍ ̴̩͚́̐͝R̵̰̫̩̱̽ú̶̬͕͙̲̄ͅc̸̩̙̫̤̊ḱ̸̫̟̦̥̃̆͗̕e̶̮̒̀̀r̶̰͑-̸̢͙̝͉̍͛̂̄͜-̵̛̠̬̐ͅ""
    n "-̴̡̣͚̳̭̯͔̯̾̌̆͆̋͝͝-̴̧̘̝̹̘̤̐̇̌́̌̄͜ ̶̡̭̟͍̂̍̑͌̂̔́͑̓̕S̷̡̞̗͈̋͗̐ḧ̸͙̪̖̬̼̱̠̺͐̀́͝ͅå̵͕̹͔̮̝̜̰̅̈̓̚͘̕͠w̶̡͈͍͌́͒͝ ̵̈́̀̈̈́̎̓̉͜͝v̶̮͖̰̘̿̈́̑.̶̜̽͠ ̷̨̛̻̤̪͇̯͇͒͑̋͝R̶̗̭͈͗͛̂͆͐̈́̿̄͘ṳ̴̢̧̞̬̥̝̰̍͊͐̃̄͗̊͐̇c̵̭͌͆̀̀͛́̿͆̿k̷̡̘͈͎̤̃̓͝ͅḙ̴͓̎́́͊͋̍̈͠ř̴̡̩͇̰̲͇̪̓͝!̴͕͖͉̹̺̠̥̤̩̟͐͛͛̈́!̶͎̪̟̣͔̇͂̆̈́͝͠-̸̡̘̮̳̩͎̱̗̈́͑-̴̻̺̘̳̺̤͖̻̪̈́""
    e "{i}Shaw.. Shaw v. something.... I'll probably recognize it on the quiz-{/i}"
    md "Now, last question! Who can tell me why the Bill of Rights was established?"
    n "T̶̢̼̜̑̀̈́̎͆̒ö̷͕̗́̏̂ ̴͚̘̣͕̙̩͚͈̒͐̓͒̈́̐͜p̷̧̯͕̟̝̭͇͒̀̈́̏ͅr̷̳̦̹̮͑̏̓͜ò̵͎̍̔̈̈̄̿̔t̷̗͖̓̈́̐͌̑͋͐̈̏̂̈́͋ẻ̴̖̟̞̿͊c̴͖̞̰̦̥̻̝͖͚̔ͅt̵͕̏̐ ̶͕̬̹̾͑̇̏̾̏̍ô̶̩̫̪̲͓̂́̕ù̵͍̞͙̦̠̖̮̣̞́̈̓͋͂̈̎̾̕͜r̵̼̞̜̪͇̺͙͔̖̼͈̠͆̏̔̏̀̂͊ ̴̝̾͒͗ŗ̷̨͈̲͚̘̠̟͎̪̑̏̉͂̂̓̒̔͠ḯ̴̧͍̞͓̹̼͈̞̓̔́̎g̴̫̻̞̘̗̲̱͙͋̅̿̉͗̽͝͝ḧ̵̟́͆͊̈́̓͗̾̆͐t̶͖̻͕̳̔̑̓̀̾͊̓͝ş̴̇̃̕ ̶̙̀̑͐̏͝f̴̜͉̆͗͒r̸̡̧͕̯͍̜̲͓̗̘͆͆́̉̍̾̏͒́͌͘ǫ̸̗͙̩̻͙̟̪̏͆̍m̵̛̗̏̓̒́́̊̊̑͆ ̷̢̡͕̝̅̃̎̄̆́̏̔̕͠t̵̲̱̫͔̦̳̟̞͈̫͓͕͊̀̀̊͒̈́͗͆̐͘h̸͚͖͙̗̯͖̜̆̉̓̐̃̎ẹ̸̘̰̩̱̱̻̯̮͉̫͈̊̈̍̂͗͂ ̶̡̢̞̖͍͙̝͖͙̲̹̽̈͂́͘ç̴̢̛̛̘̲̦̟̭̩̠̤̮̍̂͑́̑̀̈̽͜͝͠ę̸̧̢̟͉̝͖̫̯̱̍̀̂͆̔̀̈́͜n̵̡͕̮̆͐̾ẗ̴̛̛͓͓̹͍̤́̓͐̋̋͐̏r̵̬̭̲͍̮͚̀̈́̒͋̇̀a̵̧̤̥͂̎l̵̛͎͚̣̫̼̮̅̾̊̀̈́͒̄̆̈́̊ ̶̠̩̥̞̜͈̝̮̞̦͇̬̓ĝ̸̜̲̤̗̥̃̈͋̈́͗̍̌̿̚͠ǫ̵̛̋̓̄̍͒̈́̆̀͐̋͝v̶͈͚͛̌̀͒̋͐̓̈́͝e̷̯̒̈́̌̉͐̍̚͠r̵̦̗͈̲͓͉̻͙̼͕͊͑͑̎̂̂́͐̆̉͘̚͜ń̶̛̠̺͔̖̣̳̫̈́͑̾̚m̵̪͓̩̀̋͊̓̓̌̍͆̕ḙ̴̡̛̀ņ̶̗͙̻̼͓̈́̎t̷̢̡̲̦̪͔̦͛͊̆̈́͊͆͊̕ͅ!̶̧̢̯̻͔̈́̉̆̈́̊̌̃̾""
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
