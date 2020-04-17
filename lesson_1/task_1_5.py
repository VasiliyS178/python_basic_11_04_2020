"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
expenses = input('Input annual expenses: ')
revenue = input('Input annual revenue: ')

while True:
    try:
        expenses = float(expenses)
        revenue = float(revenue)
        break
    except ValueError:
        print("Input only float or integer numbers")
        expenses = input('Input annual expenses: ')
        revenue = input('Input annual revenue: ')

result = round(revenue - expenses, 2)

if result <= 0:
    print("Annual loss is:", result)
else:
    print("Annual profit is:", result)
    profitability = round(result / revenue, 2)
    print("Annual profitability is:", profitability)
    employees_count = input('Input count of employees: ')
    while True:
        if employees_count.isdigit():
            employees_count = int(employees_count)
            break
        else:
            print("Input only integer numbers")
            employees_count = input('Input count of employees: ')
    result_on_one_employee = round(result / employees_count, 2)
    print("Annual profit on 1 employee is:", result_on_one_employee)
    