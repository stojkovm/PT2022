"""
 - Example of while loop
"""
n = 1
while n < 5:
    print(n)
    n = n + 1  # or use more pythonic +=









"""
 - while loop can end with optional else clause.
 - The code in else block will be executed only when loop
    sucessfully finishes its execution.
 - It is usually used when you search something in the loop.
 - else block may introduce misconception since in loops
    behaves diferently than in if-elif-else statement.
 - Avoid using else blocks after loops because their behavior
    is not intuitive and can be confusing.
"""
n = 1
while n < 5:
    print(n)
    n = n + 1
else:
    print(f"While loop ended sucessfully!")
