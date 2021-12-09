class Location:
    def __init__(self, x: int, y: int, val: int):
        self.x = x
        self.y = y
        self.val = val

    def __int__(self):
        return self.val

    def __gt__(self, other):
        return self.val > other

    def __lt__(self, other):
        return self.val < other

    def __add__(self, other):
        return self.val + other

    def __radd__(self, other):
        return other + self.val

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Heightmap:
    def __init__(self, maplst: list):
        self.map = [[Location(x, y, val) for x, val in enumerate(row)] for y, row in enumerate(maplst)]
        self.w = len(maplst[0])
        self.h = len(maplst)
        self.low_points = self.find_low_points()
        self.basins = [self.get_basin(p) for p in self.low_points]

    def risk_level(self):
        return sum(self.low_points) + len(self.low_points)

    def basin_sizes(self):
        basins = list(sorted([len(b) for b in self.basins], reverse=True))
        return basins[0] * basins[1] * basins[2]

    def find_low_points(self):
        low_points = []
        for row in self.map:
            for p in row:
                if all([n > p for n in self.get_neighbors(p)]):
                    low_points.append(p)
        return low_points

    def get_basin(self, p: Location):
        basin = [p]
        buffer = self.get_basin_neighbors(p)
        while buffer:
            buffer += [n for n in self.get_basin_neighbors(buffer[0]) if n not in buffer]
            basin.append(buffer.pop(0))
        return basin

    def get_neighbors(self, p):
        neighbors = []
        if p.x > 0:
            neighbors.append(self.map[p.y][p.x-1])
        if p.x+1 < self.w:
            neighbors.append(self.map[p.y][p.x+1])
        if p.y > 0:
            neighbors.append(self.map[p.y-1][p.x])
        if p.y+1 < self.h:
            neighbors.append(self.map[p.y+1][p.x])
        return neighbors

    def get_basin_neighbors(self, p: Location):
        return [n for n in self.get_neighbors(p) if n.val < 9 and n.val == p.val+1]

    def is_in_basin(self, p: Location):
        return any(p in basin for basin in self.basins)

    def __str__(self):
        return '\n'.join(''.join('#' if self.is_in_basin(p) else '.' for p in row) for row in self.map)


def part_1(data):
    heightmap = Heightmap(data)
    return heightmap.risk_level()


def part_2(data):
    heightmap = Heightmap(data)
    return heightmap.basin_sizes()


with open('input.txt') as f:
    data = list(map(lambda line: [int(c) for c in line], f.read().splitlines()))

print(part_2(data))
