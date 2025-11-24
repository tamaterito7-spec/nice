import random
import string

def generate_password():
    # ---------- 1. Collect user preferences ----------
    length = int(input("Enter the desired password length: ").strip())
    include_uppercase = input("Include uppercase letters (yes/no): ").strip().lower()
    include_special   = input("Include special characters? (yes/no): ").strip().lower()
    include_digits    = input("Include digits? (yes/no): ").strip().lower()

    # ---------- 2. Basic validation ----------
    if length < 4:
        print("Password length is insecure (minimum 4)")
        return None

    # ---------- 3. Build character pools ----------
    lower   = string.ascii_lowercase                     # always included
    upper   = string.ascii_uppercase if include_uppercase == "yes" else ""
    special = string.punctuation     if include_special   == "yes" else ""
    digits  = string.digits          if include_digits    == "yes" else ""

    all_chars = lower + upper + special + digits

    # If the user turned *everything* off, we still need something to pick from
    if not all_chars:
        print("You must allow at least one character type.")
        return None

    # ---------- 4. Guarantee at least one of each requested type ----------
    password = []                                   # list of chars (mutable)
    required = 0

    if include_uppercase == "yes" and upper:
        password.append(random.choice(upper))
        required += 1
    if include_special == "yes" and special:
        password.append(random.choice(special))
        required += 1
    if include_digits == "yes" and digits:
        password.append(random.choice(digits))
        required += 1

    # ---------- 5. Fill the rest of the length ----------
    remaining = length - required
    if remaining < 0:                               # user asked for more required chars than length
        print(f"Requested {required} required characters but length is only {length}.")
        return None

    for _ in range(remaining):
        password.append(random.choice(all_chars))

    # ---------- 6. Shuffle so required chars aren't always at the start ----------
    random.shuffle(password)

    # ---------- 7. Return the final string ----------
    return "".join(password)


# --------------------- CALL THE FUNCTION ---------------------
if __name__ == "__main__":
    pwd = generate_password()
    if pwd:
        print("Generated password:", pwd)
