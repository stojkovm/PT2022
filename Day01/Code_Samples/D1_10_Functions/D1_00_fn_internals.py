x = 10


def foo(x):
    y = x * 5
    return bar(y)


def bar(x):
    y = x / 5
    return y


z = foo(x)
