"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
from itertools import cycle
from time import sleep


class TrafficLight:
    __color = {"red": 7, "yellow": 2, "green": 7}

    def running(self):
        for k in cycle(TrafficLight.__color):
            print(k)
            for i in range(TrafficLight.__color[k], 0,  -1):
                print(i)
                sleep(1)


if __name__ == '__main__':
    traffic_light_1 = TrafficLight()
    traffic_light_1.running()