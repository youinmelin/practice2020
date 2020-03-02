import pytest

num_list = [5,3,6,2,1,9,0,4,6]

@pytest.fixture
def list_a():
    return max(num_list)

@pytest.fixture(params = num_list)
def list_num(request):
    return request.param

def test_max(list_a):
    assert list_a == 9

def test_param(list_num):
    assert list_num > 0
