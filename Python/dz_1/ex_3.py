line = int(input("Введите количество рядов? "))
STEP = 2
for i in range(1, line + 1):
    spaces = " " * (line - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
