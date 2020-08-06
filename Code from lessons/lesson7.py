def gcf(value1, value2):
    if value1 > value2:
        value = value2
    else:
        value = value1
    while value > 0:
        if value1 % value == 0 and value2 % value == 0:
            return value
        else:
            value -= 1


def printList(newlist):
    for value in newlist:
        print(value)


def hockey(wild, sharks):
    wildHighest = 0
    for goals in wild:
        if goals > wildHighest:
            wildHighest = goals

def testresults(j, h, p, c):
    print(sum(j)/len(j), sum(h)/len(h), sum(p)/len(p), sum(c)/len(c))

if __name__ == "__main__":
    print(gcf(12, 8))
    printList([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1])
    wildGoals = [12, 8, 23, 25, 19, 15, 8, 11, 15, 14]
    sharksGoals = [22, 16, 7, 7, 26, 14, 12, 6, 6, 16]
    hockey(wildGoals, sharksGoals)

    jaxClass = [85, 73, 94, 91, 58, 100, 76, 78, 81, 64]
    henryClass = [91, 92, 64, 52, 88, 97, 83, 66, 74, 72]
    patrickClass = [82, 88, 89, 84, 77, 96, 79, 88, 86, 89]
    calebClass = [91, 55, 93, 100, 41, 72, 91, 94, 56, 61]
    testresults(jaxClass, henryClass, patrickClass, calebClass)
