import pytest

def add(a,b):
    return a+b

def test_add():
    c = add(2,3)
    assert 5 == c

@pytest.fixture
def add2():
    return 2+3

def test_add2(add2):
    assert 5 == add2
