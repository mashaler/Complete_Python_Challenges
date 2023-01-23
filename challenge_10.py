#write a game that: allows the user to play rock, paper, scissors against the computer
#must display the computers choice and show the result of the game

import random

computer = random.randint(1, 3)

user_choice = int(input("Enter your choice\n1=rock \n2=paper \n3=scissors"))

if computer == user_choice:
    print("correct")
    print("computers choice is:",computer)
    print("you win!")
else:
    print("Incorrect")
    print("computers choice is:",computer)
    print("computer wins")