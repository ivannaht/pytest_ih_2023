import pytest


@pytest.mark.usefixtures("user_data")
class TestFixtureWithData:

    def test_case01(self, user_data):
        print(user_data)
        assert 2 + 2 == 4

    def test_case02(self, user_data):
        print(user_data)
        assert 2 - 2 == 0
