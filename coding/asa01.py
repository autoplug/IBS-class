def sort_matrix(arg):
    dim = len(arg)
    r = []
    for x in arg:
        for y in x:
            r += [y]
    r.sort()
    for x in range(dim):
        for y in range(dim):
            arg[x][y] = r[x*dim+y]

    return arg


arr = [
    [8, 5],
    [2, 7]
]
print(sort_matrix(arr))
