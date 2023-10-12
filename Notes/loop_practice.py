# Loop Practice 
# Author: Roop Jaswal
# Date: October 10, 2023  

# Create a list of groceries 
groceries = ["hot wheels", "lego", "'ice crean", "video games"]

# Do something for each thing in the list 
# Print it out in a pretty way 

import time
import random


for item in groceries: 
    print(f"*{item}")
    print(" ---")


# Create a pyramid like this using a for loop. 

#*
#**
#***
#****
#*****

stars = ["*", "**", "***", "****", "*****","******"]
for row in stars:
    print(row)

# Problem:
# Create a new years eve countdown 
# Requirements:
# * Starts off at 10 
# * Countdown every second 
# * Instead of reaching zero it says "Happy New Year"
# Example Output: 
#   10
#   9
#   8
#   ...
#   1
#   Happy New Year!


countdown = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "HAPPY NEW YEAR!!🥳"]
for timer in countdown:
    print(timer)
    time.sleep(1)