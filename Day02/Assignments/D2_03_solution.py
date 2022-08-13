"""
 - Given a list of numbers, remove numbers with type float using list comprehension.
"""

original_list = [1, 2.33, 32.21, 5, 3.37, 9, 8.4]
only_ints = [number for number in original_list if type(number) == int]
print(only_ints)
