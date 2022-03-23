import os
print("----------------------------------")
print(os.getcwd())

# os.chdir(os.getcwd())
# os.path.isfile("/data/file.txt")
# os.path.isdir("")
# os.listdir("path/")


class fileContent:
    def __init__(self) -> None:
        pass

    def __enter__(self):
        print("Starting ...")

    def __exit__(self, exe_type, exe_value, exec_tb):
        print("exiting ...")


with fileContent() as f:
    print("do stuf")


with open("./week5/file.txt", 'a') as f:
    print(f.readline())

try:
    path_file = "./week5/file.txt"

    my_file = open(path_file)

    for line in my_file:
        print(line, end="")

except Exception as e:
    print(e)
finally:
    my_file.close()
