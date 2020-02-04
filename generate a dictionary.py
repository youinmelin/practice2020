# generate a dictionary that contains(i:i*i) such that i is a number ranging from 1 to n
n=int(input('input a int that bigger than 0:'))
con_dict = {}
for num in range(1,n+1):
    con_dict[num] = num*num
print(con_dict)
