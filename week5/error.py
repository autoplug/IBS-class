a = 1
b = 9


class MyException(Exception):
    pass


def div(a, b):
    return a / b


try:
    c = div(a, b)
    # raise ZeroDivisionError
    raise MyException
except ZeroDivisionError:
    print("b is zero")
except TypeError:
    print(type(a))
    print(type(b))
    # pass
except MyException:
    pass
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("it have to print line", "EOP")
