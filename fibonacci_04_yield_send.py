def fibonacci(num):
    n1 = 0
    n2 = 1
    c = 0
    while c < num:
        c += 1
#       print (f'{c}:{n1}')
        receive = yield n1
        print('>>>ret<<<',receive)
        n1, n2 = n2, n1 + n2
    return 'finished'

fi = fibonacci(10)
ret = next(fi)
print(ret)
ret = fi.send('***')
#send传递参数给yeild,注意第一次执行不能用传递非None参数的send，因为第一次运行无法接收参数
print(ret)
ret = fi.send('ABC')
print(ret)


#while True:
#    try:
#        ret = next(fi)
#        print(ret)
#    except Exception as e:
#        print(e.value)
#        break
