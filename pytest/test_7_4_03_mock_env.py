import os 

def test_change_env(monkeypatch):
    username1 = os.getenv("USER")
    print('username1 :', username1)

    monkeypatch.setenv('USER', 'big_name')
    username2 = os.getenv("USER")
    print('username2 :', username2)
