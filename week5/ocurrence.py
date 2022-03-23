
def most_common_letter(str1: str):
    result = str1[0]
    for char in str1:
        if len(str1.replace(result, "")) > len(str1.replace(char, "")):
            result = char
    return result


print(most_common_letter("apple"))
