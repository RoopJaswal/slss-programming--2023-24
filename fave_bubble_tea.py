# Bubble Tea Popular Algorithm
# Author: Roop Jaswal
# Date: October 30 2023

# Ask 5 users what their favourite bubble tea place is
# Print out a summary of the data

NUM_RESPONDENTS = 5

coco_likes = 0
chatime_likes = 0
suntea_likes = 0
xingfutang_likes = 0
bubble_queen_likes = 0

for _ in range(NUM_RESPONDENTS): 
        
    # Ask the user what their favourite bbt place is 
    print("What's your favourite bubble tea place?")
    fave_bubbletea = input().strip(",.?").lower()

    # Tallying/Counting Algorithm
    # Options: Coco, Chatime, Sun Tea, Xing Fu Tang, Bubble Queen
    # If they say Coco, increase the counter by one
    if fave_bubbletea == "coco": 
        coco_likes = coco_likes + 1
    elif fave_bubbletea == "chatime": 
        chatime_likes += 1            # short operand, increasing the chatime + gets one
    elif fave_bubbletea == "suntea": 
        suntea_likes += 1 
    elif fave_bubbletea == "xingfutang":
        xingfutang_likes += 1
    elif fave_bubbletea == "bbqueen": 
        bubble_queen_likes += 1


        # Print a summary of the results
print(coco_likes: 2f)

