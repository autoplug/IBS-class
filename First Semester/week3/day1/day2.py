import array


a = "alireza"
# print(a[::-1])

a = ["a", "a", "l"]
a = [x == "a" for x in a if x == "l" and x != "a"]
#fibo = [fibo[x-1]+fibo[x] for x in range(10)]


b, *c = ("a", "b", 2, 3, 4)
f = [x for x in range(5)]
print(f)


def fib(m):
    a, b = 0, 1
    i = 0
    while True:
        yield a
        a, b = b, a+b
        if i > m:
            break
        i += 1


fib_gen = fib(4)
# for i in fib_gen:
#     print(i)


def func_gen():
    print("First time")
    yield 1
    print("second time")
    yield 2


print("generator")
func_gen()


def my_fib(n): return n if n < 2 else my_fib(n-1) + my_fib(n-2)


print(my_fib(2))

my_arr = array.array("i", [2, 3, 4, 5, 6])
print(my_arr * 3)


def f(x):
    return x**3


print(list(map(f, range(5))))
