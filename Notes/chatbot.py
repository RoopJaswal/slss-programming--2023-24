# Chatbot
# Author: Roop
# Date 21 September 2023 

import random
import time

# Greet the user 
# Pause in between lines of dialogue

print ("Hello there! 🤖")
time.sleep(2)

print ("I'm a crude chatbot, here to talk to you")
time.sleep(1.5)

# Get the user's name and store in a variable 
user_name = input("So... what's your name?")

# Respond with the user's name
print (f"It's nice to meet you, {user_name}!")
time.sleep(2)

# Ask the user what their favourite food is 
fave_food = input("What's your favourite food?")

# If they answer pasta, respond with something related 
if fave_food == "pasta":
    print("🍝")
    print("I think i love pasta, too!")
elif fave_food == "burgers" or fave_food == "Burgers":
    print("🍔")
    print("Mmmm. Burgers!")
elif fave_food == "sushi" or "Sushi":
    print("🍣")
    print("Delicious!")
else: 
    # Respoond with something that is not TOO repetitive 
    # Create a list of appropriate responses 
    list_of_fave_food_responses = [
        "Mmmmm. That sounds delicious.",
        f"Yes, {fave_food} is one of my favourites, too!",
        "Cool.",
        "Interesting, I've never tried that before."
    ]

    # Choose one response randomly from the list
    import random 
    random_response = random.choice(list_of_fave_food_responses)

    # Print out the chosen response 
    print(random_response)
    time.sleep(2)

    print(list_of_fave_food_responses[2])
    time.sleep(2)