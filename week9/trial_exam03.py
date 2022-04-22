class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age+8
        self.color = color


class Dog(Animal):
    # def __init__(self, name, age, color):
    # print("pppp")

    pass


dog = Dog("aa", 67, "red")

print(dog.age)


arr = "alireza"
for char in arr:
    print(char)
