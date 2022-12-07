"""1.assign random number
2.guess a number
3.check if the number is low or high
4.correct number then print the number and stop """

import random

def user(x):
    user = 0
    random_num = random.randint(1,x)

    while user != random_num:
        user = int(input(f"Guess a number between 1 and {x}: "))
        if user < random_num:
            print("Sorry the number is too low")
        elif user > random_num:
            print("Sorry the number is too high")
    print(f"YAY you have guessed the number correctly, {random_num}")

# user(25)

# def computer_guess():
