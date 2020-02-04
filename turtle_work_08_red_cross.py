import turtle as tu
tu.color('red',"red")
i=0
tu.hideturtle()
tu.begin_fill()
times = 8
while i<times:
    tu.forward(100)
    tu.right(90)
    tu.forward(20)
    tu.right(90)
    tu.forward(100)
    tu.left(180-360/times)
    i+=1
tu.end_fill()
tu.hideturtle()
tu.done()
