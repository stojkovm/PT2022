"""
 - Some general guidelines for writing docstrings can be found in PEP257
"""
def multiply(x, y):
    """Return the product of two numbers x and y.

    Parameters
    ----------
    x : int
        The first number.
    y : int
        The second number.

    Returns
    -------
    product : int
        A product of two numbers.
    """
    product = x * y
    return product









"""
 - Functions can return multiple values as tuple.
 - Do not return more than three values since it can be error prone.
"""
def stats(numbers):
    min_val = min(numbers)
    max_val = max(numbers)
    count = len(numbers)
    return min_val, max_val, count

minimum, maximum, count = stats([1, 6, 2, 7, 3])
print(f"Min: {minimum}, Max: {maximum}, Count: {count}")








"""
 - Python 3.8 introduced 'positional-only arguments' feature.
 - These arguments can be supplied only by position and never by keyword.
 - Forward slash (/) is delimiter that says where positional arguments end.
 - Positional-only arguments ensure that callers can’t supply certain parameters using keywords, which helps reduce coupling.
 - Asterisk (*) can be used to signal where keyword arguments start.
 - Keyword-only arguments force callers to supply certain arguments by keyword (instead of by position), which makes the intention of a function call clearer. 
 - Between / and * you can have positional and keyword arguments as well.
"""
def foo(first_name, last_name, /, *, gender='Undefined'):
    print(
        f"""
        First name: {first_name}
        Last name: {last_name}
        Gender: {gender}
        """)

foo('James', 'Bond')










"""
 - Use None and Docstrings to Specify Dynamic Default Arguments
 - A default argument value is evaluated only once: during function definition at module load time.
 - This can cause odd behaviors for dynamic values (like {}, [], or custom objects).
 - Use None as the default value for any keyword argument that has a dynamic value. Document the actual default behavior in the function’s docstring.
"""
# wrong way to do it
def append_fruit_to_lst(fruit, fruit_list=[]):
    fruit_list.append(fruit)
    return fruit_list

print(append_fruit_to_lst('apple'))
print(append_fruit_to_lst('orange'))
print(append_fruit_to_lst('lemon'))










"""
 - Unpacking list
"""
first, *middle, last = append_fruit_to_lst('banana')
print(f"""First: {first}
Middle: {middle}
Last: {last}""")






# wrong way to do it
def append_fruit_to_dict(fruit, quantity, fruit_coll={}):
    fruit_coll[fruit] = quantity
    return fruit_coll


print(append_fruit_to_dict('apple', 5))
print(append_fruit_to_dict('orange', 4))
print(append_fruit_to_dict('lemon', 3))









"""
 - Unpacking dictionary
"""
first, *middle, last = append_fruit_to_dict('banana', 2)
print(f"""Dict:
First: {first}
Middle: {middle}
Last: {last}""")

# correct way to do it
def append_fruit_to_dict(fruit, quantity, fruit_coll=None):
    """Function adds fruit to collection.

        Args:
        fruit -- fruit to be added.
        quantity -- fruit quantity to be added.
        fruit_coll: collection of fruits.
            Defaults to the empty dictionary.
    """
    if not fruit_coll:
        fruit_coll = {}
    fruit_coll[fruit] = quantity
    return fruit_coll


print(append_fruit_to_dict('apple', 5))
print(append_fruit_to_dict('orange', 4))
print(append_fruit_to_dict('lemon', 3))









"""
 - Functions have the ability to “unpack” function arguments
    from sequences and dictionaries with the * and ** operators.
 - Putting a * before an iterable in a function call will unpack it
    and pass its elements as separate positional arguments to the called function.
 - ** operator is used for unpacking keyword arguments from dictionaries.
"""
def args_unpacking(first, second, third):
    print(f"{first}:{second}:{third}")

lst = [1, 2, 3]
args_unpacking(*lst)


def kwargs_unpacking(first=None, second=None, third=None):
    print(f"{first}:{second}:{third}")

dic = {'first': 1,
       'second': 2,
       'third': 3
       }
kwargs_unpacking(**dic)
