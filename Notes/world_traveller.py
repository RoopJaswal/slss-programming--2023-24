# World Traveller 
# Author: Roop Jaswal
# Nov 7, 2023

import time
import random

print("Hello there, im curious to see how many places you have visted")

time.sleep(1)

user_name = input("let's get started, can you inform me of your name?")

if user_name == "Roop" or user_name == "roop" or user_name == "Roopy" or user_name == "roopy" or user_name == "King" or user_name == "king":
    time.sleep(.5)
    print("NO WAY! We got the same name that's actually crazyy!")
else:    
    time.sleep(.76)
    print(f"Sick name, {user_name}")
    time.sleep(1)


continents_visted = 0

print(f"To start {user_name}, we will see how many continents you have been")

time.sleep(.6843543542)

print("Before we start please answer only in yes or no answers please")

asia = input("Have you been to Asia?").lower().strip(",.?! ")

time.sleep(.75)

europe = input("Have you been to Europe?").lower().strip(",.?! ")

time.sleep(.75)

north_america = input("Have you been to North America?").lower().strip(",.?! ")

time.sleep(.75)

south_america = input("Have you been to South America?").lower().strip(",.?! ")

time.sleep(.75)

australia = input("Have you been to Australia?").lower().strip(",.?! ")

time.sleep(.75)

africa = input("Have you been to Africa?").lower().strip(",.?! ")

time.sleep(.75)

antartctica = input("Have you been to Antarctica?").lower().strip(",.?! ")

time.sleep(.75)

if asia in ["yes", "sure", "yea", "yeah", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if north_america in ["yes", "sure", "yea", "yeah", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if south_america in ["yes", "sure", "yea", "yeah", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if europe in ["yes", "sure", "yea", "yeah", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if australia in ["yes", "sure", "yea", "yeah", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if africa in ["yes", "sure", "yea", "yeah", "yes please"]:
    time.sleep(1)
    continents_visted += 1

if antartctica in ["yes", "sure", "yea", "yeah", "yes please"]:
    continents_visted += 1

print(f"I see, you have been to {continents_visted}/7, very cool!")