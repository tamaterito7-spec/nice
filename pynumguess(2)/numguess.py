import random
import time
import sys

number_to_guess = random.randint(1, 100)

def loading_animation(duration=1):
    """Display a loading animation for the specified duration."""
    animation = [":[/]:", ":[-]:", ":[\\]:", ":[|]:"]
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{animation[i % 4]}")  # Print animation character
        sys.stdout.flush()  # Ensure immediate display
        time.sleep(0.1)  # Short delay between characters
        i += 1
    sys.stdout.write("\r")  # Clear the animation line
    sys.stdout.flush()

while True:
	try:
		guess = int(input("Guess the number between 1-100: "))
		loading_animation(1)
		if guess < number_to_guess:
			print("Too low!")
		elif guess > number_to_guess:
			print("Too high!")
		else:
			print("Number was correctly guessed!")
			break
	except ValueError:
		print("Must be a number.")


# Loop
# Generate a random number
# Ask for a guess
# If not valid:
#	Print "error"
# If number < guess:
#	Print "too low"
# If number > guess:
#	Print "too high"
# Else:
#	Print "well done"
