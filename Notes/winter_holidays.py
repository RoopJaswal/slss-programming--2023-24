# Winter Holidays 
# Author: Roop Jaswal 
# Jan 8, 2024 

# Requirements 
# - create a function called winter_holiday()
# - take one parameter 
#       - string
# - return a summary of an event from your holidays 

import random


def winter_holidays(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
    
    Params:
        good_or_bad - indicate what kind of event to summarize
    
    Returns:
        an event that happened during the holidays; the event is selected randomly based on the parameter"""
    
    
    if good_or_bad.lower() == "good":
        winter_events = [
            "I recieved a xbox series x from my uncle",
            "I got gifted a new monitor from my uncle",
            "I went to cousin's house in Seattle to celebrate New Years",
            " It was fill with lots of sleep, basketball, and video games with friends"]
        return random.choice(winter_events)
    elif good_or_bad.lower() == "bad":
        winter_events = [
            "I didn't get to celebrate New Year's with my brother",
            "I lost a lot of free time working on university applications"
            "I was not able to snowboard due to lack of snow"
        ]
        return random.choice(winter_events)
    else:
        return "Sorry I only take good or bad events."
# Ask user for their winter break events/summary
user_input = input("Was your winter holiday experience good or bad? ").strip().lower()
# Get a random event based on the user input
print(winter_holidays(user_input))









