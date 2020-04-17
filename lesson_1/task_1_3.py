"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
number = input('Input an integer number: ')

while True:
    if number.isdigit():
        number_1 = int(number)
        break
    else:
        print("Input only integer numbers")
        number = input('Input a number: ')

number_2, number_3 = number * 2, number * 3

print(f"{number_1} + {number_2} + {number_3} = {int(number_1) + int(number_2) + int(number_3)}")

