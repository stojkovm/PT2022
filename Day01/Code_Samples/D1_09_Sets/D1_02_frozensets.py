"""
 - frozenset type is immutable.
 - It does not allows for the dynamic insertion and deletion of elements.
 - It can be used as dictionary key or as element of another set, something that is not possible with regular (mutable) set objects.
 - Common methods for manipulating sets:
  - my_set.difference(my_set2) - returns a set containing the difference between two or more sets
  - my_set.intersection(my_set2) - returns a set, that is the intersection of two or more sets
  - my_set.union(my_set2) - update the set with another set, or any other iterable
  - my_set.symmetric_difference(my_set2) - returns a set that contains all items from both sets, except items that are present in both sets
"""
letters = frozenset({'a', 'b', 'c', 'd', 'e'})
more_letters = frozenset({'d', 'e', 'f', 'g'})
letters.difference(more_letters)  # frozenset({'b', 'c', 'a'})
letters.intersection(more_letters)  # frozenset({'d', 'e'})
letters.union(more_letters)  # frozenset({'d', 'a', 'e', 'g', 'c', 'b', 'f'})
# frozenset({'a', 'g', 'c', 'b', 'f'})
letters.symmetric_difference(more_letters)







"""
 - Frozensets can be looped over.
"""
for l in letters:
    print(l)








"""
 - You can check if value exists in frozenset using operator 'in'
"""
if 'a' in letters:
    print(f"Exists")
