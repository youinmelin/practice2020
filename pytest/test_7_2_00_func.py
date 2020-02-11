# mock一个ppp函数，ppp名字随便写？目的就是让requests.get()的结果能够通过
# MockResponse类中的ppp方法传递到mock_get中，这是我的理解
import pytest
import requests

def get_json(url):
    r = requests.get(url)
    return r


def mock_response(monkeypatch):
    def ppp():
        return {'mock_key': 'mock_response'}

    monkeypatch.setattr(requests, 'get', ppp)

def test_get_json(mock_response):
    result = get_json('https://fakeurl')
    print('type', type(result))
    assert result == {'mock_key': 'mock_response'}

