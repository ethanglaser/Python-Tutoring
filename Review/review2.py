
'''
To review what we covered today, I created a Python file with some prompts for functions to write (I wrote two of them as an example)
If you run this file without modifying it, 2 lines should be printed in the terminal:

3
Python


Reminders:
Any prompt that takes an input should have the input in the function definition (def function) and where it is called (in main)
Variable and function names can be whatever you like, as long as they are initialized and referenced by the same name
Variable names are unique to the function they are defined in
Return a value from a function using the return command in Python
'''


#Write a function that returns a number and then verify that it works by printing it in main
def returnNumber():
    number = 3
    return number

#Write a function that takes 1 input and prints that value within the function
def displayInput(input):
    print(input)

#Write a function that takes an input and prints 10 times the value that it receives (note: no need to return anything)

#Write a function that creates a string variable of your favorite food and then returns that string. Check that it works by printing in main.

#Write a function that takes an input and returns a value 3 times that input. Verify by printing in main.

#Write a function that takes an input and subtracts 7. Verify by printing in main.

#Combine the previous two functions into a single function.

#Write a function that takes TWO inputs and adds them together and returns the sum. Verify by printing in main.


if __name__ == "__main__":
    numberToPrint = returnNumber()
    print(numberToPrint)
    #note that the above two lines can be combined into: print(returnNumber())

    sample = "Python"
    displayInput(sample)