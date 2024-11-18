"""
Guess the output mini game

secret_number (computer side) 1-10

user_number= Guess a number between 1 to 10

user_number == secret_number
    print("You won")

You lost, the number was 5

"""
import random

secret_number = random.randint(1, 10)

# ... User number and compare

while True:
    print("Let's start the game")

    # user choice
    user_number = int(input("Guess a number b/w 1 to 10 = "))

    print(f"The user's number is: {user_number}")

    # while user_number not in (secret_number):
    #     user_number=input("User choice is invalid.\n"
    #                   + "Enter a valid number between 1 to 10: ")
    

    # computer choice
    # computer_choice=random.randint(1,10)

    # print(f"The computer's number is: {computer_choice}")

    if user_number == secret_number:
        print("User won")
    else:
        print(f"User lost. The secret number was {secret_number}")


    print("Do you want to play again? [Y/N] ")
    ans=input().lower()
 
    while ans not in ['n','y']:
        ans=input("User option is invalid.\n"
                      + "Enter a valid option: ")
        
    if ans=='n':
        break

print("Fuck off. Get lost")


    
# usr_nmbr= int(input("Enter the number b/n 1-10: "))
# print(usr_nmbr)
