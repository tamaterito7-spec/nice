import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input.")

max_score = 50
player_scores = [0 for _ in range(players)]
game_over = False  # Flag to track game status

while max(player_scores) < max_score and not game_over:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over.")
                current_score = 0  # Reset turn score
                break  # End the turn
            else:
                current_score += value
                print(f"You rolled a {value}")
                print(f"Your turn score is: {current_score}")

        if player_scores[player_idx] + current_score >= max_score:
            player_scores[player_idx] = max_score  # Set score to exactly max_score
            print(f"Your total score is: {player_scores[player_idx]}")
            print(f"\nPlayer {player_idx + 1} wins with a score of {player_scores[player_idx]}!")
            game_over = True  # Set flag to end the game
            break  # Exit the for loop
        else:
            player_scores[player_idx] += current_score
            print(f"Your total score is: {player_scores[player_idx]}")
    if game_over:
        break  # Exit the while loop if game is over
