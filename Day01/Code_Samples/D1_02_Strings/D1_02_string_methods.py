"""
 - Common methods used with strings:
    - lower()/upper() - converts each character in a string to lower or upper case
    - startswith(<arbitrary_string>)/endswith(<arbitrary_string>) - checks if a given string starts with or ends with provided characters
    - strip()/lstrip()/rstrip() - removes the whitespaces on both sides of a string/only left side/only right side
    - find(<arbitrary_string>) - finds the index of the first occurrence of the provided sequence or -1
    - replace(<arbitrary_string>, <other_string>) - finds and replaces all occurrences of one character sequence with another
    - join() - takes all items in an iterable and joins them into one string
    - split(<arbitrary_string>) - splits the string using optional separator into a list where each word is a list item
"""

my_variable = "James Bond"
my_variable = my_variable.lower()

my_variable = "   James Bond   "
my_variable = my_variable.strip()

my_variable = "James Bond"
index_occ = my_variable.find("Bond")  # returns 6








"""
 - Use ''.join when creating a single string for list elements
"""
name_collection = ["James", "Arthur", "John"]
result_string = ', '.join(name_collection)

name = "James Bond"
name_parts = name.split()  # ['James', 'Bond']








"""
 - To interact with user input use built-in function input()
"""
response = input("What is your name?")
print(response)  # prints whatever user typed in









"""
 - Numbers can be converted to strings with built-in function str()
 - If you do not convert numbers to strings, they cannot be concatenated with strings
    and you will gey TypeError
"""
my_variable = 5
print("The value of my_variable is: " + str(my_variable))










"""
 - Chain string functions to make a simple series of transformations more clear.
"""
actor_info = '   Name- James Bond, Profession- actor'
formatted_actor_info = actor_info.strip().replace('-', ':')
