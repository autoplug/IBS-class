from time import *


def time_calculation(func):
    def inner(*a):
        result = time()
        r = func(*a)
        print(time()-result)
        return r
    return inner


@time_calculation
def add(a, b):
    return a + b


print(add(4, 5))
