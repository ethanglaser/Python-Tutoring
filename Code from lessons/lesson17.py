import os
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

    print(a['e'])
    # A. 10
    # B. 11
    # C. 9
    # D. 5
    # E. Error

    print(a['b'] - a['c'])
    # A. 0
    # B. -6
    # C. -5
    # D. 6
    # E. Error    

    print(a['b']['d'] - a['d'])
    # A. 2
    # B. -6
    # C. -4
    # D. -3
    # E. Error  




if __name__ == "__main__":
    #quiz()
    print(os.listdir("../ProjectData"))