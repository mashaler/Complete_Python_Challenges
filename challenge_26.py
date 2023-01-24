#write a maths quiz with three question.

#it must ask the user to input their name at the start.
#at the end it should display a message informing the user of their score.
#write a function that saves the users name and quiz result in a text file.

#!/usr/bin/python3

def saveScore(name, score):
     #opens the file or creates it if it doesnt already exist
    file = open("scores.txt","a")
    #records the users score in the file
    file.write("Name: "+name+", score: "+str(score)+"\n")
    #closes the file
    file.close()
    return

print("----MATHS QUIZ---")

#variable setup
name = input("Enter your name: ")
score = 0 

#question 1
quiz1 = int(input("What is 3 + 4: "))
if quiz1 == 7:
    score = score + 1

#question 2
quiz2 = int(input("What is 3 * 4: "))
if quiz2 == 12:
    score = score + 1

#question 3
quiz3 = int(input("What is 3 - 4: "))
if quiz3 == -1:
    score = score + 1

#prints the score to the screen
print("Your score is: ",score)

#calls the saveScore function and passes the name and score variables
saveScore(name,score)