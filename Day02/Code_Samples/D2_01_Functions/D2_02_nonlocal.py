
def foo():
    x = 10

    def bar():
        nonlocal x
        x = x + 10
        print(x)

    bar()


foo()
