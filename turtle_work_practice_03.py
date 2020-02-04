import turtle as tu
from time import sleep
import random

tu.bgcolor('black')
tu.colormode(255)
for i in range(50):
    tu.penup()
    x=random.randint(-255,255)
    y=random.randint(-255,255)
    z=random.randint(-255,255)
    tu.fillcolor(abs(x),abs(y),abs(z))
    tu.setposition(x,y)
    tu.pendown()
    tu.begin_fill()
    tu.circle(random.randint(8,18))
    tu.end_fill()
tu.done()

