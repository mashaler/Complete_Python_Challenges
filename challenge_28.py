#write a random generator that asks for the user to input 5 names,
# stores them in an array and then outputs one of them at random.

#!/usr/bin/python3

import random

print("----RANDOM NAME GENARATOR----")

#creates an empty array
names = []

#asks user to enter 5 names and adds them to the array
for i in range(1,6):
    names.append(input("Enter name "+str(i)+":"))

#generates a random number between 1 and 5
num = random.randint(0,5)

#outputs the randomly chosen name
print(names[num], "has been chosen")