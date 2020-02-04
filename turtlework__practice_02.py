import turtle
from time import sleep
turtle.bgcolor('black')
tt= turtle.Pen()
tt.pencolor('white')
tt.penup()
tt.left(90)
tt.forward(270)  # go up to the top 
tt.pendown()
tt.right(90)
tt.pensize(30)
tt.speed(2)
for i in range(7):
    tt.pendown()
    tt.forward(200-i*20)  # draw a line
    tt.penup()
    tt.right(90)
    tt.forward(60)
    tt.right(90)
    tt.forward(190-i*20)  # move the pen to the left
    tt.right(180)
#tt.write('hello')
sleep(5)
