a=[1,2,6,8,3,5,4,7,0,9]
for i,num in enumerate(a):
    for i,num in enumerate(a):
        if len(a)>(i+1):
            if a[i]>=a[i+1]:
                continue
            else:
                a[i],a[i+1]=a[i+1],a[i]
                print (a)
print (a)
