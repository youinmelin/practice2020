#调用每个方法前记录进入函数的名称

import inspect

def entrence(func):
    def ask():
        answer = input('input the result of 5+2:')
        try:
            answer = int(answer)
        except Exception:
            print('False')
        else:
            if answer == 7:
                caller_name = func.__name__
                print ('[DEBUG]call function name:',caller_name)
                func()
                #return True
            else:
                print('False')
    return ask

# welcome = entrence(welcome)
@entrence
def welcome():
    caller_name = inspect.stack()[1][3]
    print ('call function name:',caller_name)
    print('That is right')

if __name__ == '__main__':
    welcome()
