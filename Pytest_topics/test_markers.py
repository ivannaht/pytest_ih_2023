import math

from Pytest_topics.rectangle import Rectangle
from Pytest_topics.circle import Circle


def test_case01():
    rectangle1 = Rectangle(4, 10)
    assert rectangle1.calculate_rectangle_area() == 40, 'verify correct area - passed'


def test_case02():
    rectangle2 = Rectangle(4, 5)
    assert rectangle2.calculate_rectangle_area() == 15, 'verify incorrect area - failed'


def test_case03():
    rectangle3 = Rectangle(5, 10)
    assert rectangle3.calculate_rectangle_perimeter() == 30, 'verify correct perimeter - passed'


def test_case04():
    rectangle4 = Rectangle(2, 5)
    assert rectangle4.calculate_rectangle_perimeter() == 10, 'verify incorrect perimeter - failed'


# verify circle
def test_case05():
    circle1 = Circle(4)
    assert round(circle1.calculate_circle_area(), 2) == 50.27, 'verify correct area - passed'


def test_case06():
    circle2 = Circle(5)
    assert circle2.calculate_circle_area() == 15, 'verify incorrect area - failed'


def test_case07():
    circle3 = Circle(10)
    assert round(circle3.calculate_circle_perimeter(), 2) == 62.83, 'verify correct perimeter - passed'


def test_case08():
    circle4 = Circle(11)
    assert circle4.calculate_circle_perimeter() == 70, 'verify incorrect perimeter - failed'
