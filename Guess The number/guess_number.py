import random
def main():
    play_again = True
    while play_again:
        
        min_number, max_number = input("what will be the min and max numbers you will be able to guess?: ").split()
        min_number = int(min_number)
        max_number = int(max_number)
        key_number = random.randint(min_number, max_number)
        guess_number = int
        
        while key_number != guess_number:
            guess_number = int(input("What is your guess: "))
            
            if guess_number > key_number:
                print("Your number is to big")
            elif guess_number < key_number:
                print("Your number is to small")
            else:
                print("You correctly guesed!")
        again = input("Do you want to play again(yes, no): ").lower()
        
        if again == "yes":
            continue
        else:
            play_again = False
            
    input("Press enter to shut down the program...")
    
if __name__ == "__main__":
    main()
    
        