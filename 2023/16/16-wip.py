class LaserGrid:
    def __init__(self, input_grid: list):
        self.grid = {y: {x: self.make_tile((x, y), c) for x, c in enumerate(row)} for y, row in enumerate(input_grid)}

    def make_tile(self, pos: tuple, c: str):
        if c in ['\\', '/']:
            return MirrorTile(pos, self, c)
        elif c in ['-', '|']:
            return SplitterTile(pos, self, c)
        else:
            return Tile(pos, self)

    def energized_tiles(self):
        return sum(sum(1 if tile.lasers else 0 for tile in row.values()) for row in self.grid.values())

    def draw(self):
        for y, row in self.grid.items():
            print(''.join(str(tile) for tile in row.values()))

    def draw_energized(self):
        for y, row in self.grid.items():
            print(''.join('#' if tile.lasers else '.' for tile in row.values()))

    def __getitem__(self, key: tuple):
        x, y = key
        try:
            return self.grid[y][x]
        except KeyError:
            return None


class Tile:
    TYPE_EMPTY = 0
    TYPE_MIRROR = 1
    TYPE_SPLITTER = 2

    DIRECTION_UP = 0
    DIRECTION_DOWN = 1
    DIRECTION_LEFT = 2
    DIRECTION_RIGHT = 3

    def __init__(self, pos: tuple, grid: LaserGrid):
        self.x, self.y = pos
        self.grid = grid
        self.neighbors = dict()
        self.type = self.TYPE_EMPTY
        self.c = '.'
        self.lasers = []

    def next(self, direction: int):
        if direction not in self.neighbors:
            if direction == self.DIRECTION_UP:
                nex = self.grid[self.x, self.y-1]
            elif direction == self.DIRECTION_DOWN:
                nex = self.grid[self.x, self.y+1]
            elif direction == self.DIRECTION_LEFT:
                nex = self.grid[self.x-1, self.y]
            else:
                nex = self.grid[self.x+1, self.y]
            self.neighbors[direction] = nex
        return self.neighbors[direction]

    def emit(self, direction: int):
        if direction in self.lasers:
            return
        self.lasers.append(direction)
        nex = self.next(direction)
        if not nex:
            return
        nex.emit(direction)

    def __str__(self):
        return '.'


class MirrorTile(Tile):
    ANGLE_DOWN = 0
    ANGLE_UP = 1

    def __init__(self, pos: tuple, grid: LaserGrid, c: str):
        super().__init__(pos, grid)
        self.angle = self.ANGLE_DOWN if c == '\\' else self.ANGLE_UP
        self.type = self.TYPE_MIRROR
        self.c = c

    def emit(self, direction: int):
        if direction == self.DIRECTION_UP:
            new_direction = self.DIRECTION_LEFT if self.angle == self.ANGLE_DOWN else self.DIRECTION_RIGHT
        elif direction == self.DIRECTION_DOWN:
            new_direction = self.DIRECTION_RIGHT if self.angle == self.ANGLE_DOWN else self.DIRECTION_LEFT
        elif direction == self.DIRECTION_RIGHT:
            new_direction = self.DIRECTION_DOWN if self.angle == self.ANGLE_DOWN else self.DIRECTION_UP
        else:
            new_direction = self.DIRECTION_UP if self.angle == self.ANGLE_DOWN else self.DIRECTION_DOWN
        super().emit(new_direction)

    def __str__(self):
        return '\\' if self.angle == self.ANGLE_DOWN else '/'


class SplitterTile(Tile):
    ORIENTATION_HORIZONTAL = 0
    ORIENTATION_VERTICAL = 1

    def __init__(self, pos: tuple, grid: LaserGrid, c: str):
        super().__init__(pos, grid)
        self.orientation = self.ORIENTATION_HORIZONTAL if c == '-' else self.ORIENTATION_VERTICAL
        self.type = self.TYPE_SPLITTER
        self.c = c

    def emit(self, direction: int):
        split = (self.orientation == self.ORIENTATION_HORIZONTAL and direction <= 1) or (
                    self.orientation == self.ORIENTATION_VERTICAL and direction > 1)
        if split:
            new_directions = [self.DIRECTION_LEFT, self.DIRECTION_RIGHT] if self.orientation == self.ORIENTATION_HORIZONTAL else [
                self.DIRECTION_UP, self.DIRECTION_DOWN]
            for new_direction in new_directions:
                super().emit(new_direction)
        else:
            super().emit(direction)

    def __str__(self):
        return '-' if self.orientation == self.ORIENTATION_HORIZONTAL else '|'


def part_1(data):
    laser = LaserGrid(data)
    laser[0, 0].emit(Tile.DIRECTION_RIGHT)
    return laser.energized_tiles()


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_1(data))
