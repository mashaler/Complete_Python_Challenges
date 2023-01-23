#write a program that, asks the user to input two numbers,calculates the average,outputs the result.

#!/usr/bin/python3

print("----AVERAGE CALCULATOR----")

#asks the user to input two numbers and stores them in the number1 and number2 variables
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))

#calculates the average of the two numbers
average = (number1 + number2) / 2

#outputs the values stored in the average variable to the screen
print("Your average is: ",str(average))