#write a program that converts between centimeters, and inches and vice versa, by:
#asking the user to input a user
#asking the user to choose between converting from centimers to inches or inches to centimeters
#calculating and outputting the result using function

#!/usr/bin/python3

print("----CM/INCHES CONVERTER----")

#asks the user to input a number and stores it in a variable num
num = int(input("Enter a number: "))

#asks the user to input the unit (cm/iches) to get the conversion they want to perform
Unit = int(input("choose an option, convert to: \n1=INCHES TO CENTIMETERS \n2=CENTIMETERS to INCHES\n"))

#converts inches to centimeters
def incTocm(num):
    convert = num * 2.54
    print(num,"in inches is:",convert,"cm")
    return
#converts centimeters to inches
def cmToinc(num):
    convert = num * 0.393700787
    print(num,"in centimeters is:",convert,"inches")
    return

#if statement to calls for appropriate function
if Unit == 1:
    print("to centimeters")
    incTocm(num)
elif Unit == 2:
    print("to inches")
    cmToinc(num)
else:
    print("invalid selection")