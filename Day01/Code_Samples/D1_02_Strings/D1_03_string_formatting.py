"""
 - Do not use this type of string formating since it is hard to read
    if more than few variables need to be part of the string.
"""
first_name = "James"
last_name = "Bond"
profession = "actor"
print("My name is " + last_name + ", " + first_name +
      " " + last_name + ". I am " + profession + ".")









"""
 - This is also old style way, using %.
"""
first_name = "James"
last_name = "Bond"
profession = "actor"
print("My name is %s, %s %s. I am %s." %
      (last_name, first_name, last_name, profession))








"""
 - There is a better way, using format()
"""
first_name = "James"
last_name = "Bond"
profession = "actor"
print("My name is {ln}, {fn} {ln}. I am {p}.".format(
    ln=last_name, fn=first_name, p=profession))










"""
 - Aaand there is the best way :) using interpolated format strings - f-strings (Python 3.6+, PEP498)
 - F-string is an expression evaluated at run time, not a constant value.
"""
first_name = "James"
last_name = "Bond"
profession = "actor"
print(
    f"My name is {last_name.upper()}, {first_name} {last_name}. I am {profession}.")









"""
    - Writting raw (unescaped) strings is done by adding !r after placeholder.
"""
my_variable = "\n\tHello\t\n"
print(f"Raw (unescaped) string {my_variable!r}")
