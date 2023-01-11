import pytest
import sys
@pytest.mark.smoke
def test_login():
    print("login Details")
@pytest.mark.regression
def test_additems():
    print("adding items")
@pytest.mark.smoke
def test_logout():
    print("logout")
@pytest.mark.skipif(sys.version_info < (3,10),reason="will execute")
def test_demo():
    print("Demo skipif")