# mock一个ppp函数，ppp名字随便写？目的就是让requests.get()的结果能够通过
# MockResponse类中的ppp方法传递到mock_get中，这是我的理解
import pytest
import requests

def get_json(url):
    r = requests.get(url)
    return r

class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def ppp():
        return {'mock_key': 'mock_response'}

@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

def test_get_json(mock_response):
    result = get_json('https://fakeurl')
    print('type', type(result))
    assert result.ppp() == {'mock_key': 'mock_response'}

