def function(value):
    print(value)

def whileloop():
    start = 1
    while start <= 5:
        print(start)
        start = start + 1

def printrange(start, end):
    while start <= end:
        print(start)
        start += 1

def printevens(start, end):
    while start <= end:
        if start % 2 == 0:
            print(start)
        start += 1

def forloop():
    for value in range(5, 20, 5):
        print(value)

def printevens2(start, end):
    for value in range(start, end+1, 1):
        if value % 2 == 0:
            print(value)

#range(start, end, increment)

def forloop2():
    for value in range(10):
        print(value)

#range(end) - start at 0, increment by 1
#range(start, end) - increment by 1



if __name__ == "__main__":
    #function(1)
    #whileloop()
    #printevens(-1, 3)
    #forloop()
    #printevens2(0,20) #0,2,4,6,8,10,12,14,16,18,20
    forloop2()