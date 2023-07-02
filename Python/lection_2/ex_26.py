a = complex(2, 3) #коvплексные числа, квадратный корень из -1
b = complex('2+3j')
print(a, b, a == b, sep='\n')

# Математические функции
# ● — возвращает абсолютное значение числа x, число по модулю.
# ● — функция принимает два числа в качестве аргументов и
# возвращает пару чисел — частное и остаток от целочисленного деления.
# Аналогично вычислению a // b и a % b.
# ● pow(base, exp[, mod]) — при передаче 2-х аргументов возводит base в
# степень exp. При передаче 3-х аргументов, результат возведения в степень
# делится по модулю на значение mod.
# ● round(number[, ndigits]) — округляет число number до ndigits цифр
# после запятой. Если второй аргумент не передать, округляет до ближайшего целого.
# abs(x)
# divmod(a, b)