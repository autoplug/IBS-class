
def my_function(list):
    result = 0
    if list[1] + list[2] == list[-1]:
        result += 1
    for n in list[3:]:
        result += n
    # 4

    for n in list[:2]:
        result += n
    # 7
    if list[1] ** 2 == list[3]:
        result += 1
    # 8
    return result


print(my_function([1, 2, 3, 4]))


#####
def increment_by_next(list):
    for i in range(len(list)-1):
        list[i] += list[i + 1]
    return list


print(increment_by_next([]))  # should print [3, 5, 3]
