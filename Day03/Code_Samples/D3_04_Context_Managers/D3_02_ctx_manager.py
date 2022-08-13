"""

 - The following code:

        with ctx() as x:
            pass

 - Can is translated to something similar to this:

        x = ctx().__enter__()
        try:
            pass
        finally:
            x.__exit__()
"""

from sqlite3 import connect


class ResourceManager:
    def __init__(self, cur):
        self.cur = cur

    def __enter__(self):
        print("__enter__")
        self.cur.execute('create table points(x int, y int)')

    def __exit__(self, *args):
        print("__exit__")
        self.cur.execute('drop table points')


with connect('test.db') as conn:
    cur = conn.cursor()
    with ResourceManager(cur):
        cur.execute('insert into points (x, y) values (1, 1)')
        cur.execute('insert into points (x, y) values (1, 2)')
        cur.execute('insert into points (x, y) values (2, 3)')
        for row in cur.execute('select x, y from points'):
            print(row)
        for row in cur.execute('select sum(x * y) from points'):
            print(row)
