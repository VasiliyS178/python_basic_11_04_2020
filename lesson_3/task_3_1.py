"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль
"""

number_1 = input("Input number #1 for test my_division_func: ")
number_2 = input("Input number #2 for test my_division_func: ")


def my_division_func(dividend, divider):
    """Returns the quotient of division
    :param dividend: int, float or str
    :param divider: int, float or str
    """
    try:
        dividend = float(dividend)
        divider = float(divider)
        if not divider:
            print("Divider can't be 0!")
            return
        print(f"{dividend} / {divider} = {dividend / divider}")
    except ValueError:
        print("Error arguments")


if __name__ == '__main__':
    my_division_func(number_1, number_2)
