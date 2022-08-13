from library2 import Base


class Derived(Base):

    def ba(self):
        return "bar"


d = Derived()
print(d.foo())
