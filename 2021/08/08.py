class SegmentDisplay:
    patterns = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

    def __init__(self, digits: list):
        self.digits = digits
        self.true_digits = ['' for i in range(10)]
        self.wires = {d: set() for d in ['a', 'b', 'c', 'd', 'e', 'f', 'g']}
        self.find_1()
        self.find_4()
        self.find_7()
        self.find_8()
        self.find_9()
        self.find_0()
        self.find_6()
        self.find(2)
        self.find(3)
        self.find(5)

    def parse(self, digit: str):
        for i, d in enumerate(self.true_digits):
            if set(digit) == set(d):
                return str(i)

    def find_1(self):
        self.true_digits[1] = self.get_by_length(2)[0]
        self.wires['c'] = set(d for d in self.true_digits[1])
        self.wires['f'] = set(d for d in self.true_digits[1])

    def find_4(self):
        self.true_digits[4] = self.get_by_length(4)[0]
        self.wires['b'] = set(d for d in self.true_digits[4] if d not in self.true_digits[1])
        self.wires['d'] = set(d for d in self.true_digits[4] if d not in self.true_digits[1])

    def find_7(self):
        self.true_digits[7] = self.get_by_length(3)[0]
        self.wires['a'] = set(d for d in self.true_digits[7] if d not in self.true_digits[1])

    def find_8(self):
        self.true_digits[8] = self.get_by_length(7)[0]
        self.wires['e'] = set(d for d in self.true_digits[8])
        self.wires['g'] = set(d for d in self.true_digits[8])
        for w in ['a', 'b', 'c', 'd', 'f']:
            for d in self.wires[w]:
                self.wires['e'].discard(d)
                self.wires['g'].discard(d)

    def find_9(self):
        candidates = self.get_by_length(6)
        pattern = set(d for d in self.true_digits[4] + self.true_digits[7])
        for c in candidates:
            diff = set(c).difference(pattern)
            if len(diff) == 1:
                self.true_digits[9] = c
                self.wires['g'] = diff
                self.wires['e'].difference_update(diff)
                break

    def find_0(self):
        candidates = [c for c in self.get_by_length(6) if c not in self.true_digits]
        pattern = set(d for d in self.true_digits[7]).union(self.wires['e'], self.wires['g'])
        for c in candidates:
            diff = set(c).difference(pattern)
            if len(diff) == 1:
                self.true_digits[0] = c
                self.wires['b'] = diff
                self.wires['d'].difference_update(diff)
                break

    def find_6(self):
        six = [c for c in self.get_by_length(6) if c not in self.true_digits][0]
        self.true_digits[6] = six
        pattern = self.get_pattern('abdeg')
        diff = set(six).difference(pattern)
        self.wires['f'] = diff
        self.wires['c'].difference_update(diff)

    def find(self, n: int):
        pattern = self.get_pattern(self.patterns[n])
        for d in self.digits:
            if d in self.true_digits:
                continue
            if len(set(d).difference(pattern)) == 0:
                self.true_digits[n] = d

    def get_by_length(self, length: int):
        return [d for d in self.digits if len(d) == length]

    def get_pattern(self, pattern: str):
        res = set()
        for d in pattern:
            res.update(self.wires[d])
        return res


def part_1(data):
    return sum(1 for d in data for x in d['output'] if len(x) in [2, 3, 4, 7])


def part_2(data):
    res = 0
    for d in data:
        display = SegmentDisplay(d['digits'])
        res += int(''.join([display.parse(n) for n in d['output']]))
    return res


with open('input.txt') as f:
    data = [{'digits': l[0].split(' '), 'output': l[1].split(' ')} for l in [line.split(' | ') for line in f.read().splitlines()]]

print(part_2(data))
