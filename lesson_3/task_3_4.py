"""
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_pow_func_version_1(x: float, y: int):
    try:
        result = x ** abs(y)
        print(result if y >= 0 else 1 / result)
    except TypeError:
        print("Error type arguments")


def my_pow_func_version_2(x: float, y: int):
    try:
        result = 1
        for i in range(abs(y)):
            result *= x
        print(result if y >= 0 else 1 / result)
    except TypeError:
        print("Error type arguments")


# test
if __name__ == '__main__':
    number = 10.0
    degree = 0
    print(f"number = {number}, degree = {degree}")
    print("Result of my_pow_func_version_1:")
    my_pow_func_version_1(number, degree)
    print("Result of my_pow_func_version_2:")
    my_pow_func_version_2(number, degree)
