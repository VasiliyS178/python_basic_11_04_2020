"""
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""

result_list = [itm for itm in range(20, 241) if not itm % 20 or not itm % 21]

print(result_list)