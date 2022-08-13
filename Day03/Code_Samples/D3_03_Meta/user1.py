"""
 - Scenario one:
    - Core library team has implemented some functionality.
    - User library team wants to use library1 module.
    - How User library team can defend themself of inapropriate implementation
        by Core library team's module?
"""

from library1 import Base

assert hasattr(Base, "foo"), "foo does not exist!"


class Derived(Base):

    def bar(self):
        return self.foo()
