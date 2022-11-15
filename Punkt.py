import math


class Punkt:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y) + " z: " + str(self.z)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

punkt1 = Punkt(0, 0, 0)
punkt2 = Punkt(1, 2, 3)

print("Distance: ", punkt1.distance(punkt2))
