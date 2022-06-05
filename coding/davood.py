def sort_matrix(arr):
    n = len(arr)
    r = []
    for x in arr:
        for y in x:
            r.append(y)
    sorted(r)

    row = []
    for y in range(n):
        for x in range(n):
            row.append(r[n*y+x])

    return r


print(sort_matrix([[1, 2], [3, 4]]))
