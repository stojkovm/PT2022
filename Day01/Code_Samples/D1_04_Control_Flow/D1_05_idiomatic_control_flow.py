"""
 - Avoid repeating variable name in compound if statement
"""
# this is not pythonic way to do it
is_found = False
name = 'John'
if name == 'James' or name == 'John' or name == 'Garry':
    is_found = True

# this is way to go
name = 'John'
is_found = name in ('James', 'John', 'Garry')








"""
 - Avoid placing conditional branch code on the same line as
    the colon (:)
"""

# this is not pythonic way to do it
# name = 'James'
# profession = 'actor'
# if name: print(name)
# print(profession)

# this is way to go
name = 'James'
profession = 'actor'
if name:
    print(name)
print(profession)








"""
 - Avoid comparing directly to True, False
 - Rely on implicit "truthiness"
 - The following are considered False:
    - None
    - False
    - zero for numeric types
    - empty sequences
    - empty dictionaries
    - a value of 0 or False returned when either __len__ or __nonzero__ is called
 - Everything else is considered True (and thus most things are implicitly True).
"""
message = None
if message:
    print(f"Detailed description: {message}")
else:
    print(f"Message is empty!")
