from time import time


def add(x, y):
    before = time()
    ret_val = x + y
    after = time()
    print(f"Elapsed: {after - before}")
    return ret_val


def sub(x, y):
    before = time()
    ret_val = x - y
    after = time()
    print(f"Elapsed: {after - before}")
    return ret_val


print(f"add(10, 20) = {add(10, 20)}")
print(f"add(20, 30) = {add(20, 30)}")
print(f"add(30, 40) = {add(30, 40)}")
print(f"sub(20, 10) = {sub(20, 10)}")
print(f"sub(10, 5) = {sub(10, 5)}")
print(f"sub(5, 1) = {sub(5, 1)}")
