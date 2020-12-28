from util.numbers import Int16Bit


class Circuit:
    def __init__(self):
        self.wires = dict()

    def run(self, instructions: list):
        self.wires = dict()
        while instructions:
            for i, ins in enumerate(instructions[:]):
                if self.execute(ins):
                    instructions.pop(i)
                    break
        return self.wires

    def execute(self, instruction: list):
        inp, out = instruction
        inp = inp.split()
        if len(inp) == 1:
            w = inp[0]
            if not w.isdigit():
                if w not in self.wires:
                    return False
                else:
                    res = self.wires[w]
            else:
                res = Int16Bit(w)
        elif len(inp) == 2:
            op, w = inp
            if w not in self.wires:
                return False
            else:
                res = ~ self.wires[w]
        else:
            w1, op, w2 = inp
            if not w1.isdigit():
                if w1 not in self.wires:
                    return False
                else:
                    w1 = self.wires[w1]
            if not w2.isdigit():
                if w2 not in self.wires:
                    return False
                else:
                    w2 = self.wires[w2]
            if op == 'AND':
                res = w1 & w2
            elif op == 'OR':
                res = w1 | w2
            elif op == 'XOR':
                res = w1 ^ w2
            elif op == 'LSHIFT':
                res = w1 << w2
            elif op == 'RSHIFT':
                res = w1 >> w2
        self.wires[out] = res
        return True


def part_1(data):
    circuit = Circuit()
    return circuit.run(data)['a']


def part_2(data):
    circuit = Circuit()
    a = circuit.run(data[:])['a']
    for d in data:
        if d[1] == 'b':
            d[0] = str(a)
    return circuit.run(data)['a']


with open('input.txt') as f:
    data = [l.split(' -> ') for l in f.read().splitlines()]

print(part_2(data))

for d in data:
    print(d)
