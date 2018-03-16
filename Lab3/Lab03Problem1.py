midterm = int(input('Enter midterm score:'))
final = int(input('Enter final score:'))
bonus = 5
bonusQualifier = 20

if final > (midterm + bonusQualifier):
    totalScore = midterm + final
    bonusTotal = midterm + final + bonus
    print('Total Score: ',totalScore)
    print('5 bonus point added to total for meeting improved target.')
    print('New total score: ',bonusTotal)
else:
    totalScore = midterm + final
    print('Total Score: ',totalScore)





