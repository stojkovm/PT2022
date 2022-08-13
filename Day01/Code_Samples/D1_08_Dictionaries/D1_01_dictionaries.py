"""
 - Dictionaries are data structures that store collection of objects as key-value pairs
 - The key is a unique name that identifies the value part of the pair
 - Key-value pairs can be of any types, even each key-value pair can be of a different types
 - Each key is separated from its value by a colon (:) 
 - Each key-value pair is separated by a comma (,) 
 - Dictionary literals are surrounded with curly braces { and }
 - From Python 3.6 the order of the key-value pairs is guaranteed to match the order in which they were inserted.
"""
countries = {
    "CH": "Switzerland",
    "US": "United States",
    "RS": "Serbia"
}

"""
 - Dictionary can be created from a sequence of tuples using the dict() built-in function.
"""
key_value_pairs = (("CH", "Switzerland"),
                   ("US", "United States"), ("RS", "Serbia"),)
countries = dict(key_value_pairs)








"""
 - Accessing dictionary values is done by providing key in square brackets [].
"""
countries["CH"]








"""
 - Updating vaulues in dictionary directly or using update() method.
"""
countries["US"] = "United States of America"
countries.update({"RS": "Republic of Serbia"})









"""
 - Adding new key-value pair.
"""
countries["DE"] = "Germany"







"""
 - Removing key-value pair with 'del' keyword or with pop() method.
 - pop() returns the value of deleted key-value pair.
"""
del countries["DE"]
countries.pop("RS")








"""
 - You can check if the KEY exists in dictionary using operator 'in'
"""
if "CH" in countries:
    print(f"Exists")








"""
 - Dictionaries are iterable, so you can loop over them in different ways.
 - By default, using for loop you iterate over keys
"""
for key in countries:
    print(f"For country {countries[key]}, country code is {key}")










"""
 - You get the same effect by using keys() method
"""
for key in countries.keys():
    print(f"For country {countries[key]}, country code is {key}")









"""
 - If both information is needed, items() method can be called.
 - items() returns list-like object (the type is dict_items) that contains tuples of key-value pairs.
"""
for key, value in countries.items():
    print(f"For country {value}, country code is {key}")
