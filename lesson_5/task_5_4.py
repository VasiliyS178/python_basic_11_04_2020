"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from sys import exit

lines_dict = {}
auxiliary_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

try:
    with open("working_files/file_1_for_5_4.txt", "r", encoding="utf-8") as f_obj:
        for line in f_obj:
            tmp_list = line.split("—")
            lines_dict[auxiliary_dict[tmp_list[0].replace(" ", "")]] = tmp_list[1].replace("\n", "").replace(" ", "")
except IOError:
    print("IO error occurred!")
    exit(-1)

try:
    with open("working_files/file_2_for_5_4.txt", "w", encoding="utf-8") as f_obj:
        for k in lines_dict:
            f_obj.write(k+" — "+lines_dict[k]+"\n") if k != "Четыре" else f_obj.write(k+" — "+lines_dict[k])
except IOError:
    print("IO error occurred!")
