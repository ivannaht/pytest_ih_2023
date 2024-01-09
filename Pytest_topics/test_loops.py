import pytest

from Pytest_topics.loops import integer_boolean

data_1 = [
    ("100101", [True, False, False, True, False, True]),
    ("10", [True, False]),
    ("001", [False, False, True]),
]


@pytest.mark.parametrize("input_value, output_value", data_1)
def test_integer_boolean(input_value, output_value):
    """verify integer_boolean function"""
    assert integer_boolean(input_value) == output_value

