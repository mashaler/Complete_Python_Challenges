#write a game that: allows the user to play rock, paper, scissors against the computer
#must display the computers choice and show the result of the game

#!/usr/bin/python3

print("----ROCK, PAPER, SCISSORS----")
import random

#generates a random number between 1 and 3
computer = random.randint(1, 3)

#Asks the  user to input their choice and stores it in a variable
user_choice = int(input("Enter your choice: \n1=rock \n2=paper \n3=scissors\n"))

#Outputs the computers's move
print("The computer has chosen",computer)

#Outputs a different string depending on the game outcome
if computer == user_choice:
    print("Tie game")
elif computer == 1 and user_choice ==3:
    print("Computer wins")
elif computer == 2 and user_choice ==1:
    print("Computer wins")
elif computer == 3 and user_choice ==2:
    print("Computer wins")
else:
    print("You win!")