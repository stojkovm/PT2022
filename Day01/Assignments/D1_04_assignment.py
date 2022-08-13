"""
 - Instead of using if-else statements, implement switch using dictionary.
 - Function interface is the same - operations(operator, x, y)
"""


def operations(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
