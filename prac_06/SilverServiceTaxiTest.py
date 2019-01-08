from prac_06.SilverServiceTaxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test Fancy Taxi", 200, 2)
    taxi.drive(0)
    print(taxi)
    print(taxi.get_fare())

main()
