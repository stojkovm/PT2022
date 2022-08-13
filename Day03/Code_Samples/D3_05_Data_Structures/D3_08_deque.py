"""
 - 'collections.deque' implements a double-ended queue that supports adding
    and removing elements from either end in O(1) time (non- amortized).
 - It can serve both as a queue (FIFO) and stack (LIFO) data structure.
"""
from collections import deque

d = deque()
d.append('a')  # ['a']
d.append('b')  # ['a', 'b']
d.appendleft('c')  # ['c', 'a', 'b']
print(d)
d.pop()  # ['c', 'a']
d.popleft()  # ['a']
print(d)
