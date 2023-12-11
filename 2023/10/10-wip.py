from util.infinitegrid import Grid2D


class Pipe:
    def __init__(self, shape, pos, pipe_map):
        self.shape, self.map = shape, pipe_map
        self.x, self.y = pos
        self._up, self._down, self._left, self._right = -1, -1, -1, -1
        self.distance = None

    def next(self):
        return [n for n in [self.up(), self.down(), self.left(), self.right()] if n]

    def up(self):
        if self._up == -1:
            self._up = None if self.shape in ['-', '7', 'F'] else self.map[self.x, self.y-1]
        return self._up

    def down(self):
        if self._down == -1:
            self._down = None if self.shape in ['-', 'L', 'J'] else self.map[self.x, self.y+1]
        return self._down

    def left(self):
        if self._left == -1:
            self._left = None if self.shape in ['|', 'L', 'F'] else self.map[self.x-1, self.y]
        return self._left

    def right(self):
        if self._right == -1:
            self._right = None if self.shape in ['|', 'J', '7'] else self.map[self.x+1, self.y]
        return self._right

    def next_up(self):
        for y in reversed(range(self.map.min_y, self.y)):
            if n := self.map[self.x, y]:
                return n
        return None


    def __eq__(self, other):
        if isinstance(other, Pipe):
            return (self.x, self.y) == (other.x, other.y)
        return False

    def __str__(self):
        if self.shape == '-':
            return '─'
        if self.shape == 'L':
            return '└'
        if self.shape == 'J':
            return '┘'
        if self.shape == '7':
            return '┐'
        if self.shape == 'F':
            return '┌'
        return '│'

    def __repr__(self):
        return str((self.x, self.y))


class PipeMap(Grid2D):
    def __init__(self):
        super().__init__()
        self.start_pos = None
        self.start = None
        self.min_x, self.max_x, self.min_y, self.max_y = None, None, None, None

    def get_start(self):
        if not self.start:
            start = self.__getitem__(self.start_pos)
            candidates = {'|', '-', 'L', 'J', '7', 'F'}
            up, down, left, right = start.up(), start.down(), start.left(), start.right()
            if not up or up.shape not in ['|', '7', 'F']:
                for c in ['|', 'L', 'J']: candidates.discard(c)
            if not down or down.shape not in ['|', 'L', 'J']:
                for c in ['|', '7', 'F']: candidates.discard(c)
            if not left or left.shape not in ['-', 'L', 'F']:
                for c in ['-', 'J', '7']: candidates.discard(c)
            if not right or right.shape not in ['-', 'J', '7']:
                for c in ['-', 'L', 'F']: candidates.discard(c)
            self.start = Pipe(candidates.pop(), self.start_pos, self)
            self.__setitem__(self.start_pos, self.start)
        return self.start

    def get_farthest_distance(self):
        if not self.start:
            self.get_start()
        self.start.distance = 0
        visited = [self.start]
        cur = self.start.next()
        d = 1
        while True:
            nex = []
            for c in cur:
                c.distance = d
                if c not in visited:
                    visited.append(c)
                nex += [n for n in c.next() if n not in visited]
                if not nex:
                    return d
            d += 1
            cur = [n for n in nex]

    def get_dimensions(self):
        non_empty = [p for p in self.all_values() if p]
        y_vals = set(p.y for p in non_empty)
        x_vals = set(p.x for p in non_empty)
        self.min_y, self.max_y = min(y_vals), max(y_vals) + 1
        self.min_x, self.max_x = min(x_vals), max(x_vals) + 1

    def draw(self):
        print('\n'.join([''.join('.' if not (c := self.__getitem__((x, y))) else str(c) for x in range(self.min_x, self.max_x)) for y in range(self.min_y, self.max_y)]))


def get_loop(pipes):
    loop = PipeMap()
    x, y = pipes.start_pos
    start = pipes.get_start()
    new_start = Pipe(start.shape, (start.x, start.y), loop)
    loop[x, y] = new_start
    cur = pipes.start.next()
    visited = [new_start]
    while True:
        nex = []
        for c in cur:
            new = Pipe(c.shape, (c.x, c.y), loop)
            loop[c.x, c.y] = new
            if new not in visited:
                visited.append(new)
            nex += [n for n in c.next() if n not in visited]
            if not nex:
                loop.get_dimensions()
                return loop
        cur = [n for n in nex]


def part_1(data):
    pipes = PipeMap()
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            pipes[x, y] = None if c == '.' else Pipe(c, (x, y), pipes)
            if c == 'S':
                pipes.start_pos = (x, y)
    return pipes.get_farthest_distance()


def part_2(data):
    pipes = PipeMap()
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            pipes[x, y] = None if c == '.' else Pipe(c, (x, y), pipes)
            if c == 'S':
                pipes.start_pos = (x, y)
    pipes.get_start()
    loop = get_loop(pipes)
    loop.draw()


with open('test2.txt') as f:
    data = [[c for c in line] for line in f.read().splitlines()]

print(part_2(data))
