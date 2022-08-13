import basic_math_functions  # import calling module


def main():
    print(f"Results of four math operations for arguments 5 and 3:")
    print(f"Addition: {basic_math_functions.add(5, 3)}")
    print(f"Substraction: {basic_math_functions.sub(5, 3)}")
    print(f"Multiplication: {basic_math_functions.mul(5, 3)}")
    print(f"Division: {basic_math_functions.div(5, 3):.2f}")


if __name__ == "__main__":
    main()
