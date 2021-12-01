from itertools import combinations
import math


def make_groups(packages: list, n: int):
    groups = []
    for c in combinations(packages, n):
        remainder = packages[:]
        for package in c:
            remainder.remove(package)
        weight = sum(c)
        if can_be_grouped(remainder, weight):
            groups.append(c)
    return groups


def can_be_grouped(packages: list, weight: int):
    i = 1
    while i <= len(packages) // 2:
        candidates = combinations(packages, i)
        for c in candidates:
            if sum(c) != weight:
                continue
            if sum(p for p in packages if p not in c) == weight:
                return True
        i += 1
    return False


def part_1(data: list):
    i = 1
    while i < len(data) - 2:
        groups = make_groups(data, i)
        if groups:
            return min([math.prod(g) for g in groups])
        i += 1


with open('input.txt') as f:
    data = list(reversed([int(x) for x in f.read().splitlines()]))

print(part_1(data))
