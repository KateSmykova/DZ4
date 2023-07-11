NAMES = ["Petr", "Ivan", "Oleg", "Stepan"]
RATES = [18_000, 25_000, 15_000, 30_000]
PERCENTS = ["10.25%", "23.00%", "6.45%", "10.75%"]


def gen_dict(names: list[str], rates: list[int], percents: list[str]):
    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(names, rates, map(lambda x: float(x[:-1]), percents))))}


if __name__ == "__main__":
    print(*gen_dict(NAMES, RATES, PERCENTS))