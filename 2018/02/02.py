from itertools import combinations


class Box:
    def __init__(self, id: str):
        self.id = id

    def contains(self, number: int):
        for c in self.id:
            if self.id.count(c) == number:
                return True
        return False

    def difference(self, box: 'Box'):
        diff = ''
        for i in range(len(self.id)):
            if self.id[i] == box.id[i]:
                diff += self.id[i]
        return diff

    def __repr__(self):
        return self.id


def part_1(data):
    twos = []
    threes = []
    for box in data:
        if box.contains(2):
            twos.append(box)
        if box.contains(3):
            threes.append(box)
    return len(twos)*len(threes)


def part_2(data):
    n = len(data[0].id)
    for pair in combinations(data, 2):
        if len(diff := pair[0].difference(pair[1])) == n - 1:
            return diff


with open('input.txt') as f:
    data = [Box(line) for line in f.read().splitlines()]

print(part_2(data))
