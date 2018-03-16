
sentinel = 'y'
upperSentinel = sentinel.capitalize()

while upperSentinel == 'Y':
    collegeName = input('Enter name of college:')
    tuition = float(input('Enter tuition:'))
    room = float(input('Enter room:'))
    board = float(input('Enter board:'))
    miscExpenses = float(input('Enter other expenses:'))
    finAid = float(input('Enter financial aid:'))
    Total = (tuition + room + board + miscExpenses) - finAid
    print('Out-of-pocket cost for this college: ',Total)
    sentinel = input('Calculate cost for another college? [y/n]')
    upperSentinel = sentinel.capitalize()
