print("Let's calculate the points!")
while True:
    try:
    #total matches played
        total_matches=int(input("Enter total number of game(s) played by team A and B: "))

        #team A & B won & tied matches
        while True:
            try:
                A_Won=int(input("Enter number of game(s) won by team A: "))
                if A_Won > total_matches:
                    print("Enter correct number of match(es) won by team A.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer.")

        while True:
            try:
                B_Won=int(input("Enter number of game(s) won by team B: "))
                if B_Won> total_matches-A_Won:
                    print("Enter correct number of match(es) won by team B.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer.")


        #C_Won=int(input("Enter number of games won by team C: "))
        tied_matches= total_matches-A_Won-B_Won

        print(f"The total game(s) played between team A and B is/are {total_matches}.")
        print (f"The game(s) tied between team A and B is/are {tied_matches}.")

    # w_p=4
    # l_p=0
    # t_p=2

    #team A points
        A_Points=A_Won*4 + tied_matches*2
        B_Points=B_Won*4 + tied_matches*2

        print(f"The game(s) won & tied by team A is {A_Won} and {tied_matches} and total points is {A_Points}. "
              f"The game(s) won & tied by team B is {B_Won} and {tied_matches} and total points is {B_Points}.")

        #print("Do you want to calculate for other amount? [Y/N] ")
        ans = input("Do you want to calculate for other amount? [Y/N]: ").lower()

        while ans not in ['n', 'y']:
            ans = input("User option is invalid.\nEnter a valid option: ")
        if ans == 'n':
            break

    except ValueError:
        print("Please enter a valid integer.")

print("Thanks for using our game points calculator.")