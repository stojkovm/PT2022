"""
 - Tuples are immutable sequences.
 - Each element in a sequence is assigned an integer, called an index, that determines the order in which the values appear.
"""
my_tuple = (1, 2, 3)










"""
 - To create tuple that has only one value, include comma (,)
"""
my_tuple_with_one_value = (1, )










"""
 - You can use built-in function tuple() to create
    a tuple from different sequence type
"""
my_tuple = tuple('Tuple')  # ('T', 'u', 'p', 'l', 'e')










"""
 - As with strings, tuples support indexing and slicing.
"""
my_tuple = (1, 2, 3)
my_tuple[1]  # 2
my_tuple = my_tuple[:2]  # (1, 2)







"""
 - Tuples are iterable, so you can loop over them.
"""
for num in my_tuple:
    print(num)








"""
 - Third way to create a tuple is to provide comma-separated list of values.
 - This process is called packing.
"""
my_tuple = 1, 2, 3
print(my_tuple)  # (1, 2, 3)









"""
 - Tuples can be unpacked.
"""
num1, num2, num3 = my_tuple








"""
 - You can check if value exists in tuple using operator 'in'
"""
if 3 in my_tuple:
    print(f"Exists")


"""
 - You should use _ as a placeholder for data in a tuple that should be ignored.
"""
num1, num2, _ = my_tuple








"""
 - Common methods for manipulating tuple objects:
    - len(<tpl>) - returns number of elements in tuple
    - min(<tpl>) - returns smallest item of tuple
    - max(<tpl>) - returns largest item of tuple
    - tpl.index(<x>) - returns index of the first occurrence of x in tuple
    - tpl.count(<x>) - returns total number of occurrences of x in tuple
"""
my_tuple = 1, 2, 3, 4, 5
len(my_tuple)  # returns 5
min(my_tuple)  # returns 1
max(my_tuple)  # returns 5
my_tuple.index(2)  # returns 1
my_tuple.count(3)  # returns 1
