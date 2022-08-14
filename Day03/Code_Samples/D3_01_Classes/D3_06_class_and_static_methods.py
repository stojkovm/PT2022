class Person:

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def instance_method(self):
        return "This is instance method!", self

    @classmethod
    def class_method(cls):
        """
         - Class methods take a 'cls' parameter that points
            to the class when the method is called.
         - The class method only has access to this cls argument
            so it cannot modify object instance state.
         - It can be used to modify class variables.
         - Class method are usually to create factory methods.
         - Factory methods return class objects (similar to a constructor) for different use cases.
        """
        return "This is class method!", cls

    @staticmethod
    def static_method():
        """
         - This type of method does not take a 'self' or a 'cls' parameter,
            but it can accept an arbitrary number of other parameters.
         - Static method cannot modify object state or class state.
         - Static method can be used as utility method. 
        """
        return "This is static method!"

    def __str__(self) -> str:
        return f"I'm {self._name} and I'm {self._age} years old."


p1 = Person("James", 36)
"""
 - Regularly binds method to 'p1' instance.
 ('This is instance method!', <__main__.Person object at 0x10679baf0>)
"""
print(p1.instance_method())






"""
 - When instance_method() is called, Python replaces the 'self' argument
    with the instance object 'p1'.
 ('This is instance method!', <__main__.Person object at 0x10679baf0>)
"""
print(Person.instance_method(p1))






"""
 - When class_method() is called, it does not have access to the <Person object>,
    but only to the <class Person> object, representing the class itself.
"""
print(p1.class_method())





"""
 - static_method() can be called on the instance object.
"""
print(p1.static_method())
print(Person.static_method())
