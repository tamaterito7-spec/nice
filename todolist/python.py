import json
from pathlib import Path

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    if Path(filename).exists():
        with open(filename, 'r') as f:
            return json.load(f)
    return []

# --- Main Program ---
FILENAME = "mytodos.json"

print("Welcome to Your To-Do List!")
todos = load_from_json(FILENAME)

while True:
    print("\n" + "="*30)
    print("Your Tasks:")
    if todos:
        for i, task in enumerate(todos, 1):
            print(f"  {i}. {task}")
    else:
        print("  (No tasks yet!)")

    print("\nOptions:")
    print("1. Add a task")
    print("2. Quit")

    choice = input("\nChoose (1 or 2): ")

    if choice == "1":
        new_task = input("What do you need to do? ")
        todos.append(new_task)
        save_to_json(todos, FILENAME)
        print("Task saved!")
    elif choice == "2":
        print("Goodbye! Your tasks are saved.")
        break
    else:
        print("Please pick 1 or 2.")