
def stripCharacters(number):
    number.strip('')

    for c in number:
        if c == '(':
            number = number.replace('(','')
        elif c == ')':
            number = number.replace(')','')
        elif c == '-':
            number = number.replace('-','')
    return number


def main():
    num1 = input('Enter phone number: ')
    print('Phone number with extra characters stripped: ', stripCharacters(num1))

    num2 = input('Enter phone number: ')
    print('Phone number with extra characters stripped: ', stripCharacters(num2))

    num3 = input('Enter phone number: ')
    print('Phone number with extra characters stripped: ', stripCharacters(num3))

main()
