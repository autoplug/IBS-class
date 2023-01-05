

def printMaxSubSquare(M):
    def isFull(a1, a2, l):
        if a1+l >= len(M):
            return False
        for x in range(a1, a1+l):
            for y in range(a2, a2+l):
                if not M[x][y]:
                    return False
        return True
    L = 0
    for i in range(len(M)):
        for j in range(len(M)):
            while i+L <= len(M) and j+L <= len(M) and isFull(i, j, L):
                L += 1
    return L


# Driver code
M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1]]

printMaxSubSquare(M)
