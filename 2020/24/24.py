from dataclasses import dataclass, field


class HexGrid:
    def __init__(self, init_steps):
        self.tiles = dict()
        tiles = flip_tiles(init_steps)
        for coords in tiles:
            self.get(coords, True)

    def get(self, coords, init_active=False):
        a, r, c = coords
        try:
            return self.tiles[a][r][c]
        except KeyError:
            tile = HexTile(self, a, r, c, init_active)
            if a not in self.tiles:
                self.tiles[a] = {r: {c: tile}}
            elif r not in self.tiles[a]:
                self.tiles[a][r] = {c: tile}
            elif c not in self.tiles[a][r]:
                self.tiles[a][r][c] = tile
            return tile

    def cycle(self):
        for a in list(self.tiles.keys()):
            for r in list(self.tiles[a].keys()):
                for c in list(self.tiles[a][r].keys()):
                    self.tiles[a][r][c].get_neighbors()
        cache = dict()
        for a in list(self.tiles.keys()):
            cache[a] = dict()
            for r in list(self.tiles[a].keys()):
                cache[a][r] = dict()
                for c in list(self.tiles[a][r].keys()):
                    cache[a][r][c] = self.tiles[a][r][c].cycle()
        for a in cache:
            for r in cache[a]:
                for c in cache[a][r]:
                    self.tiles[a][r][c].active = cache[a][r][c]

    def get_active_tiles(self):
        return sum([self.tiles[a][r][c].active for a in self.tiles for r in self.tiles[a] for c in self.tiles[a][r]])


@dataclass
class HexTile:
    grid: HexGrid
    a: int
    r: int
    c: int
    active: bool = False
    neighbors: list = field(default_factory=list)

    def get_neighbors(self):
        if self.neighbors:
            return
        coords = [step([self.a, self.r, self.c], d) for d in ['e', 'se', 'sw', 'w', 'nw', 'ne']]
        for pos in coords:
            self.neighbors.append(self.grid.get(pos))

    def cycle(self):
        if not self.neighbors:
            self.get_neighbors()
        active_neighbors = sum(n.active for n in self.neighbors)
        if self.active:
            return 1 <= active_neighbors <= 2
        else:
            return active_neighbors == 2

    def __repr__(self):
        state = 'X' if self.active else ' '
        return f'<{self.a}, {self.r}, {self.c}> ({state})'


def step(coords, d):
    a, r, c = coords
    if d == 'e':
        c += 1
    elif d == 'se':
        r += a
        c += a
        a = 1 - a
    elif d == 'sw':
        r += a
        a = 1 - a
        c -= a
    elif d == 'w':
        c -= 1
    elif d == 'nw':
        a = 1 - a
        r -= a
        c -= a
    elif d == 'ne':
        c += a
        a = 1 - a
        r -= a
    return [a, r, c]


def move(steps_string):
    pos = [0, 0, 0]
    steps = list(steps_string)
    while steps:
        d = steps.pop(0)
        if d == 'n' or d == 's':
            d += steps.pop(0)
        pos = step(pos, d)
    return pos


def flip_tiles(steps_strings):
    tiles = []
    for steps in steps_strings:
        tile = move(steps)
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.append(tile)
    return tiles


def part_1(data):
    return len(flip_tiles(data))


def part_2(data):
    grid = HexGrid(data)
    for i in range(1, 101):
        grid.cycle()
        if i < 10 or i % 10 == 0:
            print(f'Day {i}: {grid.get_active_tiles()}')
    return grid.get_active_tiles()


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
