copies = int(input('How many copies are you buying? '))

if copies <= 10:
    unitPrice = 99
    print('$', unitPrice)
    totalPrice = copies * unitPrice
    print('$', totalPrice)
elif copies > 10 and copies <= 50:
    unitPrice = 89
    print('$', unitPrice)
    totalPrice = copies * unitPrice
    print('$', totalPrice)
elif copies > 50 and copies <= 100:
    unitPrice = 79
    print('$', unitPrice)
    totalPrice = copies * unitPrice
    print('$', totalPrice)
elif copies > 100:
    unitPrice = 69
    print('$', unitPrice)
    totalPrice = copies * unitPrice
    print('$', totalPrice)

