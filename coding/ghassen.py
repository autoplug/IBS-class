def hammingDist(t1, t2):
    i = 0
    count = 0
    while i < len(t1):
        if t1[i] != t2[i]:
            count += 1
        i += 1
    return count


def cal_Hammin(t1, list1):
    list2 = []
    for e in list1:
        if hammingDist(t1, e) <= 3:
            list2.append(e)
    return list2


print(hammingDist("monkey", ["donkey", "monday", "shaker"]))
