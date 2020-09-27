
def firstfunction(filename):
    with open('Data Files/' + filename, 'r') as f:
        data = f.readlines()
    return data
    '''if numbers == False:
        return data

    
    intdata = []
    for line in data:
        intdata.append(int(line))
    return intdata


def buildings():
    buildingsData = firstfunction('buildings10.txt', True)
    print(max(buildingsData))'''

def longword():
    words = firstfunction('manyWords.txt')
    newWords = []
    for word in words:
        newWords.append(word.strip())
    print(newWords)
    leng = 0
    for word in words:
        if len(word) > leng:
            leng = len(word)
            big = word
    print(big)

if __name__ == "__main__":
    #print(firstfunction('sample.txt', True))
    #buildings()
    longword()

