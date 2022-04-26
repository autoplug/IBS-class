class Student:
    def __init__(self, id, name, language="Python"):  # define default value
        self.id = id
        self.name = name
        self.language = language

    def __str__(self):
        return f'[{self.id}] {self.name} studies {self.language}'


print(Student(1, 'Bob', "Python"))  # should print: [1] Bob studies Python
print(Student(2, 'Mark', "Java"))  # should print: [2] Mark studies Java
print(Student(3, 'Kate'))  # should print: [3] Kate studies Python

# when we want to initialize class it get two parameter but
# in the last line we instantiate class with just one argument.In this case we get an error.
# but if i have default value for every argument we can define the defult value in function
# and in this case if you does not pass the argument the default value assign to it.
