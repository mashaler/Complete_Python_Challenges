#write a program that: asks for the distance (in meters)
#asks the user for the time in seconds that a journey was completed in
#calculates and outputs the average speed using the function

#!/usr/bin/python3

print("----AVERAGE SPEED CALCULATOR----")

#function to calculate average speed calculator
distance = int(input("Enter the distance(in meters): "))
time = int(input("Enter the time that the journey was completed in(seconds):"))

def speed(distance, time):
    speed = distance / time
    return speed
#calls the function, passing distance and time variable
print("average speed is :",speed(distance,time))