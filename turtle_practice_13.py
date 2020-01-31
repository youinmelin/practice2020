import turtle as tu
a = 100
times = 4
i = 0
while i < times:
    tu.forward(a)
    tu.circle(a/3,360/times)
    i += 1
tu.done()
