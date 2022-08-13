"""
 - Common methods for manipulating list objects:
    - my_dict.get(<key>, <fallback_value>) - looks up value for provided key while providing a fallback value if the key does not exist 
    - my_dict.setdefault(<key>, <default_value>) - if the key does not exist, insert the key, with the specified value
    - my_dict.popitem() - removes the last inserted item
    - my_dict.clear() - empties the whole dictionary
    - dict.fromkeys(<keys>, <optional_value>) - returns a dictionary with the specified keys and the specified value (all the values are the same)
"""
countries = {
    "CH": "Switzerland",
    "US": "United States",
    "RS": "Serbia"
}
country = countries.get("DE")  # returns None by default

# adds new entry with "DE" : "Undefined" key-value pair
country = countries.setdefault("DE", "Undefined")

contry = countries.popitem()

alphabets = {'a', 'b', 'c'}
number = 1
my_dict = dict.fromkeys(alphabets, number)  # {'a': 1, 'c': 1, 'b': 1}









"""
 - Merging two dictionaries can be done using double asterisk (**)
 - Merging two dictionaries can be done using update() method
 - Merging two dictionaries can be done using | or |= operator
 - Later keys override previous.
"""
my_dict1 = {'a': 1, 'b': 2}
my_dict2 = {'c': 3, 'd': 4}
my_dict3 = {**my_dict1, **my_dict2}
my_dict3 = {}
my_dict3.update(my_dict1)
my_dict3.update(my_dict2)
my_dict3 = {}
my_dict3 = my_dict1 | my_dict2
my_dict1 |= my_dict2
