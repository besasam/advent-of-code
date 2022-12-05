def contains(superset: list, subset: list) -> bool:
    return superset[0] <= subset[0] and superset[1] >= subset[1]


def overlaps(set1: list, set2: list) -> bool:
    return set1[0] in range(set2[0], set2[1]+1) or set1[1] in range(set2[0], set2[1]+1)


def part_1(data: list) -> int:
    return sum(contains(pair[0], pair[1]) or contains(pair[1], pair[0]) for pair in data)


def part_2(data: list) -> int:
    return sum(overlaps(pair[0], pair[1]) or overlaps(pair[1], pair[0]) for pair in data)


with open('input.txt') as f:
    data = [[[int(x) for x in pair.split('-')] for pair in line.split(',')] for line in f.read().splitlines()]

print(part_2(data))
