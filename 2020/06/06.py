import itertools


def count_or(group):
    return len(set(''.join(group)))


def count_and(group):
    return len(set(group[0]).intersection(*group))


def part_1(data):
    return sum(map(count_or, data))


def part_2(data):
    return sum(map(count_and, data))


with open('input.txt') as f:
    data = [list(g) for k, g in itertools.groupby(f.read().splitlines(), key=bool) if k]

print(part_2(data))
