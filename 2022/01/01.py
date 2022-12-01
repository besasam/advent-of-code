def part_1(data):
    return max([sum(x) for x in data])


def part_2(data):
    return sum(sorted([sum(x) for x in data], reverse=True)[:3])


with open('input.txt') as f:
    data = [[int(l) for l in line.split('\n')] for line in f.read().split('\n\n')]

print(part_2(data))
