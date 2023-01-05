def countPairs(numbers, k):
    result = []
    for kk in range(k):
        for x in range(len(numbers)):
            for y in range(len(numbers)):
                if numbers[y] == numbers[x]+kk:
                    result.append((numbers[x], numbers[y]))

    r2 = list(set(result))
    # r2 = []
    # for x in result:
    #     find = False
    #     for y in r2:
    #         if x == y:
    #             find = True
    #     if not find:
    #         r2.append(x)

    return len(r2)


print(countPairs([1, 1, 2, 2, 3, 3], 1))
print(countPairs([1, 2, 5, 6, 9, 10], 2))
