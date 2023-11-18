class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_rectangle_area(self) -> object:
        return self.length * self.width

    def calculate_rectangle_perimeter(self) -> object:
        return 2 * (self.length + self.width)

