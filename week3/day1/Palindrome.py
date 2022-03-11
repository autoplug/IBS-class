

def createPalindrome(str1):
    result = ""
    for x in str1:
        result = x + result
    return str1 + result


print(createPalindrome("123"))
