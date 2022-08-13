"""
 - A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 
 - The criteria that must be met to create closure in Python:
    - We must have a nested function (function inside a function).
    - The nested function must refer to a value defined in the enclosing function.
    - The enclosing function must return the nested function.
"""


def outer_function(text):

    def inner_function(name):
        print(f"{text} {name}!")
    return inner_function


greeting_fn = outer_function('Hello')
greeting_fn('James')
