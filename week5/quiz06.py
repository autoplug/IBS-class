def everyNth(str, nth):
    result = ""
    for x in range(nth-1, len(str), nth):
        result += str[x]
    return result


print(everyNth('banana', 2))
