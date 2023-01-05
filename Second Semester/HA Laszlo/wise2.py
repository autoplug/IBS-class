# Python code for Maximum size square
# sub-matrix with all 1s
# (space optimized solution)

R = 6
C = 5


def printMaxSubSquare(M):

    global R, C
    Max = 0

    # set all elements of S to 0 first
    S = [[0 for col in range(C)]for row in range(2)]

    # Construct the entries
    for i in range(R):
        for j in range(C):

            # Compute the entrie at the current position
            Entrie = M[i][j]
            if(Entrie):
                if(j):
                    Entrie = 1 + min(S[1][j - 1], min(S[0][j - 1], S[1][j]))

            # Save the last entrie and add the new one
            S[0][j] = S[1][j]
            S[1][j] = Entrie

            # Keep track of the max square length
            Max = max(Max, Entrie)
    print(S)
    # Print the square
    print("Maximum size sub-matrix is: ")
    for i in range(Max):
        for j in range(Max):
            print("1", end=" ")
        print()


# Driver code
M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]

printMaxSubSquare(M)

# This code is contributed by shinjanpatra
