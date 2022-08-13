"""
 - Use built-in function range() to iterate over a set of integers.
 - range(start, stop, step) generates the immutable sequence
    of integers starting from the given start integer (including)
    to the stop integer (excluding).
"""
# prints integers 0 to 4
import itertools
for i in range(5):
    print(i)

# prints odd integers 1, 3, 5
for i in range(1, 6, 2):
    print(i)









"""
 - Use the enumerate(iterator, start_number) built-in function in loops instead of creating an “index” variable
 - You can supply a second parameter to enumerate() to specify the number from which to begin counting (zero is the default).
"""
fruits = ['apple', 'orange', 'lemon']
for i, fruit in enumerate(fruits, 1):
    print(f"{i}: {fruit}")









"""
 - Use the zip() built-in function to process collections in parallel.
 - zip() yields tuples until any one of the wrapped collections is exhausted.
 - Its output is as long as its shortest input.
"""
names = ['James', 'John', 'Fernando']
counts = [5, 4, 8]
longest_name = None
max_count = 0

# don't do it like this
for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count
print(longest_name)

# do it in a pythonic way
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
print(longest_name)










"""
 - If collections have different lenghts, use zip_longest function
     from itertools module.
"""

names = ['James', 'John', 'Fernando', 'Juan']
counts = [5, 4, 8]

for name, count in itertools.zip_longest(names, counts):
    print(f"{name} : {count}")
