def welcome(levels: list):
    print(f"            ------ Mazemania ------\n")
    print(f"For now, there are only {len(levels)} available levels.\n")
    print("You move by entering these commands in cmd:\nup, down, right, left")
    print("Have a great time!\n")

def level_to_play(levels: list) -> int:
    bad_ans = True
    while bad_ans:
        try:
            level = int(input(f"What level do you choose? There are only {len(levels)} levels: ")) - 1  # Convert to 0-based index
            if level < 0 or level >= len(levels):
                raise ValueError("Incorrect level")
        except ValueError as e:
            print(f"Incorrect level, try again. ({e})")
            bad_ans = True
        else:
            bad_ans = False
    return level



def looking_for_element_in_list(maze: list, element: str) -> tuple:
    # Find the row and column of the player in the maze
    for i, row in enumerate(maze):
        if element in row:
            return i, row.index(element)
    return -1, -1  # Return invalid index if not found



def replace_up(maze: list, player_pos: tuple) -> tuple:
    row, col = player_pos
    try:
        if row > 0 and maze[row - 1][col] != "#":  # Check if the player can move up
            # First check if the new position is the goal
            if maze[row - 1][col] == "@":  # Win condition check
                return maze, True  # Return updated maze and True if won
            
            # If it's not the goal, move the player
            maze[row][col] = "*"  # Remove player from the current position
            maze[row - 1][col] = "&"  # Place player at the new position
    except:
        print("You can't go out of bounds")
    return maze, False  # No win, return False

def replace_down(maze: list, player_pos: tuple) -> tuple:
    row, col = player_pos
    try:
        if row < len(maze) - 1 and maze[row + 1][col] != "#":  # Check if the player can move down
            # First check if the new position is the goal
            if maze[row + 1][col] == "@":  # Win condition check
                return maze, True  # Return updated maze and True if won
            
            # If it's not the goal, move the player
            maze[row][col] = "*"  # Remove player from the current position
            maze[row + 1][col] = "&"  # Place player at the new position
    except:
        print("You can't go out of bounds")
    return maze, False  # No win, return False

def replace_right(maze: list, player_pos: tuple) -> tuple:
    row, col = player_pos
    try:
        if col < len(maze[row]) - 1 and maze[row][col + 1] != "#":  # Check if the player can move right
            # First check if the new position is the goal
            if maze[row][col + 1] == "@":  # Win condition check
                return maze, True  # Return updated maze and True if won
            
            # If it's not the goal, move the player
            maze[row][col] = "*"  # Remove player from the current position
            maze[row][col + 1] = "&"  # Place player at the new position
    except:
        print("You can't go out of bounds")
    return maze, False  # No win, return False

def replace_left(maze: list, player_pos: tuple) -> tuple:
    row, col = player_pos
    try:
        if col > 0 and maze[row][col - 1] != "#":  # Check if the player can move left
            # First check if the new position is the goal
            if maze[row][col - 1] == "@":  # Win condition check
                return maze, True  # Return updated maze and True if won
            
            # If it's not the goal, move the player
            maze[row][col] = "*"  # Remove player from the current position
            maze[row][col - 1] = "&"  # Place player at the new position
    except:
        print("You can't go out of bounds")
    return maze, False  # No win, return False



def game_loop(level: int, levels: list):
    game_looping = True
    player = "&"
    won = "@"
    while game_looping:
        copy_map = levels[level]  # Get the maze for the current level

        # Display the map at the start of each loop iteration
        print(f"This is map: \n")
        for row in copy_map:
            print(" ".join(row))

        player_bad = True
        while player_bad:
            player_move = input("Where do you like to go?: ").lower()
            player_pos = looking_for_element_in_list(copy_map, player)

            if player_pos == (-1, -1):
                print("Player not found!")
                break

            # Move player and check for win condition
            if player_move == "up": 
                copy_map, won = replace_up(copy_map, player_pos)
                player_bad = False
            elif player_move == "down":
                copy_map, won = replace_down(copy_map, player_pos)
                player_bad = False
            elif player_move == "right":
                copy_map, won = replace_right(copy_map, player_pos)
                player_bad = False
            elif player_move == "left":
                copy_map, won = replace_left(copy_map, player_pos)
                player_bad = False
            else:
                print("No such move!")
                player_bad = True

    # Check if the player won
        if won:
            print("You won!")
            again = input("Do you want to play again (y/n)? ").lower()
            if again == "y":
                # Let the player select a new level after winning
                level = level_to_play(mazes)
                game_looping = True  # Exit the current loop so it restarts with the new level
                continue
            else:
                input(f"Thanks for playing! press enter to exit")
                game_looping = False  # Exit the loop if the player doesn't want to play again
                break

