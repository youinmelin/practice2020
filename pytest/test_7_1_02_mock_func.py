from pathlib import Path

def getssh():
    return Path.home() # WindowsPath('C:/Users/Administrator')

def test_getssh(monkeypatch):
    def mockreturn():
        return Path('/abc')
    monkeypatch.setattr(Path, 'home', mockreturn) 
    x = getssh()
    assert x == Path('/abc')
