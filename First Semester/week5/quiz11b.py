def most_common_letter(str):
    str = str.lower()
    alphabet = "abcdefghklmnopqrstuvxyz"
    result = []
    for letter in range(len(alphabet)):
        result.append(0)
        for char in str:
            if char == alphabet[letter]:
                result[letter] += 1
    return alphabet[result.index(max(result))]


print(most_common_letter("apple"))
