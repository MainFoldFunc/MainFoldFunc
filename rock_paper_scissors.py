import time

# Available choices
available = ["rock", "paper", "scissors"]

def win(p_1_choice, p_2_choice):
    # Simplify winning logic
    if p_1_choice == p_2_choice:
        return "Draw!"
    rules = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    if rules[p_1_choice] == p_2_choice:
        return "Player 1 wins!"
    return "Player 2 wins!"

def main():
    print("####### WELCOME TO THE ROCK, PAPER, SCISSORS GAME ########\n\n")
    play_again = True
    while play_again:
        # Player 1 input
        p_1 = input("Player 1, pick rock, paper, or scissors: ").lower()
        while p_1 not in available:
            print("Invalid choice. Please try again.")
            p_1 = input("Player 1, pick rock, paper, or scissors: ").lower()

        # Player 2 input
        p_2 = input("Player 2, pick rock, paper, or scissors: ").lower()
        while p_2 not in available:
            print("Invalid choice. Please try again.")
            p_2 = input("Player 2, pick rock, paper, or scissors: ").lower()

        # Determine winner
        print(win(p_1, p_2))

        # Ask to play again
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            play_again = False

    # Exit animation
    print("Exiting program", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")
    print()

if __name__ == "__main__":
    main()

        
    