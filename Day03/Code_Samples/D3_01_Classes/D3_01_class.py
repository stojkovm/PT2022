from __future__ import annotations


class Person:
    # class Person():
    # class Person(object):

    """
        - When we create objects for classes, it requires memory and the attribute
            are stored in the form of a dictionary.
        - '__slots__' provide a special mechanism to reduce the size of objects.
            It is a concept of memory optimisation on objects.
    """
    __slots__ = '__name', '__age'

    def __init__(self, name: str, age: int) -> None:
        """
         - In Python, there are only two types of visibility for a class's attributes - public and private
         - Private attributes are prefixed with double underscore.
         - They can be accessed directly by methods of the containing class.
        """
        self.__name = name
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, new_age: int) -> None:
        self.__age = new_age

    def __str__(self) -> str:
        """
            - str() is used for creating output for end user.
            - str's goal is to be readable.
        """
        return f"I'm {self.name} and I'm {self.age} years old."

    def __repr__(self) -> str:
        """
            - repr() compute the 'official' string representation of an object
                (a representation that has all information about the object) 
            - repr() is mainly used for debugging and development.
            - repr's goal is to be unambiguous.
            - When you call print() on an object, it calls __str__ method of the object.
            - If __str__ is not implemented, the __repr__ is called as a fallback.
        """
        return f"{Person.__name__} {self.name, self.age}"

    def __eq__(self, o: Person) -> bool:
        """
            - We can define when two objects are equal implementing __eq__.
            - If we use type hinting 'Person' will be unavailable since class is not yet created.
            - Importing 'from __future__ import annotations' will solve this issue.
        """
        return self.name == o.name and self.age == o.age


p1 = Person("James", 27)
print(p1)
print(repr(p1))
# print(p1.__dict__) # Attribute error when __slots__ are defined.
print(p1.__slots__)


p2 = Person("James", 27)
if p1 == p2:
    print("Same values!")

"""
 - This will print an error.
"""
# print(p1.__name)
