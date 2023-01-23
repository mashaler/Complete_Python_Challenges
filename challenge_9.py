#write a program that: asks the user to name one of the olympic values(Respect, Excellence and Friendship)
#if they correctly name one, output 'Thats correct',
#otherwise 'Try again'

Olympic_values = input("Name one of the Olympic Values: ")

if Olympic_values == "Respect" or Olympic_values == "Excellence" or Olympic_values == "Frienship":
    print("Thats correct")
else:
    print("Try again")