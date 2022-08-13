"""
 - Refactor the following snippets of code to be more Pythonic.
"""
a = 11
b = 57
# if in if
# if a:
#     if b:
#         pass
if a and b:
    pass





# if-else to one-liner
# if a > b:
#     x = 1
# else:
#     x = 2

x = 1 if a > b else 2









# list check
lst = [1, 2, 3]
# if len(lst) > 0:
#     pass

if lst:
    pass





# simplyfy
names = ["James", "Huan", "Pablo"]
# for i in range(len(names)):
#   print(i+1, names[i])

for i, race in enumerate(names, 1):
  print(i, race)