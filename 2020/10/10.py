class Adapter:
    def __init__(self, joltage):
        self.joltage = joltage
        self.children = []

    def connect(self, adapter):
        self.children.append(adapter)

    def paths_to(self, goal):
        if goal.joltage < self.joltage:
            return 0
        if goal == self:
            return 1
        return sum([c.paths_to(goal) for c in self.children])

    def __str__(self):
        return f'{self.joltage}: {[c.joltage for c in self.children]}'


class DefinitelyAnElectricHazard:
    def __init__(self, start=0):
        self.start = start
        self.adapters = {start: Adapter(start)}

    def make_tree(self, adapters):
        for a in adapters:
            adapter = Adapter(a)
            self.adapters.update({a: adapter})
            for i in range(1, 4):
                if a-i in self.adapters:
                    self.adapters[a-i].connect(adapter)

    def find_junctions(self):
        junctions = []
        cur = last = self.start
        for a in self.adapters:
            if len(self.adapters[a].children) > 1 and self.adapters[a] not in self.adapters[last].children:
                junctions.append(a)
                last = a
            cur = a
        junctions.append(cur)
        return junctions

    def find_possible_paths(self):
        junctions = self.find_junctions()
        paths = 1
        for i in range(len(junctions) - 1):
            paths *= self.adapters[junctions[i]].paths_to(self.adapters[junctions[i+1]])
        return paths


def this_is_surely_an_electric_hazard(chargers):
    cur = 0
    joltage_differences = {1: 0, 2: 0, 3: 1}
    for c in chargers:
        d = c - cur
        joltage_differences[d] += 1
        cur = c
    return joltage_differences


def part_1(data):
    jolts = this_is_surely_an_electric_hazard(data)
    return jolts[1] * jolts[3]


def part_2(data):
    adapters = DefinitelyAnElectricHazard()
    adapters.make_tree(data)
    return adapters.find_possible_paths()


with open('input.txt') as f:
    data = sorted([int(l) for l in f.read().splitlines()])

print(part_2(data))