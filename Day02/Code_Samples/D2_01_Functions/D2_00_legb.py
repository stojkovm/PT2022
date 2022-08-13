z = 17


def foo(x):
    def bar(y):
        print(f"{x}:{y}:{z}:{print}")
    return bar


c1 = foo(10)
c1(5)
c2 = foo(20)
c2(5)
