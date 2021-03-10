import itertools


def combinations(n: int, containers: list):
    c = []
    for k in range(1, len(containers) + 1):
        c += [i for i in itertools.combinations(containers, k) if sum(i) == n]
    return len(c)


def part_1(data):
    return combinations(150, data)


def part_2(data):
    for k in range(1, len(data) + 1):
        if c := [i for i in itertools.combinations(data, k) if sum(i) == 150]:
            return len(c)


with open('input.txt') as f:
    data = [int(x) for x in f.read().splitlines()]

print(part_2(data))
