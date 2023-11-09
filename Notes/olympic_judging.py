# Olympic Judging 
# Author: Roop Jaswal
# november 6, 2023

import random
import time

print("Welcome to the 2024 Tokyo Olympics!")

time.sleep(1)

print("Your final score from each judge is...")

list_of_scores =[
    1,
    1.5,
    2,
    2.5,
    3,
    3.5,
    4,
    4.5,
    5.5,
    5,
    6,
    6.5,
    7,
    7.5,
    8,
    8.5,
    9.5,
    9,
    10
]

random_response = random.choice(list_of_scores)

random_response_two = random.choice(list_of_scores)

random_response_three = random.choice(list_of_scores)

random_response_four = random.choice(list_of_scores)

random_resoponse_five = random.choice(list_of_scores)

print(f"Judge 1: {random_response}")

time.sleep(.5)

print(f"Judge 2: {random_response_two}")

time.sleep(.5)

print(f"Judge 3: {random_response_three}")

time.sleep(.5)

print(f"Judge 4: {random_response_four}")

time.sleep(.678)

print(f"Judge 5: {random_resoponse_five}")

print("YOUR FINAL SCORE IS...")

print(f"{(random_response + random_response_two + random_response_three + random_response_four + random_resoponse_five) / 5}. Congrats!")