#Данный модуль служит для генерации чисел Фибоначчи.

import argparse
import logging

FILE = 'log1.log'

logging.basicConfig(filename=FILE, filemode='a', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)


def pars():
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--count', default=5, help='количество выведенных чисел')
    arg = parser.parse_args()
    return fibonachi(arg.count)


def fibonachi_gen(max_count: int):
    fib1, fib2 = 0, 1
    yield fib1
    yield fib2

    count = 2

    while count < max_count:
        count += 1
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib
        yield fib


def fibonachi(count):
    try:
        count = int(count)
        fib_list = []
        for num in fibonachi_gen(count):
            fib_list.append(num)
        logger.info(f'{count}: {fib_list}')
    except ValueError:
        logger.error(f'{count} число должно быть целым!')


if __name__ == '__main__':
    pars()
