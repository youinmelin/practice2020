# list comprehensions 列表生成式
lista = list(range(11))
print("lista", lista)

listb = [i for i in range(11)]
print("listb", listb)

listc = [i*i for i in lista]
print("listc", listc)

listd = [i for i in lista if i % 2 == 0]
print("listd", listd)

liste = [m + n for m in 'ABC' for n in 'abc']
print("liste", liste)

listf = [s.lower() for s in 'ABCDEF']
print(listf)

