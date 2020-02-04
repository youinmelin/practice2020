import turtle as tt
tt.penup()
tt.setposition(0,0)
tt.pendown()
tt.color('red')
tt.pensize(3)
tt.speed(3)
petals_num = 8
width = 100
for i in range(petals_num):
    # draw a petal
    tt.circle(width,180)
    if petals_num%2==0:
        tt.left(360/petals_num)
    else:
        tt.left(180/petals_num)
#tt.hideturtle()
tt.done()
