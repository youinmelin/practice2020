import os
import pytest
def get_os_user_lower():
    username = os.getenv('USER')
    if username is None:
        raise OSError('USER enviroment is not set')
    return username.lower()

def test_upper_to_lower(monkeypatch):
    monkeypatch.setenv('USER', "TestingUser")
    assert get_os_user_lower() == 'testinguser'

def test_raise_exception(monkeypatch):
    monkeypatch.delenv('USER', raising=False)
    with pytest.raises(OSError):
        _ = get_os_user_lower()
        print('_:',_)
