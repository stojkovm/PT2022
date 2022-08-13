"""
 - '@dataclass' decorator supports PEP 526 syntax to declare instance attributes.
 - The decorator reads the variable annotations and automatically
    generates methods for your class.
 - The class is still mutable, except when explicitly setting the argument 'frozen' to True.
 - dataclass function interface looks like this: 
    - dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False,
        frozen=False, match_args=True, kw_only=False, slots=False)
"""
from dataclasses import dataclass, field


"""
 - class Person(frozen=True):
 - @dataclass emulates immutability by generating __setattr__ and __delattr__, which raise data
    class.FrozenInstanceError when the user attempts to set or delete a field.
"""


@dataclass
class Person:

    name: str
    age: int
    """
        - The 'default_factory' parameter needs a function, class, or any other callable.
        - This will be invoked with zero arguments to build a default value each time an instance of the data class is created.
        - This prevents that all instances share the same list from the class.
    """
    hobbies: list[str] = field(default_factory=list)

    """
     - dataclass will add __init__ method like this:
     
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
    """

    def __str__(self) -> str:
        return f"I'm {self.name} and I'm {self.age} years old."


p1 = Person("James", 27)
print(p1)
# in case 'frozen=True' this will not work
p1.address = "New York"
print(repr(p1))
print(p1.address)
