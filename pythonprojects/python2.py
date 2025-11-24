import random
import string

def generate_password():
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters (yes/no): ").strip().lower()
    include_special = input("Include special characters? (yes/no): ").strip().lower()
    include_digits = input("Include digits? (yes/no): ").strip().lower()
    
    if length < 4:
        print("Password length is insecure")
        return

    lower = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation if include_special == "yes" else ""
    digits = string.digits if include_digits == "yes" else ""
    
    all_characters = lower + uppercase + special + digits
    
    required_characters = []
    if include_uppercase == "yes":
        required_characters.append(random.choice(uppercase))
    if include_special == "yes":
        required_characters.append(random.choice(special))  # Fixed: was uppercase
    if include_digits == "yes":
        required_characters.append(random.choice(digits))
    
    remaining_length = length - len(required_characters)  # Fixed: was "length = len(...)"
    password = required_characters[:]
    
    for _ in range(remaining_length):
        character = random.choice(all_characters)
        password.append(character)
    
    random.shuffle(password)
    str_password = "".join(password)
    return str_password  # Return the password string

# Call the function and print result
password = generate_password()
print(password)
