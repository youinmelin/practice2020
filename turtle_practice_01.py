import turtle
from time import sleep
tt =turtle.Pen()
turtle.bgcolor("black")
i=1
tt.speed(50)
while i<=360:
    if i%4==0:
        tt.color('red')
    if i % 4 == 1:
        tt.color('yellow')
    if i % 4 == 2:
        tt.color('green')
    if i % 4 == 3:
        tt.color('blue')
    tt.forward(i*2)
    tt.left(90)
    i=i+1
    print(i)
sleep(10)