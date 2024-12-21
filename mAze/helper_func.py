import time
import curses  # For dynamic screen updates
from Mazes import mazes  # Assuming you have your maze data in this file

def welcome(levels: list):
    print("            ------ Mazemania ------\n")
    print(f"For now, there are only {len(levels)} available levels.\n")
    print("You move by entering these commands using arrow keys.\n")
    print("Have a great time!\n")

def level_to_play(levels: list) -> int:
    while True:
        try:
            level = int(input(f"What level do you choose? There are only {len(levels)} levels: ")) - 1
            if level < 0 or level >= len(levels):
                raise ValueError("Incorrect level")
            return level
        except ValueError as e:
            print(f"Incorrect level, try again. ({e})")

def looking_for_element_in_list(maze: list, element: str) -> tuple:
    for i, row in enumerate(maze):
        if element in row:
            return i, row.index(element)
    return -1, -1

def replace_up(maze: list, player_pos: tuple) -> tuple:
    row, col = player_pos
    if row > 0 and maze[row - 1][col] != "#":
        maze[row][col] = "*"  # Clear current position
        maze[row - 1][col] = "&"  # Move player
        return maze, maze[row - 1][col] == "@"
    return maze, False

def replace_down(maze: list, player_pos: tuple) -> tuple:
    row, col = player_pos
    if row < len(maze) - 1 and maze[row + 1][col] != "#":
        maze[row][col] = "*"  # Clear current position
        maze[row + 1][col] = "&"  # Move player
        return maze, maze[row + 1][col] == "@"
    return maze, False

def replace_right(maze: list, player_pos: tuple) -> tuple:
    row, col = player_pos
    if col < len(maze[row]) - 1 and maze[row][col + 1] != "#":
        maze[row][col] = "*"  # Clear current position
        maze[row][col + 1] = "&"  # Move player
        return maze, maze[row][col + 1] == "@"
    return maze, False

def replace_left(maze: list, player_pos: tuple) -> tuple:
    row, col = player_pos
    if col > 0 and maze[row][col - 1] != "#":
        maze[row][col] = "*"  # Clear current position
        maze[row][col - 1] = "&"  # Move player
        return maze, maze[row][col - 1] == "@"
    return maze, False

def won(stdscr, timer_start):
    """Function to show winning message and time taken."""
    timer_end = time.time()
    stdscr.clear()
    stdscr.addstr("\nYou won!\n")
    stdscr.addstr(f"It took you {timer_end - timer_start:.2f} seconds to beat this level.\n")
    stdscr.addstr("Press 'y' to play again or any other key to quit: ")
    stdscr.refresh()

def game_loop(level: int, levels: list):
    def play_with_curses(stdscr, level, levels):
        curses.curs_set(0)  # Hide the cursor
        stdscr.nodelay(True)  # Make getch non-blocking
        stdscr.clear()

        player = "&"
        won_flag = False
        maze = [list(row) for row in levels[level]]  # Copy the maze to modify
        timer_start = time.time()

        while True:
            # Display the maze dynamically
            stdscr.clear()
            for row in maze:
                stdscr.addstr(" ".join(row) + "\n")
            stdscr.refresh()

            # Get player's position
            player_pos = looking_for_element_in_list(maze, player)
            if player_pos == (-1, -1):
                stdscr.addstr("\nPlayer not found! Exiting...\n")
                stdscr.refresh()
                time.sleep(2)
                break

            # Get user input for movement
            key = stdscr.getch()

            if key == curses.KEY_UP:
                maze, won_flag = replace_up(maze, player_pos)
            elif key == curses.KEY_DOWN:
                maze, won_flag = replace_down(maze, player_pos)
            elif key == curses.KEY_LEFT:
                maze, won_flag = replace_left(maze, player_pos)
            elif key == curses.KEY_RIGHT:
                maze, won_flag = replace_right(maze, player_pos)
            elif key == ord("q"):  # Quit if the user presses 'q'
                break

            # Check for win condition after each move
            if won_flag:
                won(stdscr, timer_start)

                key = stdscr.getch()
                if key == ord("y"):
                    level = level_to_play(levels)
                    maze = [list(row) for row in levels[level]]
                    timer_start = time.time()
                else:
                    break

            time.sleep(0.1)  # Small delay to control game speed

    # Call the wrapper with a lambda to pass `level` and `levels`
    curses.wrapper(lambda stdscr: play_with_curses(stdscr, level, levels))
