#write a sign-Up program for an after school club;
#it should ask the user for the following details and store them in a file:
#-First name, Last Name, Gender, Form

#!/usr/bin/python3

print("----CLUB SIGN UP----")

#user enters their details
first_name = input("Enter your first name: ")
last_name = input(" Enter your last name: ")
gender = input("Enter your gender: ")
form = input("Enter your form:")

#opens the file or creates it if it doesnt already exist
file = open("signup.txt","a")

#records the users details in the file
file.write("\nFirst name: "+first_name+", Last name: "+last_name+", Gender: "+gender+", Form: "+form)

#closes the file
file.close()