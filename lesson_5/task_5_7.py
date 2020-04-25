"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
from sys import exit
import json

firms_dict = {}
firms_list = []

try:
    with open("working_files/file_for_5_7.txt", "r", encoding="utf-8") as f_obj:
        for line in f_obj:
            tmp_list = line.split()
            firms_dict[tmp_list[0]] = float(tmp_list[2]) - float(tmp_list[3])
except IOError:
    print("IO error occurred!")
    exit(-1)
except ValueError:
    print("The data in the file is incorrect!")
    exit(-1)

total_profit = 0
count = 0
for k in firms_dict:
    if firms_dict[k] > 0:
        total_profit += firms_dict[k]
        count += 1

average_profit = round(total_profit / count if count else 0, 2)

firms_list = [firms_dict, {"average_profit": average_profit}]

try:
    with open("working_files/json_file_for_5_7.json", "w") as f:
        json.dump(firms_list, f)
except IOError:
    print("IO error occurred!")

print(firms_dict)
print(f"Average_profit: {average_profit}")
