import turtle as tt
tt.penup()
tt.setposition(0,-200)
tt.pendown()
tt.speed(30)
rows_num = 8 
width = 50
for i in range(rows_num):
    # draw a square
    for j in range(4):
#        if j%2==1:
#            width = width / 5
#        else:
#            width = 50
        tt.forward(width)
        tt.right(90)
    tt.penup()
    tt.forward(width)
    tt.left(360/rows_num)
    tt.pendown()
tt.hideturtle()
tt.done()
