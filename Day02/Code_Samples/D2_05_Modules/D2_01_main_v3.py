"""
 - from <module> import <name>
 - Instead of importing the entire namespace, you can import only a specific name from a module.
"""
from basic_math_functions import add, sub, mul, div  # import calling module


def main():
    print(f"Results of four math operations for arguments 5 and 3:")
    print(f"Addition: {add(5, 3)}")
    print(f"Substraction: {sub(5, 3)}")
    print(f"Multiplication: {mul(5, 3)}")
    print(f"Division: {div(5, 3):.2f}")


if __name__ == "__main__":
    main()
