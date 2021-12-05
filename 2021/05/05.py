from util import infinitegrid


def get_line_coords(coords: dict):
    x1, y1, x2, y2 = coords.values()
    if x1 == x2:
        return [(x1, min(y1, y2)+i) for i in range(abs(y1-y2)+1)]
    elif y1 == y2:
        return [(min(x1, x2)+i, y1) for i in range(abs(x1-x2)+1)]
    else:
        x = 1 if x1 <= x2 else -1
        y = 1 if y1 <= y2 else -1
        return [(x1+(i*x), y1+(i*y)) for i in range(abs(x1-x2)+1)]


def solve(coords, part2=False):
    if not part2:
        coords = [c for c in data if c['x1'] == c['x2'] or c['y1'] == c['y2']]
    grid = infinitegrid.Grid2D(0)
    for coord in coords:
        for c in get_line_coords(coord):
            grid[c] += 1
    return len([v for v in grid.all_values() if v > 1])


with open('input.txt') as f:
    data = [{'x1': int(l[0]), 'y1': int(l[1]), 'x2': int(l[2]), 'y2': int(l[3])} for l in
              [line.replace(' -> ', ',').split(',') for line in f.read().splitlines()]]

print(solve(data, True))
