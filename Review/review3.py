
#Write a function that asks for user input and outputs either your first, middle, or last name based on the input
def name():
    nametype = input("Enter First, Middle, or Last: ")
    if nametype == "First":
        print("Ethan")
    elif nametype == "Middle":
        print("Philipp")
    elif nametype == "Last":
        print("Glaser")
    else:
        print("No name type correctly specified")

#Write a function that takes in two values and returns or prints the larger of the two values (doesn't ask for user input)

#Write a function that takes in a test score (would be 0 to 100) and prints out the grade: 90-100 is an A, 80-89 is a B, 70-79 is a C, 60-69 is a D, and lower than 60 is an F

#Write your own function using either user input or if statements - anything you want

if __name__ == "__main__":
    name()
