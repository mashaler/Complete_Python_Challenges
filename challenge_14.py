#write a program that: asks then user to input a sentence
#outputs the number of times the word 'the' occurs in it.

#!/usr/bin/python3

#asks the user to input a sentence amd store it in the sentence variable
sentence = input("Enter a sentence: ")

#outputs the number of times the 'the' occurs in the sentence
print("This word 'the' occurs",sentence.count("the"),"times")