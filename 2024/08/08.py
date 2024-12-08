from itertools import combinations


class Node:
    def __init__(self, x: int, y: int, signal: str=None):
        self.x = x
        self.y = y
        self.signal = signal
        self.antinode = False

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return self.signal if self.signal is not None else '#' if self.antinode else '.'

    def __repr__(self):
        return f'<{self.x}, {self.y}>'


class AntennaMap:
    def __init__(self, data: list):
        self.width = len(data[0])
        self.height = len(data)
        self.grid = dict()
        self.antennae = dict()
        self.antinodes = set()
        for y, row in enumerate(data):
            self.grid[y] = dict()
            for x, c in enumerate(row):
                node = Node(x, y, c if c != '.' else None)
                self.grid[y][x] = node
                if c != '.':
                    if c not in self.antennae:
                        self.antennae[c] = []
                    self.antennae[c].append(node)

    def find_antinodes(self, antenna_pair: tuple):
        a, b = antenna_pair
        dx = b.x - a.x
        dy = b.y - a.y
        if (x := a.x - dx) in range(self.width) and (y := a.y - dy) in range(self.height):
            self.grid[y][x].antinode = True
            self.antinodes.add(self.grid[y][x])
        if (x := b.x + dx) in range(self.width) and (y := b.y + dy) in range(self.height):
            self.grid[y][x].antinode = True
            self.antinodes.add(self.grid[y][x])

    def find_all_antinodes(self):
        for signal in self.antennae:
            pairs = combinations(self.antennae[signal], 2)
            for pair in pairs:
                self.find_antinodes(pair)

    def find_antinodes_with_resonant_harmonics(self, antenna_pair: tuple):
        a, b = antenna_pair
        dx = b.x - a.x
        dy = b.y - a.y
        for d in range(self.width):
            if (x := a.x - d*dx) in range(self.width) and (y := a.y - d*dy) in range(self.height):
                self.grid[y][x].antinode = True
                self.antinodes.add(self.grid[y][x])
            else:
                break
        for d in range(self.width):
            if (x := b.x + d*dx) in range(self.width) and (y := b.y + d*dy) in range(self.height):
                self.grid[y][x].antinode = True
                self.antinodes.add(self.grid[y][x])
            else:
                break

    def find_all_antinodes_with_resonant_harmonics(self):
        for signal in self.antennae:
            pairs = combinations(self.antennae[signal], 2)
            for pair in pairs:
                self.find_antinodes_with_resonant_harmonics(pair)

    def get_all_nodes(self):
        return [self.grid[y][x] for x in range(self.width) for y in range(self.height)]

    def __str__(self):
        return '\n'.join(''.join(str(self.grid[y][x]) for x in range(self.width)) for y in range(self.height))


def part_1(data: list) -> int:
    antenna_map = AntennaMap(data)
    antenna_map.find_all_antinodes()
    return len(antenna_map.antinodes)


def part_2(data: list) -> int:
    antenna_map = AntennaMap(data)
    antenna_map.find_all_antinodes_with_resonant_harmonics()
    return len(antenna_map.antinodes)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))
