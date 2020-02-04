# sum two matrixes
matrixa=matrixb=[[0,1,2],[3,4,5],[6,7,8]]
sum_matrix=[]
for i,a in enumerate(matrixa):
    sum_matrix.append([])
    for j,b in enumerate(a):
        sum_matrix[i].append(0)
        sum_matrix[i][j]=matrixa[i][j]+matrixb[i][j]
print (sum_matrix)
