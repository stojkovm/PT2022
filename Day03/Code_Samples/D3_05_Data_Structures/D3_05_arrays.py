"""
 - Python's lists are implemented as dynamic arrays behind the scenes.
 - This means a list allows elements to be added or removed, and the list
    will automatically adjust the backing store that holds these elements by allocating or releasing memory.
 - 'array.array' provides space-efficient storage of basic C-style data types like bytes, 32-bit integers, floating point numbers.
 - They behave as lists with only difference they can contain only elements of a single data type.
 - Because of this constraint, array.array objects with many elements are more space-efficient than lists and tuples.
"""
from array import array

my_array1 = array('f', (2.3, 1.6, 7.5))
my_array2 = array('f', [2.3, 1.6, 7.5])
my_array1[0] = 1.2
del my_array2[1]
print(my_array1)
print(my_array2)
my_array1.append("a")  # TypeError
