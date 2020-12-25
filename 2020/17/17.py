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
        for z in list(self.map.keys()):
            for y in list(self.map[z].keys()):
                for x in list(self.map[z][y].keys()):
                    self.map[z][y][x].get_neighbors()
        cache = dict()
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

    def get_active_cubes(self):
        return sum([self.map[z][y][x].active for z in self.map for y in self.map[z] for x in self.map[z][y]])

    def __str__(self):
        res = ''
        layer_start = min([min(self.map[z].keys()) for z in self.map])
        layer_end = max([max(self.map[z].keys()) for z in self.map])
        row_start = min([min(self.map[z][y].keys()) for z in self.map for y in self.map[z]])
        row_end = max([max(self.map[z][y].keys()) for z in self.map for y in self.map[z]])
        span = abs(row_end - row_start) + 1
        for z in sorted(self.map.keys()):
            res += f'z={z}\n'
            for y in range(layer_start, layer_end + 1):
                if y in self.map[z]:
                    for x in range(row_start, row_end + 1):
                        if x in self.map[z][y]:
                            res += str(self.map[z][y][x])
                        else:
                            res += '.'
                else:
                    res += '.'*span
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
        if self.neighbors:
            return
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


class HyperDimension:
    def __init__(self, data):
        self.map = {0: {0: dict()}}
        self.active = set()
        for y, row in enumerate(data):
            self.map[0][0][y] = dict()
            for x, val in enumerate(row):
                cube = HyperCube(self, 0, 0, y, x, val)
                self.map[0][0][y][x] = cube
                if val:
                    self.active.add(cube)

    def get(self, w, z, y, x):
        try:
            cube = self.map[w][z][y][x]
        except KeyError:
            cube = HyperCube(self, w, z, y, x, False)
            if w not in self.map:
                self.map[w] = {z: {y: {x: cube}}}
            elif z not in self.map[w]:
                self.map[w][z] = {y: {x: cube}}
            elif y not in self.map[w][z]:
                self.map[w][z][y] = {x: cube}
            elif x not in self.map[w][z][y]:
                self.map[w][z][y][x] = cube
        self.active.add(cube)
        return cube

    def cycle(self):
        for cube in self.active.copy():
            cube.get_neighbors()
        cache = dict()
        for cube in self.active.copy():
            state = cube.cycle()
            if cube.w not in cache:
                cache[cube.w] = {cube.z: {cube.y: {cube.x: state}}}
            elif cube.z not in cache[cube.w]:
                cache[cube.w][cube.z] = {cube.y: {cube.x: state}}
            elif cube.y not in cache[cube.w][cube.z]:
                cache[cube.w][cube.z][cube.y] = {cube.x: state}
            else:
                cache[cube.w][cube.z][cube.y][cube.x] = state
        for w in cache:
            for z in cache[w]:
                for y in cache[w][z]:
                    for x in cache[w][z][y]:
                        self.map[w][z][y][x].active = cache[w][z][y][x]
        self.prune()

    def prune(self):
        self.active = set()
        for w in self.map:
            for z in self.map[w]:
                for y in self.map[w][z]:
                    for x in self.map[w][z][y]:
                        if self.map[w][z][y][x].active:
                            self.active.add(self.map[w][z][y][x])
        for cube in self.active.copy():
            for n in cube.neighbors:
                self.active.add(n)

    def get_active_cubes(self):
        return sum([self.map[w][z][y][x].active for w in self.map for z in self.map[w] for y in self.map[w][z] for x in self.map[w][z][y]])


class HyperCube:
    def __init__(self, hyper_dimension: HyperDimension, w, z, y, x, active):
        self.hd = hyper_dimension
        self.w, self.z, self.y, self.x = w, z, y, x
        self.active = active
        self.neighbors = []

    def get_neighbors(self):
        if self.neighbors:
            return
        coords = get_neighbouring_hypercoordinates(self.w, self.z, self.y, self.x)
        for c in coords:
            self.neighbors.append(self.hd.get(c[0], c[1], c[2], c[3]))

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

    def __repr__(self):
        state = 'active' if self.active else 'inactive'
        return f'<{self.w}, {self.z}, {self.y}, {self.x}>: {state}'


def get_neighbouring_coordinates(z, y, x):
    r = [-1, 0, 1]
    return [(z+nz, y+ny, x+nx) for nx in r for ny in r for nz in r if not nx == ny == nz == 0]


def get_neighbouring_hypercoordinates(w, z, y, x):
    r = [-1, 0, 1]
    return [(w+nw, z+nz, y+ny, x+nx) for nx in r for ny in r for nz in r for nw in r if not nx == ny == nz == nw == 0]


def part_1(data):
    pd = PocketDimension(data)
    for i in range(1, 7):
        pd.cycle()
        print(f'cycle {i}: {pd.get_active_cubes()}')
    return pd.get_active_cubes()


def part_2(data):
    hd = HyperDimension(data)
    print(f'cycle 0: {hd.get_active_cubes()}')
    for i in range(1, 7):
        hd.cycle()
        print(f'cycle {i}: {hd.get_active_cubes()}')
    return hd.get_active_cubes()


with open('input.txt') as f:
    data = [[True if c == '#' else False for c in d] for d in f.read().splitlines()]

print(part_2(data))
