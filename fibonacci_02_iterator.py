# create a Fibonacci sequence
# use iterator
class IteratorFibonacci():
    def __init__(self,num):
        self.n = num
        self.num1 = 0
        self.num2 = 1
        self.current = 0
    def __iter__(self):
        return(self)
    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1,self.num2 = self.num2 , self.num1 + self.num2
            self.current += 1
            return num
        else:
            raise StopIteration


def main():
    num = 15 
    iter_list = IteratorFibonacci(num)
    #for i in iter_list:
    #    print(i,end=' ')
    fi = tuple(iter_list)
    print(fi)

if __name__ == '__main__':
    main()
