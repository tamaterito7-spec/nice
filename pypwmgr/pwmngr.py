from cryptography.fernet import Fernet

def write_key():
    """Generate and save a new encryption key."""
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """Load the encryption key from file."""
    try:
        with open("key.key", "rb") as file:
            return file.read()
    except FileNotFoundError:
        print("Key file not found. Generating new key...")
        write_key()
        with open("key.key", "rb") as file:
            return file.read()

# Initialize key and Fernet
try:
    master_pwd = input("What is the master password? ")
    key = load_key() + master_pwd.encode()  # Convert master_pwd to bytes
    fer = Fernet(key)
except ValueError:
    print("Invalid key format. Please ensure the master password is correct.")
    exit()

def view():
    try:
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                line = line.rstrip()
                if not line:  # Skip empty lines
                    continue
                try:
                    user, passw = line.split(":")
                    decrypted_pwd = fer.decrypt(passw.encode()).decode()
                    print(f"User: {user}, Password: {decrypted_pwd}")
                except ValueError:
                    print(f"Invalid entry format for line: {line}")
                except Exception as e:
                    print(f"Error decrypting password for {user}: {e}")
    except FileNotFoundError:
        print("No passwords file found. Add some passwords first!")

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open("passwords.txt", "a") as f:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()  # Encode to bytes, encrypt, then decode to string
        f.write(f"{name}:{encrypted_pwd}\n")

while True:
    mode = input("(v)iew, (a)dd or (q)uit? ")
    if mode == "q":
        break
    if mode == "v":
        view()
    elif mode == "a":
        add()
    else:
        print("Invalid selection.")
