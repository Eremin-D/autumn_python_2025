#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().

A = float(input("Введите длину отрезка A: "))
B = float(input("Введите длину отрезка B: "))
C = float(input("Введите длину отрезка C: "))

AC = abs(A - C)
BC = abs(B - C)

sum_ = AC + BC

print(AC)
print(BC)
print(sum_)