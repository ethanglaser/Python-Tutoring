
def function(value):
    print(value)

def getInput():
    favorite = input("What is your favorite number?")
    return favorite

def ifpractice():
    value = 1
    if value > 0:
        print("Positive")
        if value < 10:
            print("Single Digit")
        else:
            print("Multi Digit")
    else:
        print("Negative")

def ifpractice2(location):
    if location == "Minnesota":
        name = "Wild"
    elif location == "Washington":
        name = "Capitals"    
    elif location == "Tampa Bay":
        name = "Lightning"
    else:
        name = "Sharks"
    print(name)

def absolutevalue(number):
    #code here
    if number < 0:
        absolute = -1 * number
    else:
        absolute = number
    return absolute

def mcdonalds():
    number = input("What would you like to order? Enter 1 for Cheeseburger, 2 for Chicken sandwich, or 3 for McNuggets.")

    if number == "1":
        food = "Cheeseburger"
    elif number == "2":
        food = "Chicken Sandwich"
    elif number == "3":
        food = "McNuggets"
    
    print(food)



if __name__ == "__main__":
    number = 12

    #function(number)

    #value = getInput()
    #print(value)

    #ifpractice()
    #location = 'Calgary'
    #ifpractice2(location)
    #number = 1
    #firstResult = absolutevalue(number)
    #print(firstResult)
    #secondResult = absolutevalue(-123456789)
    #print(secondResult)

    mcdonalds()

