def help(games):
    print("------ WELCOME TO THE CASINO ------")
    print(f"There are only 2 games for now:\n{games}")
    help_l = True
    while help_l:
        wich_game = input("To wich game would you like some help: \n\n").lower()
        if wich_game in games:
            if wich_game == "blackjack":
                print("In this game you are playing against the dealer")
                print("You both draw cards that have diffrent numerical values.")
                print("Pleayer loses if his score is more than 21 or when dealer pleayer passes.")
                print("Pleayer wins when dealer points are more than 21 or when diller passes.")
                print("Money:\n")
                print("When pleayer wins his money multiplies")
                print("When pleyer losses his money that he put in is zeroed")
                help_l = False
            elif wich_game == "roulette":
                print("In this game you can bet on diffrent type of places like:\n Black - Odd number spining\n Red - Divisible by two number spining")
                print("Number from 1 - 18 that will spin\nNumber from 19 - 36")
                print("If pleayer correctly guesses the number from 1 - 18 of 19 - 36 his money is sqared m^2")
                print("When pleayer correctly guesse a odd or even number his money is multiplicated by 2.")
                print("When pleyer losses his money that he put in is erresed.")
                help_l = False

        else:
            print("Print this game is not in avalible in our casino.")
            help_l = True

