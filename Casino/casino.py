import random
avalible_games = {"blackjack"}

def enter_money():
    money = int(input("How much money would you like to deposit: "))
    return money
def what_game(avalible_games):
    print(f"Avalible games for now are:\n {avalible_games}")
    game = input("What game would you like to play: ")
    return game.lower()

def black_jack(money):
    pass_user = True
    your_points = 0
    dealer_points = 0
    while pass_user:
        if dealer_points + random.randint(2, 10) > 21:
            print("Dealer passes")
            pass_user = False
            money *= 2
            break
        else:
            print("Dealers move: ")
            dealer_points += random.randint(2, 10)
            print(f"Dealer points are {dealer_points}")
            if dealer_points > 21:
                print("Dealer lost")
                pass_user = False
                money *= 2
                break
            pass_user = input("Do you want to pass: ").lower()
            if pass_user == "yes":
                pass_user = False
                money = 0
            else:
                pass_user = True
            print("Pleayers move:")
            your_points += random.randint(2, 10)
            print(f"Pleayer points are: {your_points}")
            if your_points > 21:
                print("Dealer passes")
                pass_user = False
                money *= 2
                break
            pass_user = input("Do you want to pass: ").lower()
            if pass_user == "yes":
                pass_user = False
                print("Dealer passes")
                pass_user = False
                money = 0
                break
            else:
                pass_user = True
    print(f"You won {money / 2}$")
    return money
def main():
    money = enter_money()
    choice_game = True
    while choice_game:
        game = what_game(avalible_games)
        if game in avalible_games:
            # In progress
            choice_game = False
        else:
            print("Invalid game. Please choice again")
            game = ""
        if game == "blackjack":
            bet_money = int(input("How much money would you like to bet"))
            money -= bet_money
            money += black_jack(bet_money)
            print(f"Your entire money is: {money}")
            
main()
            
    
        