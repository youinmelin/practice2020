import pytest
import tasks
from tasks import Task

@pytest.fixture()
def tasks_db(tmpdir):
    '''prepare for the test. before the test, build the db envirment'''
    tasks.start_tasks_db(str(tmpdir),'tiny')
    yield
    tasks.stop_tasks_db()

def test_add_return_valid_id(tasks_db):
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id,int)

def test_add_return_valid_id2(tasks_db):
    new_task = Task('do anything')
    task_id = tasks.add(new_task)
    assert type(task_id)==int
