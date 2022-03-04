first = 1
second = 1
for x in range(10):
    j = first + second
    #print(j)
    first = second
    second = j

array = [["a","b"],["c","k"]]
for x in array:
    for y in x:
        print(y, end='')