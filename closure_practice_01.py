# function:y=x*k+b ,computer y with giving x,k,b
def line_points(k,b):
    def line_x(x):
        # print (x * k + b)
        return(x * k + b)
    return line_x

line = line_points(1,2)
print(line(0))
print(line(1))
print(line(2))
line = line_points(11,22)
print(line(0))
print(line(1))
print(line(2))
print(line_points(5,6)(1))
