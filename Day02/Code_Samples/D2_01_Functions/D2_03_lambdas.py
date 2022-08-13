"""
 - The 'lambda' keyword creates an anonymous function within a Python expression.
 - This syntax limits the body of lambda functions to be pure expressions,
    i.e., the body cannot contain other Python statements such as while, try, etc. 
 - The best use of anonymous functions is in the context of an argument list for a higher-order function.
"""

"""
 - Sorting a list of words by their length using lambda.
"""
fruits = ['apple', 'kiwi', 'orange', 'lemon', 'banana']
fruits = sorted(fruits, key=lambda word: len(word))
print(fruits)
