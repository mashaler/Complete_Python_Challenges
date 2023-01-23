#write a program that: asks the user how long on average they spend watching Tv each day.
#if it is less than 2 hours ,outputs 'that shouldnt rot your brain too much'
#if it is less than 4 hours per day, outputs 'arent you getting square eyes?';
#otherwise outputs 'Fresh air beats channel flicking'

#!/usr/bin/python3

#Asks the user to input a value and stores it in the time variable
time = int(input("How many hours on average do you soend watching Tv each day?"))

#if the statement that outputs differemt strings depending on the value stored in
#the time variable
if time < 2:
    print("That shouldnt rot your brain too much")
elif time < 4:
    print("Arent you getting square eyes?")
else:
    print("Fresh air beats channel flicking")