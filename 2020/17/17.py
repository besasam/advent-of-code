class PocketDimension:
    def __init__(self, data):
        self.map = {0: dict()}
        for y, row in enumerate(data):
            self.map[0][y] = dict()
            for x, val in enumerate(row):
                self.map[0][y][x] = ConwayCube(self, 0, y, x, val)

    def get(self, z, y, x):
        try:
            return self.map[z][y][x]
        except KeyError:
            cube = ConwayCube(self, z, y, x, False)
            if z not in self.map:
                self.map[z] = {y: {x: cube}}
            elif y not in self.map[z]:
                self.map[z][y] = {x: cube}
            elif x not in self.map[z][y]:
                self.map[z][y][x] = cube
            return cube

    def cycle(self):
        cache = dict()
        for z in list(self.map.keys()):
            cache[z] = dict()
            for y in list(self.map[z].keys()):
                cache[z][y] = dict()
                for x in list(self.map[z][y].keys()):
                    self.map[z][y][x].get_neighbors()
        for z in list(self.map.keys()):
            cache[z] = dict()
            for y in list(self.map[z].keys()):
                cache[z][y] = dict()
                for x in list(self.map[z][y].keys()):
                    cache[z][y][x] = self.map[z][y][x].cycle()
        for z in cache:
            for y in cache[z]:
                for x in cache[z][y]:
                    self.map[z][y][x].active = cache[z][y][x]

    def __str__(self):
        res = ''
        for z in sorted(self.map.keys()):
            res += f'z={z}\n'
            for y in sorted(self.map[z].keys()):
                for x in sorted(self.map[z][y].keys()):
                    res += str(self.map[z][y][x])
                res += '\n'
            res += '\n'
        return res


class ConwayCube:
    def __init__(self, pocket_dimension: PocketDimension, z, y, x, active):
        self.pd = pocket_dimension
        self.z, self.y, self.x = z, y, x
        self.active = active
        self.neighbors = []

    def get_neighbors(self):
        coords = get_neighbouring_coordinates(self.z, self.y, self.x)
        for c in coords:
            self.neighbors.append(self.pd.get(c[0], c[1], c[2]))

    def cycle(self):
        if not self.neighbors:
            self.get_neighbors()
        active_neighbors = sum(n.active for n in self.neighbors)
        if self.active:
            return 2 <= active_neighbors <= 3
        else:
            return active_neighbors == 3

    def __str__(self):
        return '#' if self.active else '.'


def get_neighbouring_coordinates(z, y, x):
    r = [-1, 0, 1]
    return [(z+nz, y+ny, x+nx) for nx in r for ny in r for nz in r if not nx == ny == nz == 0]


with open('example.txt') as f:
    data = [[True if c == '#' else False for c in d] for d in f.read().splitlines()]

pd = PocketDimension(data)
print(pd)
pd.cycle()
print(pd)
