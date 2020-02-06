def outside(func):
    def inside(num):
        print('begin--->')
        func(num)
        j = 0
        for i in range(num+1):
            j += i
        print(j)
        print('<---end')
    return inside

@outside  # equal: count = outside(count)
def sum_result(arg):
    #a = 1
    print(arg)

sum_result(100)
