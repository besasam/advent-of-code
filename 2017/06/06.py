class Memory:
    def __init__(self):
        self.m = dict()

    def insert(self, state):
        cache = self.m
        for i, s in enumerate(state):
            if s not in cache:
                cache.update(self.make(state[i:]))
                return True
            cache = cache[s]
        return False

    def make(self, vals):
        d = dict()
        for i in reversed(vals):
            d = {i: d}
        return d

    def find(self, state):
        cache = self.m
        for s in state:
            if s not in cache:
                return False
            cache = cache[s]
        return True


class MemoryBanks:
    def __init__(self, state):
        self.state = state
        self.memory = Memory()
        self.buffer = 0
        self.cur = 0

    def realloc(self):
        self.cur = self.state.index(max(self.state))
        self.buffer = self.state[self.cur]
        self.state[self.cur] = 0
        while self.buffer > 0:
            if self.cur == len(self.state) - 1:
                self.cur = 0
            else:
                self.cur += 1
            self.state[self.cur] += 1
            self.buffer -= 1

    def cycle(self):
        cycles = 0
        while True:
            save = self.memory.insert(self.state)
            if not save:
                return cycles
            self.realloc()
            cycles += 1


def part_1(data):
    m = MemoryBanks(data)
    return m.cycle()


test = [0, 2, 7, 0]
with open('input.txt') as f:
    data = [int(x) for x in f.readline().split()]
print(part_1(data))