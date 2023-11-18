import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circle_area(self) -> object:
        return math.pi * self.radius ** 2

    def calculate_circle_perimeter(self) -> object:
        return math.pi * self.radius * 2

