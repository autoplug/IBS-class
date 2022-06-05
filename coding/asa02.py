def f(text, arr):
    r = []
    for x in arr:
        hammin_distance = 0
        for c in range(len(x)):
            if x[c] != text[c]:
                hammin_distance += 1
        if hammin_distance <= 3:
            r.append(x)
    return r


a = ["apple", "apply", "tuple", "alter"]
b = f("apple", a)
print(b)
