import requests

def get_json(url):
    r = requests.get(url)
    return r.json()

class MockResponse:

    @staticmethod
    def json():
        return {'mock_key': 'mock_response'}

def test_get_json(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)
    print('mock_get:', mock_get())
    print(MockResponse())

    result = get_json('https://fakeurl')
    assert result['mock_key'] == 'mock_response'

