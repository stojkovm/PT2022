"""
 - Common methods for manipulating list objects:
    - lst.append(<el>) - adds new element at the end of the list
    - lst.pop(<index>) - retrieves and removes element from specified position (or element at the end if index is not provided) 
    - lst.insert(<index>, <el>) - inserts new element on specified position
    - lst.extend(<iterable>) - extends one list with another (+= does the same)
    - len(<lst>) - returns number of elements in list
    - min(<lst>) - returns smallest item of list
    - max(<lst>) - returns largest item of list
    - lst.index(<x>) - returns index of the first occurrence of x in list
    - lst.count(<x>) - returns total number of occurrences of x in list
    - lst.sort(*, key=None, reverse=False) - sorts the list in-place
    - sorted(lst, /, *, key=None, reverse=False) - creates new instance
"""
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # [1, 2, 3, 4, 5, 6]
my_list.extend([7, 8])  # [1, 2, 3, 4, 5, 6, 7, 8]
my_list.insert(2, 17)  # [1, 2, 17, 3, 4, 5, 6, 7, 8]
my_list.pop(2)  # returns and removes 17
len(my_list)  # returns 8
min(my_list)  # returns 1
max(my_list)  # returns 8
my_list.index(2)  # returns 1
my_list.count(3)  # returns 1
my_list += [9, 10]  # [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
# after calling sort, my_list looks like this [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
my_list.sort(reverse=True)
fruit_list = ['apple', 'pineapple', 'kiwi']
# after calling sorted with len function provided, new list with elements sorted by string length is returned ['kiwi', 'apple', 'pineapple']
fruit_list = sorted(fruit_list, key=len)
