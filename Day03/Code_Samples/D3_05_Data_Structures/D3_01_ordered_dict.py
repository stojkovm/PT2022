"""
 - Python includes a specialized dict subclass that remembers the insertion order of keys added to it - 'collections.OrderedDict'.
 - While standard 'dict' instances preserve the insertion order of keys in CPython 3.6 and above,
    this is just a side effect of the CPython implementation and is not defined in the language specification.
"""
from collections import OrderedDict

d = OrderedDict(key1='c', key2="b", key3='a')
print(d)
d['key4'] = 'd'
print(d)
print(d.keys())
