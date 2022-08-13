"""
 - Partial function as an extension of another specified function.
 - A partial function has the same functionality of the specified function, but with pre-filled values (freezed) for a certain number of arguments.
 - partial() allows the program to output a function object resembling the original function with a fixed argument(s) passed into it
 - This is useful to adapt a function that takes one or more arguments to an API that requires a callback with fewer arguments.
"""
from functools import partial

def multiply(x, y):
    return x * y

times_seven = partial(multiply, 7)
print(times_seven(3))

"""
 - We can pass object methods to partial and create new behavior.
 - We have created new function that always adds new elements at index 1.
"""
fruit_list = ['apple', 'orange', 'lemon']
add_fruit = partial(fruit_list.insert, 1)
add_fruit('kiwi')
print(fruit_list)

"""
 - You can simulate partial using lambdas.
"""
fruit_list = ['apple', 'orange', 'lemon']
add_fruit = lambda fruit: fruit_list.insert(1, fruit)
add_fruit('kiwi')
print(fruit_list)
