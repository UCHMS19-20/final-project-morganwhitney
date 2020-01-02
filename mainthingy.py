name = input("What is your name?")
import sys

def wakeup(): 
    wakeup_options = {1:"Hit snooze",
     2:"Turn the alarm off, you'll wake up on time naturally",
     3:"Drag yourself out of bed, a little exhaustion never hurt anyone."}
    for k,v in wakeup_options:
        print(f"{k}: {v}")
    user_choice_w = input("Which would you like to do? Choose 1, 2, or 3.")
    if user_choice_w == 2:
        print("We both know that never works. You overslept and missed your bus. Since mom is at work already, you have to stay home today and miss your physics test.")
        sys.exit
    if user_choice_w == 1:

    

