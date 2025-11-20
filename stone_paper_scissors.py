# SIMPLE GAME
'''
1 = Stone
2 = Paper
3 = Scissors
'''

import random

computer_choice = random.choice([1, 2, 3])
user_choice = int(input("Enter your choice (1 = Stone, 2 = Paper, 3 = Scissors): "))

reverse_dict = {1: "Stone", 2: "Paper", 3: "Scissors"}

print(f"You choose: {reverse_dict[user_choice]}")
print(f"Computer choose: {reverse_dict[computer_choice]}")

if computer_choice == user_choice:
    print("It's a draw")

elif (computer_choice == 1 and user_choice == 2) or \
     (computer_choice == 2 and user_choice == 3) or \
     (computer_choice == 3 and user_choice == 1):
    print("You win!")

else:
    print("You lose!")
