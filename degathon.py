print("        DEGATHON        ")
print("************************")
print("     1. Play game       ")
print("     2. Quit game       ")

menu_choice = int(input("\n     Select option: "))
username = input("     Username? ")
game_over = "Game over!"

if menu_choice != 1:
	quit()

while True:
		print("\n************************")
		answer = input("\nYou arrive at the end of a road, \n ahead is a house, which way? (N, S, W, E): ")
		if answer == "N":
			print("The house is worn down, with a glass of milk inside, \n heading back out you face the road.")
		if answer == "W":
			print("The world seems to fall short here.")
		if answer == "E":
			answer = input("You find yourself at the edge of a river, swim? (Y/N): ")
			if answer == "Y":
				print("You were swept away by the current, you hear the screams of people behind you.")
				print(game_over)
				break
			elif answer == "N":
				print("You decide to back away...")
		if answer == "S":
			print("There is a town infront of you, from where you left.")
			answer = input("(N, S, W, E (?)): ")
			if answer == "N":
				print("You are scolded and have to leave...")
			elif answer == "S":
				print("You walk back to where you started this journey")
			if answer == "W":
				answer = input("You find yourself in a lush forest...\nPick an apple? (Y/N): ")
				if answer == "Y":
					print("You were poisoned and fall to the ground with your heart clamping.")
					print(game_over)
					break
				elif answer == "N":
					print("There was something off about the colour of that apple...")
			if answer == "E":
				answer = input("There is an abandoned coal mine here...\nEnter the mine? (Y/N): ")
				if answer == "Y":
					print("You stumble into the mine...\n It smells terrible in here.")
					answer = input("Light a match? (Y/N): ")
					if answer == "Y":
						print("You saw a brief flash for a moment...")
						print(game_over)
						break
				if answer == "N":
					input("Which way from here? (N, S, W, E): ")
					if answer == "N":
						print("You see some light and head towards it,\n stepping out of the cave you see your house")
						print("Game won!")
					if answer == "S":
						print("The entrance collapses along with the rest of the mine...")
						print(game_over)
					if answer == "W":
						print("You fall down a mineshaft instantly exploding upon impact")
						print(game_over)
					if answer == "E":
						print("You bump your head...")


