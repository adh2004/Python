from creditCard import CreditCard
from debitCard import DebitCard




def chooseCreditCard(cardNum, custName):
    cardType = CreditCard(cardNum, custName)
    rate = float(input('Enter interest rate: '))
    limit = int(input('Enter credit limit: '))
    cardType.inputInfo(rate,limit)
    cardType.displayIdName()
    cardType.displayInfo()

def chooseDebitCard(cardNum, custName):
    cardType = DebitCard(cardNum, custName)
    pin = int(input('Enter pin number: '))
    fund = float(input('Enter fund available: '))
    cardType.inputInfo(cardNum, custName)
    cardType.displayIdName()
    cardType.displayInfo()

def main():
    number = int(input('Enter card number: '))
    name = input('Enter customer name: ')

    choice = int(input('Enter 1 for credit card and 2 for debit card: '))

    if choice == 1:
        chooseCreditCard(number, name)
    elif choice == 2:
        chooseDebitCard(number, name)
main()
