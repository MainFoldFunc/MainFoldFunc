import random

def random_word():
    # Load the word bank file
    try:
        with open("Wordle/word-bank.csv", "r") as f:
            word_pool = f.read().splitlines()
    except FileNotFoundError:
        print("Error: Word bank file not found. Ensure 'word-bank.csv' exists in the 'Wordle' directory.")
        return None

    # Return a single random word
    return random.choice(word_pool)


def main():
    print("###### WELCOME TO WORDLE-LIKE GAME ######\n\n")
    print("You have only 6 tries, so hurry up!\n")
    print("Letters in the correct position will be marked before it as: $\n")
    print("Letters in the word but wrong position will be marked before it as: @\n")

    play_again = True
    while play_again:
        # Get the secret word
        key_word = random_word()
        if not key_word:
            break  # Exit if the word file is missing

        key_word = list(key_word)
        print(f"The secret word has {len(key_word)} letters.\n")

        for attempt in range(6):
            guess_word = list(input(f"What is your guess #{attempt + 1}: "))

            # Ensure the guess length matches the secret word length
            if len(guess_word) != len(key_word):
                print(f"Your guess must have exactly {len(key_word)} letters!")
                continue

            # Feedback for the current guess
            feedback = []
            for k, g in zip(key_word, guess_word):
                if g == k:
                    feedback.append(f"$ {g}")
                elif g in key_word:
                    feedback.append(f"@ {g}")
                else:
                    feedback.append(f"  {g}")

            print(" ".join(feedback))

            # Check if the guess is correct
            if guess_word == key_word:
                print(f"\nCongratulations! You guessed the word: {''.join(key_word)}\n")
                break
        else:
            print(f"\nYou ran out of tries. The correct word was: {''.join(key_word)}\n")

        # Ask to play again
        again = input("Do you want to play again? (yes or no): ").strip().lower()
        play_again = (again == "yes")

    print("Thank you for playing! Goodbye.")


# Run the game
main()
