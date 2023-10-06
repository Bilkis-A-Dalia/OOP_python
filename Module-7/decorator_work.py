# decorator-->nested function
import math
import time
# function declare
def timer(func):
    def inner(*args,**kwargs):
        print('Time stared')
        start = time.time()
        # print(func)
        func(*args,**kwargs)
        print('time ened')
        end = time.time()
        print(f'Total time taken {end - start}')
    return inner
# timer()()

@timer
def get_factorial(n):
    print('Factorial starting')
    result = math.factorial(n)
    print(f'Factorial of {n} is : {result}')

# timer(get_factorial)() vejal way to decorate
get_factorial(n=5)
