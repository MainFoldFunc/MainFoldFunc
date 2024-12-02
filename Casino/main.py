import random
from blackjack import black_jack
from russrulete import rulette
avalible_games = {"blackjack", "roulette"}

def enter_money():
    money = int(input("How much money would you like to deposit: "))
    return money
def what_game(avalible_games):
    print(f"Avalible games for now are:\n {avalible_games}")
    game = input("What game would you like to play: ")
    return game.lower()

def main():
    money = enter_money()
    choice_game = True
    run = True
    while run:
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
                if run == "yes":
                    continue
                else:
                    input("Goodbye press any kee to escape.")
                    break
                
            elif game == "roulette":
                money == rulette(money)
                print(f"Your total money is {money}")
                run = input("Do you want to play again: ").lower()
                if run == "yes":
                    continue
                else:
                    input("Goodbye press any kee to escape.")
                    break
                
            
main()
            
    
        