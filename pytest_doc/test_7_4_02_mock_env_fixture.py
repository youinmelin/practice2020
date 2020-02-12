import os
import pytest
def get_os_user_lower():
    username = os.getenv('USER')
    if username:
        return username.lower()
    else:
        raise OSError('USER enviorment is not set.')

@pytest.fixture
def mock_env_user(monkeypatch):
    monkeypatch.setenv('USER', 'TestingUser')

@pytest.fixture
def mock_env_missing(monkeypatch):
    monkeypatch.delenv('USER', raising=False)

def test_upper_to_lower(mock_env_user):
    assert get_os_user_lower() == 'testinguser'

def test_raise_exception(mock_env_missing):
    with pytest.raises(OSError):
        e = get_os_user_lower()
