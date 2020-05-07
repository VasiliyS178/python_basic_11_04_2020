"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    __dates = []
    __parsed_dates = {}

    def __init__(self, date: str):
        MyDate.__dates.append(date)
        self.__date = date

    @classmethod
    def parse_date(cls):
        try:
            for itm in MyDate.__dates:
                MyDate.__parsed_dates[itm] = [int(i) for i in itm.split("-") if i.isdigit()]
            return MyDate.__parsed_dates
        except TypeError:
            print("Value error, can't parse")

    @staticmethod
    def is_valid_date(my_date):
        try:
            if 0 < MyDate.__parsed_dates[my_date.date][0] < 32 \
                    and 0 < MyDate.__parsed_dates[my_date.date][1] < 13 \
                    and MyDate.__parsed_dates[my_date.date][2] < 9999:
                return True
            else:
                return False
        except IndexError:
            return False
        except AttributeError:
            print("Error attribute")

    @property
    def date(self):
        return self.__date


if __name__ == '__main__':
    test_date_1 = '30-05-2020'
    test_date_2 = '06-15-2020'
    my_date_1 = MyDate(test_date_1)
    my_date_2 = MyDate(test_date_2)
    print(my_date_1.date)
    print(my_date_2.date)
    print(MyDate.parse_date())
    print(MyDate.is_valid_date(my_date_1))
    print(MyDate.is_valid_date(my_date_2))
