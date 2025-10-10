#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...). Вывести название соответствующего
#  времени года ("зима", "весна" и т.д.).

month = int(input("Введите номер месяца от (1-12): "))

if month == 12 or month == 1 or month == 2:
    print("зима")
elif month == 3 or month == 4 or month == 5:
    print("весна")
elif month == 6 or month == 7 or month == 8:
    print("лето")
elif month == 9 or month == 10 or month == 11:
    print("осень")
else:
    print("Ошибка: число может быть только от 1 до 12!")