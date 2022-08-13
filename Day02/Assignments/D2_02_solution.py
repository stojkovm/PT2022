"""
 - Extend the existing code with meta decorator @repeat(<arbitrary_number>)
    that calls the original function <arbibrary_number> of times.
"""

from time import time
from functools import wraps


def repeat(arg):
    def timer(fnc):
        """Calculates execution speed."""
        @wraps(fnc)
        def f(*args, **kwargs):
            for _ in range(times):
                print(f"Running {fnc.__name__}")
                before = time()
                ret_val = fnc(*args, **kwargs)
                after = time()
                print(f"Elapsed: {after - before}")
            return ret_val
        return f
    if callable(arg):
        times = 1
        return timer(arg)
    else:
        times = arg
        return timer


@repeat(3)
def add(x, y):
    """Calculates sum of two numbers."""
    return x + y


@repeat(3)
def sub(x, y):
    return x - y


print(f"add(10, 20) = {add(10, 20)}")
print(f"add(20, 30) = {add(20, 30)}")
print(f"add(30, 40) = {add(30, 40)}")
print(f"sub(20, 10) = {sub(20, 10)}")
print(f"sub(10, 5) = {sub(10, 5)}")
print(f"sub(5, 1) = {sub(5, 1)}")
print(add.__doc__)
