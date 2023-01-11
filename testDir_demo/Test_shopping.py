import pytest
@pytest.mark.parametrize("user,password",[("admin","123"),("user","1234")])
def test_u(user,password):
    if user=="admin" and password=="123" :
        assert True
    if user=="user" and password=="1234" :
        assert True
    else:
        assert False
@pytest.mark.parametrize("price",[100,200,98,600,500])
def test_cart(price):
    if price >100:
        assert True
    else:
        assert False
@pytest.mark.smoke
def test_logout():
    print("logout")