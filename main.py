class Vehicle:
    def __init__(self):
        super().__init__()
        self.vehicle_type = None


class Car:
    horse_power = 100

    def __init__(self):
        super().__init__()
        self.price = 1000000

    def horse_powers(self):
        return Car.horse_power


class Nissan(Car, Vehicle):

    def __init__(self):
        super().__init__()
        self.price = 2500000
        self.vehicle_type = "car"

    def horse_powers(self):
        self.horse_power = 200
        print("{}'s horse power is {}".format(
            self.__class__.__name__, self.horse_power
        ))


nissan_gtr = Nissan()
print("Nissan GTR's type is {} and price is {}".format(
    nissan_gtr.vehicle_type, nissan_gtr.price)
)
nissan_gtr.horse_powers()