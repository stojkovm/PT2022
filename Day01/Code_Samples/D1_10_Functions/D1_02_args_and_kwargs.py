"""
 - *args and **kwargs allow a function to accept optional arguments.
 - If we call the function with additional arguments, 'args' will collect extra positional arguments
    as a tuple because the parameter name has a * prefix.
 - 'kwargs' will collect extra keyword arguments as a dictionary
    because the parameter name has a ** prefix.
 - Both args and kwargs can be empty if no extra arguments are passed to the function.
 - args and kwargs can be substituted with other names,
    asterisk (*) and double asterisk (**) are important parts. 
"""


def foo(required, *args, **kwargs):
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


# generates an TypeError since we have one required argument
# foo()

foo('my required arg')
foo('my required arg', 1, 2, 'hello')
foo('my required arg', key1='val1', key2='val2')
foo('my required arg', 1, 2, 'hello', key1='val1', key2='val2')








"""
 - It is possible to pass optional or keyword parameters from one function to another. 
"""
def bar(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )
    foo(x, *new_args, **kwargs)

bar('my required arg', 1, 2, 'hello', key1='val1', key2='val2')









"""
 - Arguments can have default values if nothing is passed.
"""
def foo(greeting='Hello', name=None):
    print(f"{greeting} {name}!")


foo(name='James')
