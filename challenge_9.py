#write a program that: asks the user to name one of the olympic values(Respect, Excellence and Friendship)
#if they correctly name one, output 'Thats correct',
#otherwise 'Try again'

#!/usr/bin/python3

#Asks the user to input one of the Olympic Values and stores it in a variable
Olympic_values = input("Name one of the Olympic Values: ")

#Outputs different strings depending on whether the user correctly 
#entered the name of an Olympic value
if Olympic_values == "Respect" or Olympic_values == "Excellence" or Olympic_values == "Frienship":
    print("Thats correct")
else:
    print("Try again")