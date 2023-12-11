from itertools import combinations


# First you must walk...
def expand(galaxy_map):
    def ex():
        i = 0
        while True:
            if i >= len(galaxy_map):
                break
            cur = galaxy_map[i]
            if len(set(cur)) == 1:
                galaxy_map.insert(i, cur)
                i += 2
            else:
                i += 1
    ex()
    galaxy_map = [''.join(z) for z in zip(*galaxy_map[::-1])]
    ex()
    return [''.join(z) for z in zip(*galaxy_map)][::-1]


# ...so then you may fly
def get_expanded_coords(galaxy_map, galaxy_coords, expansion=1000000):
    empty_y = [y for y, row in enumerate(galaxy_map) if len(set(row)) == 1]
    empty_x = [x for x, col in enumerate([''.join(z) for z in zip(*galaxy_map[::-1])]) if len(set(col)) == 1]
    new_coords = []
    for x, y in galaxy_coords:
        expand_x = sum(1 for ex in empty_x if ex < x) * (expansion - 1)
        expand_y = sum(1 for ey in empty_y if ey < y) * (expansion - 1)
        new = (x + expand_x, y + expand_y)
        new_coords.append((x + expand_x, y + expand_y))
    return new_coords


def distance(a, b):
    x_a, y_a = a
    x_b, y_b = b
    return abs(x_a - x_b) + abs(y_a - y_b)


def part_1(data):
    galaxy_map = expand(data)
    galaxies = []
    for y, row in enumerate(galaxy_map):
        for x, c in enumerate(row):
            if c == '#': galaxies.append((x, y))
    return sum(distance(a, b) for a, b in combinations(galaxies, 2))


def part_2(data):
    galaxies = []
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == '#': galaxies.append((x, y))
    expanded = get_expanded_coords(data, galaxies, 1000000)
    return sum(distance(a, b) for a, b in combinations(expanded, 2))


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
