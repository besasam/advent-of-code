class Octopus:
    def __init__(self, energy: int, x: int, y: int):
        self.energy = energy
        self.x = x
        self.y = y
        self.flashes = 0
        self.neighbors = []

    def __repr__(self):
        return f'({self.energy}/{self.flashes})'


class OctopusCave:
    def __init__(self, grid: list):
        self.grid = [[Octopus(n, x, y) for x, n in enumerate(row)] for y, row in enumerate(grid)]
        self.w = len(self.grid[0])
        self.h = len(self.grid)
        self.octopi = []
        for row in self.grid:
            for octopus in row:
                self.octopi.append(octopus)
                self.get_neighbors(octopus)
        self.has_flashed = []

    def step(self):
        self.has_flashed = []
        for octopus in self.octopi:
            octopus.energy += 1
            if octopus.energy == 10:
                octopus.flashes += 1
                self.has_flashed.append(octopus)
        while self.has_flashed:
            self.propagate(self.has_flashed.pop(0))
        for octopus in self.octopi:
            if octopus.energy > 9:
                octopus.energy = 0

    def propagate(self, octopus: Octopus):
        for neighbor in octopus.neighbors:
            neighbor.energy += 1
            if neighbor.energy == 10:
                neighbor.flashes += 1
                self.has_flashed.append(neighbor)

    def get_neighbors(self, octopus: Octopus):
        ox, oy = octopus.x, octopus.y
        xs = [x for x in [ox-1, ox, ox+1] if 0 <= x < self.w]
        ys = [y for y in [oy-1, oy, oy+1] if 0 <= y < self.h]
        octopus.neighbors = [self.grid[y][x] for x in xs for y in ys if not (x == ox and y == oy)]

    def __str__(self):
        return '\n'.join(''.join(str(octopus.energy) for octopus in row) for row in self.grid)


def part_1(data):
    cave = OctopusCave(data)
    for _ in range(100):
        cave.step()
    return sum(octopus.flashes for octopus in cave.octopi)


def part_2(data):
    cave = OctopusCave(data)
    i = 0
    while True:
        i += 1
        cave.step()
        if all(octopus.energy == 0 for octopus in cave.octopi):
            return i


with open('input.txt') as f:
    data = [[int(c) for c in line] for line in f.read().splitlines()]

print(part_2(data))
