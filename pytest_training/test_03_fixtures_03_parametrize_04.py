import pytest

list_add = [(1,2,3),(11,12,23),(90,10,100),(0,0,0),(-1,-5,-6)]

@pytest.fixture(params=list_add)
def add(request):
    return request.param

def test_add(add):
    assert add[0] + add[1] == add[2]
