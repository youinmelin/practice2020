import pytest
import requests

@pytest.fixture()
def req():
    url = 'http://www.sina.com.cn'
    ret = requests.get(url)
    return ret

def test_ret(req):
    assert req.status_code == 200
