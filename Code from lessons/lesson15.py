import os

def lettercounter(mystring):
    letterdict = {}
    for letter in mystring:
        letterdict[letter] = mystring.count(letter)
    #print(letterdict)

def filecounter():
    path = os.path.join("../ProjectData", "spanish.txt")
    with open(path, "r") as f:
        lines = f.readlines()
    letterdict = {}
    for letter in lines[0]:
        letterdict[letter] = lines[0].count(letter)
    print(letterdict)

    #note - newdict.keys()
    newdict = {}
    for line in lines:
        for letter in line:
            if letter in newdict.keys():
                newdict[letter] += 1
            else:
                newdict[letter] = 1
    print(newdict)

    firstline = lines[0].lower().strip()
    print(firstline)
    print(len(firstline))
    print(firstline[0] + firstline[1])
    print(firstline[0:3])

    #15
    sequences = []
    for index in range(len(firstline) - 2):
        sequences.append(firstline[index:index+3])
    print(sequences)





# m-1, i-4, s-4, p-2

if __name__ == "__main__":
    var = "mississippi"
    lettercounter(var)


    filecounter()
