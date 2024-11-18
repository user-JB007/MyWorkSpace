"""
ROCK PAPER SCISSORS

computer_choice = rock/paper/scissors

user_choice = Enter your choice = 

You won

You lost, the computer choice was 

You tied
"""

import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")


options = ["rock", "paper", "scissors"]

#user choice logic

    


while True:
    print("Let's start the game.")

    user_choice = input("Guess rock/paper/scissors = ").lower()
    print("Choice of user is: ", user_choice)
    
    while user_choice not in (options):
        user_choice=input("User choice is invalid.\n"
                      + "Enter a valid choice: ")
        
        
    #computer choice logic
    computer_choice = random.choice(options)
    print("Choice of computer is: ", computer_choice)

    print (user_choice,"vs", computer_choice)

#logic for draw
    if user_choice==computer_choice:
     print("Session tied")
     result=0

    #for winning rules
    if (user_choice=='rock' and computer_choice=='paper'):
        print("Paper Wins")
        result='C1'
    elif (user_choice=='paper' and computer_choice=='rock'):
        print("Paper Win")
        result='U1'
    
    if (user_choice=='paper' and computer_choice=='scissors'):
        print("Scissors Wins")
        result='C2'
    elif (user_choice=='scissors' and computer_choice=='paper'):
        print("Scissors win")
        result='U2'

    if (computer_choice=='rock' and user_choice=='scissors'):
        print("Rock wins") 
        result='C3'
    elif (computer_choice=='scissors' and user_choice=='rock'):
        print("Rock win")
        result='U3'

#declaring the result

    if result==0:
     print("Match tied")
    elif result=='C1' or result=='C2' or result=='C3':
     print("Computer won")
    else:
     print("User won")
     

    print("Do you want to continue the play? [Y/N] ")
    ans=input().lower()
    
    while ans not in ['n','y']:
        ans=input("User option is invalid.\n"
                      + "Enter a valid option: ")
    if ans=='n':
        break

print("Thanks for playing")