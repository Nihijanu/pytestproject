import pytest
@pytest.fixture(scope="session",autouse=True)
def setup():
    print("open the browser")
    print("login")
    yield
    print("logout")