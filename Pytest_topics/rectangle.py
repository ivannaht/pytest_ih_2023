import pytest
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_rectangle_area(self):
        if not isinstance(self.length, (int, float)):
            raise TypeError("Length must be a number")
        if not isinstance(self.width, (int, float)):
            raise TypeError("Width must be a number")
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Length and width must be positive")
        return self.length * self.width

    def calculate_rectangle_perimeter(self):
        if not isinstance(self.length, (int, float)):
            raise TypeError("Length must be a number")
        if not isinstance(self.width, (int, float)):
            raise TypeError("Width must be a number")
        if self.length <= 0 or self.width <= 0:
            raise ValueError("Length and width must be positive")
        return 2 * (self.length + self.width)
