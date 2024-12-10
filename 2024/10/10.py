class Node:
    def __init__(self, x: int, y: int, height: int):
        self.x = x
        self.y = y
        self.height = height
        self.prev = []
        self.reachable_nines = set()
        self.score = 0

    def backtrack(self, start_node):
        if self.height == 0:
            self.score += 1
            self.reachable_nines.add(start_node)
        else:
            for node in self.prev:
                node.backtrack(start_node)

    def __key(self):
        return self.x, self.y

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        return False


class HikingMap:
    def __init__(self, data: list):
        self.map = dict()
        self.trailheads = []
        self.trailtails = []
        for y, row in enumerate(data):
            self.map[y] = dict()
            for x, val in enumerate(row):
                node = Node(x, y, val)
                self.map[y][x] = node
                if val == 0:
                    self.trailheads.append(node)
                if val == 9:
                    self.trailtails.append(node)
        for y in self.map:
            for x in self.map:
                cur = self.map[y][x]
                if y-1 in self.map and self.map[y-1][x].height == cur.height - 1:
                    cur.prev.append(self.map[y-1][x])
                if y+1 in self.map and self.map[y+1][x].height == cur.height - 1:
                    cur.prev.append(self.map[y+1][x])
                if x-1 in self.map[y] and self.map[y][x-1].height == cur.height - 1:
                    cur.prev.append(self.map[y][x-1])
                if x+1 in self.map[y] and self.map[y][x+1].height == cur.height - 1:
                    cur.prev.append(self.map[y][x+1])

    def traverse(self):
        for node in self.trailtails:
            node.backtrack(node)


def part_1(data: list) -> int:
    hiking_map = HikingMap(data)
    hiking_map.traverse()
    return sum(len(node.reachable_nines) for node in hiking_map.trailheads)


def part_2(data: list) -> int:
    hiking_map = HikingMap(data)
    hiking_map.traverse()
    return sum(node.score for node in hiking_map.trailheads)


with open('input.txt') as f:
    data = [[int(x) for x in line] for line in f.read().splitlines()]

print(part_2(data))
