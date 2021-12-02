def navigate(instructions):
    hpos = 0
    depth = 0
    for i, n in instructions:
        if i == 'down':
            depth += n
        elif i == 'up':
            depth -= n
        else:
            hpos += n
    return hpos, depth


def navigate_with_aim(instructions):
    hpos = 0
    depth = 0
    aim = 0
    for i, n in instructions:
        if i == 'down':
            aim += n
        elif i == 'up':
            aim -= n
        else:
            hpos += n
            depth += aim*n
    return hpos, depth


def part_1(data):
    p = navigate(data)
    return p[0] * p[1]


def part_2(data):
    p = navigate_with_aim(data)
    return p[0] * p[1]


with open('input.txt') as f:
    data = [(line[0], int(line[1])) for line in [l.split(' ') for l in f.read().splitlines()]]

print(part_2(data))
