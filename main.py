 #wakeup
print ("It's 5 am. Your alarm goes off, waking you up after a mere 4 and a half hours of sleep.")
wakeup_options = ["   1: Hit snooze",
"   2: Turn the alarm off, you'll wake up on time naturally",
"   3: Drag yourself out of bed, a little exhaustion never hurt anyone."]
for choice in wakeup_options:
    print(choice)
user_choice_w = int(input("Which would you like to do? Choose 1, 2, or 3."))
wchoice1 = "You hit snooze. Your alarm goes off at 6:40 and you wake up, but your mom yells at you for being late"
wchoice2 = "We both know that never works. You overslept and missed your bus. Since mom is at work already, you have to stay home today and miss your physics test."
wchoice3 = "You make breakfast and by the time you're done, you feel fully awake"
if user_choice_w == 1:
    wresult = wchoice1
    print(wresult)
if user_choice_w == 2:
    wresult = wchoice2
    print(wresult)
    exit()
if user_choice_w == 3:
    wresult = wchoice3
    print(wresult)

#sans
if wresult == wchoice1:
    print ("Still half asleep, you arrive at school. You stumble into Mr. Sanservino's class and take a seat.After sitting in awkward silence for a few minutes, he stands up and takes a breath. You know what's coming: a pop quiz.Since your brain is still cloudy from your late awakening, you get a 60 on the quiz.")
if wresult == wchoice3:
    print ("Fully awake and not in the worst mood of your life, you get to Mr. Sanservino's room. You sit in your chair and wallow in the uncomfortable silence. Is a quiz coming? You hope not. He stands up and tells you you're watching a movie. The whole class sighs in relief. The movie sucks, but it's better than history.")

#tech
print ("You leave Sanservino and make your way down the hall to tech. You get to class and sit down. You have the period to work uninterrupted on your project, but you're mostly done and there's plenty of time before it's due. Do you: ")
tech_options = ["   1: Work on your project. Sure, you have time. but it's better to get it out of the way.",
"   2: Talk to your friends. They always have something interesting to say, and you have a few weeks. Besides, who likes sitting in silence?",
"   3: Take a nap. You know you want to."]
for choice in tech_options:
    print(choice)
user_choice_t = int(input("So what's it gonna be? 1, 2, or 3?"))
tchoice1 = "You put in your headphones and get to work. Before you know it, the period is over and you were more prodictive than expected. If you keep this up, maybe you'll be done by next class :)"
tchoice2 = "You sit back and talk to your friends about what's been going on with your life. The period drags on for longer than you thought it would, but at least you had a (mostly) productive conversation? Your project is still in the back of your mind, eating away at you because you know it'll be due someday and when it is you'll have to actually do it."
tchoice3 = "Dude. Why? naps have never really agreed with you, so when you finally wake up, you're a groggy disaster and you regret all of your life decisions. Man, I gotta stop taking naps."
if user_choice_t == 1:
    tresult = tchoice1
    print (tresult)
if user_choice_t == 2:
    tresult = tchoice2
    print (tresult)
if user_choice_t == 3:
    tresult = tchoice3
    print (tresult)

#co
if tresult == tchoice3:
    print ("You manage to get it together during co. You don't have lab together, which gives you the time to collect yourself and really wake up in time for physics.")
if tresult == tchoice1 or tchoice2:
    print("Co passes quickly, but it always does. Nothing special happens. You walk to phsyics with your friends and prepare yourself emotionally.")

#physics
print ("You sit down in physics. Today you're mostly doing review problems, which you don't really want to do. Do you: ")
physics_options = ["   1: Suck it up and do the problems. Sure, you know how to do them by now, but it's good to have the practice",
"   2: Zone out. You can kinda listen so it's like you're paying attention, but you don't have to be too bored for 83 minutes.",
"   3: Take a nap. That's always a good idea"]
for choice in physics_options:
    print(choice)
user_choice_p = int(input("What's the plan? 1, 2, or 3?"))
pchoice1 = "Like a good student, you do the problems. Yeah, you'd rather be sleeping, but you'll pass the test."
pchoice2 = "The period drags on, but it's better than doing the problems I guess? You wind up half asleep by the end of the period."
pchoice3 = "Bruh. Naps are bad for you. You can't keep taking naps. You hate naps. Stop."
if user_choice_p == 1:
    presult = pchoice1
    print (presult)
if user_choice_p == 2:
    presult = pchoice2
    print (presult)
if user_choice_p == 3:
    presult = pchoice3
    print (presult)

#math
print ("Math time! You like math, so you know this period is gonna be fine.")
mopt1 = "You're still in a productive mood from physics so you take good notes. It's the last period of the day, and it's a good end to it."
mopt2 = "You're a little drowsy, but it's hard to be in a bad mood with Mrs. Draesel teaching, let's be honest. You end up being productive."
mopt3 = "Or at least it would be if you hadn't taken this nap. You're still tired from your nap. Why do you ever nap? Please. Stop. You're exhausted."
if user_choice_p == 1:
    mresult = mopt1
    print (mresult)
if user_choice_p == 2:
    mresult = mopt2
    print (mresult)
if user_choice_p == 3:
    mresult = mopt3
    print (mresult)

#dinner
print ("You've made it home! You have a lot of homework to do because you're a magnet student, but you have three hour practice tonight. Do you: ")
dinner_options = ["   1: Eat dinner. Sure, you have homework, but it's a bad idea to not eat. You can do the work later.",
"   2: Grab a protein bar and do the work. You'll be a little hungry during practice, but you'll live.",
"   3: Ignore dinner you don't need food. Live love magnet."]
for choice in dinner_options:
    print(choice)
user_choice_d = int(input("So what's it gonna be? 1, 2, or 3?"))
dchoice1 = "You eat dinner so you're ready for practice. You manage to get some of the work done too, so later you'll be on the right track."
dchoice2 = "You grab a protein bar and get to work. You don't finish, but you'll have enough time later."
dchoice3 = "You grind for a bit and get work done. You're hungry, though."
if user_choice_d == 1:
    dresult = dchoice1
    print (dresult)
if user_choice_d == 2:
    dresult = dchoice2
    print (dresult)
if user_choice_d == 3:
    dresult = dchoice3
    print (dresult)

#rehearsal
print ("You make it to practice, excited to get work done. This is your favorite part of the day :).")
rchoice1 = "You get to learn more of your show. The work you get is fun, and you're excited to see how the final product is."
rchoice2 = "So turns out a granola bar isn't enough dinner. During basics you get dizzy and have to sit down. A friend had food, so you eat some and get back to normal. You're still kinda out of it for the rest of the practice."
rchoice3 = "You messed up. During basics, you pass out. Eat dinner next time, man."
if user_choice_d == 1:
    rresult = rchoice1
    print (rresult)
if user_choice_d == 2:
    rresult = rchoice2
    print (rresult)
if user_choice_d == 3:
    rresult = rchoice3
    print (rresult)

#bedtime
print ("You've had quite the day. When you get home, you finish up the rest of your homework. You're tired now. Do you: ")
bed_options = ["   1: Go to bed before 10pm. You have to wake up early tomorrow.",
"   2: Stay up late watching Netflix. You'll still go to bed before midnight, though",
"   3: Stay up until 2am. You'll wake up and it'll all be fine nothing matters."]
for choice in bed_options:
    print(choice)
user_choice_b = int(input("So what's it gonna be? 1, 2, or 3?"))
bchoice1 = "Good for you, getting to bed. You get a good night's sleep and you'll wake up well rested."
bchoice2 = "You watch a few episodes before you force yourself to go to bed. You'll get less sleep than you need, but it's fine."
bchoice3 = "Why would you do this to yourself? You definitely don't get enough sleep. Be better."
if user_choice_b == 1:
    bresult = bchoice1
    print (bresult)
if user_choice_b == 2:
    bresult = bchoice2
    print (bresult)
if user_choice_b == 3:
    bresult = bchoice3
    print (bresult)