# https://github.com/antsticky/IBS2022
# numpy
# tk --> Tkinter
# virialenv
import tk
import time


def fibo(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1

    return fibo(n-1)+fibo(n-2)


def time_measure(f, *args):
    return


def memoize(f):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            return 0


t0 = time.time()
a = fibo(3)
t0 = time.time()-t0
print("Elapsed time : ", t0, " Fibo value : ", a)

top = Tk()
# Code to add widgets will go here...
top.mainloop()
