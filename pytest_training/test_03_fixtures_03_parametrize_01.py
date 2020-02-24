import pytest

list_a = [('a','a'),('b','b'),('c','d')]
list_id =['1','2','3']

@pytest.fixture(params=list_a,ids = list_id)
def list_fuc(request):
    return request.param

def test_str(list_fuc):
    assert list_fuc[0] == list_fuc[1]
