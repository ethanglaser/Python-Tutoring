# Git review - clone, add, commit, push, branches
# check in on particular topics - 
# more project ideas - other games (hangman, )
# review file I/O, strings - write function that takes coordinate string and returns x, y
# matplotlib intro - hist and scatter


import matplotlib.pyplot as plt

def processcoord(coordtext):
    coordlist = coordtext[1:-2].split(',')
    return float(coordlist[0]), float(coordlist[1])

def processfile(loc):
    with open(loc, 'r') as f:
        data = f.readlines()
    x = []
    y = []
    for point in data:
        vals = processcoord(point)
        x.append(vals[0])
        y.append(vals[1])
    histscatter(x, y)

def histscatter(x, y):
    plt.hist(y)
    plt.show()
    plt.figure()
    plt.xlabel('Number of hours studied')
    plt.ylabel('Test score')
    plt.ylim([0,100])
    plt.title("Test performance based on studying")
    plt.scatter(x,y)
    plt.show()

if __name__ == "__main__":
    processfile("../Data Files/xydata.txt")
