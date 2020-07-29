# Write a function that takes in a number and prints the sum of all numbers squared up to and including that value
# example: function(3) = 1 + 4 + 9 = 13
def sumSquared(number):
    total = 0
    for value in range(number + 1):
        total += (value ** 2)
    print(total)


# Write a function that takes in two numbers and finds the smallest number that is evenly divsible by both numbers (least common multiple)
# I recommend using a while loop
# example: function(4,6) = 12
# example: function(8,20) = 40


# Write a function that takes in two numbers and finds the largest number that evenly divides each number (greatest common factor)
# Again I recommend using a while loop
# example: function(24,60) = 12
# example: function(32,49) = 1


# Write a function that takes a list of values and adds them all together and prints the sum
# example: function([1,5,3,11]) would print 20
# example: function([100,300]) would print 400


# Write a function that takes a list of values and a number
# The function should determine how many values in that list are greater than the specified number
# example: function([1,2,3,4,5,6,7], 4) would print 3 because 3 values in the list are greater than 4
# example: function([9,10,11], 20) would print 0 because none of the values in the list are greater than 20


if __name__ == "__main__":
    sumSquared(20)