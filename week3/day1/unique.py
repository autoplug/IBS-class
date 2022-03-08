list = [2, 6, 9, 2]


def unique(ls):
    result = []
    for x in ls:
        if x not in result:
            result.append(x)
    return result


print(unique(list))
