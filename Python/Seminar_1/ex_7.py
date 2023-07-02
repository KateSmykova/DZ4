while True:
    num = int(input("Введите число от 1 до 999 .... "))

    if num < 10:
        print("Это цифра!", num ** 2)
        break
    elif num >= 10 and num < 100:
        tmp1 = num // 10
        tmp2 = num % 10
        print ("Это двухзначное число", tmp1 * tmp2)
        break
    elif num >= 100 and num < 1000:
        tmp1 = num // 100
        tmp2 = num // 10 % 10
        tmp3 = num % 10
        print("Это трехзначное число", tmp3 * 100 + tmp2 * 10 + tmp1)
        break
    else:
        print("Ошибка, введено число не из диапозона")
        continue