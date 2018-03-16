class Car:
    def __init__(self, car_make, car_model):

        self.__make = car_make
        self.__model = car_model
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def decelerate(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0
    def getSpeed(self):
        return self.__speed
    def __str__(self):
        return 'Car make: ' + self.__make +' Car model: ' + self.__model + ' Car speed: ' + str(self.__speed)
