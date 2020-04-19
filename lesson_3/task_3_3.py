"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов
"""


def my_func(var_1: int, var_2: int, var_3: int):
    """Returns the sum of the two maximum arguments
        :param var_1: int
        :param var_2: int
        :param var_3: int
    """
    tmp_list_1 = [var_1, var_2, var_3]
    max_1 = max(tmp_list_1)
    tmp_list_2 = tmp_list_1[:]
    tmp_list_2.remove(max_1)
    max_2 = max(tmp_list_2)
    return max_1 + max_2


# Test my_func
if __name__ == '__main__':
    var_1, var_2, var_3 = 13, 127, 17
    print(f"We have 3 numbers: {var_1}, {var_2}, {var_3}")
    print(f"Result of my_func's work is: {my_func(var_1, var_2, var_3)}")
