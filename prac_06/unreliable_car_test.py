from prac_06.unreliable_car import UnreliableCar

car_1 = UnreliableCar("GULI", 100, 95)
car_2 = UnreliableCar("FILI", 100, 5)

for i in range(1,5):
    print("Attempt to drive {} km:".format(i))
    print("{} drove {}km".format(car_1.name,car_1.drive(i)))
    print("{} drove {}km".format(car_2.name,car_2.drive(i)))

print(car_1)
print(car_2)
