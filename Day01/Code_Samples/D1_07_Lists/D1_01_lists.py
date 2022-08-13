"""
 - Lists are mutable sequences.
 - Each element in a sequence is assigned an integer, called an index, that determines the order in which the values appear.
"""
my_list = [1, 2, 3]







"""
 - You can use built-in function list() to create
    a list from different sequence type
"""
my_list = list('list')  # ['l', 'i', 's', 't']








"""
 - There is a more useful way to create a list from a string
    using split(<separator>) and passing the separator string. 
 - split() always returns a string whose length is one more than
    the number of separators contained in the string. 
"""
fruits = "apple, orange, lemon"
fruit_list = fruits.split(", ")  # ['apple', 'orange', 'lemon']

"""
 - As with tuples, lists support indexing and slicing.
"""
my_list = [1, 2, 3, 4]
my_list[1]  # 2
my_list = my_list[:3]  # [1, 2, 3]








"""
 - Lists are iterable, so you can loop over them.
"""
for num in my_list:
    print(num)








"""
 - Lists can be unpacked.
"""
num1, *nums = my_list  # num1 = 1, nums = [2, 3]










"""
 - You can check if value exists in list using operator 'in'
"""
if 2 in my_list:
    print(f"Exists")








"""
 - You should use _ as a placeholder for data in a list that should be ignored.
"""
num1, num2, _ = my_list






"""
 - Lists are muttable, so you can swap their values
    one by one or using slice assignment.
"""
my_list[1] = 4  # now list has [1, 4, 3]
my_list[:2] = [5, 6]  # now list has [5, 6, 3]








"""
 - Be careful, since when the length of the list being assigned to the slice is
    less than the length of the slice, the overall length of the original list is reduced:
"""
my_list = ['apple', 'orange', 'lemon', 'banana', 'kiwi']

# ['apple', 'pineapple', 'cherry', 'kiwi']
my_list[1:4] = ['pineapple', 'cherry']








"""
 - Delete all elements from a list but save a reference to a list object with 'del'
"""
my_list = [1, 2, 3, 4]
del my_list[:]  # my_list is now empty []








"""
 - Creating list of arbitrary number of integers
"""
my_list = [3] * 5  # [3, 3, 3, 3, 3]
