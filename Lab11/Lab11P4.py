def verifyInput(productCode):
    digit_Verify = productCode.isdigit()
    print()
    return digit_Verify

def verifyLength(productCode):
    if len(productCode) == 4:
        length_Verify = True
        return length_Verify
    else:
        length_Verify = False
        print('Error code must not be greater or shorter than 4')
        return length_Verify

def verifyDigit(productCode):
    if productCode[-1] != '4' or productCode[-1] != '7':
        digit_Verify = False
        print('Error the last digit must be 4 or 7')
        return digit_Verify
    else:
        digit_Verify = True
        return digit_Verify

def checkState(productCode):
    if productCode[-1] == '4':
        print('This orange is from California')
    elif productCode[-1] == '7':
        print('This orange is from Florida')

def main():
    prod_code = input('Enter product code: ')
    prod_code = prod_code.strip()

    digits_OK = verifyInput(prod_code)
    length_OK = verifyLength(prod_code)
    digit_OK = verifyDigit(prod_code)

    while digit_OK == False or length_OK == False or digit_OK == False:
        prod_code = input('Enter product code: ')
        digits_OK = verifyInput(prod_code)
        length_OK = verifyLength(prod_code)
        digit_OK = verifyDigit(prod_code)
    checkState(prod_code)

main()

