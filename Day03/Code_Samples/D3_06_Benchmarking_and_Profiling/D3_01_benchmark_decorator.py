import time
from functools import wraps


def timer(fnc):
    @wraps(fnc)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        ret_val = fnc(*args, **kwargs)
        end = time.perf_counter()
        runtime = end - start
        print(f"Function: {fnc.__name__}, running time: {runtime}.")
        return ret_val
    return inner


@timer
def num_sum():
    """Sums first 100 numbers with a little delay."""
    sum = 0
    for n in range(100):
        sum += n
        time.sleep(.05)
    return sum


print(f"Result: {num_sum()}")
