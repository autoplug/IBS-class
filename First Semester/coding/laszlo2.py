def d(arg_str):
    name_city = []
    for x in arg_str:
        p = x.split(';')
        if p[1] not in name_city:
            name_city.append(p[1])
    max = 0
    result_city = ""
    for c1 in name_city:
        test_max = 0
        for x in arg_str:
            if "SNOWY" in x and c1 in x:
                test_max += 1
        if test_max > max:
            result_city = c1
            max = test_max

    return result_city


s = ""
with open("snow.txt", "r") as f:
    s = f.readlines()

print(d(s))
