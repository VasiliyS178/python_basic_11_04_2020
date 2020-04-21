"""
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input()
"""
# test_list = ["i1", "i2", "i3", "i4", "i5", "i6", "i7"]
command = None
test_list = []
while True:
    command = input('Input something or exit to stop input: ')
    if command != "exit":
        test_list.append(command)
    else:
        break

print(test_list)

tmp_list = []
i = 0
while i < len(test_list):
    item_1 = test_list[i]
    try:
        item_2 = test_list[i + 1]
        tmp_list.append(item_2)
        tmp_list.append(item_1)
        i += 2
    except IndexError:
        tmp_list.append(item_1)
        break

test_list = tmp_list
print(test_list)
