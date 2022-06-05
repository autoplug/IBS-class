def Hamming_distance(str1, str2):
    result = 0
    for x in range(len(str1)):
        if str1[x] != str2[x]:
            result += 1
    return result


def function(txt, m):
    d = []
    for element in m:
        if Hamming_distance(txt, element) <= 3:
            d.append(element)
    return d


print(function("monkey", ["donkey", "monday", "shaker"]))


str1 = "ab"
str2 = "ac"
print(str1 & str2)
