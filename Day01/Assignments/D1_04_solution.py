"""
 - Instead of using if-else statements, implement switch using dictionary.
 - Function interface is the same - operations(operator, x, y)
"""


def add(x, y):
    """Function returns result of addition of two numbers."""
    return x + y


def sub(x, y):
    """Function returns result of substraction of two numbers."""
    return x - y


def mul(x, y):
    """Function returns result of multiplication of two numbers."""
    return x * y


def div(x, y):
    """Function returns result of division of two numbers."""
    return x / y


def operations(operator, x, y):
    return {
        'add': add(x, y),
        'sub': sub(x, y),
        'mul': mul(x, y),
        'div': div(x, y),
    }.get(operator, None)


print(operations('div', 5, 3))
