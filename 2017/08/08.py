class CPU:
    def __init__(self):
        self.r = dict()

    def execute(self, i):
        [r1, cmd, v1, r2, cmp, v2] = i[:3] + i[4:]
        if self.compare(r2, v2, cmp):
            return self.modify(r1, v1, cmd)
        return self.get(r1)

    def get(self, r):
        if r not in self.r:
            self.r.update({r: 0})
        return self.r[r]

    def compare(self, reg, val, cmp):
        r = self.get(reg)
        v = int(val)
        if cmp == '>':
            return r > v
        if cmp == '<':
            return r < v
        if cmp == '>=':
            return r >= v
        if cmp == '<=':
            return r <= v
        if cmp == '==':
            return r == v
        if cmp == '!=':
            return r != v
        return False

    def modify(self, reg, val, cmd):
        r = self.get(reg)
        v = int(val)
        if cmd == 'inc':
            self.r[reg] = r + v
            return self.r[reg]
        if cmd == 'dec':
            self.r[reg] = r - v
            return self.r[reg]
        return None


def part_1(data):
    cpu = CPU()
    for i in data:
        cpu.execute(i)
    return max(cpu.r.values())


def part_2(data):
    cpu = CPU()
    highest = 0
    for i in data:
        v = cpu.execute(i)
        if v > highest:
            highest = v
    return highest


with open('example.txt') as f:
    example = [l.split() for l in f.read().splitlines()]
with open('input.txt') as f:
    data = [l.split() for l in f.read().splitlines()]

print(part_2(data))
