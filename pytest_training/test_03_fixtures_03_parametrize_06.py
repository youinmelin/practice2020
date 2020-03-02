import pytest
import sys
# 导入上级目录的模块
sys.path.append('..')
import oo_practice_count_time_arg

list_time = [((10,30,30),(2,45,50),(13,16,20)),
        ((10,3,30),(2,45,0),(12,48,30)),
        ((0,90,80),(2,85,100),(4,58,0))
        ]

@pytest.fixture(params = list_time)
def fix_count(request):
    return request.param

def test_count(fix_count):
    # print ('param:',fix_count[0],fix_count[1])
    # 参数加星号是因为传入的参数应该是三个数，但是列表中的元素是元祖，所以需要拆包
    start_time = oo_practice_count_time_arg.Time(*fix_count[0])
    duration_time = oo_practice_count_time_arg.Time(*fix_count[1])
    end_time = start_time.add_time(duration_time)
    assert end_time == fix_count[2]
