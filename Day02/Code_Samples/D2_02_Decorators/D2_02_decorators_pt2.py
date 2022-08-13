from time import time


def timer(fnc, x, y):
    before = time()
    ret_val = fnc(x, y)
    after = time()
    print(f"Elapsed: {after - before}")
    return ret_val


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


print(f"add(10, 20) = {timer(add,10, 20)}")
print(f"add(20, 30) = {timer(add, 20, 30)}")
print(f"add(30, 40) = {timer(add, 30, 40)}")
print(f"sub(20, 10) = {timer(sub, 20, 10)}")
print(f"sub(10, 5) = {timer(sub, 10, 5)}")
print(f"sub(5, 1) = {timer(sub, 5, 1)}")
