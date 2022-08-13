"""
 - Functions can have side-effects, which means that they can affect something
    external to the function itself.
 - E.g. print() function prints strings in console but does not return any text as a value.
 - Although Python has no rules for the number of spaces used to indent code in a function body, PEP8 recommends indenting with four spaces.
"""


def multiply(x, y):
    product = x * y
    return product


print(multiply(3, 5))

# access to docstrings
print(multiply.__doc__)


"""
 - Python adds an implicit return None statement to the end of any function.
 - If a function does not specify a return value, it returns None by default.
"""


def foo():
    print(f"Function without return value")


print(foo())  # prints None






"""
 - Unimplemented functions can you 'pass' keyword to ommit errors.
"""
def foo():
    pass
