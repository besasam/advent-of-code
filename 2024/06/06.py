class Tile:
    def __init__(self, x: int, y: int, visited: bool=False, obstacle: bool=False):
        self.x = x
        self.y = y
        self.visited = visited
        self.obstacle = obstacle

    def __str__(self):
        return '#' if self.obstacle else 'X' if self.visited else '.'


class Grid:
    class Vector:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y
    MOVES = [Vector(0, -1), Vector(1, 0), Vector(0, 1), Vector(-1, 0)]

    def __init__(self, data: list):
        self.grid = dict()
        self.cur = None
        self.direction = 0
        for y, row in enumerate(data):
            self.grid[y] = dict()
            for x, c in enumerate(row):
                tile = Tile(x, y, c == '^', c == '#')
                self.grid[y][x] = tile
                if c == '^':
                    self.cur = tile

    def move(self) -> bool:
        try:
            nex = self.grid[self.cur.y + self.MOVES[self.direction].y][self.cur.x + self.MOVES[self.direction].x]
            if nex.obstacle:
                self.direction = (self.direction + 1) % 4
            else:
                nex.visited = True
                self.cur = nex
            return True
        except KeyError:
            return False

    def count_visited(self):
        return sum(self.grid[y][x].visited for x in range(len(self.grid[0])) for y in range(len(self.grid)))

    def __str__(self):
        return '\n'.join(''.join(str(self.grid[y][x]) for x in range(len(self.grid[0]))) for y in range(len(self.grid)))


def part_1(data: list) -> int:
    grid = Grid(data)
    while grid.move():
        continue
    return grid.count_visited()


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_1(data))
