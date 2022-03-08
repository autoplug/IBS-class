a = "dog"
b = "ogd"


def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    for x in str1:
        if str1.count(x) != str2.count(x):
            return False
    return True


print(isAnagram(a, b))
