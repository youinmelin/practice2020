import turtle as tu

tu.bgcolor('black')
tu.colormode(255)
tu.penup()
tu.goto(0,100)
tu.pendown()
i=0
while i<18:
    tu.pencolor(0,255,0)
    tu.circle(i*i)
    tu.right(i*2)
    i=i+1

tu.done()
