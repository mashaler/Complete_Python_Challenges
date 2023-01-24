#A gardener wants to buy some turf for a project they are working on.
# The gardener is rectangular with a circularflower bed in the middle
#write a program that: asks the user for the dimensions of the lawn and 
# the radius of the circle (in meters)
# uses a fuction to calculate and output the amount of turf needed

#!/usr/bin/python3
 
import math

print("----TURF CALCULATOR----")

#user input a width and length of the lawn and the radius of the bed
width = int(input("Enter the width of the lawn: "))
length = int(input("Enter the length of the lawn: "))
radius = int(input("Enter the radius of the flower bed: "))

#function to calculate the amount if turf required
def Calculate(width,length,radius):
    lawn_area = width * length
    bed_area = math.pi * (radius * radius)
    turf = lawn_area - bed_area
    print("you need",turf,"square meters of turf")
    return 

#calls the calculate function, passiing the width, length and radius variables
Calculate(width,length,radius)