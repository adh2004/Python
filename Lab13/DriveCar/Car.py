class Car:
    def __init__(self, car_make, car_model):

        self.make = car_make
        self.model = car_model
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def decelerate(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0
