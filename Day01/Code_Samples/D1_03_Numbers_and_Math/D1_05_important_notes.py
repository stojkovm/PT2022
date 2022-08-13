"""
 - The floating-point representation error.
 - The x below is expected to be 0.3, but it is actually
    0.30000000000000004 due to a floating-point representation error.
 - The number 0.1 can be represented correctly in base10 representation.
    That is not the case in base2 or binary representation.
 - Some numbers can have the same binary approximation,
    and Python prints the shortest decimal number that shares the approximation.
 - In the example below, Python adds two binary approximations for 0.1 and 0.2,
    which gives a number that is not the binary approximation for 0.3.
 - Solution: use decimal module or 3rd party modules with arbitrary precision such as mpmath, sympy, etc.
"""
x = 0.1 + 0.2







"""
 - Common built-in functions used with numbers are:
    - abs() - get the absolute value of a number
    - pow() - raise a number to arbitrary power
    - round() - round number to some number of decimal places
"""
y = abs(-5.0)

# pow() takes basis 2 and raises it to a power of 3
z = pow(2, 3)

# pow takes optional third argument 4 that takes the modulo of 2^3 - (x ** y) % z
z = pow(2, 3, 4)








"""
 - The round() function might have unexpected behavior if the number ends with .5.
 - Python follows a rounding strategy called "Round to nearest - ties to even".
 - In this strategy, a tie is a number that has five as a last digit.
 - The strategy rounds the number by looking at the number that is left to the last digit in a tie.
 - If that digit is even, the number is round down.
 - If that digit is odd, the number is round up.
"""
p = round(7.5)  # 8

q = round(8.5)  # 8
