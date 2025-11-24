import random

user_score = 0
computer_score = 0
WINNING_SCORE = 5  # Set the target score to win

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        if d1 > d2:
            user_score += 1
            print(f"User wins this round! ({d1} vs {d2})")
        elif d1 == d2:
            print(f"Draw! ({d1} vs {d2})")
        else:
            computer_score += 1
            print(f"Computer wins this round! ({d1} vs {d2})")
        print(f"User score: {user_score}")
        print(f"Computer score: {computer_score}")
        
        # Check for winner
        if user_score >= WINNING_SCORE:
            print(f"Congratulations! You won with {user_score} points!")
            break
        elif computer_score >= WINNING_SCORE:
            print(f"Game Over! Computer won with {computer_score} points!")
            break
    elif choice == 'n':
        print("Farewell!")
        break
    else:
        print('Not a valid selection.')
