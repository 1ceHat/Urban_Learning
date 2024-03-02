class Building:
    def __init__(self, numFloor=None, type=None):
        self.numberOfFloors = 0
        self.buildType = "House"
        if numFloor: self.numberOfFloors = numFloor
        if type: self.buildType = type

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors) and (self.buildType == other.buildType)

my_house = Building(numFloor=9)
second_house = Building(type="Hospital", numFloor=3)
print(f"Я первая постройка! Мой тип {my_house.buildType}. Я {my_house.numberOfFloors}-этажная постройка.")
print(f"Я вторая постройка! Мой тип {second_house.buildType}. Я {second_house.numberOfFloors}-этажная постройка.")
print(my_house == second_house)


