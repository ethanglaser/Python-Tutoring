import math
import os
import sys

def function():
    return

def helloWorld():
    print("Hello, world!")

def declareVariables():
    integerValue = 1
    floatValue = 3.999
    stringValue= 'abc'
    booleanValue = True


    return integerValue, floatValue, stringValue, booleanValue

def returnOne():
    one = 1
    return one

def doMath():
    addValue = 1 + 2
    subtractValue = 12.97 - 3.5
    multiplyValue = addValue * subtractValue
    divideValue = multiplyValue / 2

    #These are equivalent statements
    addValue = addValue + 1
    addValue += 1

    squaredValue = divideValue ** 2
    cubedValue = 4 ** 3

    modulusValue = 10 % 3

    return

def learnLists():
    blankList = []
    nonBlankList = [1,2,3,4]

    firstElement = nonBlankList[0]

    nonBlankList.append(5)

    statesList = ["Minnesota", "Wisconsin"]
    valuesList = [addValue, subtractValue, multiplyValue]
    randomList = ["string", 4, blankList]

def conditionals():
    if addValue == 14:
        addValue -= 2
    
    #notice that == is used to check whether a statement is true
    #and = is used to set a variable to a value
    if squaredValue > cubedValue and squaredValue is not 0:
        newVariable = 2
    elif squaredValue < cubedValue or squaredValue == 0:
        newVariable = 1
    else:
        newVariable = -1

def loops():
    #which values will be printed here?
    value = 1
    while value < 10:
        print(value)
        value += value

    #which values will be printed here?
    value = 22
    while value >= 0:
        if value % 6 == 0:
            print(value)
        value -= 2

    for x in range(1, 11, 2):
        print(x)

    for y in range(5):
        print(y)

    numbers = [1, 3, 6, 14, 23]
    for number in numbers:
        print(number)

def passVariable(variable):
    print(variable)

def passVariable2(number):
    newnumber = number * 2
    print(newnumber)

def returnVariable():
    value = 4
    value += 6
    return value

def getInput():
    print("What is your favorite food?")
    favorite = input()
    print(favorite)


def listFunctions():
    newList = [1,2,3,4,5]
    listLength = len(newList) #5
    listSum = sum(newList) #15
    listMin = min(newList) #1
    listMax = max(newList) #5

def otherList():
    myList = [1,2,3,4]
    myList.append(5)
    print(myList)
    if 3 in myList:
        print("3 is in myList")
    else:
        print("3 is not in myList")
    if 10 in myList:
        print("10 is in myList")
    else:
        print("10 is not in myList")

def readFile():
    with open("Data Files/overview.txt", 'r') as f:
        text = f.readlines()
    for line in text:
        print(int(line))

def firstStrings():
    string1 = "a"
    string2 = "Hi my name is Ethan"
    string3 = str(12)

    newString = "abcdefg"
    print(newString[0])
    for character in newString:
        print(character)

    #find length of a string the same way as a lit
    string1 = "abcdefghijklmnopqrstuvwxyz"
    print(len(string1))

    #strings do not have an append function but can be combined
    string1 += "ABC"
    print(string1)

    #some list functions are more relevant to strings than lists
    string2 = "Mississippi"
    print(string2.count("i"))

    string1 = "abcdefghijklmnopqrstuvwxyz"
    print(string1[-5:])

    string2 = "Minnesota Vikings"
    print(string2[5:15])

    sentence1 = "Hello my name is Ethan"
    print(sentence1.split())
    numbers = "1,2,3,4,5,6,7,8,9"
    print(numbers.split(','))

def osStuff():
    print(os.curdir)
    print(os.listdir(os.curdir))



if __name__ == "__main__":

    #comment like this with a hashtag

    '''
    Multi
    line
    comments
    need 3 quotation marks
    before and after
    '''

    '''helloWorld()
    declareVariables()
    value = returnOne()
    doMath()
    learnLists()
    conditionals()
    loops()

    variable = 2
    passVariable(variable)

    value = returnVariable()'''
    #otherList()
    #readFile()
    #firstStrings()
    osStuff()