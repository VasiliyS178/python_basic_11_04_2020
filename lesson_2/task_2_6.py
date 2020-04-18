"""
Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь 
с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
test_list = [
(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}), 
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods_list = []
names_list = []
prices_list = []
counts_list = []
measure_units_set = set()
measure_units_list = []
params_list = []
keys_list = []
goods_dict = {}
result_dict = {}

# filling data to goods_list
i = 1
while True:
    print(f"Введите параметры товара #{i} или exit вместо названия для завершения ввода: ")
    name = input("название: ")
    price = 0
    quantity = 0
    measure_unit = None
    if name != "exit":
        price = input("цена: ")
        price = int(price) if price.isdigit() else 0
        quantity = input("количество: ")
        quantity = int(quantity) if quantity.isdigit() else 0
        measure_unit = input("единица измерения: ")
        goods_dict["название"] = name
        goods_dict["цена"] = price
        goods_dict["количество"] = quantity
        goods_dict["eд"] = measure_unit
        copy_goods_dict = dict(goods_dict)
        goods_list.append((i, copy_goods_dict))
        i += 1
    else:
        break
print("=" * 150)
print(f"Перечень товаров, добавленных в список:\n{goods_list}")

for key in goods_dict.keys():
    keys_list.append(key)

# parsing from goods_list
for i in goods_list:
    names_list.append(i[1].get("название"))
    prices_list.append(i[1].get("цена"))
    counts_list.append(i[1].get("количество"))
    measure_units_set.add(i[1].get("eд"))
measure_units_list.extend(measure_units_set)
params_list = [names_list, prices_list, counts_list, measure_units_list]

for i in range(0, len(keys_list)):
    key = keys_list[i]
    result_dict[key] = params_list[i]
    i += 1
print("=" * 150)
print(f"Сформированная аналитика по товарам в списке:\n{result_dict}")
