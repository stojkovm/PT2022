"""
 - Example of for loop
"""
fruits = ['apple', 'orange', 'lemon']  # collection
for fruit in fruits:
    print(fruit)









"""
 - for loop can end with optional else clause.
 - The code in else block will be executed only when loop
    sucessfully finishes its execution.
 - It is usually used when you search something in the loop.
 - else block may introduce misconception since in loops
    behaves diferently than in if-elif-else statement.
 - Avoid using else blocks after loops because their behavior
    is not intuitive and can be confusing.
"""
fruits = ['apple', 'orange', 'lemon']  # collection
for fruit in fruits:
    print(fruit)
else:
    print(f"For loop ended sucessfully!")








"""
 - If 'break' keyword is used to break out of for loop, else is not called.
"""
fruits = ['apple', 'orange', 'lemon']  # collection
for fruit in fruits:
    print(fruit)
    break
else:
    print(f"For loop ended sucessfully!")









"""
 - 'continue' keyword is used to skip the rest of the code in the loop
    and jump onto another iteration.
"""
fruits = ['apple', 'orange', 'lemon']  # collection
for i, fruit in enumerate(fruits):
    if fruit == 'apple':
        continue
    print(f"{i} : {fruit}")
else:
    print(f"For loop ended sucessfully!")
