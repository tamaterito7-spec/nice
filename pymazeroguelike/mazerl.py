import os
import random

# Terminal clear command
def clear():
    os.system("clear" if os.name == "posix" else "cls")

# --- Maze Generation ---
def generate_maze(width, height):
    # Initialize all walls
    maze = [["#" for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width-1 and 1 <= ny < height-1 and maze[ny][nx] == "#":
                maze[ny - dy//2][nx - dx//2] = " "
                maze[ny][nx] = " "
                carve(nx, ny)

    # Start carving from random odd coordinates
    start_x, start_y = random.randrange(1, width, 2), random.randrange(1, height, 2)
    maze[start_y][start_x] = " "
    carve(start_x, start_y)
    return maze

# --- Setup Game ---
WIDTH, HEIGHT = 21, 15
maze = generate_maze(WIDTH, HEIGHT)

# Find random floor for player start and exit
def random_floor():
    while True:
        y, x = random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2)
        if maze[y][x] == " ":
            return x, y

player_x, player_y = random_floor()
exit_x, exit_y = random_floor()
maze[player_y][player_x] = "O"
maze[exit_y][exit_x] = "X"

# --- Player and Enemy Setup ---
player = {"hp": 10, "xp": 0, "level": 1}
enemies = []

def place_enemies(count=6):
    for _ in range(count):
        ex, ey = random_floor()
        enemies.append({"x": ex, "y": ey, "hp": 3})
        maze[ey][ex] = "E"

place_enemies()

# --- Gameplay Functions ---
def draw():
    clear()
    for row in maze:
        print("".join(row))
    print(f"\nHP: {player['hp']}  XP: {player['xp']}  Level: {player['level']}")

def fight_enemy(x, y):
    enemy = next((e for e in enemies if e["x"] == x and e["y"] == y), None)
    if not enemy:
        return
    while enemy["hp"] > 0 and player["hp"] > 0:
        enemy["hp"] -= random.randint(1, 3)
        player["hp"] -= random.randint(0, 2)
    if player["hp"] <= 0:
        draw()
        print("\n💀 You were defeated!")
        exit()
    print("\n⚔️ You defeated an enemy! +5 XP")
    player["xp"] += 5
    enemies.remove(enemy)
    maze[y][x] = " "

def level_up():
    if player["xp"] >= player["level"] * 10:
        player["level"] += 1
        player["hp"] += 5
        print("\n✨ You leveled up! HP increased!")
        input("Press Enter...")

def move(dx, dy):
    global player_x, player_y
    nx, ny = player_x + dx, player_y + dy
    if maze[ny][nx] == "#":
        return
    if maze[ny][nx] == "E":
        fight_enemy(nx, ny)
    elif maze[ny][nx] == "X":
        draw()
        print("\n🎉 You found the exit! You win!")
        exit()

    maze[player_y][player_x] = " "
    player_x, player_y = nx, ny
    maze[player_y][player_x] = "O"

# --- Main Game Loop ---
while True:
    draw()
    level_up()
    move_input = input("Move (WASD): ").lower()
    if move_input == "w": move(0, -1)
    elif move_input == "s": move(0, 1)
    elif move_input == "a": move(-1, 0)
    elif move_input == "d": move(1, 0)
    elif move_input == "q":
        print("Goodbye!")
        break
