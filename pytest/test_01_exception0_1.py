import pytest
import tasks

def test_raises():
    with pytest.raises(TypeError) as excinfo:
        tasks.add(task = 'no a Task object')
    print ('------',excinfo)
