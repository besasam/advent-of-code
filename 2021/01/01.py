def get_pairs(lst):
    for i in range(len(lst) - 1):
        yield lst[i], lst[i+1]


def get_triples(lst):
    for i in range(len(lst) - 2):
        yield lst[i], lst[i+1], lst[i+2]


def count_increases(lst):
    return sum(p[1] > p[0] for p in get_pairs(lst))


def part_1(data):
    return count_increases(data)


def part_2(data):
    return count_increases([sum(t) for t in get_triples(data)])


with open('input.txt') as f:
    data = [int(line) for line in f.read().splitlines()]

print(part_2(data))
