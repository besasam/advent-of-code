class LightGrid:
    def __init__(self, grid: dict, part_2: bool=False):
        self.map = grid
        self.part_2 = part_2
        if self.part_2:
            self.grid_size = len(grid.keys()) - 1
            self.map[0][0] = self.map[0][self.grid_size] = self.map[self.grid_size][0] = self.map[self.grid_size][self.grid_size] = True

    def cycle(self):
        cache = dict()
        for y in self.map:
            cache[y] = dict()
            for x in self.map[y]:
                cache[y][x] = self.next_state(x, y)
        for y in cache:
            for x in cache[y]:
                self.map[y][x] = cache[y][x]

    def next_state(self, x: int, y: int):
        if self.part_2 and ((x == 0 and y == 0) or (x == 0 and y == self.grid_size) or (x == self.grid_size and y == 0) or (x == self.grid_size and y == self.grid_size)):
            return True
        neighbors = sum(self.neighbors(x, y))
        if self.map[y][x]:
            return 2 <= neighbors <= 3
        return neighbors == 3

    def neighbors(self, x: int, y: int):
        res = []
        for ny in [-1, 0, 1]:
            for nx in [-1, 0, 1]:
                if not nx == ny == 0 and 0 <= (mx := x+nx) < len(self.map) and 0 <= (my := y+ny) < len(self.map):
                    res.append(self.map[my][mx])
        return res

    def count_lights(self):
        return sum([sum(self.map[y].values()) for y in self.map])

    def __str__(self):
        return '\n'.join([''.join(['#' if self.map[y][x] else '.' for x in self.map[y]]) for y in self.map])


def part_1(data: dict):
    grid = LightGrid(data)
    for _ in range(100):
        grid.cycle()
    return grid.count_lights()


def part_2(data: dict):
    grid = LightGrid(data, True)
    for _ in range(100):
        grid.cycle()
    return grid.count_lights()


with open('input.txt') as f:
    grid = {y: {x: True if c == '#' else False for x, c in enumerate(row)} for y, row in enumerate(f.read().splitlines())}

print(part_2(grid))
