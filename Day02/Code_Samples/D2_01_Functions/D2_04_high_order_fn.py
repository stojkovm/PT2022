"""
 - map(<func>, <iterable>) function returns a map object(which is an iterator) of the results
    after applying the given function to each item of a given iterable (list, tuple etc.)
"""
from functools import reduce


def square(n):
    return n ** 2


numbers = [1, 2, 3, 4]
result = map(square, numbers)
print(list(result))
result = map(lambda n: n ** 2, numbers)
print(list(result))

"""
 - The filter(<func>, <iterable>) method filters the given sequence
    with the help of a function that tests each element in the sequence to be true or not.
 - filter() returns an iterator.
"""


def is_vowel(letter):
    letters = ['a', 'e', 'i', 'o', 'u']
    return True if letter in letters else False


letters = ['a', 'g', 'a', 'v', 'a']
filtered = filter(is_vowel, letters)
print(list(filtered))

"""
 - You can combine map with other functions.
"""


def is_odd(num):
    return num % 2 != 0


numbers = [1, 2, 3, 4]
filtered = map(square, filter(is_odd, numbers))
print(list(filtered))


"""
 - reduce(<fun>, <iterable>) function is used to apply a particular
    function passed in its argument to all of the list elements mentioned in the sequence passed along.
 - reduce() is defined in “functools” module.
 - How it works:
  - First two elements of sequence are picked and the function is applied.
  - The same function is applied to the result returned and the next element.
  - This process is repeated until no elements in iterable is left.
"""

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120

"""
 - all(<iterable>) function returns True if all elements in sequence are evaluated as True.
"""
numbers = [0, 1, 2, 3]
print(all(numbers))  # returns False

"""
 - any(<iterable>) function returns True if any element in sequence are evaluated as True.
"""
booleans = [True, False, False, True]
print(any(booleans))  # returns True
