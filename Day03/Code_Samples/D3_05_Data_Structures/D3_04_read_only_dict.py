"""
 - 'types.MappingProxyType' is a wrapper around a standard dictionary
    that provides a read-only view into the wrapped dictionary's data.
 - This can be helpful if you would like to return a dictionary carrying
    internal state from a class or module, while discouraging write access to this object. 
"""
from types import MappingProxyType

original_dict = {'a': 1, 'b': 2}
read_only_dict = MappingProxyType(original_dict)

print(read_only_dict['a'])
# read_only_dict['a'] = 3 # TypeError

"""
 - Updates to tthe original are reflected in the read-only dict.
"""
original_dict['c'] = 3
print(read_only_dict['c'])
