# Write a function that takes in a string and number and prints the last number of characters based on the input number
# example: function("Minnesota", 6) would print 'nesota'
# example: function("Pizza", 3) would print 'zza'


# Write a function that takes in a sentence and finds the number of words in it
# example: function("Python is fun") would return 3


# Write a function that takes in a string and returns the number of vowels in it
# Can assume "y" will not be considered a vowel and that only lowercase letters will be used
# Can use built-in functions (ex: .count())
# example: function("red and blue combine to form purple") would return 11


# Write a function that takes in a string and returns the reverse of the string
# example: function('abcdef') would return 'fedcba'



# Bonus/Challenge:

# Write a function that identifies the most common character in a string
# Can assume that there will be a single most common character
# Treat capital and lowercase letters as separate values
# Can use built-in functions
# example: function("There are 50 states in the United States.") would return 'e'
def findMost(sentence):
    sentence.replace(" ", "")
    maxFrequency = 0
    for letter in sentence:
        if sentence.count(letter) > maxFrequency:
            maxFrequency = sentence.count(letter)
            maxLetter = letter


# Write a function that takes in a string and returns either 'character', 'word', or 'sentence' depending on the input
# example: function('q') would return 'character'
# example: function('Python') would return 'word'
# example: function('Welcome home.') would return 'sentence'
# Assume that all inputs will be one of these three types
# hint: what are defining characteristics of each type?



if __name__ == "__main__":
    