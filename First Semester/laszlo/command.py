from functions import *

help = """
Command Line Todo application
=============================

Command line arguments:
    -h   Help list all command.
    -l   Lists all the tasks.
    -a   Adds a new task.
    -r   Removes an task.
    -c   Completes an task.
    -q   Quit the app.
"""

print(help)

Load()

while True:
    input_string = input("Enter command : ")

    command = input_string[0:3].strip()
    arg = input_string[3:].strip()

    if command == "-a":
        Add(arg)

    elif command == "-l":
        Print()

    elif command == "-r":
        try:
            value = int(arg) - 1
            Remove(value)
        except ValueError:
            print("Insert a number instead a string.")

    elif command == "-c":
        try:
            value = int(arg) - 1
            Complete(value)
        except ValueError:
            print("Insert a number instead a string.")

    elif command == "-q":
        break

    elif command == "-h":
        print(help)

    else:
        print("there is not such command.")
