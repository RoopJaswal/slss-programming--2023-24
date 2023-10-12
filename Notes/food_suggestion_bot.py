# Food Suggestion Bot
# Author: Roop Jaswal
# Date: October 6, 2023 

# A bot that asks the user what their favourite 
# food is. The bot identifies the type?cuisine 
# of the food and offer a suggestion for a restaurant 

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is 
print("Hello, I am here to suggest a restaurant to you.")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, tell me what your favourite food is.")
time.sleep(1)



# If they answer with an Italian dish 
# Suggest an Italian Restaurant 
# List all the Italian dishes
italian_food = ["pizza", "pasta", "canneloni", "tiramisu"]

if fave_food .lower().strip(",.?!") in italian_food:
    print("I think that you may like Italian food🍝")
  
if fave_food == "pizza" or fave_food == "pasta" or fave_food == "tiramisu":
    time.sleep(1)
    print("I suggest Bella Roma Italian Ristorante Richmond")
    time.sleep(1)
    print("You can find the address below")
    print("8368 Alexandra Rd, Richmond")

  
else: 
    print("Sorry, I don't recognize your favourite food")
    time.sleep(1.5)
    print("The algorithm is still being worked on")
    time.sleep(1.5)
    print(" I can't offer a good suggestion for you")
    
