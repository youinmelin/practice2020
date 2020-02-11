import os 
import pytest

@pytest.fixture
def change_env(monkeypatch):
    username1 = os.getenv("USER")
    print('username1 :', username1)

    monkeypatch.setenv('USER', 'big_name')

def test_env(change_env):
    username2 = os.getenv("USER")
    print('username2 :', username2)
    assert username2 == 'big_name'
