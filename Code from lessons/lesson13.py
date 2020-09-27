import pprint

def readfile():
    with open('Data Files/manyWords.txt', 'r') as f:
        data = f.readlines()
    cleanData = []
    for word in data:
        cleanData.append(word.strip())
    return cleanData

def findwords(letter):
    words = readfile()
    count = 0
    for word in words:
        if word[0] == letter:
            count += 1
    return count

def findmax():
    countmax = 0
    #pairs = []
    for letter in "abcdefghijklmnopqrstuvwxyz":  #['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        #pairs.append((findwords(letter), letter))
        if findwords(letter) > countmax:
            countmax = findwords(letter)
            lettermax = letter
    print(countmax, lettermax)
    #print(list(reversed(sorted(pairs))))

def findcount(number):
    words = readfile()
    count = 0
    for word in words:
        if len(word) == number:
            count += 1
    return count

def lengthlist():
    lengths = []
    for leng in range(25):
        lengths.append(findcount(leng))
    return lengths



if __name__ == "__main__":
    readfile()
    findwords('a')
    findmax()
    findcount(10)
    print(lengthlist())
