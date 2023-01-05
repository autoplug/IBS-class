def Slution(A):
    m = max(A)

    for i in range(m, 1, -1):
        if i not in A:
            return i
    if m > 0:
        return m+1
    else:
        return 1


def solution(A):
    m = max(A)
    if m < 1:
        return 1

    A = set(A)
    B = set(range(1, m + 1))
    D = B - A
    if len(D) == 0:
        return m + 1
    else:
        return min(D)


print(solution([3, 6, 4,  2]))
