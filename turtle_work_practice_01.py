import turtle
import time
tu = turtle.Pen()
color_list = ['red','blue','green','yellow','orange',\
              'yellow','gold','purple','black']

for i in range(50):
    j = i%len(color_list)
    tu.pencolor(color_list[j])
    tu.forward(20-i/5)
    print(20-i/5)
    tu.right(i+i)
    print(i*i)

time.sleep(5)
