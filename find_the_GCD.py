a=[60,90,15,45,30,5,5,5,5,58]
result =1 
i=1
while i<max(a)+1:
    j=True
    for item in a:
        if (item % i) != 0 :
            j = False

    if j:
        result = i
        print(i)
    i += 1
print("GCD = ",result)
