# mock
import pytest
import requests

def get_json(url):
    r = requests.get(url)
    return r

class MockResponse:

    # mock json() method always returns a specific testing dictionary
    @staticmethod
    def json():
        return {'mock_key': 'mock_response'}

@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

def test_get_json(mock_response):
    result = get_json('https://fakeurl')
    print(type(result))
    assert result['mock_key'] == 'mock_response'

