#improve your maths quiz from challenge 20 and 27 
# by storing all the questions and possible answers in a two-dimensional array
#write a fuction that can be reused to ask each of the questions

#!/usr/bin/python3

#function that can be used to ask each question
def ask(q,s):
    answer = int(input(questions[0][q]))
    if answer == questions[1][q]:
        s = s + 1
        return s

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

questions = [["What is 3 + 4?: ","What is 3 * 4?: ","what is 3 - 4?: "],[7,12,-1]]

#loops to call ask function to ask each question
for i in range(len(questions) +1):
    score = ask(i,score)

#opens the file in append mode
file = open("score.txt","a")

#prints the score to the screen
print("your score is:",score)

#records the users score in the file
file.write("Name: "+name+", score: "+str(score)+"\n")
#closes the file
file.close()