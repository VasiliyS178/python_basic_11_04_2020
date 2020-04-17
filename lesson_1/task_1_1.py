"""
Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.
"""
name = input("What is your name? ")
age = input("How old are you? ")
city = input("What city do you live in? ")

while True:
    if age.isdigit():
        age = int(age)
        break
    else:
        print("Your age is unknown. Use only numbers")
        age = input("How old are you? ")

print(f'Check your details:\n name: {name}\n age: {age}\n city: {city}')
