# write a program that: asks the user to input a number
# and repeat until they guess the number 7
#congratulate the user with a 'well done' message when they guess correctly

#!/usr/bin/python3

print("----GUESS THE NUMBER----")

# assigned variable guess to 7
guess = 7

#asks the user to enter the guess number
num = int(input("Enter the guess number: "))
 #loops until the user guesses the number 7
while num != 7:
    num = int(input("incorrect guess!try again: "))
    
print("well done")