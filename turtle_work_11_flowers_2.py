import turtle as tt
tt.penup()
tt.setposition(0,0)
tt.pendown()
tt.color('red')
tt.pensize(3)
tt.speed(10)
petals_num = 11
radius = 50
for i in range(petals_num):
    # draw a petal
    tt.circle(radius,180)
    tt.right(180-360/petals_num)
#tt.hideturtle()
tt.done()
