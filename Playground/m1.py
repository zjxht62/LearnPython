class Bike:
    def __init__(self, name):
        self.name = name


class MountainBike(Bike):
    def __init__(self):
        super(MountainBike, self).__init__("山地车")


class RoadBike(Bike):
    def __init__(self):
        super(MountainBike, self).__init__("公路车")


class BikeFactory:
    @staticmethod
    def make_bike(type):
        if type == 0:
            return MountainBike()
        elif type == 1:
            return RoadBike()


bike = BikeFactory.make_bike(0)
print(type(bike))  # <class '__main__.MountainBike'>
print(bike.name)  # 山地车
