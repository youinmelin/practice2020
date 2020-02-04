import turtle as tu
import time
tu.tracer(0)
tu.circle(90)
tu.penup()
tu.sety(90)
tu.pendown()
tu.dot()
tu.setheading(90)

for i in range(60):
    tu.forward(90)
    time.sleep(0.5)
    #tu.undo()
    tu.setposition(0,90)
    tu.right(6)
    tu.update()


tu.done()