"""
 - Genexp (generator expression) saves memory because it yields items one by one using the iterator protocol
    instead of building a whole list just to feed another constructor.
 - Genexps use the same syntax as listcomps, but are enclosed in parentheses rather than brackets.
"""

import itertools
import math


def is_prime(i):
    return all(i % j for j in range(2, i))


def is_perfect_square(sq):
    num = int(math.sqrt(sq))
    return num * num == sq


def is_fibonacci(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


def print_fib(gen, n=3):
    for i, _ in zip(gen, range(n)):
        print(i)


def prim_fib():
    for i in itertools.count():
        if is_prime(i) and is_fibonacci(i):
            yield i


print_fib(prim_fib(), 5)

prim_fib = (i for i in range(100) if is_prime(i) and is_fibonacci(i))
print_fib(prim_fib)
