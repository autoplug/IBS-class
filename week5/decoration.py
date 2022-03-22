def decorate_add(func):
    def inner(a, b):
        print("before func")
        result = func(a, b)
        print("End of func")
        return result
    return inner


@decorate_add
def add(a, b):
    return a+b


print(add(4, 5))
