#write a program that: converts and outputs marks into grades, using the following data.
#-Greater than or equal to 75 = A
#-Greater than or equal to 60 = B
#-Greater than or equal to 35 = C
#less than 35 = D

#!/usr/bin/python3

print("----GRADE CALCULATOR----")

#Aks the user to input the mark and stores it in the mark variable 
mark = int(input("Enter your mark: "))

#if statement that outputs diffferent strings depending on the value stored
#in the mark variable
if mark >= 75:
    print("Grade : A")
elif mark >= 60:
    print("Grade : B")
elif mark >= 35:
    print("Grade : C")
else:
    print("Grade : D")