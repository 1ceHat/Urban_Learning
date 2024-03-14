class Car:
    horsePow = 0
    def __init__(self, horse_power=None):
        self.price = 1000000
        if horse_power:
            Car.horsePow = horse_power

    def horse_powers(self):
        return self.horsePow


class Nissan(Car):

    def __init__(self):
        self.price = 2500000

    def horse_powers(self, horse_power):
        self.horsePow = horse_power
        print("Now {}'s horse powers is {}".format(self.__class__.__name__,
                                                   self.horsePow))


class Kia(Car):
    def __init__(self):
        self.price = 1700000

    def horse_powers(self, multip):
        self.horsePow = int(self.horsePow * multip)
        print("Now {}'s horse powers is {}".format(self.__class__.__name__,
                                                   self.horsePow))


car_prototype = Car(horse_power=100)
nissan_gtr = Nissan()
kia_rio = Kia()

print("Car prototype's horse powers is", car_prototype.horse_powers())
nissan_gtr.horse_powers(horse_power=200)
kia_rio.horse_powers(multip=1.5)
