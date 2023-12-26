import pytest
from Pytest_topics.circle import Circle
from Pytest_topics.rectangle import Rectangle
pytestmark = [pytest.mark.rectangle, pytest.mark.circle]


# verify rectangle
@pytest.mark.smoke
@pytest.mark.rectangle
def test_case01(setup):
    rect1 = Rectangle(4, 10)
    assert rect1.calculate_rectangle_area() == 40, \
        'verify correct area - passed'


@pytest.mark.rectangle
@pytest.mark.xfail(raises=AssertionError, reason='known issue')
def test_case02(setup):
    rect2 = Rectangle(4, 5)
    assert rect2.calculate_rectangle_area() == 15, \
        'verify incorrect area - failed'


@pytest.mark.rectangle
def test_case03(setup):
    rect3 = Rectangle(5, 10)
    assert rect3.calculate_rectangle_perimeter() == 30, \
        'verify correct perimeter - passed'


@pytest.mark.rectangle
@pytest.mark.xfail
def test_case04(setup):
    rect4 = Rectangle(2, 5)
    assert rect4.calculate_rectangle_perimeter() == 10, \
        'verify incorrect perimeter - failed'


# verify circle
@pytest.mark.smoke
@pytest.mark.circle
def test_case05(setup):
    cir1 = Circle(4)
    assert round(cir1.calculate_circle_area(), 2) == 50.27, \
        'verify correct area - passed'


@pytest.mark.circle
@pytest.mark.xfail
def test_case06(setup):
    cir2 = Circle(5)
    assert cir2.calculate_circle_area() == 15, \
        'verify incorrect area - failed'


@pytest.mark.circle
def test_case07(setup):
    cir3 = Circle(10)
    assert round(cir3.calculate_circle_perimeter(), 2) == 62.83, \
        'verify correct perimeter - passed'


@pytest.mark.circle
@pytest.mark.xfail
def test_case08(setup):
    cir4 = Circle(11)
    assert cir4.calculate_circle_perimeter() == 70, \
        'verify incorrect perimeter - failed'
