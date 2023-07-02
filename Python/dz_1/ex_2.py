i = 2
count = 0
NOT_SIMPLE = 1
MIN = 0
MAX = 100000

while True:
    num = int(input("Введите число от 0 до 100000 ________"))

    if MIN < num < MAX:
        while i <= num - 1:
            if num % i == 0:
                count += 1
            i += 1
        if count >= NOT_SIMPLE:
            print("Число составное")
        else:
            print("Число простое")
        break
    else:
        print("Недопустимое значение")