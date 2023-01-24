#write a program that: asks the user to input a number,
#outputs the times table for that number
#starts again everytime it finishes

#!/usr/bin/python3

print("----TIMES TABLE GENERATOR----")
#a loop that will continually repeats the program
while True:
    #asks the user to input a number and stores it in a variable num
    num = int(input("\nEnter a number: "))

    #a loop that outputs the times table for the number stored in variable num
    for i in range(0,10):
        print(str((i + 1) * num))
        