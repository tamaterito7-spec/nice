import curses

maze = [
    "####################",
    "#                  #",
    "#  #####  ######## #",
    "#        #      #  #",
    "#  ##### # #### #  #",
    "#  #   # # #    #  #",
    "#  # # # # # ## #  #",
    "#    #   #   ##    #",
    "#  ##### ######### #",
    "#                  #",
    "####################"
]

def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(100)

    player_y, player_x = next((y, x) for y, row in enumerate(maze)
                              for x, cell in enumerate(row) if cell == "@")
    maze[player_y] = maze[player_y].replace("@", ' ', 1)

    while True:

        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                stdscr.addch(y, x, cell if (y, x) != (player_y, player_x) else '@')
        stdscr.refresh()

        key = stdscr.getch()
        dy, dx = 0, 0
        if key == curses.KEY_UP:
            dy = -1
        elif key == curses.KEY_DOWN: 
            dy = 1
        elif key == curses.KEY_LEFT:
            dx = -1
        elif key == curses.KEY_RIGHT:
            dx = 1
        elif key == ord('q'):
            break

        new_y, new_x = player_y + dy, player_x + dx
        if maze[new_y][new_x] == ' ':
            player_y, player_x = new_y, new_x

curses.wrapper(main)