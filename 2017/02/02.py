def find_even_divison(row):
    r = row[:]
    while r:
        n = r.pop(r.index(max(r)))
        for x in r:
            if n % x == 0:
                return int(n / x)


def part_1(array):
    return sum([max(row) - min(row) for row in array])


def part_2(array):
    return sum([find_even_divison(row) for row in array])


with open('example.txt') as f:
    test = [[int(s) for s in l.split()] for l in f.read().splitlines()]
with open('example_2.txt') as f:
    test_2 = [[int(s) for s in l.split()] for l in f.read().splitlines()]
with open('input.txt') as f:
    data = [[int(s) for s in l.split()] for l in f.read().splitlines()]
print(part_2(data))