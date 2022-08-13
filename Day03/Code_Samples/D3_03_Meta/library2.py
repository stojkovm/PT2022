"""
 - Scenario two:
    - Core library team has implemented some functionality.
    - User library team wants to use library1 module.
    - How Core library team can defend themself of inapropriate usage
        by User library team's module?
"""


class Meta(type):
    def __new__(cls, name, bases, dct):
        if name != "Base" and not "bar" in dct:
            raise TypeError("User method 'bar' does not exist!")
        return super().__new__(cls, name, bases, dct)


class Base(metaclass=Meta):
    # class Base:

    def foo(self):
        return self.bar()

    # def __init_subclass__(cls, **kwargs):
    #     if not cls.bar:
    #         raise TypeError("User method 'bar' does not exist!")
    #     super().__init_subclass__(**kwargs)
