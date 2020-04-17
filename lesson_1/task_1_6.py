"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a = input('Input how many kilometers did you run? ')
b = input('Input how many kilometers would you like to run? ')

while True:
    try:
        a = float(a)
        b = float(b)
        if a >= 0 and b >= 0:
            break
        else:
            print("Input only positive integer or float numbers")
            a = input('Input how many kilometers do you run? ')
            b = input('Input how many kilometers would you like to run? ')
    except ValueError:
        print("Input only positive integer or float numbers")
        a = input('Input how many kilometers did you run? ')
        b = input('Input how many kilometers would you like to run? ')

day = 1
while a <= b:
    a *= 1.1
    day += 1

print(f"On {day}-th day you will be able to run at least {b} km")
