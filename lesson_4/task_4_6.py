"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
from itertools import count, cycle
from time import sleep

# task a


def test_count(start_number):
    for el in count(start_number):
        print(el)
        sleep(0.4)


# task b


def test_cycle(iterable_for_test):
    for el in cycle(iterable_for_test):
        print(el)
        sleep(0.4)


if __name__ == '__main__':
    start_number_for_test = 100
    test_list = ["A", "B", "C", "D"]
    test_count(start_number_for_test)
    # test_cycle(test_list)
