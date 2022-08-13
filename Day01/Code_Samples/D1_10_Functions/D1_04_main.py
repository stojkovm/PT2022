def multiply(x, y):
    """Return the product of two numbers x and y.

    Parameters
    ----------
    x : int
        The first number.
    y : int
        The second number.

    Returns
    -------
    product : int
        A product of two numbers.
    """
    product = x * y
    return product


def main():
    print(f"Result of multiplication: {multiply(5, 3)}")


"""
 - Since there is no main() function in Python, when the command to run a Python program is given to the interpreter,
    the code that is at level 0 indentation is to be executed.
 - Before doing that, it will define a __name__ variable.
 - If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”.
 - If this file is being imported from another module, __name__ will be set to the module’s name.
 - __name__ is a built-in variable which evaluates to the name of the current module.
"""

if __name__ == "__main__":
    main()
