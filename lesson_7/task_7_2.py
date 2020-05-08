"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
from math import ceil


class ClothesAbstract(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(ClothesAbstract):
    def __init__(self, v: int):
        self.__v = v

    @property
    def fabric_consumption(self):
        return self.__v / 6.5 + 0.5


class Suit(ClothesAbstract):
    def __init__(self, h: int):
        self.__h = h

    @property
    def fabric_consumption(self):
        return 2 * self.__h + 0.3


# Container class for calculating the number of rolls of fabric for the production of a given number of coats and suits
class FabricRoll:

    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length
        self.square = width * length
        self.clothes_list = []
        self.__total_fabric_consumption = 0
        self.__coat_count = 0
        self.__suit_count = 0

    def add_coat(self, v):
        self.clothes_list.append(Coat(v))
        self.__coat_count += 1

    def add_suit(self, h):
        self.clothes_list.append(Suit(h))
        self.__suit_count += 1

    def get_total_fabric_consumption(self):
        tmp = 0
        for itm in self.clothes_list:
            tmp += itm.fabric_consumption
        __total_fabric_consumption = ceil(tmp)
        return __total_fabric_consumption

    def get_total_fabric_consumption_in_rolls(self):
        total_fabric_consumption_in_rolls = ceil(self.get_total_fabric_consumption() / self.square)
        return total_fabric_consumption_in_rolls

    def get_coat_count(self):
        return self.__coat_count

    def get_suit_count(self):
        return self.__suit_count


fabric_roll = FabricRoll(2, 10)
fabric_roll.add_coat(10)
fabric_roll.add_coat(11)
fabric_roll.add_coat(12)
fabric_roll.add_coat(13)
fabric_roll.add_suit(4)
fabric_roll.add_suit(5)
fabric_roll.add_suit(6)

print(f"You need {fabric_roll.get_total_fabric_consumption()} m2 of fabric to produce:\n"
      f"{fabric_roll.get_coat_count()} coats\n"
      f"{fabric_roll.get_suit_count()} suits")

print(f"You need {fabric_roll.get_total_fabric_consumption_in_rolls()} rolls of fabric")
