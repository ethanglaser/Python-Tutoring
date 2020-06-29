def function():
    print("Welcome")

def twooperations(value):
    squared = value ** 2
    divided = squared / 2
    return divided

def xyz(variable):
    print(variable + 3)

def square(value):
    variable = value ** 2
    return variable

def divbytwo(value):
    variable = value / 2
    return variable


if __name__ == "__main__":
    '''function()
    abc = 6
    xyz(abc)
    variable1 = 10
    variable2 = 231
    variable1 = variable1 + variable2
    square(variable1)
    square(variable2)
    #square(variable3)
    square(6)'''
    xyz = square(6)
    xyz = 6 ** 2
    new = divbytwo(xyz)
    print(new)

    xyz = twooperations(6)
    print(xyz)
    #print(newvariable)