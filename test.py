 #wakeup
print ("It's 5 am. Your alarm goes off, waking you up after a mere 4 and a half hours of sleep.")
wakeup_options = ["1: Hit snooze",
"2: Turn the alarm off, you'll wake up on time naturally",
"3: Drag yourself out of bed, a little exhaustion never hurt anyone."]
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
print ("You get to tech and sit down. You have the period to work uninterrupted on your project, but you're mostly done and there's plenty of time before it's due. Do you: ")
tech_options = ["1: Work on your project. Sure, you have time. but it's better to get it out of the way.",
"2: Talk to your friends. They always have something interesting to say, and you have a few weeks. Besides, who likes sitting in silence?",
"3: Take a nap. You know you want to."]
for choice in tech_options:
    print(choice)
user_choice_t = int(input("So what's it gonna be? 1, 2, or 3?"))