"""
 - set type is mutable.
 - It allows for the dynamic insertion and deletion of elements.
 - Python’s sets are backed by the dict data type and share the same performance characteristics.
"""
my_set = set()
my_set = {'apple', 'orange', 'lemon'}








"""
 - Common methods for manipulating sets:
  - my_set.add() - adds an element to the set
  - my_set.pop() - removes a random an element from the set
  - my_set.remove(<el>) - Removes the specified element
  - my_set.difference(my_set2) - returns a set containing the difference between two or more sets (my_set - my_set2)
  - my_set.intersection(my_set2) - returns a set, that is the intersection of two or more sets (my_set & my_set2)
  - my_set.union(my_set2) - update the set with another set, or any other iterable (my_set | my_set2)
  - my_set.symmetric_difference(my_set2) - returns a set that contains all items from both sets, except items that are present in both sets (my_set ^ my_set2)
"""
letters = {'a', 'b', 'c', 'd', 'e'}
more_letters = {'d', 'e', 'f', 'g'}
letters.add('f')
letters.remove('d')
letters.difference(more_letters)  # {'b', 'c', 'a'}
letters.intersection(more_letters)  # {'f', 'e'}
letters.union(more_letters)  # {'d', 'a', 'e', 'g', 'c', 'b', 'f'}
letters.symmetric_difference(more_letters)  # {'d', 'a', 'g', 'c', 'b'}








"""
 - Sets can be looped over.
"""
for l in letters:
    print(l)








"""
 - You can check if value exists in set using operator 'in'
"""
if 'a' in letters:
    print(f"Exists")
