num = int(input('Введите целое число: '))

def dec_to_n(num, system):
    new_num = ''
    convert = 16

    while num >= 1:
        res = num % convert
        if convert == 16:
            if res == 10:
                res = 'a'
            if res == 11:
                res = 'b'
            if res == 12:
                res = 'c'
            if res == 13:
                res = 'd'
            if res == 14:
                res = 'e'
            if res == 15:
                res = 'f'
        new_num += str(res)
        num = num // convert
    return new_num[::-1]


print(dec_to_n(num, 16))
print(hex(num))
