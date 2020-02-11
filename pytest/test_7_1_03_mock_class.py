
from pathlib import Path

def getpath():
    return Path.home()

class MockResponse:
    def mockreturn():
        return Path('/abc')

def test_getpath(MockResponse):
    def mockresponse():
        return MockResponse()

    monkeypatch.setattr(path, 'home', mockreturn)
    xpath = getpath()
    assert xpath == mockresponse
