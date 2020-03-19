class Add:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(f'{self.a} + {self.b} = {self.a + self.b}')
        return self.a + self.b

addlist = []
for i in range(10):
    j = i*2
    ab_add = Add(i,j)
    addlist.append(ab_add)

for i in range(10):
    j = i*3
    locals()[f'add{i}'] = Add(i,j)

addlist[0].a = 10
for ab in addlist:
    method_result = ab.add
    result = method_result()
    print(method_result,result)

i=0
while i<10:
    locals()[f'add{i}'].add()
    i += 1

    
