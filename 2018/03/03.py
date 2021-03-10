class Claim:
    def __init__(self, specification: str):
        spec = specification.split()
        self.id = int(spec[0][1:])
        self.x, self.y = [int(n) for n in spec[2][:-1].split(',')]
        self.w, self.h = [int(n) for n in spec[3].split('x')]

    def get_coordinates(self):
        coords = []
        for y in range(self.h):
            for x in range(self.w):
                coords.append([self.y+y, self.x+x])
        return coords

    def __repr__(self):
        return f'#{self.id} @ {self.x},{self.y}: {self.w}x{self.h}'


class Fabric:
    def __init__(self, size):
        self.map = dict()
        for y in range(size):
            self.map[y] = dict()
            for x in range(size):
                self.map[y][x] = set()

    def add_claim(self, claim: Claim):
        for [y, x] in claim.get_coordinates():
            self.map[y][x].add(claim)

    def count_all_overlaps(self):
        overlaps = 0
        for y in self.map:
            for x in self.map[y]:
                if len(self.map[y][x]) > 1:
                    overlaps += 1
        return overlaps

    def get_all_claims_in_area(self, claim: Claim):
        claims = set()
        for [y, x] in claim.get_coordinates():
            claims |= self.map[y][x]
        return claims

    def __str__(self):
        rows = []
        for y in self.map:
            row = ''
            for x in self.map[y]:
                if (n := len(self.map[y][x])) == 0:
                    row += ' '
                elif n == 1:
                    row += '░'
                elif n == 2:
                    row += '▒'
                elif n == 3:
                    row += '▓'
                else:
                    row += '█'
            rows.append(row)
        return '\n'.join(rows)


def part_1(data):
    fabric = Fabric(1000)
    for claim in data:
        fabric.add_claim(claim)
    return fabric.count_all_overlaps()


def part_2(data):
    fabric = Fabric(1000)
    candidates = set()
    for claim in data:
        fabric.add_claim(claim)
        candidates.add(claim)
        if len(claims := fabric.get_all_claims_in_area(claim)) > 1:
            candidates -= claims
    return candidates


with open('input.txt') as f:
    data = [Claim(line) for line in f.read().splitlines()]

print(part_2(data))
