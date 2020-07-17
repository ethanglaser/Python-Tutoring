
def modpractice():
    value = 10 % 3
    print(value)
    print(10 % 5)

def divsiblebytwo(number):
    if number % 2:
        return False
    else:
        return True

def function(number):
    #return 1 if even+positive, 2 if odd+positive, 3 if even+negative, 4 if odd+negative
    if number % 2 == 0:
        if number > 0:
            return 1
        elif number < 0:
            return 3
    else:
        if number > 0:
            return 2
        elif number < 0:
            return 4

def function2(number):
    #and, or, not, is
    if number % 2 == 0 and number > 0:
        return 1
    elif number % 2 == 1 and number > 0:
        return 2
    elif number % 2 == 0 and number < 0:
        return 3
    elif number % 2 == 1 and number < 0:
        return 4

def divbythree(number):
    if number % 3 == 0:
        return True
    elif number % 3 is not 0:
        return False

def function3(number):
    if number % 2 is 0 and number > 0:
        return 1
    elif number % 2 is 1 and number > 0:
        return 2
    elif number % 2 is 0 and number < 0:
        return 3
    elif number % 2 is 1 and number < 0:
        return 4

def checkdigit(number):
    #return true if single digit
    if number >= 10 or number <= -10:
        return False

def function4(number):
    if number % 2 is not 0:
        return 'Odd'
    elif number % 2 is 0:
        return 'Even'

def divsiblebyten(number):
    #print 'False' if number isnt divisible by 10
    if number % 10 is not 0:
        print(False)




if __name__ == "__main__":
    #modpractice()

    #divsiblebytwo(10)

    #value = function(10)
    #print(value)
    #10 -> 1
    #-5 -> 4
    #201 -> 2
    #-2 -> 3

    print(function2(10))

    value = function2(10)
    print(value)
