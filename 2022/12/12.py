from string import ascii_lowercase


class Cell:
    def __init__(self, x: int, y: int, height: int):
        self.x = x
        self.y = y
        self.height = height

    def __repr__(self):
        return f'<{self.x}/{self.y}> : {self.height}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class HillClimber:
    def __init__(self, heightmap: list):
        self.grid = []
        for y, row in enumerate(heightmap):
            self.grid.append([])
            for x, c in enumerate(row):
                if c == 'S':
                    height = 0
                    self.start = Cell(x, y, height)
                elif c == 'E':
                    height = 25
                    self.target = Cell(x, y, height)
                else:
                    height = ascii_lowercase.find(c)
                self.grid[y].append(Cell(x, y, height))
        self.grid_height = len(self.grid)
        self.grid_width = len(self.grid[0])

    def find_paths(self, cur: Cell, visited: list[Cell], shortest=None):
        if shortest is None:
            shortest = self.grid_width * self.grid_height
        if len(visited) >= shortest:
            print('too long - passing')
            return
        target_cells = [cell for cell in self.get_valid_moves(cur) if cell not in visited]
        if self.target in target_cells:
            if len(visited) < shortest:
                shortest = len(visited)
            yield visited + [self.target]
        for nex in target_cells:
            yield from self.find_paths(nex, visited + [cur], shortest)

    def get_valid_moves(self, cur: Cell) -> list[Cell]:
        return [cell for cell in self.get_adjacent_cells(cur) if cell.height <= cur.height + 1]

    def get_adjacent_cells(self, cur: Cell) -> list[Cell]:
        cells = []
        [x, y] = cur.x, cur.y
        if x > 0:
            cells.append(self.grid[y][x-1])
        if x < self.grid_width - 1:
            cells.append(self.grid[y][x+1])
        if y > 0:
            cells.append(self.grid[y-1][x])
        if y < self.grid_height - 1:
            cells.append(self.grid[y+1][x])
        return cells


def part_1(data):
    climber = HillClimber(data)
    return min(len(path) for path in climber.find_paths(climber.start, []))


with open('test.txt') as f:
    data = f.read().splitlines()

print(part_1(data))
