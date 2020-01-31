import turtle as tu

tu.color('red','red')
tu.hideturtle()
tu.bgcolor('black')
i=0
tu.begin_fill()
tu.speed(12)
#times = int(input("请输入次数："))
times = 3
while i<times:

    tu.forward(i+30)
    tu.left(90)
    tu.forward(20)
    tu.left(90)
    tu.forward(50)
    tu.right(180-360/times)
    i=i+1
#tu.end_fill()
tu.done()