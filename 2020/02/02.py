def validate(pwd):
    [min, max], c, p = pwd
    return min <= p.count(c) <= max


def idiot_shopkeeper(pwd):
    [i1, i2], c, p = pwd
    pos = p[i1-1]+p[i2-1]
    return pos.count(c) == 1


def part_1(data):
    return sum(map(lambda x: validate(x), [pwd for pwd in data]))


def part_2(data):
    return sum(map(lambda x: idiot_shopkeeper(x), [pwd for pwd in data]))


data = []
with open('input.txt') as f:
    for line in [l.split(' ') for l in f.read().splitlines()]:
        data.append([[int(x) for x in line[0].split('-')], line[1][:-1], line[2]])

print(part_2(data))
