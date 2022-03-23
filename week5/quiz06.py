def everyNth(str, nth):
    result = ""
    for x in range(nth-1, len(str), nth):
        result += str[x]
    return result


print(everyNth('banana', 2))


def my_function(s, n):
    result = []
    for i in range(n):
        result.append([s[i]] * n)
    return result


my_result = my_function('apple', 5)
print(my_result)
