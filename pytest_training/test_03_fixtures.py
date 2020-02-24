import pytest

@pytest.fixture()
def abc():
    a_list = []
    b_list = [5,8,10,65,3,63,10,9,17]
    for i in b_list:
        if i > 10:
            a_list.append(i)
    return a_list
def test_add_increases_count(abc):
    assert len(abc) == 3
