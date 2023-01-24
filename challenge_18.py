#write a program that: asks the user to input a number,
#  output the times table for that number

#!/usr/bin/python3

print("----TIMES TABLE GENERATOR----")
#asks the user to input a number and stores it in variable num.
num = int(input("Enter a number: "))

#a loop that outputs the times time for the number stored in num variable 
for i in range(0,10):
    print(str((i+1)*num))