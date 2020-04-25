"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint

test_random_list = []
for i in range(0, 10):
    test_random_list.append(randint(0, 100))

print(test_random_list)

try:
    with open("working_files/file_for_5_5.txt", "w") as f_obj:
        for i in test_random_list:
            f_obj.write(str(i)+" ")
except IOError:
    print("IO error occurred!")

print(f"Sum of all numbers in the file: {sum(test_random_list)}")
