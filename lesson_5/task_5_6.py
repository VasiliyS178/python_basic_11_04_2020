"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
result_dict = {}

try:
    with open("working_files/file_for_5_6.txt", "r", encoding="utf-8") as f_obj:
        for line in f_obj:
            tmp_list = line.split(":")
            numbers_string = tmp_list[1].replace("(", " ").replace(")", " ")
            tmp_numbers_list = [int(s) for s in numbers_string.split() if s.isdigit()]
            result_dict[tmp_list[0]] = sum(tmp_numbers_list)
except IOError:
    print("IO error occurred!")
    exit(-1)
except ValueError:
    print("The data in the file is incorrect!")
    exit(-1)

print(result_dict)
