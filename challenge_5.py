#write a program that: asks the user their name, 
# asks what their favourite subject is(using their name in the question), 
# responds to their answer by saying that you like that subject as well.

#!/usr/bin/python3

#Asks the user to input their name and stores it in a variable
name = input("What is your name? ")

#Asks the user to input their favourite subject ,using the value stored in the name variable in the question
subject  = input(name + "," +" what is your favourite subject? ")

#Outputs the value stored in the food variable
print("Wow!, i like",subject,"as well")
