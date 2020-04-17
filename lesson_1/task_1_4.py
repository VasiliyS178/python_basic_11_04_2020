"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number = input('Input an integer positive number: ')

while True:
    if number.isdigit():
        number = int(number)
        break
    print("Input only integer positive numbers")
    number = input('Input an integer positive number: ')

result = 0
while number and result != 9:
    tmp = number % 10
    if tmp > result:
        result = tmp
    number //= 10

print(f"The maximum digit in your number is: {result}")

