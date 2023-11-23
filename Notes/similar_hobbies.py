# Similar Hobbies
# Author: Roop Jaswal 
# Nov 17, 2023 

person1_fav_hobbies = input("Hello there, what are your top 4 hobbies? please seperate them with spaces!").lower().split(" ")

person2_fav_hobbies = input("Hello there, what are your top 4 hobbies? please seperate them with spaces! ").lower().split(" ")


print(f"Person 1: {person1_fav_hobbies}")
      
print(f"Person 2: {person2_fav_hobbies}")
      


similarity_score = 0

for hobby in person1_fav_hobbies:
    if hobby in person2_fav_hobbies:
        similarity_score += 1 

print(f"You have {similarity_score} hobbies in common!")
