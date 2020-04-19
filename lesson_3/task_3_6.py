"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()
"""


def int_func(s: str):
    return str(s).capitalize()


def capitalize_all_words_in_string(s: str):
    result_list = map(int_func, str(s).split(" "))
    return " ".join(result_list)


# test
if __name__ == '__main__':
    test_str = "some words and numbers (10, 20) in the sentence"
    print(test_str)
    print(capitalize_all_words_in_string(test_str))
