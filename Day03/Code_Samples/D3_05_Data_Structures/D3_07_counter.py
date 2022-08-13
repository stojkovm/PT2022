"""
 - 'collections.Counter' class in the Python standard library implements a multiset (or bag)
    type that allows elements in the set to have more than one occurrence.
 - This is useful if you need to keep track of not only if an element is part
    of a set, but also how many times it is included in the set.
"""
from collections import Counter

inventory = Counter()
apples = {'apple': 30}
inventory.update(apples)  # {'apple': 22}
apples_and_oranges = {'apple': 22, 'orange': 31}
inventory.update(apples_and_oranges)  # {'apple': 52, 'orange': 31}
print(inventory)
