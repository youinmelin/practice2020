def fibonacci(num):
    n1 = 0
    n2 = 1
    c = 0
    while c < num:
        c += 1
#        print (f'{c}:{n1}')
        yield n1
        n1, n2 = n2, n1 + n2
    return 'finished'

fi = fibonacci(10)
while True:
    try:
        ret = next(fi)
        print(ret)
    except Exception as e:
        print(e.value)
        break