f_name = "list.txt"
f = open(f_name, "r")
s = f.read()
f.close()


def sn(txt):
    s = txt.split("\n")
    max = 0
    city = ""
    for x in s:
        max2 = 0
        city2 = ""
        d = x.split(";")
        for y in s:
            f = y.split(";")
            if f[1] == d[1]:
                max2 += int(f[2])
                city2 = f[1]
        if max2 > max:
            max = max2
            city = city2
    return city


print(sn(s))
