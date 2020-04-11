"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number = input('Input an integer number: ')

while True:
    if number.isdigit():
        break
    else:
        print("Input only integer numbers")
        number = input('Input a number: ')

i = 0
numbers_list = []
while i < len(number):
    numbers_list.append(int(number[i]))
    i += 1
else:
    print("The maximum digit in your number is:", max(numbers_list))
