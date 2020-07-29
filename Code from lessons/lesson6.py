
def function():
    for x in range(5): #[0,1,2,3,4]
        print("hello")

#sumTotal(5) = 15
#sumTotal(10) = 55
#sumTotal(1) = 1
def sumTotal(number):
    total = 0
    for value in range(number + 1):
        total += value
    print(total)

def findDigits(number):
    digits = 0
    while number >= 10:
        digits += 1
        number /= 10
    digits += 1
    print(digits)

def listfunction(value1, value2):
    values = [value1, value2]
    firstList = [9, 3, 5, 2]
    print(firstList)
    for value in firstList:
        print(value)

def test():
    scores = [91,82,85,97,64,89,80,100,41,73,77,77,85,94,88,82,71,74,66,97,100]
    maxScore = 0
    for score in scores:
        if score > maxScore:
            maxScore = score
    print(maxScore)
    count = 0
    for score in scores:
        count += 1
    print(count)


if __name__ == "__main__":
    #findDigits(1000000)
    test()

