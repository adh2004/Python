from customer import Customer


def readPriceList():
    lines = []
    item_code = []
    price = []
    fileName = "price_list.txt"
    price_file = open(fileName, 'r')

    for line in price_file:
        item_code.append(line[:4])
        new_line = line[5:]
        final_price = new_line.replace('\n','')
        price.append(final_price)

    priceDict = dict((zip(item_code,price)))
    return priceDict


def readCouponList():
    lines=[]
    item_code = []
    coupon_price = []
    fileName = "coupon_list.txt"
    coupon_file = open(fileName, 'r')

    for line in coupon_file:
        item_code.append(line[:4])
        new_line = line[5:]
        final_price = new_line.replace('\n','')
        coupon_price.append(final_price)

    couponDict = dict((zip(item_code, coupon_price)))
    return couponDict

def scanPrices():
    priceLookup = readPriceList()
    print('Price List:')
    print(priceLookup)
    product_code = ""
    total = 0.0
    i = 0

    while product_code != "9999":
        product_code = input("Enter product code: ")
        for key in priceLookup.keys():
            if key == product_code:
                i = i + 1

        if i > 0:
            print('Item found  Price: ', priceLookup.get(product_code))
            total = total + float(priceLookup.get(product_code))
            i = 0
        elif i == 0:
                print('Item not found.')
    return total

def scanCoupons():
    couponLookup = readCouponList()
    print('Coupon List:')
    print(couponLookup)
    coupon_code = ""
    total = 0.0
    i = 0

    while coupon_code != "9999":
        coupon_code = input("Enter product code: ")
        for key in couponLookup.keys():
            if key == coupon_code:
                i = i + 1

        if i > 0:
            print('Item found  Price: ', couponLookup.get(coupon_code))
            total = total + float(couponLookup.get(coupon_code))
            i = 0
        elif i == 0:
                print('Item not found.')
    return total

def makePayment(cust: Customer, total):
    secCodeOK = False
    while secCodeOK == False:
        print('Please choose payment method.')
        payment_method = int(input('Please enter 1 for credit card, 2 for debit card: '))

        if payment_method == 1:
            security_code = input('Please enter 3-digit security code: ')
            secCodeOK = cust.verifyCredCard(security_code)
            if secCodeOK == True:
                print('The amount of ', total, ' will be charged to card ending with ', cust.creditCardLastFour())
            else:
                print("Security code incorrect. Payment rejected.")
        elif payment_method == 2:
            pin_code = input('Please enter 4-digit security code: ')
            secCodeOK = cust.verifyDebitCard(pin_code)
            if secCodeOK == True:
                print('The amount of ', total, ' will be charged to card ending with ', cust.debitCardLastFour())
            else:
                print("Security code incorrect. Payment rejected.")
def main():
    print('Welcome to Wake-Mart. Please register.')
    name = input('Enter name: ')
    new_customer = Customer(name)
    new_customer.inputCardInfo()
    print('Registration completed')
    print('\n')
    total = scanPrices()
    coupon_total = scanCoupons()
    adjusted_total = total - coupon_total
    print('Total price: ', total)
    print('Total coupon value: ', coupon_total)
    print('\n')
    print('Please pay this amount: ', adjusted_total)
    makePayment(new_customer, adjusted_total)



main()
