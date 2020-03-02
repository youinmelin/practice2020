import tasks
import pytest

@pytest.fixture(autouse=True)
def abc(tasks_db,tasks_just_a_few):
    '''tasks_db and tasks_just_a_few are from fixture in conftest.py'''
    for t in tasks_just_a_few:
        print('t:',t)
        tasks.add(t)

def test_add_increases_count():
    tasks.add(tasks.Task('add_new'))
    assert tasks.count() == 4
