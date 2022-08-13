"""
 - We can refactor code to use generators!
"""

from sqlite3 import connect


def temptable(cur):
    print("__enter__")
    cur.execute('create table points(x int, y int)')
    yield
    cur.execute('drop table points')
    print("__exit__")


class contextmanager:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        self.gen = temptable(self.cur)
        next(self.gen)

    def __exit__(self, *args):
        next(self.gen, None)


with connect('test.db') as conn:
    cur = conn.cursor()
    with contextmanager(cur):
        cur.execute('insert into points (x, y) values (1, 1)')
        cur.execute('insert into points (x, y) values (1, 2)')
        cur.execute('insert into points (x, y) values (2, 3)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)
