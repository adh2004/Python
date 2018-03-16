def scanPrices():
    item_price = []
    sentinel = 0
    subtotal = 0

    while sentinel != -1:
        if len(item_price) > 0:
            item_price.append(float(input('Enter price of next item[or -1 to stop]: ')))
        else:
            item_price.append(float(input('Enter price of first item[or -1 to stop]: ')))

        if item_price[-1] == -1:
            sentinel = item_price[-1]
            item_price.remove(-1)

    for price in item_price:
        subtotal = subtotal + price

    print('Subtotal: ', subtotal)
    return subtotal

def scanCoupons():
    coupons = []
    sentinel = 0
    coupon_total = 0

    while sentinel != -1:
        if len(coupons) > 0:
            coupons.append(float(input('Enter value of next coupon[or -1 to stop]: ')))
        else:
            coupons.append(float(input('Enter value of first coupon[or -1 to stop]: ')))

        if coupons[-1] == -1:
            sentinel = coupons[-1]
            coupons.remove(-1)

    for coups in coupons:
        coupon_total = coupon_total + coups

    return coupon_total


def clubMember():
    sentinel = ""
    sUpper = sentinel.upper()

    while sUpper != 'Y' or sUpper != 'N':
        sentinel = input('Are you a member of the Wake-Mart Club? [y/n]: ')
        sUpper = sentinel.upper()

        if sUpper == 'Y':
            return True
        else:
            return False

def makePayment(balance):
    i = 0
    print('Payment Options:')
    i = int(input('Enter 1 for cash, 2 for debit: '))

    if i == 1:
        payCash(balance)
    elif i == 2:
        payDebit(balance)

def payDebit(balance):
    debit_card = ""
    pin = ""
    pay_amt = 0
    debit_card = input('Please enter a 16-digit card number: ')
    pin = input('Please enter a 4-digit pin: ')
    pay_amt = float(input('Please enter payment amount: '))

    if pay_amt > balance:
        balance = pay_amt - balance
        print('Cash back: ', balance)

def payCash(balance):
    amt_paid = balance
    insert_amt = 0
    print('This machine only accepts $10, $5 and $1 bills')


    while balance > 0:
        insert_amt = float(input('Please enter 10, 5, or 1: '))
        if insert_amt == 10:
            print('$10 bill inserted')
            if balance > insert_amt:
                balance = balance - insert_amt
                print('Balance: ' , balance)
            elif balance < insert_amt:
                balance = balance - insert_amt
                print('Change: ' , abs(balance))
        elif insert_amt == 1:
            print('$1 bill inserted')
            if balance > insert_amt:
                balance = balance - insert_amt
                print('Balance: ' , balance)
            elif balance < insert_amt:
                balance = balance - insert_amt
                print('Change: ' , abs(balance))

        elif insert_amt == 5:
            print('$5 bill inserted')
            if balance > insert_amt:
                balance = balance - insert_amt
                print('Balance: ' , balance)
            elif balance < insert_amt:
                balance = balance - insert_amt
                print('Change: ' , abs(balance))


def main():
    print('Welcome to the self checkout system of Wake-mart')
    subTotal = scanPrices()
    coupons = scanCoupons()
    new_subTotal = subTotal - coupons
    print('New subtotal: ', new_subTotal)
    member = clubMember()

    if member == True:
        new_subTotal = new_subTotal * .95
        print('New subtotal after membership discount: ', new_subTotal)

    makePayment(new_subTotal)
main()
