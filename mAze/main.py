from Mazes import mazes
from helper_func import welcome, level_to_play, game_loop

def main():
    welcome(mazes)
    level = level_to_play(mazes)
    game_loop(level=level, levels=mazes)

if __name__ == "__main__":
    main()

