"""
 Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
 эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, text=""):
        self.text = text


try:
    a = 7
    b = 0
    if not b:
        raise MyZeroDivisionError("My Zero Division Error Text")
    else:
        c = a / b
except MyZeroDivisionError as e:
    print(e)
