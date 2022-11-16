
def most_common_letter(str):
    letter = ""
    count = 0
    letter2 = ""
    count2 = 0
    for x in "abcdefghklmnopqrstuvwxyz":
        count2 = 0
        for y in str:
            if x.lower() == y.lower():
                letter2 = x
                count2 += 1

        if count2 > count:
            letter = letter2
            count = count2
    return letter


print(most_common_letter("apple"))
