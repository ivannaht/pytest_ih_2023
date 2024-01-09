import pytest

from Pytest_topics.loops import *

data_1 = [
    ("100101", [True, False, False, True, False, True]),
    ("10", [True, False]),
    ("001", [False, False, True]),
]


@pytest.mark.parametrize("input_value, output_value", data_1)
def test_integer_boolean(input_value, output_value):
    """verify integer_boolean function"""
    assert integer_boolean(input_value) == output_value


data_2 = [
    ("Celebration", 5),
    ("HJHKKttt", 0),
    ("Palm", 1),
    ("Prediction", 4),
    ("Y-+56565i", 1)
]


@pytest.mark.parametrize("input_value, output_value", data_2)
def test_count_vowels(input_value, output_value):
    """verify count_vowels function"""
    assert count_vowels(input_value) == output_value


data_3 = [
    (1, "1"),
    (5, "101"),
    (10, "1010"),
    (25, "11001"),
    (0, "0")
]


@pytest.mark.parametrize("input_value, output_value", data_3)
def test_binary(input_value, output_value):
    """verify binary function"""
    assert binary(input_value) == output_value


data_4 = [
    (25, 2, "11001"),
    (25, 16, "19")
]


@pytest.mark.parametrize("input_value1, input_value2, output_value", data_4)
def test_base_converter(input_value1, input_value2, output_value):
    """verify base_converter function"""
    assert base_converter(input_value1, input_value2) == output_value


data_5 = [
    (42, 3),
    (12345, 3),
    (1024, 2)
]


@pytest.mark.parametrize("input_value, output_value", data_5)
def test_mean(input_value, output_value):
    """verify mean function"""
    assert mean(input_value) == output_value


data_6 = [
    ("Algorithm", True),
    ("PasSword", False),
    ("Consecutive", False)
]


@pytest.mark.parametrize("input_value, output_value", data_6)
def test_is_isogram(input_value, output_value):
    """verify is_isogram function"""
    assert is_isogram(input_value) == output_value


data_7 = [
    (),
    (),
    ()
]

