import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between (1 to {x}: )"))
        if guess < random_number:
            print("Sorry, the number is too low")
        elif guess > random_number:
            print("Sorry, the number is too high")
    print(f"Yes, you have guessed the correct number: {random_number}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        
        feedback = input(f'Is {guess} too high (H), too low(L), or correct (C)'.lower())
        
        if feedback == 'h':
            high =  guess - 1 
        elif feedback == 'l':
            low = guess + 1
    print(f"Yes, the computer has guessed your number correctly {guess}")

computer_guess(1000)
