#write a functiom that takes two numbers.
#the first number indicates the number of spaces that should be displayed and 
# the second indicates the number of Xs that should be displayed.
# These should bith be displayed on the same line.

#Now write another function that makes multiple calls to your first function and draws a picture with Xs

#!/usr/bin/python3

#Function to draw a line of the image
def drawLine(s,x):
    for i in range(0,s):
        print(" ", end="")

    for i in range(0,x):
        print("X", end="")
        print()
        return
#Function to call the drawline function to draw image
def drawPicture():
    drawLine(5,1)
    drawLine(4,3)
    drawLine(3,5)
    drawLine(2,7)
    drawLine(1,9)
    drawLine(4,3)
    drawLine(4,3)

    return

drawPicture()

