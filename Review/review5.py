# write functions that take a start and end value and prints numbers that are not evenly divisible by 3 between/including the start and end values
# write 2 functions, one that uses a while loop and one that uses a for loop
def whileExample(start, end):
    while start <= end:
        if start % 3 is not 0:
            print(start)
        start += 1

def forExample(start, end):
    for value in range(start, end + 1, 1):
        if value % 3 is not 0:
            print(value) 


#write a function that takes 2 variables, the first gets printed the number of times indicated by the second number
# example: function(1,5) would print 1,1,1,1,1
# example: function("hello",2) would print hello hello


# write a function that takes in an integer and prints the first 5 numbers that are divisible by 5 after the input
# example: function(3) would print 5,10,15,20,25
# example: function(105) would print 110,115,120,125,130


# write a function that takes a start and end value and prints every value in between
# NOTE: end can be greater OR less than start
# example: function(1,5) would print 1,2,3,4,5
# example: function(6,3) would print 6,5,4,3


# write a function that takes an input and prints square numbers less than the input (starting with 1)
# example: function(10) would print 1,4,9
# example: function(101) would print 1,4,9,16,25,36,49,64,81,100



if __name__ == "__main__":
    whileExample(1, 7)
    forExample(1, 7)