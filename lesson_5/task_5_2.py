"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
lines_list = []
try:
    with open("working_files/file_for_5_2.txt", "r", encoding="utf-8") as f_obj:
        for line in f_obj:
            lines_list.append(line.split())
except IOError:
    print("Произошла ошибка ввода-вывода!")

print(f"We have {len(lines_list)} lines in the file file_for_5_2.txt:")
for itm in lines_list:
    print(f"Line: {itm} - {len(itm)} words")
