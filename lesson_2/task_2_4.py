"""
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове
"""
test_string = input("Input some words: ")
words_list = test_string.split()
for i in range(0, len(words_list)):
    print(f"{i} - {words_list[i][0:10]}")