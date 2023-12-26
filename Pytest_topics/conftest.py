import pytest


@pytest.fixture()
def setup():
    print(f"\nBefore test execution")
    yield
    print(f"\nAfter test execution")
