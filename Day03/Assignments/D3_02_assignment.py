"""
 - first_names.txt contains list of first names correctly written.
 - last_names.txt contans list of last names with all capital letters.
 - Assignment:
    - Using context manager syntax merge two files into one.
    - Last names must have only first letter capitalized.
    - full_names.txt content should look like this:
        James Bond
        Aghata Christie
        Sherlock Holmes
    

 - Hits:
    - open(filename, "r") opens file in read mode
    - open(fn_filename, "w") opens file in write mode
    - ctx managers have specific syntax: with ctx(___) as x:
"""


def convert(fn_filename, ln_filename, full_name):
    pass


if __name__ == "__main__":
    convert('first_names.txt', "last_names.txt", "full_names.txt")
