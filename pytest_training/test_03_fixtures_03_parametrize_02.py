import pytest
import requests

list_a = [('https://www.sohu.com',200),
        ('https://www.sina.com.cn',200),
        ('https://www.sina.com.cn',200),
        ('https://www.hlgnet.com',200)]
list_id =['1','2','3','4']

@pytest.fixture(params=list_a,ids = list_id)
def list_fuc(request):
    return request.param

def test_str(list_fuc):
    ret = requests.get(list_fuc[0])
    assert ret.status_code == list_fuc[1]
