import random

def slot_machine(full_money):
    ask_m = True
    while ask_m:
        money = int(input(f"How much would you like to deposit (you have {full_money} left): "))
        if money < 0 or money > full_money:
            print("Invalid money number, please enter again.")
        else:
            ask_m = False

        signs = ["@", "#", "$"]

        slot_m = [signs[random.randint(0, 2)] for _ in range(9)]
        
        print("Slot machine statement is:")
        for j in range(len(slot_m)):
            if j == 3 or j == 6:
                print() 
            print(slot_m[j], end=" ")

        if slot_m[0] == slot_m[1] == slot_m[2] or slot_m[3] == slot_m[4] == slot_m[5] or slot_m[6] == slot_m[7] == slot_m[8]:
            print("\nYou win!")
            full_money += money 
        else:
            print("\nYou lose!")
            full_money -= money

        if full_money <= 0:
            print("You ran out of money! Game over.")
            break
