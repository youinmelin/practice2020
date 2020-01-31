
class Factorial():

    def factorial(self,count):
        if count == 1 :
            return count
        else:
            return count*self.factorial(count-1)

if __name__ == '__main__':
    count = 5
    count_factotial = Factorial()
    result = count_factotial.factorial(count)
    print(result)
