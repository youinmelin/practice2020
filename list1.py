list1= [0,1,2,3]
i=0
dirnum=0
def gomaze(dirnum = 2):
    global i
    if i<10:
        print(list1[dirnum])
        dirnext = (dirnum + 3)%4
        i+=1
        return gomaze(dirnext)
    else:
        return 0

gomaze()