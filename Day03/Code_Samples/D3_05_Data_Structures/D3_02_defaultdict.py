"""
 - 'collections.defaultdict' class is 'dict' subclass that accepts a callable
    in its constructor whose return value will be used if a requested key cannot be found.
"""
from collections import defaultdict

d = defaultdict(list)

"""
 - We are trying to access key 'first_name' that does not exist.
 - defaultdict will create empty list for the new key.
"""
d['first_names'].append('James')
d['first_names'].append('John')
d['first_names'].append('Huan')
print(d['first_names'])
