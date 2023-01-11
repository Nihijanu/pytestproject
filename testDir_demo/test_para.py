import pytest
class Testdemo:
    @pytest.mark.parametrize("data",[5,6,10])
    def test_num(self,data):
        if data>5:
            assert True
        else:
            assert False
