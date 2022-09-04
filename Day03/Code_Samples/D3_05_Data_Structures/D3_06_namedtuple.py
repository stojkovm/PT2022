"""
 - The 'NamedTuple' structure provides an extension of the built-in 'tuple' data type.
 - NamedTuple objects are immutable.
 - Each object stored in them can be accessed through a unique identifier.
 - NamedTuple objects are implemented as regular Python classes internally.
 - NamedTuple objects are more memory efficient than regular classes
    and just as memory efficient as regular tuples.
 - NamedTuples support type hints.
"""
from typing import NamedTuple
from sys import getsizeof


class Person(NamedTuple):
    first_name: str
    last_name: str


named_tuple = Person("James", "Bond")
regular_tuple = ("James", "Bond")

print(f"NamedTuple: {named_tuple}")
print(f"Person name: {named_tuple.first_name}")

print(f"Size of NamedTuple: {getsizeof(named_tuple)}")
print(f"Size of regular tuple: {getsizeof(regular_tuple)}")
