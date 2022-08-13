"""
- PEP8 recommends separating both operands
    from an operator with whitespace.
"""

# ADDition
x = 1.0 + 4

# SUBstraction
y = 4.2 - 2

# MULtiplication
z = 3 * 3






"""
 - DIVision with / always returns a float.
 - If you need an integer, you have to convert the result with int()
"""
p = 12.0 / 3







"""
 - Integer division with //
 - The operator // first divides the number on the left by the number
    on the right and then rounds down to an integer.
"""
q = 12 // 3







"""
 - To raise a number to a power use ** operator.
"""
r = 3 ** 3








"""
 - To return the remainder of division, use % (modulus) operator.
 - When using % on negative numbers, Python uses the equation for x % y:
    r = x - (y * (x // y))
"""
s = 5 % -3
