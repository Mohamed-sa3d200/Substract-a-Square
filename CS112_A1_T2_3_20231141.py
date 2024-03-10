# CS112_A1_T2_3_20231141
# This is a two-player game starts with assigning number of coins. each player must choose a square number of coins to take . the player who take the last coin wins
# Mohamed Saad Taha Mohamed
# 20231141

import math # Math library includes square root (sqrt) function

# Function that checks if submitted number is a square number
def is_square(sq_num):
    if sq_num <= 0:
        return 0
    root = int(math.sqrt(sq_num))
    return root * root == sq_num

# Welcome message, start game and game status
print("Welcome to Subtract a Square! This is a two-player game.")
choice = input("If you want to start, press 'q': ")
# Game
while choice.lower() == 'q':
    score = int(input("Enter the initial score: "))
    while score <= 0:
        score = int(input("Invalid input, Enter positive score: "))
    while score > 0:
        # Player 1 turn
        num = int(input("Player 1, enter a square number: "))
        while (not is_square(num)) or (num >= score):
            num = int(input("Invalid input. Enter a small positive square number: "))
        score -= num
        if score <= 0:
            print("Player 1 has won this game!")
            break

        # Player 2 turn
        num2 = int(input("Player 2, enter a square number: "))
        while (not is_square(num2)) or (num2 >= score):
            num2 = int(input("Invalid input. Enter a small positive square number: "))
        score -= num2
        if score <= 0:
            print("Player 2 has won this game!")
            break

    # Continue playing or exit
    continue_choice = input("If you want to continue playing, press 'q'. Otherwise, enter any other key: ")
    if continue_choice.lower() != 'q':
        break