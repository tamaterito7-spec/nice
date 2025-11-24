import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"] 

while True:
	user_input = input("Type Rock/Paper/Scissors, otherwise Q to quit: ").lower()
	if user_input == "q":
		break
	
	if user_input not in options:
		continue
		
	random_number = random.randint(0, 2)
	# rock: 0, paper: 1, scissors: 2
	computer_pick = options[random_number]
	print("Computer choose", computer_pick + ".")
	
	if user_input == "rock" and computer_pick == "scissors":
		print("Success!")
		user_wins += 1

	elif user_input == "paper" and computer_pick == "rock":
		print("Success!")
		user_wins += 1

	elif user_input == "scissors" and computer_pick == "paper":
		print("Success!")
		user_wins += 1

	else: 
		print("Fail!")
		computer_wins += 1

print("Your score is", user_wins)
print("Computer score is", computer_wins)

print("Goodbye!")
		
		
