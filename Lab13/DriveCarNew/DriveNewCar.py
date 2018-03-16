from Car import Car

def main():
    make = ''
    model = ''
    sentinel = 0


    make = input('Enter car make: ')
    model = input('Enter car model: ')
    new_Car = Car(make, model)
    print(new_Car.__str__())
    print('')

    while sentinel != 3:
        sentinel = int(input('Enter 1 for accelerate, 2 for decelerate or 2 to exit: '))

        if  sentinel == 1:
            new_Car.accelerate()
            print('Car speed: ', new_Car.getSpeed())
        elif sentinel == 2:
            new_Car.decelerate()
            print('Car speed: ', new_Car.getSpeed())
main()
