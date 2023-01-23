#write a program that :asks the user to input a sentence,
#  asks the user to input: -the word they want to replace
#  -the word they want to replace it with
# Outputs the new sentence

#!/usr/bin/python3

#asks the user to input a sentence and stores it in the sentence variable
sentence = input("Enter a sentence: ")

word1 = input("Enter the word you want to replace:")
word2 = input("Enter the word you want to replace it with: ")

#outputs the sentence with the original word replaced with the new word
print("New sentence is as follows: ",sentence.replace(word1,word2))