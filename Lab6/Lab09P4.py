def getScores(name):
    i = 1

    _list = []
    while i <= 2:
        if i == 1:
            _list.append(float(input("Enter first score of %s : "% name)))
        else:
            _list.append(float(input("Enter second score of %s : "% name)))
        i += 1
    return _list

def printScores(name,_list):
    print("Scores of %s :" % name)
    for i in _list:
        print(i)

Amy = getScores("Amy")
Beth = getScores("Beth")
Connie = getScores("Connie")
x = 0
athletes = [Amy,Beth,Connie]
while x <= len(athletes):
    if x == 0:
        printScores("Amy",athletes[x])
    elif x == 1:
        printScores("Beth",athletes[x])
    elif x == 2:
        printScores("Connie", athletes[x])

    x += 1

