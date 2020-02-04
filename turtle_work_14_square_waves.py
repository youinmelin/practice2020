import turtle as tt
tt.penup()
tt.setposition(-200,0)
tt.pendown()
tt.color('red')
tt.pensize(3)
tt.speed(10)

for i in range(10):
    tt.forward(20)
    tt.left(90)
    tt.forward(20)
    tt.right(90)
    tt.forward(20)
    tt.right(90)
    tt.forward(20)
    tt.left(90)

tt.done()
