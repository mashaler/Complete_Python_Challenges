#write a program that allows user to create and store a checklist for a holiday.

#it should start by asking them the destination of the holiday, how many things they need
# to pack and how many tasks they need to complete to prepare.

#The user should then be able to enter each item they need to pack and each task they need to complete

#!/usr/bin/python3

print("----HOLIDAY CHECKLIST----")

packList = []
tasks = []

name = input("Enter the destination of the holiday: ")
itemsNum = int(input("Enter the number of items you need to pack: "))
tasksNum = int(input("How many tasks do you need to complete to prepare for the holiday?: "))

for i in range(0,itemsNum):
    packList.append(input("Enter the name of the item "+str(i+1)+": "))
for i in range(0,tasksNum):
    tasks.append(input("Enter the task"+str(i+1)+": "))

file = open((name+"checklist.txt"), "w")
file.write("Destination: "+name+"\npacking list: \n")

for item in packList:
    file.write(item+"\n")
file.write("Tasks: \n")
for item in tasks:
    file.write(item+"\n")
file.close()
print("your list has been saved")
