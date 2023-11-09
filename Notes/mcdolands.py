# Mcdoland's Order 
# Author: Roop Jaswal
# November 6, 2023 

import time
import random

print("Welcome to mcdolands, I am here to take your order!")

time.sleep(2)

burger_price = input("Would you like a very tasty burger for only 5 bucks?").lower().strip(",.?! ")

fries_price = input("What about some peri peri fries for as little as 3 bucks!").lower().strip(",.?! ")

total_price = 0

# If they want a burger
if burger_price in ["yes", "sure", "yea", "yeah", "yes please", "yup"]:
    time.sleep(1.5)
    # add a burger to their total_price
    total_price += 5

if fries_price in ["yes", "sure", "yea", "yeah", "yes please", "yup"]:
    time.sleep(1.5)
    # add fries to their total_price
    total_price += 3


# Calculate the total price with taxes
print(f"Your total price is ${total_price * 1.14}!")
time.sleep(.5)
print("How would you like to pay?")

