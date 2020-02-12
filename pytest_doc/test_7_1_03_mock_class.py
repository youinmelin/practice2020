# 通过类传递值到test函数，失败，原因目前还搞不清楚2020-2-8

from pathlib import Path

def getpath():
    return Path.home()

class MockResponse:
    @staticmethod
    def mockreturn():
        return '/abc'

def test_getresopnse(monkeypatch):
    def getmock(*args, **kwargs):
        return MockResponse()
    print(getmock())
    print(getmock)
    monkeypatch.setattr(Path, 'home', getmock)
    xpath = getpath()
    print('xpath',xpath)
    assert xpath == '/abc'

#getresopnse()
