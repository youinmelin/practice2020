import time

def add_str(arg):
    def func():
        data = '--- '+arg()+' ---'
        #print(data)
        return data
    return func

def count_time(arg):
    def func():
        time0 = time.time()
        ret = str(arg())
        time1 = time.time()
        #print(time1 - time0,'s')
        return str(time1 - time0 )+'>>>'+ ret
    return func

@add_str
@count_time   # main = count_time(main)
def main():
    n = 100000
    suma = 0
    for i in range(n+1):
        suma += i
    # i = 0
    # while i < n:
    #     suma += i
    #     i += 1
    return (str(suma))
    

if __name__ == '__main__':
    print(main())
