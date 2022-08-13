from time import time
from functools import wraps


def timer(fnc):
    """Calculates execution speed."""
    @wraps(fnc)
    def f(*args, **kwargs):
        before = time()
        ret_val = fnc(*args, **kwargs)
        after = time()
        print(f"Elapsed: {after - before}")
        return ret_val
    return f


@timer
def add(x, y):
    """Calculates sum of two numbers."""
    return x + y


#add = timer(add)

@timer
def sub(x, y):
    return x - y


#sub = timer(sub)


print(f"add(10, 20) = {add(10, 20)}")
print(f"add(20, 30) = {add(20, 30)}")
print(f"add(30, 40) = {add(30, 40)}")
print(f"sub(20, 10) = {sub(20, 10)}")
print(f"sub(10, 5) = {sub(10, 5)}")
print(f"sub(5, 1) = {sub(5, 1)}")
print(add.__doc__)
