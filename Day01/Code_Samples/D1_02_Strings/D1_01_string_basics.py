"""
- String is a sequence of characters with abbreviated name - str.
- If we want to check what is the type of a value of a variable,
    we can call the built-in function type()
"""
x = type("this is a string")








"""
 - Every string has a length that is determined by calling
    the built-in function len()
"""
y = len("this is a string")








"""
 - PEP8 recommends that each line of Python code contains
    no more than 79 characters including spaces.
 - Multiline strings can be constructed by ending each but the last line with backslash
    or surrounding string with triple quotes as delimiters.
"""
z = "This is \
    multiline string."






"""
 - Triple quotes preserve whitespaces printing strings as original literals.
"""
p = """This
is also multiline
string."""







"""
 - String concatenation is done with operator +.
"""
first_name = "James"
last_name = "Bond"
full_name = first_name + " " + last_name







"""
 - Each character in a string has its position - index.
 - Accessing the character in a specific position is done
    by placing index between square brackets after the string variable.
 - The counting starts at 0 (zero).
"""
my_variable = "James Bond"
letter = my_variable[6]  # reads letter 'B'






"""
 - Strings support negative indices.
 - This makes it easy to read the character in the last position.
"""
my_variable = "James Bond"
letter = my_variable[-1]  # reads letter 'd'







"""
 - String slicing can be done by manipulating with indexes.
 - variable[x:y] reads the substring that starts with character at index x and
    goes up to but not including character at index y.
 - By omitting the index x, it is assumed that slicing starts at index 0.
 - By omitting the index y, it is assumed that slicing ends with the last character in the string.
"""
my_variable = "James Bond"
print(my_variable[0:5])  # prints 'James'






"""
 - Strings are immutable meaning that they cannot be changed once created.
 - You must create completely new string instead.
"""
my_variable = "James Bond"
# this will generate TypeError
# my_variable[0] = "H"
my_variable = "H" + my_variable[1:]
