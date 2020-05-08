"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см
*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, length: int, width: int):
        Road._length = length
        Road._width = width

    def calculating_mass_of_asphalt(self, consumption: int, depth: int):
        return self._width * self._length * consumption * depth / 1000


if __name__ == '__main__':
    road_1 = Road(length=5000, width=20)
    print(f"Consumption of the asphalt for the road is: {road_1.calculating_mass_of_asphalt(25, 5)} tons")
