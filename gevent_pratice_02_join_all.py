from gevent import monkey
import gevent
import time

monkey.patch_all()

def func(num,func_name):
    for i in range(num):
        print(f'--------------{func_name}:{i}--------------')
        time.sleep(0.5)
gevent.joinall([
    gevent.spawn(func,10,'f1'),
    gevent.spawn(func,10,'f2')
])
