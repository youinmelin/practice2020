# mock一个ppp函数，ppp名字随便写？目的就是让requests.get()的结果能够通过
# MockResponse类中的ppp方法传递到mock_get中，这是我的理解
# 通过函数的返回值直接返回value，r后边就不用加函数名。
# 看这个例子是直接在value处填写数据，失败，错误提示是 TypeError: 'dict' object is not callable,看来还是需要函数
import pytest
import requests

def get_json(url):
    r = requests.get(url)
    return r

def test_get_json(monkeypatch):
    monkeypatch.setattr(requests, 'get',{'mock_key': 'mock_response'})
    result = get_json('https://fakeurl')
    print('type', type(result))
    assert result == {'mock_key': 'mock_response'}

