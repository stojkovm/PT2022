import math

"""
 - A set comprehension is a short-hand for a 'for' loop.
"""
def is_prime(i):
    return all(i % j for j in range(2, i))


def is_perfect_square(sq):
    num = int(math.sqrt(sq))
    return num * num == sq


def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


def is_fibonacci(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)


print([fibonacci(num) for num in range(10)])

"""
 - The following example can be replaced with set comprehension.
"""
primes = set()
fibonaccis = set()
for i in range(2, 1000):
    if is_prime(i):
        primes.add(i)
    if is_fibonacci(i):
        fibonaccis.add(i)
result = primes & fibonaccis
print(result)



"""
 - In one line!
"""
result = {num for num in range(2, 1000) if is_prime(num) and is_fibonacci(num)}
print(set(result))
