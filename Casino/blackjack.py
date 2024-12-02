import random
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