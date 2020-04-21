"""
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict
"""
seasons_dict = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter',
}

seasons_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn',
                'autumn', 'winter']

number = input("Input positive integer number from 1 to 12 for test our DICTIONARY: ")
while True:
    if number.isdigit():
        number = int(number)
        if number != 0 and number < 13:
            print(f'By our DICTIONARY the month #{number} is {seasons_dict[number]}')
            break
        else:
            number = input("Input positive integer number from 1 to 12: ")
    else:
        number = input("Input positive integer number from 1 to 12: ")

number = input("Input positive integer number from 1 to 12 for test our LIST: ")
while True:
    if number.isdigit():
        number = int(number)
        if number != 0 and number < 13:
            print(f'By our LIST the month #{number} is {seasons_list[number - 1]}')
            break
        else:
            number = input("Input positive integer number from 1 to 12: ")
    else:
        number = input("Input positive integer number from 1 to 12: ")