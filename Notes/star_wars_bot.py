# Star Wars Bot
# Author: Roop Jaswal 
# October 16, 2023 

import time 
import random 

# Greet the user 
print("Hello there fellow spacewalker, my name is Star Bot")
time.sleep(2.5)
print("I am here to inform you of the path you are destined to take")
time.sleep(2.5)
# Ask if their favourite colour is red 
print("The start to choosing your faith begins with these 2 questions")
time.sleep(2.5)
fave_colour = input("Does the colour red happen to be your favourite colour?")
time.sleep(2.5)

# Ask user if they like capes
opinion_cape = input("Do you by any chance like capes?")
time.sleep(2.5)

if opinion_cape.lower().strip("!?,.") == "yes" or opinion_cape.lower().strip("!?,.") == "yup" or opinion_cape.lower().strip("!?,.") == "yea":
    print("YOU ARE DESTINED TO BE ON THE DARK SIDE!!")

else: print("YOU ARE DESTINED TO JOIN THE LIGHT SIDE!!")
time.sleep(1.5)
print("I am wishing you the best of luck on your adventure")