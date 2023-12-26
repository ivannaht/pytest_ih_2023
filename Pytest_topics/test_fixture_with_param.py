from Pytest_topics.conftest import cross_browser


def test_case01(cross_browser):
    print(cross_browser)
    assert 2 + 2 == 4

def test_case02(cross_browser):
    print(cross_browser)
    assert 2 - 2 == 0
