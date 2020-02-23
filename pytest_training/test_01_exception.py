import pytest
import tasks

def test_raises1():
    with pytest.raises(Exception) as excinfo:
        '1'/'b' 
    print(excinfo.type)
def test_raises2():
    with pytest.raises(ZeroDivisionError) as excinfo:
        a = 5 / 0
