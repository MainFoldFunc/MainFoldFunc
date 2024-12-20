mazes = [
    [
        ["*", "*", "*", "*", "#"],
        ["#", "#", "*", "#", "*"],
        ["*", "*", "*", "#", "*"],
        ["#", "#", "*", "#", "*"],
        ["&", "*", "*", "*", "@"]
    ],
    [
        ["&", "*", "#", "#", "#"],
        ["#", "*", "*", "#", "*"],
        ["#", "#", "*", "#", "*"],
        ["#", "*", "*", "*", "*"],
        ["#", "#", "#", "*", "@"]
    ],
    [
        ["*", "#", "#", "#", "#"],
        ["*", "*", "*", "*", "#"],
        ["#", "#", "#", "*", "#"],
        ["&", "*", "#", "*", "*"],
        ["#", "#", "#", "#", "@"]
    ],
    [
        ["*", "*", "*", "*", "*"],
        ["#", "#", "#", "*", "#"],
        ["&", "*", "#", "*", "*"],
        ["#", "*", "#", "#", "*"],
        ["#", "*", "*", "*", "@"]
    ]
]

def welcome(levels: list):
    print(f"Hello user, welcome to the maze game")
    print(f"For now, there are only {len(levels)} available levels.")
    print("You move by entering these commands in cmd:\nup, down, right, left")
    print("Have a great time!")

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

def replace_up(maze: list, player_pos: tuple) -> list:
    row, col = player_pos
    try:
        if row > 0 and maze[row - 1][col] != "#":  # Check if the player can move up
            # Move the player
            maze[row][col] = "*"
            maze[row - 1][col] = "&"

    except:
        print(f"You can't go out of bounds")
    return maze

def replace_down(maze: list, player_pos: tuple) -> list:
    row, col = player_pos
    try:
        if row > 0 and maze[row + 1][col] != "#":  # Check if the player can move up
            # Move the player
            maze[row][col] = "*"
            maze[row + 1][col] = "&"
    except:
        print(f"You can't go out of bounds")
    return maze

def replace_right(maze: list, player_pos: tuple) -> list:
    row, col = player_pos
    try:
        if row > 0 and maze[row][col + 1] != "#":  # Check if the player can move up
            # Move the player
            maze[row][col] = "*"
            maze[row][col + 1] = "&"
    except:
        print(f"You can't go out of bounds")
    return maze

def replace_left(maze: list, player_pos: tuple) -> list:
    row, col = player_pos
    try:
        if row > 0 and maze[row][col - 1] != "#":  # Check if the player can move up
            # Move the player
            maze[row][col] = "*"
            maze[row][col - 1] = "&"
    except:
        print("You can't go out of bands")
    return maze

def game_loop(level: int, levels: list):
    player = "&"
    end = "@"
    block = "#"
    space = "*"
    copy_map = levels[level]
    game_looping = True

    while game_looping:
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

            if player_move == "up": 
                copy_map = replace_up(copy_map, player_pos)
            elif player_move == "down":
                copy_map = replace_down(copy_map, player_pos)
            elif player_move == "right":
                copy_map = replace_right(copy_map, player_pos)
            elif player_move == "left":
                copy_map = replace_left(copy_map, player_pos)
            elif player_move == "exit":
                print(f"Goodbye")
                game_looping = False
                player_bad = False
            else:
                print("No such move!")
                player_bad = True

            # Check if the player reached the end (@) tile
            player_pos = looking_for_element_in_list(copy_map, player)
            if copy_map[player_pos[0]][player_pos[1]] == end:
                print("You won!")
                game_looping = False
                player_bad = False
def main():
    welcome(mazes)
    level = level_to_play(mazes)
    game_loop(level=level, levels=mazes)

if __name__ == "__main__":
    main()

