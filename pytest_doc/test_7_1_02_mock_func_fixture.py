# monkeypatching functions

from pathlib import Path
import pytest

def getssh():
    return Path.home() # WindowsPath('C:/Users/Administrator')

@pytest.fixture
def mock_response(monkeypatch):
    def mock_path():
        return Path('/abc')
    monkeypatch.setattr(Path, 'home', mock_path)

def test_getssh(mock_response):
    x = getssh()
    assert x == Path('/abc')
