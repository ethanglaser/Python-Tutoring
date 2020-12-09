# General recommended steps:

# 1. Create a function to read in each file where the language is known (readlines)

# 2. Break each line into n-grams (3 letter sequences) and compile a list of all sequences for each file

# 3. Identify the most common n-grams in each file (Use a dictionary with sequence as key and frequency as value)

# 4. Identify the most common n-grams in the mystery file and compare its most common sequences to the most common sequences for the known languages

# 5. Predict the language of the mystery file


# languageA.txt - most common letters abc,def,ghi,jkl,xyz
# languageB.txt - most common letters aaa,bbb,ccc,ddd,eee

# mystery.txt - most common letters ccc,xyz,eee,prq,bbb


#Alta Edad Media - ['Alt', 'lta', 'ta ', 'a E' ...]


# sort dictionary - sorted(d.items(), key=lambda x: x[1], reverse=True)