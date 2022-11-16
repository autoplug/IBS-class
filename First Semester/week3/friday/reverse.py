def reverse(str1):
    result = ""
    for char in str1:
        result = char + result
    return result


print(reverse("Alireza"))
