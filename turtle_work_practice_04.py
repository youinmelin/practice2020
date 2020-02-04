import turtle
from time import sleep
turtle.bgcolor('black')
tt= turtle.Pen()
tt.pencolor('white')

for x in range(5):
    # draw a row
    for i in range(5):
        # draw a square
        for j in range(4):
            tt.forward(50)
            tt.right(90)
        tt.penup()
        tt.forward(50)
        tt.pendown()
    tt.penup()
    tt.right(90)
    tt.forward(50)
    tt.setheading(0)
    tt.backward(250)
    tt.pendown()
#sleep(5)
turtle.done()
