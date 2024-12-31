import random
def play_again():
    play_again = input("Do you want to play again: ").lower()
    if play_again == "yes":
        return True
    return False
def rulette(tot_mon):
    money = 0
    type_bets = {"1-18", "19-36", "Black", "Red"}
    playing = True
    while playing:
        tot_mon += money
        print(f"Your current money is: {money}")
        print(f"Your total money is {tot_mon}")
        money += int(input("How much money would you like to add to this game account: "))
        tot_mon -= money
        if money <= 0:
            print("You can't play with no money.\n Goodbye.")
            break
        elif money > tot_mon:
            print("You deposited to much to your account.")
            break
        curr_number = random.randint(1, 36)
        
        color = ""
        if curr_number % 2:
            color = "black"
        else:
            color = "red"
            
        good_bet = True
        
        while good_bet:
            type_of_bet = input(f"What type of bet would you like to make:\n {type_bets}")
            
            if type_of_bet in type_bets:
                pass
                good_bet = False
            else:
                print("Wrong bet please try again.")
                type_of_bet = ""
                
        if type_of_bet == "1-18":
            good_num = True
            
            while good_num:
                sp_type = int(input("What egzact number from 1 to 18 would you like to bet on: "))
                
                if sp_type > 18 and sp_type < 1:
                    print("Wrong number plese try again")
                    continue
                
                else:
                    good_num = False
                    
                if sp_type == curr_number:
                    print("You won!")
                    money *= money
                    playing = play_again()
                    
                else:
                    print("You lost")
                    money = 0
                    playing = play_again()

        elif type_of_bet == "19-36":
            good_num = True
            
            while good_num:
                sp_type = int(input("What egzact number from 19 to 36 would you like to bet on: "))
                
                if sp_type > 36 and sp_type < 18:
                    print("Wrong number plese try again")
                    continue
                
                else:
                    good_num = False
                    
                if sp_type == curr_number:
                    print("You won!")
                    money *= money
                    playing = play_again()
                    
                else:
                    print("You lost")
                    money = 0
                    playing = play_again()
                
        elif type_of_bet == "Black":
            
            if color == "black":
                print("You won")
                money *= 2
                playing = play_again()
                
            else:
                print("You lost")
                money = 0
                playing = play_again()

                
        elif type_of_bet == "Red":
            
            if color == "red":
                print("You won!")
                money *= 2
                playing = play_again()
                
            else:
                print("You lost")
                money = 0
                playing = play_again()
    return tot_mon