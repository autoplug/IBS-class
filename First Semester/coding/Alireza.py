def sort_matrix(arr):
    dimension = len(arr)
    max = 0
    for i in range(dimension):
        for j in range(dimension):
            for f in range(dimension):
                for k in range(dimension):
                    if arr[f][k] > arr[i][j]:
                        max = arr[f][k]
                        arr[f][k] = arr[i][j]
                        arr[i][j] = max

    for x in arr:
        print(x)
    return arr


arr = [
    [4, 2, 3],
    [2, 1, 7],
    [7, 2, 6]
]
sort_matrix(arr)
