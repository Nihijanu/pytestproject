import pytest
@pytest.mark.parametrize("num,result",[(2,4),(3,9),(4,16)])
def test_checksquare(num,result):
    assert num*num==result
@pytest.mark.parametrize("u,p",[("admin","123"),("admin1","132")])
def test_users(u,p):
    print(u)
    print(p)
