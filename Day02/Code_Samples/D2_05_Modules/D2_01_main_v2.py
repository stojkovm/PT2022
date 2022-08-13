"""
 - import <module> as <other_name>
 - When you import a module this way, the module's namespace is accessed
 through <other_name> instead of <module>.
"""
import basic_math_functions as bmf  # import calling module


def main():
    print(f"Results of four math operations for arguments 5 and 3:")
    print(f"Addition: {bmf.add(5, 3)}")
    print(f"Substraction: {bmf.sub(5, 3)}")
    print(f"Multiplication: {bmf.mul(5, 3)}")
    print(f"Division: {bmf.div(5, 3):.2f}")


if __name__ == "__main__":
    main()
