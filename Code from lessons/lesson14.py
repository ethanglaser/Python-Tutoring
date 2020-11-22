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
def loop():
    for i in range(100):
        if i % 7 == 0:
            print(i)

#print numbers from a list that are even and greater than 10
def printlist(mylist):
    for value in mylist:
        if value > 10 and value % 2 == 0:
            print(value)

#take a string and print how many times a letter appears
def stringfunction(mystring, letter):
    #print(mystring.count(letter))
    count = 0
    for char in mystring:
        if char == letter:
            count += 1
    print(count)

#take a sentence and determine how many words are in it
def countwords(val):
    wordlist = val.split()
    print(len(wordlist))

#find the length of the longest word in a sentence
def findlong(sentence):
    wordlist = sentence.split()
    maxlength = 0
    for word in wordlist:
        wordlength = len(word)
        if wordlength > maxlength:
            maxlength = wordlength
            maxword = word
    print(maxlength, maxword)

#read in a file and determine how many words are in it
def numwords():
    with open("spanish.txt", "r") as f:
        lines = f.readlines()
    count = 0
    for line in lines:
        words = line.split()
        numwords = len(words)
        count += numwords
    print(count)

def liststuff():
    new = [1,2,3,4,5,6,9,1,3]
    print(new[0])

    mylist = []
    mylist.append(5)

    points = [[100, 7], [20, 500]]
    pointsdict = {}
    vikings = {}
    vikings['pf'] = 100
    vikings['pa'] = 7
    print(vikings)
    packers = {}
    packers['pf'] = 20
    packers['pa'] = 500

    pointsdict['Vikings'] = vikings
    pointsdict['Packers'] = packers

    print(pointsdict)


    spanish = {}
    spanish['el '] = 100
    spanish['los'] = 82
    spanish['ero'] = 29




if __name__ == "__main__":
    loop()
    newlist = [1,3,9,12,25,42]
    printlist(newlist)
    mystring = 'mississippi'
    letter = 'i'
    stringfunction(mystring, letter)
    sentence = "Hi my name is Ethan"
    countwords(sentence)
    findlong(sentence)
    numwords()
    liststuff()






















#take a list of integers and number, add that number of numbers together to form a new list



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

