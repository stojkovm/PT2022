"""
 - The cProfile profiler is used for analyzing a running application
    and collecting deterministic profiles on the frames evaluated.
 - The result of profiling is written in table:
    - 'ncalls' is the number of calls made.
    - 'tottime' is a total of the time spent in the given function.
    - 'percall' refers to the quotient of tottime divided by ncalls.
    - 'cumtime' is the cumulative time spent in this and all subfunctions.
    - 'percall' column is the quotient of cumtime divided by primitive calls.
    - 'filename:lineno(function)' provides the respective data of each function.
"""

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
