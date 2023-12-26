import pytest
from Pytest_topics.user import User


@pytest.fixture()
def setup():
    print(f"\nBefore test execution")
    yield
    print(f"\nAfter test execution")


@pytest.fixture()
def user_data():
    user1 = User("user1", "First", "Last")
    return f"Logged in as {user1.show_user()}"


@pytest.fixture(scope="module", params=["Chrome", "Safari"])
def cross_browser(request):
    return request.param
