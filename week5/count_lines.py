# Write a function called countLines() that takes a filename as string as a parameter
# and  returns the number of lines the file contains.
# It should return zero if it can't open the file and
# should not raise any error.

def countLines(file_path):
    result = 0
    try:
        file = open(file_path)
        for line in file:
            result += 1

    except Exception as e:
        print(e)

    return result
