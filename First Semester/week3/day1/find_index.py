list = [2, 5, 8, 90]


def find_index(num, ls):
    result = -1
    index = 0
    for x in ls:
        if x == num:
            result = index
        index += 1
    return result


print(find_index(5, list))
