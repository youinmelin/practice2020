import turtle as tu
tu.penup()
tu.goto(-200,100)
tu.pendown()
i=0
a=50
while i<11:

    if i%4==0:
        tu.fillcolor("yellow")
    if i % 4 == 1:
        tu.fillcolor("red")
    if i%4==2:
        tu.fillcolor('green')
    if i%4==3:
        tu.fillcolor('darkorange1')

    tu.begin_fill()

    for ii in range(4):  #画正方形
        tu.forward(a)
        tu.right(90)

    tu.forward(a)
    tu.end_fill()



    i=i+1

tu.done()
