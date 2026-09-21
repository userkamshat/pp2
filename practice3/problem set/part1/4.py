import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return math.sqrt(
            (self.x - other.x) ** 2 +
            (self.y - other.y) ** 2
        )


p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()

p1.move(3, 5)
p1.show()

print(p1.dist(p2))