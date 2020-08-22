
def function():
    letter = 'a'
    word = 'hello'
    sentence = "Hi, my name is Ethan."

    number = 12
    number2 = 5
    print(number + number2)
    
    #int(), str()
    num = str(number)
    num2 = str(number2)
    print(num + num2)

    print(type(number), type(num))

def function2():
    word = 'abcdefhijklmnopqrstuvwxyz'
    #letter = word[5:10]
    #print(letter)
    for letter in word:
        print(letter)

def lengthOfString(myString):
    total = 1
    for char in myString:
        total += 1
    return total

def findFrequency(character, string):
    count = 0
    for letter in string:
        if letter == character:
            count += 1
    return count

def pythonStrings():
    sentence = "Today is Saturday."
    stringLength = len(sentence)
    print(stringLength)
    numberofA = sentence.count('a')
    print(numberofA)


def firstLetters(strings):
    for string in strings:
        print(string[0])

def splitting():
    phrase = "My name is Ethan Glaser"
    words = phrase.split()
    print(words)
    states = "Minnesota, Wisconsin, Ohio, Alaska"
    statelist = states.split(', ')
    print(statelist)

def groceries(groceryString):
    plurals = []
    groceryList = groceryString.split(', ')
    for grocery in groceryList:
        if grocery[-1] == 's':
            plurals.append(grocery)
    print(plurals)




if __name__ == "__main__":
    #function()
    #function2()

    testString = ';igtuuuuuuuuuuuuuuuuuuueaoielgjoaisghosifzdkhn fs kgcimavnszid.migk;sinfeislemvlzisueovmiildgoisnzo'
    #print(lengthOfString(testString))

    word = 'mississippi'
    letter = 'i'

    #pythonStrings()

    stringList = ['Jax', 'Patrick', 'Caleb']
    #firstLetters(stringList)
    splitting()

    numList = [1,2,3,4,5]
    stringList = []
    for num in numList:
        stringList.append(str(num))

    groceryString = 'apples, banana, carrots, peach, grapes, plum, pepper'
    groceries(groceryString)



