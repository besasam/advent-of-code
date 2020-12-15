class NumbersGame:
    def __init__(self):
        self.cache = dict()

    def play(self, start, stop):
        self.cache = dict()
        i = 1
        for s in start[:-1]:
            self.cache[s] = i
            i += 1
        n = start[-1]
        i += 1
        while i <= stop:
            if n not in self.cache:
                self.cache[n] = i - 1
                n = 0
            else:
                diff = i - 1 - self.cache[n]
                self.cache[n] = i - 1
                n = diff
            i += 1
        return n


def part_1(data):
    ng = NumbersGame()
    return ng.play(data, 2020)


def part_2(data):
    ng = NumbersGame()
    return ng.play(data, 30000000)


with open('input.txt') as f:
    data = [int(x) for x in f.readline().split(',')]

test = [0, 3, 6]

print(part_2(data))
