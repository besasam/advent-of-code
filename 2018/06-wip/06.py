from util import infinitegrid


class Point:
    def __init__(self, key: tuple, id=None):
        self.x, self.y = key
        self.id = id
        self.distance = dict()

    def distance(self, point: 'Point'):
        if point.id not in self.distance:
            self.distance[point.id] = abs(self.x - point.x) + abs(self.y - point.y)
            point.distance[self.id] = self.distance[point.id]
        return self.distance[point.id]

    def __repr__(self):
        r = 'Point'
        if self.id is not None:
            r += f' {self.id}'
        return r + f'({self.x}, {self.y})'


class Map:
    def __init__(self, points: list):
        self.map = infinitegrid.Grid2D(False)
        self.points = {i: points[i] for i in range(len(points))}

    def insert(self, key: tuple, val):
        self.map[key] = val

    def fill(self):
        for c in self.points:
            self.insert(self.points[c], Point(self.points[c], c))

    def get_candidates(self):
        rows = [self.points[p][0] for p in self.points]
        cols = [self.points[p][1] for p in self.points]
        left, right = min(cols), max(cols)
        up, down = min(rows), max(rows)
        return [left, right, up, down]


with open('example.txt') as f:
    data = [tuple([int(x[0]), int(x[1])]) for x in [line.split(', ') for line in f.read().splitlines()]]

m = Map(data)
m.fill()

print(m.map)
print(m.points)
print(m.get_candidates())
