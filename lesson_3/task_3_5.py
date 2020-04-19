"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу
"""


def sum_numbers_in_string():
    string_of_numbers = ""
    final_sum = 0
    while string_of_numbers != "#":
        string_of_numbers = input("Enter several numbers separated by a space or # to stop input: ")
        if string_of_numbers != "#":
            tmp_list = string_of_numbers.split()
            if "#" not in string_of_numbers:
                try:
                    numbers_list = map(float, tmp_list)
                    sum_of_numbers = sum(numbers_list)
                    final_sum = final_sum + sum_of_numbers
                    print(f"Sum of numbers is: {final_sum}")
                except ValueError:
                    print("You input something bad! Please, be careful!")
                    continue
            else:
                end_index = tmp_list.index("#")
                tmp_list = tmp_list[:end_index]
                try:
                    numbers_list = map(float, tmp_list)
                    sum_of_numbers = sum(numbers_list)
                    final_sum = final_sum + sum_of_numbers
                    print(f"Final sum of numbers is: {final_sum}")
                    break
                except ValueError:
                    print("You input something bad! Please, be careful!")
                    continue
        else:
            print(f"Final sum of numbers is: {final_sum}")
            break


# test sum_numbers_in_string
if __name__ == '__main__':
    sum_numbers_in_string()
