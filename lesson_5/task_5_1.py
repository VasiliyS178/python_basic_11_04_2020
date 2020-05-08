"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
try:
    with open("working_files/file_for_5_1.txt", "w", encoding="UTF-8") as f_obj:
        data = input("Enter something to write in the file or empty string for exit:\n")
        while data:
            f_obj.write(data+"\n")
            data = input("Enter something to write in the file or empty string for exit:\n")
except IOError:
    print("IO error occurred!")
