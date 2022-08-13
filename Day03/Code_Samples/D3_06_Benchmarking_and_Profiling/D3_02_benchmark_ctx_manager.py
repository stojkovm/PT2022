import time


class TimerCtx:
    def __init__(self, fnc):
        self.start = time.perf_counter()
        self.fnc = fnc

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        end = time.perf_counter()
        runtime = end - self.start
        print(f"Function: {self.fnc.__name__}, running time: {runtime}.")


def num_sum():
    sum = 0
    for n in range(100):
        sum += n
        time.sleep(.05)
    return sum


with TimerCtx(num_sum):
    print(num_sum())
