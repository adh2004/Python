donorCount = int(input('How many people made donations today? '))
sentinel = 0
Total = 0

while donorCount != sentinel:
    runningTotal = float(input('Enter amount of donation: '))
    Total = Total + runningTotal
    donorCount = donorCount - 1
print('Total amount of money raised today: ', Total)
