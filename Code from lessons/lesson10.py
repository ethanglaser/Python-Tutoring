
def printWord(sentence, number):
    print(sentence.split()[number - 1])

def printLetter(sentence, num1, num2):
    print(sentence.split()[num1 - 1][num2 - 1])

def findLongest(sentence):
    maxLen = 0

def stringfunctions(sentence):
    up = sentence.upper()
    low = sentence.lower()
    newsentence = "     string  "
    print(newsentence)
    print(newsentence.strip())

    stringlist = ['hi', 'my', 'name', 'is', 'ethan']
    divider = ' '
    newsentence2 = divider.join(stringlist)
    print(newsentence2)

def quicklist(mylist, first, second):
    swapping = mylist[first - 1]
    mylist[first - 1] = mylist[second - 1]
    mylist[second - 1] = swapping
    print(mylist)

def swapWords(sentence, first, second):
    wordlist = sentence.split()
    new = wordlist[first - 1]
    wordlist[first - 1] = wordlist[second - 1]
    wordlist[second - 1] = new
    return ' '.join(wordlist)


if __name__ == "__main__":
    sentence = "This is our tenth session"
    number = 3
    printWord(sentence, number)
    printLetter(sentence, 4, 1)
    findLongest(sentence)
    stringfunctions(sentence)

    mylist = [1,2,3,4,5] # -> [1,3,2,4,5]
    mylist2 = [9,3,4,5] #  -> [9,4,3,5]
    num1 = 2
    num2 = 3
    quicklist(mylist, num1, num2)
    print(swapWords(sentence, num1, num2))
