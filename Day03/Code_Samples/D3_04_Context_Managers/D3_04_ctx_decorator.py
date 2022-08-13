from sqlite3 import connect
"""
 - This is already provided through contextlib for us:
 - from contextlib import contextmanager
"""


class contextmanager:
    def __init__(self, gen):
        self.gen = gen

    def __call__(self, *args, **kwargs):
        self.args, self.kwargs = args, kwargs
        return self

    def __enter__(self):
        self.gen_instance = self.gen(*self.args, **self.kwargs)
        next(self.gen_instance)

    def __exit__(self, *args):
        next(self.gen_instance, None)


@contextmanager
def temptable(cur):
    print("__enter__")
    cur.execute('create table points(x int, y int)')
    try:
        yield
    finally:
        cur.execute('drop table points')
        print("__exit__")


"""
 - Is this maybe syntax for decorators?
"""
#temptable = contextmanager(temptable)


with connect('test.db') as conn:
    cur = conn.cursor()
    with temptable(cur):
        cur.execute('insert into points (x, y) values (1, 1)')
        cur.execute('insert into points (x, y) values (1, 2)')
        cur.execute('insert into points (x, y) values (2, 3)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)
