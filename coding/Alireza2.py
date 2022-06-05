def func(path):
    try:
        file = open(path, "r")
        content = file.readlines()
        file.close()
    except IOError:
        print("There is problem with the file.")
        exit()

    cities = []
    rain = []
    for line in content:
        c = line.split(";")
        if c[1] not in cities:
            cities.append(c[1])
            rain.append(int(c[2]))
        else:
            rain[cities.index(c[1])] += int(c[2])
    return cities[rain.index(max(rain))]


print(func("list.txt"))
