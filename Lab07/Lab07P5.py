def main():
    scoreList = []
    i = 0

    while i <= 4:
        scoreList.append(float(input("Enter a score: ")))
        i += 1
    score_calculator(scoreList)

def score_calculator(_list):
    i = 0
    for  item in _list:
        i += item
    average = i/5
    print("The average score is: ",average)

main()

