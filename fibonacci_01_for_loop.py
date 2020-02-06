# create a Fibonacci sequence

# use for loop

class NormalFibonacci():
    def __init__(self,num):
        self.num = num
    def creator(self):
        fi = [0,1]
        for i in range(2,self.num):
            fi.append(fi[i-1]+fi[i-2])
        print(fi)

def main():
    num = 15 
    created_list = NormalFibonacci(num)
    created_list.creator()

if __name__ == '__main__':
    main()
