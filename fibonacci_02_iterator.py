# create a Fibonacci sequence
# use iterator
class IteratorFibonacci():
    def __init__(self,num):
        self.n = num
        self.num1 = 0
        self.num2 = 1
        self.current = 0
    def __iter__(self):
        '''if a object contain a __iter__ method, it is iterable'''
        # __iter__方法要返回一个迭代器，迭代器自身正是一个迭代器，
        # 所以迭代器的__iter__方法返回自身即可
        return(self)
    def __next__(self):
        '''一个实现了__iter__方法和__next__方法的对象，就是迭代器'''
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
