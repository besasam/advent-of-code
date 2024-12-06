class Tile:
    def __init__(self, x: int, y: int, visited: bool=False, obstacle: bool=False):
        self.x = x
        self.y = y
        self.visited = visited
        self.obstacle = obstacle
        self.visited_count = 0

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
                    tile.visited_count += 1

    def move(self) -> bool:
        try:
            nex = self.grid[self.cur.y + self.MOVES[self.direction].y][self.cur.x + self.MOVES[self.direction].x]
            if nex.obstacle:
                self.direction = (self.direction + 1) % 4
            else:
                nex.visited = True
                nex.visited_count += 1
                self.cur = nex
            return True
        except KeyError:
            return False

    def get_visited(self):
        return [self.grid[y][x] for x in range(len(self.grid[0])) for y in range(len(self.grid)) if self.grid[y][x].visited]

    def count_visited(self):
        return len(self.get_visited())

    def __str__(self):
        return '\n'.join(''.join(str(self.grid[y][x]) for x in range(len(self.grid[0]))) for y in range(len(self.grid)))


def part_1(data: list) -> int:
    grid = Grid(data)
    while grid.move():
        continue
    return grid.count_visited()


def part_2(data: list) -> int:
    grid = Grid(data)
    while grid.move():
        continue
    possible_loops = 0
    visited_positions = grid.get_visited()
    for tile in visited_positions:
        print(tile.x, tile.y)
        modified_grid = Grid(data)
        modified_grid.grid[tile.y][tile.x].obstacle = True
        while modified_grid.move():
            if modified_grid.cur.visited and modified_grid.cur.visited_count > 4:  # hail mary
                possible_loops += 1
                break
    return possible_loops


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
