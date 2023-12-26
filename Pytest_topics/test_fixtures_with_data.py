import pytest

from Pytest_topics.base import BaseClass


@pytest.mark.usefixtures("user_data")
class TestFixtureWithData(BaseClass):

    def test_case01(self, user_data):
        log = self.get_logger()
        log.info(user_data)
        assert 2 + 2 == 4

    def test_case02(self, user_data):
        log = self.get_logger()
        log.info(user_data)
        assert 2 - 2 == 0
