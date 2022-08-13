lst = ['a', 'b', 'c']
for el in lst:
    print(el)

"""

 - The code below is similar to the code above.
"""
it = iter(lst)
while True:
    el = next(it)
    print(el)
