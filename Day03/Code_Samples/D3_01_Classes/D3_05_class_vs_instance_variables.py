"""
 - Class variables are declared inside the class definition (but outside of any instance methods).
 - They are not tied to any particular instance of a class.
 - Instead, class variables store their contents on the class itself, and all objects created
    from a particular class share access to the same set of class variables.
 - This means, for example, that modifying a class variable affects all object instances at the same time.
 
 
 
 - Instance variables are always tied to a particular object instance.
 - Their contents are not stored on the class, but on each individual object created from the class.
 - Therefore, the contents of an instance variable are completely independent from one object instance to the next.
 - Modifying an instance variable only affects one object instance at a time.
"""
from enum import Enum


class Personality(Enum):
    SANGUINE = 1,
    CHOLERIC = 2,
    MELANCHOLIC = 3,
    PHLEGMATIC = 4,


class Person:
    PERSONALITY = Personality.PHLEGMATIC

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"I'm {self.name} and I'm {self.age} years old."


p1 = Person("James", 35)
p2 = Person("Pablo", 22)
print(p1.PERSONALITY.name)




"""
 - In the code below we actually created instance variable to p1 instance
    which shadows the class variable.
 - The proper way would be to do this:
    p1.__class__.PERSONALITY = Personality.CHOLERIC
"""
# p1.PERSONALITY = Personality.CHOLERIC
Person.PERSONALITY = Personality.CHOLERIC



print(Person.PERSONALITY)
print(p2.PERSONALITY)
