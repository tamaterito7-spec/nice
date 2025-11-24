def get_choice(prompt, valid_options, allow_quit=False):
    """Get validated user input from a list of options. Loops until valid."""
    options_str = "/".join(valid_options)
    quit_option = " or q to quit" if allow_quit else ""
    while True:
        choice = input(f"{prompt}\n(Enter {options_str}{quit_option}): ").lower().strip()
        if allow_quit and choice == "q":
            return None  # Signal quit
        if choice in valid_options:
            return choice
        print(f"Invalid option. Please choose from: {options_str}.")

# Main game
name = input("Type your name: ")
print(f"Welcome, {name}, to our land!")

# First choice
direction = get_choice(
    "You are on a dirt road, ahead the road has come to an end...",
    ["left", "right"]
)

if direction == "left":
    # River path
    river_choice = get_choice(
        "There is a raging river ahead.",
        ["yes", "no"]
    )
    if river_choice == "yes":
        print("You swam across, but the current carried you out to sea...\nGame over.")
    elif river_choice == "no":
        print("As you turn back, you hear screams—people sprinting toward the water in fear!\n"
              "They trample you in the chaos, and you are met by your end...\nGame over.")
    else:  # Shouldn't reach here, but safety
        print("Invalid choice. Game over.")

elif direction == "right":
    # Forest path
    print("You head right into a dense forest.\n"
          "Suddenly, you stumble upon a hidden treasure chest!\nYou win!")

print("Thanks for playing!")
