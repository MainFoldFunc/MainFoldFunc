import random
from blackjack import black_jack
from slot_machine import slot_machine
from russrulete import rulette
from poker import poker
from help import help_casino
avalible_games = {"blackjack", "roulette", "slotmachine", "poker"}

def enter_money():
    money = int(input("How much money would you like to deposit: "))
    return money
def what_game(avalible_games):
    print(f"Avalible games for now are:\n {avalible_games}")
    game = input("What game would you like to play: ")
    return game.lower()

def another_round():
    another = input("Do you want to play another game: ").lower()
    if another != "yes":
        another = False
    else:
        another = True
    return another

def main():
    money = enter_money()
    help_q = input("Do you want any help about games: ").lower()
    if help_q == "yes":
        help_casino(avalible_games)
    choice_game = True
    run = True
    while run:
        while choice_game:
            game = what_game(avalible_games)
        if game == "blackjack":
            bet_money = int(input("How much money would you like to bet"))
            money -= bet_money
            money += black_jack(bet_money)
            print(f"Your entire money is: {money}")
            run = another_round()
    
        elif game == "roulette":
            money == rulette(money)
            print(f"Your total money is {money}")
            run = input("Do you want to play again: ").lower()
            run = another_round()
            
        elif game == "slotmachine":
            money = slot_machine(money)
            print(f"Your total money is {money}")
            run = another_round()
        elif game == "poker":
            money = poker(money)
            print(F"Your total money is {money}")
            run = another_round()
        else:
            print("Invalid game. Please choice again")
            game = ""
                        
            
main()
            
    
        
