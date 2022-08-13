"""
 - Assignment expression (walrus operator :=) is introduced in Python 3.8
    to solve code duplication problem.
 - It enables assigning variables in places this is not allowed, such as if statement.
"""
fruits = {
    'apple': 11,
    'orange': 7,
    'lemon': 9,
}

if (count := fruits.get('apple', 0)) >= 2:
    print(f"Making juice...")
else:
    print(f"Out of stock!")







"""
 - 'Faking' the switch statement with walrus operator.
"""

fruits = {
    'apple': 11,
    'orange': 7,
    'lemon': 9,
}

if (count := fruits.get('apple', 0)) >= 2:
    print(f"Making apple juice...")
    # do something with apples
elif (count := fruits.get('orange', 0)) >= 3:
    print(f"Making orange juice...")
    # do something with oranges
elif count := fruits.get('lemon', 0):
    print(f"Making lemonade...")
    # do something with lemons
else:
    print(f"Not enough fruit...")
    # do something with apples
