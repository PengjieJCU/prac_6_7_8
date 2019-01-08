from prac_06.Car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.odometer = 0

    def drive(self, distance):
        randomNumber = randint(0,100)
        if randomNumber >= self.reliability:
            distance = 0
        drivingDistance = super().drive(distance)
        return drivingDistance
