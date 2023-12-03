from util.infinitegrid import Grid2D


class PartNumber:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, PartNumber):
            return self.x == other.x and self.y == other.y
        return False

    def __int__(self):
        return self.val

    def __add__(self, other):
        return self.val + other

    def __radd__(self, other):
        return other + self.val

    def __iadd__(self, other):
        self.val += other
        return self

    def __mul__(self, other):
        return self.val * other

    def __rmul__(self, other):
        return other * self.val

    def __imul__(self, other):
        self.val *= other
        return self


class EngineSchematic(Grid2D):
    def get_full_number(self, x, y):
        if not self[x, y].isdigit():
            return None
        if self[x-1, y].isdigit():
            return self.get_full_number(x-1, y)
        res = self[x, y]
        while self[x+1, y].isdigit():
            res += self[x+1, y]
            x += 1
        return PartNumber(x, y, int(res))

    def get_adjacent_numbers(self, x, y):
        res = set()
        for x1 in [x-1, x, x+1]:
            for y1 in [y-1, y, y+1]:
                if (v := self.get_full_number(x1, y1)) is not None:
                    res.add(v)
        return res


def part_1(data):
    grid = EngineSchematic('.')
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            grid[x, y] = val
    part_numbers = set()
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val != '.' and not val.isdigit():
                part_numbers |= grid.get_adjacent_numbers(x, y)
    return sum(part_numbers)


def part_2(data):
    grid = EngineSchematic('.')
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            grid[x, y] = val
    gear_ratios = []
    for y, row in enumerate(data):
        for x, val in enumerate(row):
            if val == '*' and len(adjacent := list(grid.get_adjacent_numbers(x, y))) == 2:
                gear_ratios.append(adjacent[0] * adjacent[1])
    return sum(gear_ratios)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
