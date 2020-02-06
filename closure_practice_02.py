def circle(radius):
    def circumference():
        c = 3.14*radius*2
        print (f'circumference is {c}') 
        return c
    def area():
        a = 3.14*radius**2
        print (f'area is {a}')
        return a
    return circumference,area

print(circle(3))
cir,are = circle(3)
print(cir(),are())

for i in circle(11):
    print ("--->",i())

