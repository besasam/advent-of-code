def sum_r(x):
    s = int(x / 3) - 2
    if s <= 0:
        return 0
    return s + sum_r(s)


def part_1(data):
    return sum([int(x / 3) - 2 for x in data])


def part_2(data):
    return sum([sum_r(x) for x in data])


with open('input.txt') as f:
    data = [int(l) for l in f.read().splitlines()]

print(part_2(data))