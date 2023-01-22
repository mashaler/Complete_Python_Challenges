#write a program that: converts and outputs marks into grades, using the following data.
#-Greater than or equal to 75 = A
#-Greater than or equal to 60 = B
#-Greater than or equal to 35 = C
#less than 35 = D

marks = int(input("Enter your marks: "))
if marks >= 75:
    print("Grade : A")
elif marks >= 60:
    print("Grade : B")
elif marks >= 35:
    print("Grade : C")
else:
    print("Grade : D")