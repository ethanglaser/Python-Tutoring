'''
Things to review:
Loops
Conditionals
Lists
Strings - lower, strip, split
File reading

Things to introduce:
Dictionaries
NLP
N-grams
'''

#print all numbers less than 100 that are divisible by 7

#print numbers from a list that are even and greater than 10

#take a string and print how many times a letter appears

#take a sentence and determine how many words are in it

#find the length of the longest word in a sentence

#take a list of integers and number, add that number of numbers together to form a new list

#read in a file and determine how many words are in it

'''
Dictionaries:
data structure like a list except elements are accessed in key value pairings
ex: lastNames = {"Ethan": "Glaser", "Lebron": "James", "Obi-Wan": "Kenobi"}
    lastNames["Ethan"] = "Glaser"
keys can be strings or numbers and values can be strings, numbers, lists, other dictionaries, etc.
keys of a dictionary can be accesses with .keys(). ex: lastNames.keys() = ["Ethan", "Lebron", "Obi-Wan"]
'''

'''
Natural Language Processing
NLP is a branch of artificial intelligence that deals with analyzing text using software
Examples include chat bots, auto-correct, sentiment analysis, text summarization, etc.

Project idea:
Determine the language of a document (in the form of a text file)

Provided:
Labelled text files, where the language is known
Mystery text files, where the language is unknown and needs to be determined

Process:
Read in the labelled text files and determine most common sequences of characters based on the language
Use this information to match the mystery files based on their most common sequences
'''

