"""
Module contains custom implementation of map (dict).
"""


class MapElement(object):
    """
    Class models elements of a map.
    """

    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    @property
    def key(self):
        pass

    @property
    def value(self):
        pass

    @value.setter
    def value(self, new_value):
        pass

    def __str__(self):
        pass

    def __repr__(self) -> str:
        pass


class Map(object):
    """
    Class models map data structure.
    """

    def __init__(self):
        self.__data = []

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __len__(self):
        return len(self.__data)

    def __contains__(self, key):
        pass

    def __iter__(self):
        pass

    def items(self):
        pass

    def keys(self):
        pass

    def values(self):
        pass

    def clear(self):
        pass


if __name__ == '__main__':
    map = Map()
    map[3] = 10
    map['x'] = 11
    map['asd'] = 'abcdefg'

    # access to elements
    print(map['asd'])
    print(map.values())
    print(map.keys())

    # method __contains__
    if 'y' in map:
        print('Map contains y.')
    else:
        print('Map does not contain y.')

    # iterate throuh map
    for item in map:
        print(item, map[item])

    # delete element
    del map['asd']
    print(len(map) == 2)

    # clear method
    map.clear()
    print(len(map) == 0)
