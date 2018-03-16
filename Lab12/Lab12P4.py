import math
def calculateArea():
    error = True
    while error == True:
        try:
            area = 0

            radius = float(input('Enter radius: '))
            area = math.pi * math.pow(radius, 2)
            print('Area of the circle: ', area)
            error = False
        except ValueError:
            print('Invalid input')


def main():
    calculateArea()

main()
