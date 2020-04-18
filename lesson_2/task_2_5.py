"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]
"""
test_list_1 = [7, 5, 3, 3, 2]
test_list_2 = [2, 3, 3, 5, 7]


def input_positive_int_number():
    number = input("Input positive integer number for test: ")
    while True:
        if number.isdigit():
            number = int(number)
            break
        else:
            number = input("Input positive integer number for test: ")
    return number


def insert_number(number, test_list):
    print(f'List before insert: {test_list}')
    target_index = None
    if number in test_list:
        number_index = test_list.index(number)
        number_count = test_list.count(number)
        target_index = number_index + number_count
    else:
        max_number_index = test_list.index(max(test_list))
        min_number_index = test_list.index(min(test_list))
        if max_number_index == 0:
            if number > max(test_list):
                target_index = 0
            elif number < min(test_list):
                target_index = min_number_index + 1
            else:
                for i in test_list:
                    if i > number:
                        i += 1
                    else:
                        target_index = test_list.index(i)
                        break
        else:
            if number > max(test_list):
                target_index = max_number_index + 1
            elif number < min(test_list):
                target_index = 0
            else:
                for i in test_list:
                    if i < number:
                        i += 1
                    else:
                        target_index = test_list.index(i)
                        break
    test_list.insert(target_index, number)
    print(f'List after insert: {test_list}')


if __name__ == '__main__':
    print("Test #1 from 2 with a growing list")
    insert_number(input_positive_int_number(), test_list_1)
    print("Test #2 from 2 with a descending list")
    insert_number(input_positive_int_number(), test_list_2)
