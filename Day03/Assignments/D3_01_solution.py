"""
Module contains custom implementation of map (dict).
"""


class MapElement:
    """
    Class models elements of a map.
    """
    __slots__ = '__key', '__value'

    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    @property
    def key(self):
        return self.__key

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def __str__(self):
        return f"{self.key}, {self.value}"

    def __repr__(self) -> str:
        return f"MapElement {self.key}, {self.value}"


class Map:
    """
    Class models map data structure.
    """

    def __init__(self):
        self.__data = []

    def __getitem__(self, key):
        """
        Method gets element with specified key.

        Method searches elements by key.
        If element with specified key exists, element is returned.
        If element with specified key does not exist, exception is thrown.
        """
        for item in self.__data:
            if key == item.key:
                return item.value

        raise KeyError(f"There is no element with specified {key}")

    def __setitem__(self, key, value):
        """
        Method adds/updates element with specified key with new value.

        Method searches elements by key.
        If element with specified key exists, element is updated.
        If element with specified key does not exist, new entry is written to the map.
        """
        for item in self.__data:
            if key == item.key:
                item.value = value
                return

        # element not found, add new entry
        self.__data.append(MapElement(key, value))

    def __delitem__(self, key):
        """
        Method deletes element for specified key.

        Method searches elements by key.
        If element with specified key exists, element is removed.
        If element with specified key does not exist, exception is thrown.

        """
        length = len(self.__data)
        for i in range(length):
            if key == self.__data[i].key:
                self.__data.pop(i)
                return

        raise KeyError(f"There is no element with specified {key}")

    def __len__(self):
        return len(self.__data)

    def __contains__(self, key):
        """
        Method checks if value exists for specific key.
        """
        for item in self.__data:
            if key == item.key:
                return True

        return False

    def __iter__(self):
        for item in self.__data:
            yield item.key

    def items(self):
        for item in self.__data:
            yield item.key, item.value

    def keys(self):
        """
        Method returns all keys from map.
        """
        keys = []
        for key in self:
            keys.append(key)

        return keys

    def values(self):
        """
        Method returns all values from map.
        """
        values = []
        for key in self:
            values.append(self[key])

        return values

    def clear(self):
        """
        Method removes all elements from map.
        """
        self.__data = []


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
