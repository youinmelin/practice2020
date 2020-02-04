import turtle
turtle.bgcolor('black')
tt= turtle.Pen()
tt.goto(-200,200)
tt.color('white','white')
tt.speed(15)
rows_num = 4
cols_num = 6
width = 50
for y in range(cols_num):
    # draw a row
    for i in range(rows_num):
        # draw a square
        if (i%2==0 and y%2==0) or (i%2==1 and y%2==1):
            tt.begin_fill()
        for j in range(4):
            tt.forward(width)
            tt.right(90)
        if (i%2==0 and y%2==0) or (i%2==1 and y%2==1):
            tt.end_fill()
        tt.penup()
        tt.forward(width)
        tt.pendown()
    tt.penup()
    tt.right(90)
    tt.forward(width)
    tt.setheading(0)
    tt.backward(width*rows_num)
    tt.pendown()
turtle.done()
