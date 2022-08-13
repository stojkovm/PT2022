"""
 - A list comprehension is a short-hand for a 'for' loop.
"""
numbers = [1, 2, 3]
square_numbers = []
for num in numbers:
    square_numbers.append(num ** 2)







"""
 - A list comprehension is replacement for map()/filter() functions.
"""
def square(num):
    return num ** 2


def is_even(num):
    return num % 2 == 0


square_numbers = list(map(square, numbers))
square_numbers = list(map(square, filter(is_even, numbers)))


square_numbers = [num ** 2 for num in numbers]




"""
 - List comprehensions can have if conditions too.
"""
even_square_numbers = [num ** 2 for num in range(10) if num % 2 == 0]





"""
 - Avoid more than two control subexpressions in comprehensions.
"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)

matrix = [[x ** 2 for x in row] for row in matrix]







"""
 - What is wrong with this code?
"""
zeros = [[0, 0, 0]] * 3
print(zeros) # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
zeros[0][2] = 1 # [[0, 0, 1], [0, 0, 1], [0, 0, 1]]
print(zeros)
# solution
zeros = [[0] * 3 for _ in range(3)]
print(zeros)






"""
 - Scope of variables in list comprehensions is local if walrus operator (:=) is not used.
"""
numbers = [1, 2, 3]
#square_numbers = [num ** 2 for num in numbers]
# print(num) # NameError: name 'num' is not defined.
square_numbers = [last := num ** 2 for num in numbers]
print(last)  # prints 9
