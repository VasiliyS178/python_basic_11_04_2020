"""
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""
from functools import reduce

test_list = [itm for itm in range(100, 1001, 2)]


def my_func(itm_1, itm_2):
    return itm_1 * itm_2


res_list = reduce(my_func, test_list)

print(test_list)
print(res_list)
