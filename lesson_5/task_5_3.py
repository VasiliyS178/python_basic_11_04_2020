"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""
from sys import exit

lines_dict = {}
min_salary = 20000.00
try:
    with open("working_files/file_for_5_3.txt", "r", encoding="utf-8") as f_obj:
        for line in f_obj:
            tmp_list = line.split()
            lines_dict[tmp_list[0]] = float(tmp_list[1])
except IOError:
    print("IO error occurred!")
    exit(-1)
except ValueError:
    print("The data in the file is incorrect!")
    exit(-1)

print(f"Staff of employees: {lines_dict}")
salary_fund = 0
for k in lines_dict:
    if lines_dict[k] < min_salary:
        print(f"{k} has salary less than minimum!")
    salary_fund += lines_dict[k]

avg_salary = salary_fund / len(lines_dict) if lines_dict else 0

print(f"Average salary is: {avg_salary}")
