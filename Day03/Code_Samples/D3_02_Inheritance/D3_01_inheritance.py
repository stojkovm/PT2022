from abc import ABC, abstractmethod


class Player:
    def __init__(self, health, mana):
        self.__health = health
        self.__mana = mana

    @property
    def health(self):
        return self.__health

    @property
    def mana(self):
        return self.__mana

    @health.setter
    def health(self, new_value):
        self.__health = new_value

    @mana.setter
    def mana(self, new_value):
        self.__mana = new_value

    def __str__(self):
        return "Player[health = " + str(self.__health) + ", mana = " + str(self.__mana) + "]"


class Item(ABC):

    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @abstractmethod
    def use(self, player):
        """
         - We define abstract method that needs to be implemented by the child classes.
        """
        pass

    def __str__(self):
        return "Item[value = " + str(self._value) + "]"


class Food(Item):

    def use(self, player):
        player.health += self._value

    def __str__(self):
        return "Food[value = " + str(self._value) + "]"


class Potion(Item):

    def __init__(self, value, type):
        super().__init__(value)
        self.__type = type

    def use(self, player):
        if self.__type.lower() == "health":
            player.health += self._value
        else:
            player.mana += self._value

    def __str__(self):
        return "Potion[value = " + str(self._value) + ", type = " + self.__type + "]"


player = Player(100, 100)
print(player)

f1 = Food(100)
p1 = Potion(200, "health")
p2 = Potion(300, "mana")

item_list = [f1, p1, p2]

for item in item_list:
    print(item)
    item.use(player)
    print(player)

"""
 - Item cannot be created since it is an abstract class that defines abstract method.
 TypeError: Can't instantiate abstract class Item with abstract method use
"""
# item = Item(200)
# print(item)
print(issubclass(Food, Item))
print(isinstance(Potion(200, "health"), Item))
