import turtle

tu = turtle.Pen()
tu.pencolor("white")
turtle.bgcolor('black')
tu.speed(10)
i = 0
j = 0
while i < 50:
    tu.forward(j)
    tu.left(90)
    i=i+1
    j = j + 5
turtle.done()
