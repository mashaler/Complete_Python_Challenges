#write a program that: asks the user their name, 
# if it is the same as your name, outputs 'you're cool',
#  otherwise outputs 'Nice to meet you'.

#!/usr/bin/python3

#assigning variable name to 'Rolva'
name = "Rolva"

#Asks the user to input their name and stores it in a variable
user = input("Enter your name: ")

#Asks the Question: is the value in the name eqaul to 'Rolva'?
if user == name:
    #if the answer to the question is is yes this line is outputted
    print("You're cool")
else:
    #otherwise this line is outputted
    print("Nice to meet you")