"""
 - Object copies are shallow by default.
 - Use deepcopy to create separate instances without references to existing objects data.
"""

from copy import copy, deepcopy


class Person:
    __slots__ = '__name', '__age', '__addresses'

    def __init__(self, name: str, age: int, addresses: list[str]) -> None:
        self.__name = name
        self.__age = age
        self.__addresses = addresses

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

    @property
    def addresses(self) -> int:
        return self.__addresses

    @addresses.setter
    def addresses(self, new_addresses: list[str]) -> None:
        self.__addresses = new_addresses

    def __str__(self) -> str:
        return f"I'm {self.name} and I'm {self.age} years old."

    def __repr__(self) -> str:
        return f"{Person.__name__} {self.name, self.age}"


p1 = Person("James", 33, ["Address 1", "Address 2", "Address 3"])
p2 = copy(p1)
p3 = deepcopy(p1)
p4 = p1
print(p1 == p2)  # prints False
print(p1 == p4)  # prints True

p1.addresses.remove("Address 1")
print(p2.addresses)
print(p3.addresses)
