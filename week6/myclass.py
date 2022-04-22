class Cat:
    obj_type = "Animal"

    def __init__(self, name):
        self.name = name

    @classmethod
    def def_with_age(cls, name, age):
        pass

    @staticmethod
    def add(a, b):
        print(a+b)

    def getter(self):
        print("pppppp")


my_cat = Cat("mica")
print(my_cat)


class Geeks:
    def __init__(self):
        self._age = 0

    # function to get value of _age
    def get_age(self):
        print("getter method called")
        return self._age

    # function to set value of _age
    def set_age(self, a):
        print("setter method called")
        self._age = a

    # function to delete _age attribute
    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)
