"""
 - Count the number of spaces in a string using list comprehension.
"""
sentence = 'The quick brown fox jumps over the lazy dog.'
num_spaces = [s for s in sentence if s == ' ']
print(len(num_spaces))
