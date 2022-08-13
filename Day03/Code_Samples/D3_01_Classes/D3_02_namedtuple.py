"""
 - Although 'NamedTuple' appears in the class statement as a superclass,
    it is not true.
 - 'typing.NamedTuple' uses the advanced functionality of a metaclass
    to customize the creation of the user's class.
"""
from typing import NamedTuple


class Person(NamedTuple):
    name: str
    age: int

    def __str__(self) -> str:
        return f"I'm {self.name} and I'm {self.age} years old."


# prints error since NamedTuple is not class
# print(issubclass(Person, NamedTuple))
print(issubclass(Person, tuple))  # prints True

p1 = Person("James", 36)
print(p1)
print(repr(p1))  # we even did not implement __repr__
