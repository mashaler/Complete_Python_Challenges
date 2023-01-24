#Extends your maths quiz program from challenge 26 by including a list of the 
# scores of the people that have taken the quiz before

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
print("----SCORES-----")

 #opens the file or creates it if it doesnt already exist
file = open("score.txt", "a")
file.close()
#opens the file in read-only mode
file = open("score.txt", "r")

#loop that prints each line from the file
for line in file:
    print(line)

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