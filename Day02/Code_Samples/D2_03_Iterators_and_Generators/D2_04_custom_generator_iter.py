"""
 - Example implementation of custom iterator using generator function.
"""


def counter_generator(low, high):
    current = low
    while current < high:
        yield current
        current += 1


for c in counter_generator(1, 4):
    print(c)
