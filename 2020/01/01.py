import itertools


def find_ntuple_with_sum(data, n, x):
    for tpl in itertools.combinations(data, n):
        if sum(tpl) == x:
            return eval('*'.join(str(i) for i in tpl))  # extremely cursed. i love it


def part_1(data):
    return find_ntuple_with_sum(data, 2, 2020)


def part_2(data):
    return find_ntuple_with_sum(data, 3, 2020)


with open('input.txt') as f:
    data = [int(x) for x in f.read().splitlines()]

print(part_2(data))
