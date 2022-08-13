fruit = ['apple', 'orange', 'lemon']


def first_item():
    global fruit
    fruit = fruit[0]


def print_fruits():
    global fruit
    for entry in fruit:
        print(entry)


print_fruits()  # first_item()
print("----------")
print(fruit)
print("----------")
first_item()  # print_fruits()
print(fruit)
