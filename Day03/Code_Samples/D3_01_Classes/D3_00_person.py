class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")


p1 = Person("James", 27)
