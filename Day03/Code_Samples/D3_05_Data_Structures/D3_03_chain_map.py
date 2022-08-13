"""
 - 'collections.ChainMap' data structure groups multiple dictionaries into a single mapping.
 - Lookups search the underlying mappings one by one until a key is found.
 - Insertions, updates, and deletions only affect the first mapping added to the chain.
"""
from collections import ChainMap

my_dict1 = {'a': 1, 'b': 2}
my_dict2 = {'c': 3, 'd': 4}
chain_dict = ChainMap(my_dict1, my_dict2)
print(chain_dict['d'])
