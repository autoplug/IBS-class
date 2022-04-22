

temperatures = [
    {
        'monday': 12,
        'wednesday': 13,
        'friday': 14
    },
    {
        'monday': 15,
        'friday': 12
    },
    {
        'tuesday': 10,
        'thursday': 11,
        'saturday': 12
    },
]


def get_hottest_day(temp):
    weekday = ["monday", "tuesday", "saturday", "friday"]
    average = []
    for day in weekday:
        count = 0
        sum = 0
        for e in temp:
            if e.get(day):
                sum += e.get(day)
                count += 1
        if count:
            average.append(sum/count)
        else:
            average.append(0)
    print(average)
    return weekday[average.index(max(average))]


def get_hottest_day2(temp):
    average = ""


print(get_hottest_day(temperatures))  # should return "monday"
