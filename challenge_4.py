#write a program that: asks the user to input two numbers,
#  divides the first number by the second number and outputs the results.

#!/usr/bin/python3

print("----DIVEDER----")

#Asks the user to input two numbers and stores them in two variables
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

#Divides the value in the number1 variable by the value in the number2 variable
divides = number1 / number2

#outputs the value stored in the result variable to the screen
print("the result is: ",str(divides))