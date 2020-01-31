import turtle as tu

tu.bgcolor('black')
tu.speed(10)
a=9
i=1
while i<a+4:
    if i<=a/3:
        tu.color('yellow')
    elif i<=2*(a/3):
        tu.color('green')
    elif i<=3*(a/3):
        tu.color('red')
    tu.circle(100,90)
    tu.left(30)
    i=i+1
tu.done()