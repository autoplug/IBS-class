def rainiest(filename):
    filename = open(filename, "r")
    text = filename.readlines()
    filename.close()

    r = []
    for x in text:
        y = x.replace("\n", "").split(";")
        r.append(y)

    d = {}
    for x in r:
        if x[1] in d:
            d[x[1]] += int(x[2])
        else:
            d[x[1]] = 0

    max = 0
    ee = ""
    for x in d:
        if d[x] > max:
            ee = x
            max = d[x]
    return ee


print(rainiest("rainy.txt"))
