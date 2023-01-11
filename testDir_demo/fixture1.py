import pytest
@pytest.fixture
def log():
    print("entering")
    print("login")
    yield
    print("logout")
def test_add(log):
    print("adding")
def test_dele(log):
    print("deleting")