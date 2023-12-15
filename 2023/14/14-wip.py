class Platform:
    def __init__(self, platform_data):
        self.grid = [list(line) for line in platform_data]
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.empty_y = {y: [] for y in range(self.height)}
        self.empty_x = {x: [] for x in range(self.width)}
        self.blocks_y = {y: [] for y in range(self.height)}
        self.blocks_x = {x: [] for x in range(self.width)}
        for y, row in enumerate(self.grid):
            for x, c in enumerate(row):
                if c == '.':
                    self.empty_y[y].append(x)
                    self.empty_x[x].append(y)
                if c == '#':
                    self.blocks_y[y].append(x)
                    self.blocks_x[x].append(y)

    # this is broken, don't use lmao
    def cycle(self):
        self.slide_up()
        self.slide_left()
        self.slide_down()
        self.slide_right()

    def slide_up(self):
        for y in range(1, self.height):
            for x, c in enumerate(self.grid[y]):
                if c == 'O':
                    next_empty_y = self.next_up_pos(x, y)
                    if next_empty_y >= 0:
                        self.grid[next_empty_y][x] = 'O'
                        self.empty_y[next_empty_y].remove(x)
                        self.empty_x[x].remove(next_empty_y)
                        self.grid[y][x] = '.'
                        self.empty_y[y].append(x)
                        self.empty_x[x].append(y)

    def slide_down(self):
        for y in reversed(range(self.height-1)):
            for x, c in enumerate(self.grid[y]):
                if c == 'O':
                    next_empty_y = self.next_down_pos(x, y)
                    if next_empty_y < self.height:
                        self.grid[next_empty_y][x] = 'O'
                        self.empty_y[next_empty_y].remove(x)
                        self.empty_x[x].remove(next_empty_y)
                        self.grid[y][x] = '.'
                        self.empty_y[y].append(x)
                        self.empty_x[x].append(y)

    def slide_left(self):
        for y in range(1, self.width):
            for x, c in enumerate(self.grid[y]):
                if c == 'O':
                    next_empty_x = self.next_left_pos(x, y)
                    if next_empty_x >= 0:
                        self.grid[y][next_empty_x] = 'O'
                        self.empty_x[next_empty_x].remove(y)
                        self.empty_y[y].remove(next_empty_x)
                        self.grid[y][x] = '.'
                        self.empty_x[x].append(y)
                        self.empty_y[y].append(x)

    def slide_right(self):
        for y in reversed(range(self.width-1)):
            for x, c in enumerate(self.grid[y]):
                if c == 'O':
                    next_empty_x = self.next_right_pos(x, y)
                    if next_empty_x < self.width:
                        self.grid[y][next_empty_x] = 'O'
                        self.empty_x[next_empty_x].remove(y)
                        self.empty_y[y].remove(next_empty_x)
                        self.grid[y][x] = '.'
                        self.empty_x[x].append(y)
                        self.empty_y[y].append(x)

    def next_up_pos(self, x, y):
        block = -1 if not (blocks := [bx for bx in self.blocks_x[x] if bx < y]) else max(blocks)
        return -1 if not (empties := [ex for ex in self.empty_x[x] if block < ex < y]) else min(empties)

    def next_down_pos(self, x, y):
        block = self.height if not (blocks := [bx for bx in self.blocks_x[x] if bx > y]) else min(blocks)
        return self.height if not (empties := [ex for ex in self.empty_x[x] if block > ex > y]) else max(empties)

    def next_left_pos(self, x, y):
        block = -1 if not (blocks := [by for by in self.blocks_y[y] if by < x]) else max(blocks)
        return -1 if not (empties := [ey for ey in self.empty_y[y] if block < ey < x]) else min(empties)

    def next_right_pos(self, x, y):
        block = self.width if not (blocks := [by for by in self.blocks_y[y] if by > x]) else min(blocks)
        return self.width if not (empties := [ey for ey in self.empty_y[y] if block > ey > x]) else max(empties)

    def load(self):
        return sum((self.height-y)*row.count('O') for y, row in enumerate(self.grid))

    def draw(self):
        print('\n'.join(''.join(c for c in line) for line in self.grid))


class PlatformTilter:
    def __init__(self, grid):
        self.grid = grid
        self.memo_grid = {''.join(line for line in grid): dict()}
        self.memo_rows = {x: dict() for x in grid}
        self.memo_cols = {x: dict() for x in columns(grid)}

    def cycle(self):
        state = '-'.join(line for line in self.grid)
        if state not in self.memo_grid:
            self.north().west().south().east()
            self.memo_grid[state] = self.grid
        else:
            self.grid = self.memo_grid[state]

    def north(self):
        tilted_grid = []
        for col in columns(self.grid):
            if col not in self.memo_cols:
                self.memo_cols[col] = dict()
            if 'up' not in self.memo_cols[col]:
                self.memo_cols[col]['up'] = tilt(col, True)
            tilted_grid.append(self.memo_cols[col]['up'])
        self.grid = columns(tilted_grid)
        return self

    def west(self):
        tilted_grid = []
        for row in self.grid:
            if row not in self.memo_rows:
                self.memo_rows[row] = dict()
            if 'up' not in self.memo_rows[row]:
                self.memo_rows[row]['up'] = tilt(row, True)
            tilted_grid.append(self.memo_rows[row]['up'])
        self.grid = tilted_grid
        return self

    def south(self):
        tilted_grid = []
        for col in columns(self.grid):
            if col not in self.memo_cols:
                self.memo_cols[col] = dict()
            if 'down' not in self.memo_cols[col]:
                self.memo_cols[col]['down'] = tilt(col)
            tilted_grid.append(self.memo_cols[col]['down'])
        self.grid = columns(tilted_grid)
        return self

    def east(self):
        tilted_grid = []
        for row in self.grid:
            if row not in self.memo_rows:
                self.memo_rows[row] = dict()
            if 'down' not in self.memo_rows[row]:
                self.memo_rows[row]['down'] = tilt(row)
            tilted_grid.append(self.memo_rows[row]['down'])
        self.grid = tilted_grid
        return self


def tilt(segment, is_north_or_west=False):
    return '#'.join(''.join(sorted(s, reverse=is_north_or_west)) for s in segment.split('#'))


def columns(grid):
    return [''.join(s) for s in zip(*grid)]


def load(grid):
    return sum((len(grid)-y)*row.count('O') for y, row in enumerate(grid))


def part_1(data):
    p = Platform(data)
    p.slide_up()
    return p.load()


def part_2(data):
    t = PlatformTilter(data)
    for i in range(1000000000):
        t.cycle()
    return load(t.grid)


with open('test.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
