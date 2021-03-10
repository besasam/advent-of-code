from sympy import divisors


def get_number_of_presents(n: int):
    ds = divisors(n)
    return sum(10*d for d in ds)


def get_new_number_of_presents(n: int):
    ds = divisors(n)
    return sum(11*d for d in ds if d*50 <= n)


def part_1(n: int):
    i = 1
    while True:
        if get_number_of_presents(i) >= n:
            return i
        i += 1


def part_2(n: int):
    i = 1
    while True:
        if get_new_number_of_presents(i) >= n:
            return i
        i += 1


print(part_2(29000000))