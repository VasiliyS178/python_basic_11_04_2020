"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
данных о пользователе одной строкой
"""


def get_user_settings(**kwargs):
    return kwargs


user_settings = get_user_settings(
    name=input("name: ")
    , surname=input("surname: ")
    , birth_year=input("born_year: ")
    , city=input("city: ")
    , email=input("email: ")
    , phone_number=input("phone_number: ")
)

print(user_settings)
