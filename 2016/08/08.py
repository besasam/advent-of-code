class Screen:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.grid = [[0 for col in range(w)] for row in range(h)]

    def execute(self, instruction):
        [cmd, a, b] = instruction
        if cmd == 0:
            self._rect(a, b)
        elif cmd == 1:
            self._rotate_row(a, b)
        else:
            self._rotate_col(a, b)

    def _rect(self, a, b):
        for x in range(a):
            for y in range(b):
                self.grid[y][x] = 1

    def _rotate_row(self, a, b):
        offset = self.w - (b % self.w)
        self.grid[a] = self.grid[a][offset:] + self.grid[a][:offset]

    def _rotate_col(self, a, b):
        col = [row[a] for row in self.grid]
        offset = self.h - (b % self.h)
        col = col[offset:] + col[:offset]
        for i in range(self.h):
            self.grid[i][a] = col[i]

    def count_pixels(self):
        count = 0
        for row in self.grid:
            for x in row:
                if x == 1:
                    count += 1
        return count

    def print(self):
        for row in self.grid:
            print(''.join(['█' if x == 1 else ' ' for x in row]))
        print()


def parse(instruction):
    ls = instruction.split(' ')
    if ls[0] == 'rect':
        cmd = 0
        [p1, p2] = ls[1].split('x')
    else:
        p = ls[2].split('=')
        p1 = ls[2].split('=')[1]
        p2 = ls[4]
        if ls[1] == 'row':
            cmd = 1
        else:
            cmd = 2
    return [cmd, int(p1), int(p2)]


def part_1(data):
    instructions = [parse(line) for line in data]
    scr = Screen(50, 6)
    for i in instructions:
        scr.execute(i)
    return scr.count_pixels()


def part_2(data):
    instructions = [parse(line) for line in data]
    scr = Screen(50, 6)
    for i in instructions:
        scr.execute(i)
    scr.print()


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))