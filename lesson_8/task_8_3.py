"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class MyValueError(Exception):
    def __init__(self, text, num):
        self.text = text
        self.num = num


def append_numbers_to_list():
    result_list = []
    while True:
        input_str = input("Enter number: ")
        if input_str != "stop":
            try:
                number = float(input_str)
                result_list.append(number)
            except ValueError:
                try:
                    raise MyValueError("<- this is not a number!", input_str)
                except MyValueError as err:
                    print(err.num, err.text)
                    continue
        else:
            print(result_list)
            break


if __name__ == '__main__':
    append_numbers_to_list()