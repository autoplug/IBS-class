
def Palindrome(str1):
    result = ""
    for x in str1:
        result = x + result
    return str1 + result


print(Palindrome("alireza"))
