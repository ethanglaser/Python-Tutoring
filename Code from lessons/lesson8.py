
def function(j, h, p, c):
    newScore = 85
    j.append(newScore)

    allStudents = []
    classes = [j, h, p, c]
    for group in classes:
        for score in group:
            allStudents.append(score)
    for score in j:
        if score < 60:
            j.remove(score)

    index = 0
    length = 41
    while index < length:
        score = allStudents[index]
        if score < 60:
            allStudents.remove(score)
            length -= 1
        else:
            index += 1

    numStudents = 0
    for value in allStudents:
        numStudents += 1
    
    #in
    return allStudents









def newfunction(students):
    listLength = len(students)
    listMax = max(students)
    listMin = min(students)
    listSum = sum(students)

    











if __name__ == "__main__":
    jaxClass = [85, 73, 94, 91, 58, 100, 76, 78, 81, 64]
    henryClass = [91, 92, 64, 52, 88, 97, 83, 66, 74, 72]
    patrickClass = [82, 88, 89, 84, 77, 96, 79, 88, 86, 89]
    calebClass = [91, 55, 93, 100, 41, 72, 91, 94, 56, 61]

    allStudents = function(jaxClass, henryClass, patrickClass, calebClass)
    newfunction(allStudents)

    list1 = [1,2,3,4,5,6,7,8,9,10]
    list2 = [2,4,6,8,10,12]
    #compareLists(list1, list2)
