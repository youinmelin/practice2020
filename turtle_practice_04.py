import turtle as tu
import random

tu.colormode(255)
tu.bgcolor(0,0,0)
tu.speed(20)
i = 0
#tu.hideturtle()
while i < 80:
    radius = random.randint(8, 18)
    tu.begin_fill()
    tu.circle(radius)
    tu.end_fill()
    tu.pencolor(0,200,0)
    x = random.randint(-255,255)
    y = random.randint(-255,255)
    z = random.randint(-255, 255)
    tu.color((abs(x),abs(y),abs(z)),(abs(x),abs(y),abs(z)))
    tu.penup()
    tu.goto(x,y)
    tu.pendown()
    # print(radius)
    i += 1

tu.done()