
def rg(no):
    yield 1
    yield 2
    yield 3


for x in rg(5):
    print(x)
