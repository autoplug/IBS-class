class Person:
    name = ""
    age = 0
    gender = "male"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # def __init__(self, name,  gender):
    #     self.name = name
    #     self.age = 0
    #     self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender}.")

    @classmethod
    def create_newborn(cls, name, gender):
        cls.age = 90
        return cls(name, 0, gender)

    @staticmethod
    def get_goal():
        print("My goal is: Live for the moment!")

    def display(self):
        print("pppppp")


class Student(Person):
    def __init__(self):
        print("ppppp")


# Person.create_newborn("alirzea", "pppp")
# p = Person("alireza", "--", "pp")
# p.introduce()


a = Student()
a.introduce()


class Mentor(Person):
    level = ""

    def __init__(self, name, age, gender, level):
        super().__init__(name, age, gender)
