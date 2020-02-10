def factorial(n):
    if n == 1:
        return n
    else:
        return(n*cumulation(n-1))

ret = factorial(10)
print(ret)
