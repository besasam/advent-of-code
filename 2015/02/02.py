def get_wrapping_paper_area(present: tuple[int, ...]):
    l, w, h = present
    sides = [l*w, l*h, w*h]
    return sum(2*s for s in sides) + min(sides)


def get_ribbon_length(present: tuple[int, ...]):
    l, w, h = sorted(present)
    return 2*l + 2*w + l*w*h


def part_1(data):
    return sum(get_wrapping_paper_area(d) for d in data)


def part_2(data):
    return sum(get_ribbon_length(d) for d in data)


with open('input.txt') as f:
    data = [tuple(int(x) for x in line.split('x')) for line in f.read().splitlines()]

print(part_2(data))
