#write a program that, asks the user to input the width and height,calculates the area, outputs the result.

#!/usr/bin/python3

print("--------AREA CALCULATOR----------")

#asks the user to input the width and height and stores them in a variables
width = int(input("Enter the width:"))
height = int(input("Enter the height:"))

#Calculates the area and stores it in the area variable
area = width * height

#Outputs the value stored in the area variable to the screen
print("Your area is:",str(area))