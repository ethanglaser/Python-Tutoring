# quiz - dictionaries
# project check-in
# os - listdir()
# strings - contains, split
# NLP Project - several mystery files mystery-#.txt, create dictionary with # as key and language as value


# QUIZ
def quiz():
    a = {}
    b = {"d": 1, "e": 5, "f": 4}
    c = {"c": 2, "d": 3, "e": 6}
    a['b'] = b
    a['c'] = 6
    a['d'] = 4
    a['e'] = b['e'] + c['e']

    #print(a['e'] + b['e'] + c['e'])


def sets():
    mylist = [1,2,3,2,1]
    myset = set(mylist)
    print(myset)
    if 3 in mylist:
        print('yes')
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    mystring = "soidughaoipghjpoaijslkkjlqhkjlhksjlhkjxhvkjheiojpopqaoijzoijxlkjlsfkjlkjsldkjzvcasdkjflkasjdfklalsfdj"
    myset2 = set(mystring)
    print(myset2)
    print(len(myset2))

    print(len(set(letters)))

    print(set(letters) - myset2)

if __name__ == "__main__":
    quiz()
    sets()
