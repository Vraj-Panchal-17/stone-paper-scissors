# SIMPLE GAME
'''
1 = Stone
2 = Paper
3 = Scissors
'''

import random  # importing random module to let computer choose randomly

# Computer randomly picks a number between 1, 2, and 3
computer_choice = random.choice([1, 2, 3])

# Taking user input (1, 2, or 3)
user_choice = int(input("Enter your choice (1 = Stone, 2 = Paper, 3 = Scissors): "))

# Dictionary to convert numbers into words
reverse_dict = {1: "Stone", 2: "Paper", 3: "Scissors"}

# Showing what user and computer selected
print(f"You choose: {reverse_dict[user_choice]}")
print(f"Computer choose: {reverse_dict[computer_choice]}")

# Checking game result:
# If both choose the same --> Draw
if computer_choice == user_choice:
    print("It's a draw")

# Winning conditions:
# 1.Paper beats Stone
# 2.Scissors beats Paper
# 3.Stone beats Scissors
elif (computer_choice == 1 and user_choice == 2) or \
     (computer_choice == 2 and user_choice == 3) or \
     (computer_choice == 3 and user_choice == 1):
    print("You win!")

# If not draw and not win --> user loses
else:
    print("You lose!")
