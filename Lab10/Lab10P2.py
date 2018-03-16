import length

def main():
    inches = 0
    feet = 0
    m = 0
    cm = 0
    miles = 0
    km = 0

    inches = int(input('How many inches?: '))
    cm = length.inches_to_cm(inches)
    print('It is equivalent to ', cm , ' cm')

    feet = int(input('How many feet?: '))
    m = length.feet_to_m(feet)
    print('It is equivalent to ', m , ' m')

    miles = int(input('How many miles?:'))
    km = length.miles_to_km(miles)
    print('It is equivalent to ', km , ' km')

main()
