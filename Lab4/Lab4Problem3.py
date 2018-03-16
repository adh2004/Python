customerAmount = int(input('How many customers: '))
sentinel = 0
sHFee = 2.99
sellPrice = 4.99
customerNumber = 1

while customerAmount != sentinel:
    print('Customer',customerNumber)
    purchaseCount = int(input('Enter number of discs purchased: '))
    Total = (purchaseCount * sellPrice) + sHFee
    print('Please pay this amount: ',Total)
    customerAmount = customerAmount - 1
    customerNumber = customerNumber + 1



