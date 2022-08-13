"""
 - Example implementation of custom iterator.
"""


class CounterIterator:

    def __init__(self, low, high):
        self._current = low
        self._high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self._current >= self._high:
            raise StopIteration
        else:
            self._current += 1
            return self._current - 1


for c in CounterIterator(1, 4):
    print(c)
