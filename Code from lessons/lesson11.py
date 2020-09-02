def leapyear(year):
    #print true if leap year print false if not
    if year % 400 == 0:
        return True

def readfile():
    with open('firsttext.txt', 'r') as f:
        text = f.readlines()
    print(text)

if __name__ == "__main__":
    leapyear(2020)
    readfile()