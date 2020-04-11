"""
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
duration = input("Input interval in seconds: ")

while True:
    if duration.isdigit():
        duration = int(duration)
        break
    else:
        print("Input only positive numbers")
        duration = input("Input interval in seconds: ")

duration_hours = duration // 3600
duration_minutes = (duration - duration_hours * 3600) // 60
duration_seconds = duration - duration_hours * 3600 - duration_minutes * 60

print(f'{duration_hours:>02}:{duration_minutes:>02}:{duration_seconds:>02}')
