class Building:
    total = 0
    def __init__(self, numFloor=None, type=None):
        Building.total += 1
        self.numberOfFloors = 1
        self.buildType = "House"
        if numFloor: self.numberOfFloors = numFloor
        if type: self.buildType = type

    def __eq__(self, other):
        return (self.numberOfFloors == other.numberOfFloors) and (self.buildType == other.buildType)

for i in range(40):
    new_build = Building()
    print(f"Я {i+1}-ая постройка! Мой тип {new_build.buildType}. Я {new_build.numberOfFloors}-этажная постройка.")

print(Building.total)


