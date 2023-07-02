from fractions import Fraction

a1 = str(input("Введите числитель первой дроби "))
b1 = str(input("Введите знаменатель первой дроби "))
a2 = str(input("Введите числитель второй дроби "))
b2 = str(input("Введите знаменатель второй дроби "))

num_a1 = int(a1)
num_b1 = int(b1)
num_a2 = int(a2)
num_b2 = int(b2)

print(f' Произведение дробей равно {(num_a1 / num_b1) * (num_a2 / num_b2)}')
print(f' Сумма дробей равна {(num_a1 / num_b1) + (num_a2 / num_b2)}')

a = Fraction(num_a1, num_b1)
b = Fraction(num_a2, num_b2)
print(f'проверка произведения {a * b}')
print(f'проверка суммы {a + b}')