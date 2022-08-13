"""
 - For a given list of numbers, write a function that checks if all numbers
    are unique.
"""


def is_unique(lst):
    nums_set = set(lst)
    return len(lst) != len(nums_set)


print(is_unique([1, 2, 3, 4, 5]))
print(is_unique([1, 2, 3, 3, 4]))
print(is_unique([1, 2, 3, 4, 4]))
