import turtle as tt
tt.penup()
tt.setposition(0,0)
tt.pendown()
tt.color('red')
tt.pensize(3)
tt.speed(8)
petals_num = 12
width = 200
for i in range(petals_num):
    # draw a petal
    tt.circle(width,90)
    tt.left(120)

#tt.hideturtle()
tt.done()
