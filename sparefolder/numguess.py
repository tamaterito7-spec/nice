import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))  # <- ADDED ": " for clarity
        print(f"You guessed: {guess}")  # <- IMPROVED PRINT
        
        if guess < random_number:
            print("Too low!")
        elif guess > random_number:
            print("Too high!")
        else:
            print("CORRECT! 🎉")
            break  # <- ADDED to exit loop
    
    print(f"The number was {random_number}")

guess(10)  # Runs immediately when you execute
