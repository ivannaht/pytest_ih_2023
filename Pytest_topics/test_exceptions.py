import pytest
from Pytest_topics.rectangle import Rectangle


@pytest.mark.usefixtures("setup")
class TestExceptions:

    def test_zero_values(self):
        rect1 = Rectangle(0, 4)
        rect2 = Rectangle(5, 0)
        rect3 = Rectangle(0, 0)
        with pytest.raises(ValueError):
            assert rect1.calculate_rectangle_area()
        with pytest.raises(ValueError):
            assert rect2.calculate_rectangle_area()
        with pytest.raises(ValueError):
            assert rect3.calculate_rectangle_area()

    def test_negative_values(self):
        rect4 = Rectangle(-2, 5)
        rect5 = Rectangle(1, -4)
        rect6 = Rectangle(-3, -5)
        with pytest.raises(ValueError):
            assert rect4.calculate_rectangle_perimeter()
        with pytest.raises(ValueError):
            assert rect5.calculate_rectangle_perimeter()
        with pytest.raises(ValueError):
            assert rect6.calculate_rectangle_perimeter()

    def test_non_number_values(self):
        rect7 = Rectangle('two', 5)
        rect8 = Rectangle(1, 'five')
        rect9 = Rectangle('one', 'seven')
        with pytest.raises(TypeError):
            assert rect7.calculate_rectangle_perimeter()
        with pytest.raises(TypeError):
            assert rect8.calculate_rectangle_perimeter()
        with pytest.raises(TypeError):
            assert rect9.calculate_rectangle_perimeter()
