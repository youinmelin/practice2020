import turtle as tutu

tutu.bgcolor('black')
tutu.pencolor('white')
tutu.pensize(30)
tutu.penup()
tutu.goto(0,-300)
i = 0
while i<10:
    tutu.pendown()
    tutu.forward(220)
    tutu.penup()
    tutu.left(90)
    tutu.forward(60)
    tutu.left(90)
    tutu.forward(220)
    tutu.right(180)
    i=i+1

tutu.done()



tutu.done()