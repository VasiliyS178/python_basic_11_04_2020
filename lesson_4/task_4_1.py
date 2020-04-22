"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def wage_calculation(productivity: float, hourly_rate: float, bonus: float):
    try:
        return float(productivity) * float(hourly_rate) + float(bonus)
    except ValueError:
        print("Error arguments")


if __name__ == '__main__':
    try:
        print(wage_calculation(argv[1], argv[2], argv[3]))
    except ValueError:
        print("Error arguments")
    except IndexError:
        print("Error arguments")
