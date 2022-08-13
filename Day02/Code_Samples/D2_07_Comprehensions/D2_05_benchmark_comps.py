import timeit

TIMES = 10000

REPEAT = 5

SETUP = """
def is_even(num):
    return num % 2 == 0

def square(num):
    return num ** 2
"""


def run(label, cmd):
    result = timeit.repeat(cmd, setup=SETUP, number=TIMES, repeat=REPEAT)
    print(f"{label} {[f'{t:.2f}' for t in result]}")
    print(f"{label} Avg: {sum(result)/len(result):.2f}")


run("filter + lambda     :",
    "list(filter(lambda num: num % 2 == 0, map(square, range(100))))")
run("filter + function   :", "list(filter(is_even, map(square, range(100))))")
run("listcomp            :",
    "[num ** 2 for num in range(100) if num % 2 == 0]")
run("listcomp + function :",
    "[num ** 2 for num in range(100) if is_even(num)]")
