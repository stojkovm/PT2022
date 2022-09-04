"""
 - PEP 484—Type Hints introduced syntax and semantics for explicit type declarations in
    function arguments, return values, and variables.
 - The goal is to help developers to find bugs in Python codebases via static analysis,
    i.e., without actually running the code through tests.
 - Type hinting is:
  - Optional
  - Does not catch type errors at runtime
  - Does not enhance performance
"""
"""
 - Mypy is an optional static type checker for Python that aims to combine
    the benefits of dynamic (or "duck") typing and static typing.
 - Installation:
    - pip install mypy
 - Usage:
    - mypy <file_name>.py --strict
"""


def multiply(x: int, y: int) -> int:
    return x * y


lst: list[int] = ['a', 'b', 'c']
