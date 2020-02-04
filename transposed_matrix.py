matrixa=[[1,2],[3,4],[5,6]]
matrixb=[]

arow = len(matrixa)
acolumn= len(matrixa[0])

# build a new matrix
for i in range(acolumn):
    matrixb.append([])
    for j in range(arow):
        matrixb[i].append(0)

# transposed matrix
for i,a in enumerate(matrixa):
    for j,b in enumerate(a):
        matrixb[j][i]=b
        print("j=%d,i=%d"%(j,i))
print(matrixb)

