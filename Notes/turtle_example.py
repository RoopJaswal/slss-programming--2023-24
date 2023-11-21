# Turtle Example 
# Author: Roop Jaswal 
# November 21, 2023

import turtle 

# --- CONSTANTS
TURTLE_MAGNITUDE = 50


# Create a turtle
michaelangelo = turtle.Turtle()

# Get some instructions from the user 
print("""To give commands, type: 
F - to go forward
L - to go left
R - to go right""")

# Repeat the below code INDEFINITELY
done = False

while not done:
    command = input("Where should I go?").strip(".,?! ").lower()

    # Based on those insturctions, move the turtle
    # on the screen

# If the user says stop, quit the loop 

    if command.strip(",.?! ").lower() == "f":
        michaelangelo.forward(TURTLE_MAGNITUDE)
    elif command in ["l", "left"]:
     michaelangelo.left(90)
    elif command in ["r", "right"]:
        michaelangelo.right(90)
    elif command in ["b", "backward"]: 
        michaelangelo.backward(TURTLE_MAGNITUDE)
    elif command == "stop":
       done = True


