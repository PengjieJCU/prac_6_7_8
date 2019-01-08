from prac_06.Car import Car


def main():
    limo = Car(100)
    limo.add_fuel(20)
    print("fule =",limo.fuel)
    limo.drive(115)

    print("odo =", limo.odometer)
    print(limo)

    print("Car {}, {}".format(limo.fuel, limo.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=limo))


main()
