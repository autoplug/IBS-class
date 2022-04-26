list = []


def Add(title: str):
    title = title.strip()
    if not title:
        print("\033[31m", "Unable to add: no task provided", "\u001b[0m")
        return
    list.append("[ ] "+title)
    print("\u001b[32m", "Successfully add task to list.", "\u001b[0m")
    Save()
    return


def Remove(index: int):
    if index > len(list):
        print("\033[31m",
              "Unable to remove: index is out of bound.", "\u001b[0m")
        return

    list.pop(index)
    print("\033[31m", "Successfully remove task from list.", "\u001b[0m")
    Save()


def Print():
    if len(list) == 0:
        print("\033[31m", "No todos for today! :)", "\x1b[0m")
        return

    for line in list:
        print("\033[37m", line, "\x1b[0m")


def Complete(index: int):
    if index > len(list):
        print("\033[31m", "There is not task with this number.", "\x1b[0m")
        return

    if list[index][0:4] == "[X] ":
        list[index] = "[ ] "+list[index][4:]
    else:
        list[index] = "[X] "+list[index][4:]
    Save()


path = "tasks.txt"


def Load():
    try:
        file = open("tasks.txt", "r")
        file = file.read()
        file = file.split("\n")
        for line in file:
            line = line.replace("\n", "")
            if line:
                list.append(line)
        file.close()
    except:
        print("Can not load file.")


def Save():
    try:
        f = open(path, "w")
        for line in list:
            f.write(line.replace("\n", "")+"\n")
        f.close()
    except:
        print("Can not save.")
