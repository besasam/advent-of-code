from util.infinitegrid import Grid2D


class LightGrid:
    def __init__(self):
        self.grid = Grid2D(False)

    def execute(self, instruction: list):
        action, [start_x, start_y], [end_x, end_y] = instruction
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                self.grid[x, y] = True if action == 1 else False if action == -1 else not self.grid[x, y]


class LightGridAdvance:
    def __init__(self):
        self.grid = Grid2D(0)

    def execute(self, instruction: list):
        action, [start_x, start_y], [end_x, end_y] = instruction
        for x in range(start_x, end_x+1):
            for y in range(start_y, end_y+1):
                self.grid[x, y] += 1 if action == 1 else -1 if action == -1 else 2
                if self.grid[x, y] < 0:
                    self.grid[x, y] = 0


def part_1(data):
    grid = LightGrid()
    for d in data:
        grid.execute(d)
    return sum(grid.grid.all_values())


def part_2(data):
    grid = LightGridAdvance()
    for d in data:
        grid.execute(d)
    return sum(grid.grid.all_values())


with open('input.txt') as f:
    data = [[1 if s[1] == 'on' else -1 if s[1] == 'off' else 0, [int(x) for x in s[-3].split(',')], [int(x) for x in s[-1].split(',')]] for s in [line.split() for line in f.read().splitlines()]]

print(part_2(data))
